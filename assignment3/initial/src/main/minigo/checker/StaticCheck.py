"""
 * @author nhphung
"""
import copy
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class SymbolType(Symbol): # for struct and interface
    def __init__(self, name, mtype, field: List[Symbol] = None, method: List[Symbol] = [], value = None):
        self.name = name
        self.mtype = mtype
        self.field = field # None if interface
        self.method = method

    def __str__(self):
        return "SymbolType(" + str(self.name) + "," + str(self.mtype) + ")"


class StaticChecker(BaseVisitor,Utils):

    builtin_env = [
        # Symbol("getInt",MType([],IntType())),
        # Symbol("putInt",MType([IntType()],VoidType())),
        # Symbol("putIntLn",MType([IntType()],VoidType())),
        # Symbol("getFloat",MType([],FloatType())),
        # Symbol("putFloat",MType([FloatType()],VoidType())),
        # Symbol("putFloatLn",MType([FloatType()],VoidType())),
        # Symbol("getBool",MType([],BoolType())),
        # Symbol("putBool",MType([BoolType()],VoidType())),
        # Symbol("putBoolLn",MType([BoolType()],VoidType())),
        # Symbol("getString",MType([],StringType())),
        # Symbol("putString",MType([StringType()],VoidType())),
        # Symbol("putStringLn",MType([StringType()],VoidType())),
        # Symbol("putLn",MType([],VoidType()))
    ]    
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = self.builtin_env.copy()
        self.type : List[SymbolType] = []
 
    
    def check(self):
        return self.visit(self.ast, self.global_envi)
    
    def inferSymbol(self, symbol: Symbol, c: List[List[Symbol]]):
        """
        Infer the type of a symbol.
        """
        # If symbol already has a type, return it
        if symbol.mtype is not None:
            return symbol.mtype
        
        # If symbol has an initialization value, infer type from it
        if symbol.value is not None:
            return self.inferType(symbol.value, c)
        
        # For function symbols with MType
        if hasattr(symbol.mtype, 'rettype'):
            return symbol.mtype.rettype
        
        # If no type can be inferred, return None
        return None

    def inferType(self, expr: Expr, c: List[List[Symbol]]) -> AST.Type:
        """
        Infer the type of an expression.
        """
        if isinstance(expr, Id):
            # Look up variable in all scopes
            sym = self.lookup(expr.name, sum(c, []), lambda x: x.name)
            if sym is None:
                raise Undeclared(Identifier(), expr.name)
            return sym.mtype
        
        elif isinstance(expr, IntLiteral):
            return IntType()
        
        elif isinstance(expr, FloatLiteral):
            return FloatType()
        
        elif isinstance(expr, BooleanLiteral):
            return BoolType()
        
        elif isinstance(expr, StringLiteral):
            return StringType()
        
        elif isinstance(expr, NilLiteral):
            return NilLiteral()
        
        elif isinstance(expr, ArrayLiteral):
            return ArrayType(expr.dimens, expr.eleType)
        
        elif isinstance(expr, BinaryOp):
            ltype = self.inferType(expr.left, c)
            rtype = self.inferType(expr.right, c)
            
            # Arithmetic operators
            if expr.op in ['+', '-', '*', '/', '%']:
                if type(ltype) is IntType and type(rtype) is IntType:
                    return IntType()
                elif (type(ltype) in [IntType, FloatType] and 
                    type(rtype) in [IntType, FloatType]):
                    return FloatType()
                else:
                    raise TypeMismatch(expr)
            
            # Comparison operators - result is boolean
            elif expr.op in ['==', '!=', '<', '<=', '>', '>=']:
                # Allow comparison between same types or between numeric types
                if type(ltype) is type(rtype) or (type(ltype) in [IntType, FloatType] and type(rtype) in [IntType, FloatType]):
                    return BoolType()
                else:
                    raise TypeMismatch(expr)
            
            # Logical operators - operands and result are boolean
            elif expr.op in ['&&', '||']:
                if type(ltype) is not BoolType or type(rtype) is not BoolType:
                    raise TypeMismatch(expr)
                return BoolType()
            
            else:
                raise TypeMismatch(expr)
        
        elif isinstance(expr, UnaryOp):
            operandType = self.inferType(expr.body, c)
            print("operandType: ", operandType)
            
            if expr.op == '!':
                if type(operandType) is not BoolType:
                    raise TypeMismatch(expr)
                return BoolType()
            
            elif expr.op == '-':
                if type(operandType) not in [IntType, FloatType]:
                    raise TypeMismatch(expr)
                return operandType
            
            else:
                raise TypeMismatch(expr)
        
        # need further fix
        elif isinstance(expr, ArrayCell):
            arrType = self.inferType(expr.arr, c)
            
            if not isinstance(arrType, ArrayType):
                raise TypeMismatch(expr)
            
            # Validate index expressions
            for idx in expr.idx:
                idxType = self.inferType(idx, c)
                if type(idxType) is not IntType:
                    raise TypeMismatch(expr)
            
            return arrType.eleType
        

        elif isinstance(expr, FieldAccess):
            receiverType = self.inferType(expr.receiver, c)
            
            # Find the struct or interface definition
            structSym = None
            for scope in c:
                for sym in scope:
                    if isinstance(sym, SymbolType) and sym.name == receiverType.name:
                        structSym = sym
                        break
                if structSym:
                    break
            
            if not structSym or not structSym.field:
                raise TypeMismatch(expr)
            
            # Find the field
            fieldSym = None
            for field in structSym.field:
                if field.name == expr.field:
                    fieldSym = field
                    break
            
            if not fieldSym:
                raise Undeclared(Field(), expr.field)
            
            return fieldSym.mtype
        
        # this is so good lol
        elif isinstance(expr, FuncCall):
            funcSym = self.lookup(expr.funName, sum(c, []), lambda x: x.name)
            if not funcSym:
                raise Undeclared(Function(), expr.funName)
            
            if not isinstance(funcSym.mtype, MType):
                raise TypeMismatch(expr)
            
            # Check parameter types
            if len(expr.args) != len(funcSym.mtype.partype):
                raise TypeMismatch(expr)
            
            for i, arg in enumerate(expr.args):
                argType = self.inferType(arg, c)
                paramType = funcSym.mtype.partype[i].mtype
                if not self.isSameType(argType, paramType):
                    raise TypeMismatch(expr)
            
            return funcSym.mtype.rettype
        
        elif isinstance(expr, MethCall):
            # Handle method calls similar to FuncCall but with receiver
            # This is a simplified version - you'll need to adapt it based on your language spec
            receiverType = self.inferType(expr.receiver, c)
            
            # Find the struct or interface definition
            typeSym = None
            for scope in c:
                for sym in scope:
                    if isinstance(sym, SymbolType) and sym.name == receiverType.name:
                        typeSym = sym
                        break
                if typeSym:
                    break
            
            if not typeSym or not typeSym.method:
                raise TypeMismatch(expr)
            
            # Find the method
            methodSym = None
            for method in typeSym.method:
                if method.name == expr.metName:
                    methodSym = method
                    break
            
            if not methodSym:
                raise Undeclared(Method(), expr.metName)
            
            # Check parameter types
            if len(expr.args) != len(methodSym.mtype.partype):
                raise TypeMismatch(expr)
            
            for i, arg in enumerate(expr.args):
                argType = self.inferType(arg, c)
                paramType = methodSym.mtype.partype[i].mtype
                if not self.isSameType(argType, paramType):
                    raise TypeMismatch(expr)
            
            return methodSym.mtype.rettype
        
        raise TypeMismatch(expr)  # Default case if type can't be inferred

    
    
    def isSameType(self, type1: AST.Type, type2: AST.Type) -> bool:
        """
        Check if two Types are exactly the same.
        """
        if type(type1) is ArrayType or type(type2) is ArrayType:
            if type(type1) is not ArrayType or type(type2) is not ArrayType:
                return False
            if type(type1.eleType) is not type(type2.eleType):
                return False
            if len(type1.dimens.size) != len(type2.dimens.size):
                return False
            return all(type1.dimens.size[i] == type2.dimens.size[i] for i in range(len(type1.size)))
        return type(type1) is type(type2)

    def visitProgram(self,ast: Program, c: List[Symbol]):
        
        return reduce(lambda acc, ele: self.visit(ele, acc), ast.decl, [c])
        pass

    # DECLARATION
    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]):
        print(ast)
        res = self.lookup(
            ast.varName,
            # filter out SymbolType
            list(filter(lambda x: not isinstance(x, SymbolType), c[0])),
            lambda x: x.name)
        # lookup list of symbol in c, compare with varName
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        if ast.varInit:
            initType = self.inferType(ast.varInit, c)
            print("type: ", initType)
            if ast.varType is None:
                # if varType is None, infer type from initType
                ast.varType = initType
                
            if not type(ast.varType) is type(initType):
                raise TypeMismatch(ast)
        
        else:
            try:
                # for varType is user-defined (ID), visit it
                # if Undeclared occurs, raise Undeclared(Type) because the Id visitor will raise Undeclared(Identifier)
                self.visit(ast.varType, c)
            except Undeclared:
                raise Undeclared(Type(), ast.varType.name)
        
        c[0].append(Symbol(ast.varName, ast.varType, ast.varInit))

        return c
    
    def visitParamDecl(self, ast: ParamDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.parName, c[0], lambda x: x.name) 
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        
        c[0].append(Symbol(ast.parName, ast.parType, None))

        return c
    
    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)
        
        
        c[0].append(Symbol(name=ast.conName, mtype=self.inferType(ast.iniExpr, c), value=ast.iniExpr))

        return c

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]):
        res = self.lookup(
            ast.name, 
            list(filter(lambda x: not isinstance(x, SymbolType), c[-1])),
            lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)

        # create new scope for function        
        env = [[]] + copy.deepcopy(c)

        # Param
        env = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, env)

        func_symbol = Symbol(name=ast.name, mtype=MType(partype=copy.deepcopy(env[0]), rettype=ast.retType))

        # Add function to the list of symbol, global
        env[-1].append(func_symbol)
        # check body

        self.visit(ast.body, env)

        c[-1].append(func_symbol)

        # will do later
        # if not self.isSameType(returnType, ast.retType):
        #     raise TypeMismatch(ast)

        return c
    
    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]):
        # Find the struct in c[-1]
        struct : SymbolType = next((x for x in c[-1] if x.name == ast.recType.name), None)

        # Check if struct was found
        if struct is None:
            raise Undeclared(Type(), ast.recType.name)

        env = struct.method

        res = self.lookup(ast.fun.name, env, lambda x: x.name)

        if not res is None:
            raise Redeclared(Method(), ast.fun.name)

        # check method for the same struct
        ret_env = self.visit(ast.fun, copy.deepcopy(c))

        fun = ret_env[-1][-1]


        # add method to the list of method of the struct
        env.append(Symbol(name=ast.fun.name, mtype=MType(partype=fun.mtype.partype, rettype=fun.mtype.rettype)))
        

        printEnv(c)

        return c

    def visitPrototype(self, ast: Prototype, c: List[List[Symbol]]):
        # c here is a list of symbol of prototypes of an interface, with c[-1][-1] is the interface

        # since prototype is declared in the interface, there will be always interface, and it is the latest item in c[-1]
        interface : SymbolType = c[-1][-1]
        
        prototypes = interface.method

        res = self.lookup(ast.name, prototypes, lambda x: x.name)

        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        
        param = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, c)
        
        # add prototype in the 2nd last list of c[-1], so the last item of c[-1] (c[-1][-1]) is the interface
        prototypes.append(Symbol(name=ast.name, mtype=MType(partype=param[0], rettype=ast.retType)))
        
        
        return c

    
    # TYPE
    

    def visitIntType(self, ast, c: List[List[Symbol]]):
        return c

    def visitFloatType(self, ast, c: List[List[Symbol]]):
        return c

    def visitBoolType(self, ast, c: List[List[Symbol]]):
        return c

    def visitStringType(self, ast, c: List[List[Symbol]]):
        return c

    def visitVoidType(self, ast, c: List[List[Symbol]]):
        return c

    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]):
        
        

        # this is hard

        

        return c

    def visitStructType(self, ast, c: List[List[Symbol]]):
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            raise Redeclared(Type(), ast.name)
        
        # check elements: list[Tuple[str, Type]], where str is the name of the field, Type is the type of the field, no visit, just check if there is two duplicate name in the elements

        # if valid add to field of struct

        fields : List[Symbol] = []
        seen_fields = set()
        
        for element in ast.elements:
            field_name = element[0]
            if field_name in seen_fields:
                raise Redeclared(Field(), field_name)
            
            seen_fields.add(field_name)
            fields.append(Symbol(name=field_name, mtype=element[1]))  
        
        

        # check methods
        #method = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, filter(lambda x: x.value == ast.name, c), c)
        c[-1].append(SymbolType(name=ast.name, mtype=type(ast), method=[], field=fields))
        
        

        return c

    def visitInterfaceType(self, ast: InterfaceType, c: List[List[Symbol]]):
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            raise Redeclared(Type(), ast.name)
        
        # check prototypes
        # c here is a list of symbol of prototypes of an interface
        c[-1].append(SymbolType(name=ast.name, mtype=type(ast), field=None, method=[]))

        reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, c)

        return c

    # STATEMENT

    def visitBlock(self, ast, c: List[List[Symbol]]):
        return reduce(lambda acc, ele: self.visit(ele, acc), ast.member, c)

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]):
        # check LHS
        lhsType = self.inferType(ast.lhs, c)
        # check RHS
        rhsType = self.inferType(ast.rhs, c)

        if not self.isSameType(lhsType, rhsType):
            raise TypeMismatch(ast)


        return c

    def visitIf(self, ast: If, c: List[List[Symbol]]):
        # check condition
        self.inferType(ast.expr, c)

        # then stmt is a block
        # create local scope for then stmt
        env = [[]] + copy.deepcopy(c)

        self.visit(ast.thenStmt, env)

        if ast.elseStmt is not None:
            # else stmt scope unrelated to then stmt

            if type(ast.elseStmt) is If:
                env = copy.deepcopy(c)
            else:
                env = [[]] + copy.deepcopy(c)
            self.visit(ast.elseStmt, env)

        return c

    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]):
        # check the condition

        env = [[]] + copy.deepcopy(c)
        self.visit(ast.loop, env)

        return c

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]):
        # checking init
        env = [[]] + copy.deepcopy(c)

        # basically just add the init variable to the scope
        env = self.visit(ast.init, env)
        
        # checking condition

        # checking update
        self.visit(ast.upda, env)

        # checking loop block
        self.visit(ast.loop, env)

        return c

    def visitForEach(self, ast: ForEach , c: List[List[Symbol]]):
        # this might just check the loop block and the arr (if it is an arrayType and declared)
        env = [[]] + copy.deepcopy(c)
        self.visit(ast.loop, env)
        return c

    def visitBreak(self, ast, c: List[List[Symbol]]):
        return c

    def visitContinue(self, ast, c: List[List[Symbol]]):
        return c

    def visitReturn(self, ast, c: List[List[Symbol]]):
        return c

    # LHS

    def visitId(self, ast, c: List[List[Symbol]]):
        res = self.lookup(ast.name, sum(c, []), lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return c
    
    def visitArrayCell(self, ast, c: List[List[Symbol]]):
        return c

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]):
        """
            get type of receiver (struct)
            check if the field is in the list of field of the struct
            if not raise Undeclared(Field())
        """

        return c

    # EXPRESSION
    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]):
        self.visit(ast.left, c)
        self.visit(ast.right, c)

        return c

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        self.visit(ast.body, c)
        return c

    def visitFuncCall(self, ast: FuncCall,c: List[List[Symbol]]):
        self.inferType(ast, c)
        return c

    def visitMethCall(self,ast : MethCall,c: List[List[Symbol]]):
        # check if the caller exist
        res = self.lookup(ast.receiver, sum(c, []), lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.receiver)
        
        # check the type of caller (struct or interface) and check if the method is in the list of method of the caller
        # do later

        return c

    # LITERALS    
    def visitIntLiteral(self,ast, c: List[List[Symbol]]):
        return c
    
    def visitFloatLiteral(self,ast, c: List[List[Symbol]]):
        return c
    
    def visitStringLiteral(self,ast, c: List[List[Symbol]]):
        return c
    
    def visitBooleanLiteral(self,ast, c: List[List[Symbol]]):
        return c
    
    def visitArrayLiteral(self,ast, c: List[List[Symbol]]):
        return c

    def visitStructLiteral(self, ast, c):
        return c

    def visitNilLiteral(self, ast, c):
        return c
    
    
def printEnv(c: List[List[Symbol]]):
    result = []
    for scope in c:
        scope_info = []
        for symbol in scope:
            if isinstance(symbol, SymbolType):
                symbol_info = {
                    "name": symbol.name,
                    "fields": [field[0] if isinstance(field, tuple) else (field.name, field.mtype) for field in symbol.field] if symbol.field else None,
                    "methods": [method.name for method in symbol.method] if symbol.method else None
                }
                scope_info.append(symbol_info)
            else:
                if isinstance(symbol.mtype, MType):
                    symbol_info = {
                        "name": symbol.name,
                        "mtype": symbol.mtype.rettype,
                        "partype": [(partype.name, partype.mtype) if hasattr(partype, 'name') else partype for partype in symbol.mtype.partype]
                    }
                else:
                    symbol_info = {
                        "name": symbol.name,
                        "mtype": symbol.mtype
                    }
                scope_info.append(symbol_info)
        result.append(scope_info)
    
    print(result)