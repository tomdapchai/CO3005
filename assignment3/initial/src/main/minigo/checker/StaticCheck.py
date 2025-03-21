"""
 * @author nhphung
"""
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

class StaticChecker(BaseVisitor,Utils):

    builtin_env = [
        Symbol("getInt",MType([],IntType())),
        Symbol("putInt",MType([IntType()],VoidType())),
        Symbol("putIntLn",MType([IntType()],VoidType())),
        Symbol("getFloat",MType([],FloatType())),
        Symbol("putFloat",MType([FloatType()],VoidType())),
        Symbol("putFloatLn",MType([FloatType()],VoidType())),
        Symbol("getBool",MType([],BoolType())),
        Symbol("putBool",MType([BoolType()],VoidType())),
        Symbol("putBoolLn",MType([BoolType()],VoidType())),
        Symbol("getString",MType([],StringType())),
        Symbol("putString",MType([StringType()],VoidType())),
        Symbol("putStringLn",MType([StringType()],VoidType())),
        Symbol("putLn",MType([],VoidType()))
    ]    
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = self.builtin_env.copy()
 
    
    def check(self):
        return self.visit(self.ast, self.global_envi)
    
    def inferSymbol(self, symbol: Symbol, env: List[List[Symbol]], error: StaticError) -> AST.Type:
        # this function will infer the type of a symbol
        for symbolList in env:
            symbol = self.lookup(symbol.name, symbolList, lambda x: x.name)
            if symbol:
                symbol.mtype = self.inferType(symbol.value, env, error)
                return symbol.mtype
        pass

    def inferType(self, expr: Expr, env: List[List[Symbol]], error: StaticError) -> AST.Type:
        """
        Infer type of an expression
        """
        if type(expr) is BinaryOp:
            left = self.inferType(expr.left, env, error)
            right = self.inferType(expr.right, env, error)
            if not self.isSameType(left, right):
                raise error(expr)
            return left
        if type(expr) is UnaryOp:
            return self.inferType(expr.body, env, error)
        if type(expr) is Id:
            res = self.lookup(expr.name, env, lambda x: x.name)
            if res is None:
                raise error(expr)
            return res.mtype
        if type(expr) is FuncCall:
            res = self.lookup(expr.method.name, env, lambda x: x.name)
            if res is None:
                raise error(expr)
            if not type(res.mtype) is MType:
                raise error(expr)
            if len(res.mtype.partype) != len(expr.param):
                raise error(expr)
            for i in range(len(res.mtype.partype)):
                if not self.isSameType(self.inferType(expr.param[i], env, error), res.mtype.partype[i]):
                    raise error(expr)
            return res.mtype.rettype

    
    def isSameType(self, type1: AST.Type, type2: AST.Type) -> bool:
        """
        Check if two Types are exactly the same.
        """
        if type(type1) is ArrayType or type(type2) is ArrayType:
            if type(type1) is not ArrayType or type(type2) is not ArrayType:
                return False
            if type(type1.eleType) is not type(type2.eleType):
                return False
            if len(type1.size) != len(type2.size):
                return False
            return all(type1.size[i] == type2.size[i] for i in range(len(type1.size)))
        return type(type1) is type(type2)

    def visitProgram(self,ast: Program, c: List[Symbol]):
        
        return reduce(lambda acc, ele: self.visit(ele, acc), ast.decl, [c])
        pass

    # DECLARATION
    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        # lookup list of symbol in c, compare with varName
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        
        if ast.varInit:
            initType = self.visit(ast.varInit, c)
            if ast.varType is None:
                # if varType is None, infer type from initType
                ast.varType = initType
            if not type(ast.varType) is type(initType):
                raise TypeMismatch(ast)
        
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
        

        if not type(ast.conType) is type(ast.iniExpr):
            raise TypeMismatch(ast)
        
        c[0].append(Symbol(ast.conName, ast.conType, ast.iniExpr))

        return c

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        # check param
        env = [[]] + c

        # Param
        env = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, env)

        # Add function to the list of symbol, global
        env[-1].append(Symbol(name=ast.name, mtype=MType(partype=env, rettype=ast.retType)))
        
        # check body

        env = self.visit(ast.body, env)
    

        # will do later
        # if not self.isSameType(returnType, ast.retType):
        #     raise TypeMismatch(ast)


        return env
    
    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]):
        # only take list of method in appropriate struct
        env = list(filter(lambda x: x.value == ast.recType.name, c[-1]))

        res = self.lookup(ast.fun.name, env, lambda x: x.name)

        if not res is None:
            raise Redeclared(Method(), ast.fun.name)

        # check fun
        env = self.visit(ast.fun, [env])

        
        fun = env[-1][-1]

        c[-1].append(Symbol(name=ast.fun.name, mtype=MType(partype=fun.mtype.partype, rettype=fun.mtype.rettype), value=ast.recType.name))

        return c

    def visitPrototype(self, ast: Prototype, c: List[List[Symbol]]):
        # c here is a list of symbol of prototypes of an interface
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        
        param = reduce(lambda acc, ele: self.visit(ele, acc) , ast.params, c)

        c[-1].append(Symbol(name=ast.name, mtype=MType(partype=param, rettype=ast.retType)))
        
        return c

    
    # TYPE
    

    def visitIntType(self, ast, c: List[List[Symbol]]):
        return ast

    def visitFloatType(self, ast, c: List[List[Symbol]]):
        return ast

    def visitBoolType(self, ast, c: List[List[Symbol]]):
        return ast

    def visitStringType(self, ast, c: List[List[Symbol]]):
        return ast

    def visitVoidType(self, ast, c: List[List[Symbol]]):
        return ast

    def visitArrayType(self, ast, c: List[List[Symbol]]):
        # looking for redeclared array name
        res = self.lookup(ast.eleType, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.eleType)

        pass

    def visitStructType(self, ast, c: List[List[Symbol]]):
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            raise Redeclared(Type(), ast.name)
        
        # check elements: list[Tuple[str, Type]], where str is the name of the field, Type is the type of the field, no visit, just check if there is two duplicate name in the elements

        for i in range (len(ast.elements) - 1):
            for j in range(i + 1, len(ast.elements)):
                if ast.elements[i][0] == ast.elements[j][0]:
                    raise Redeclared(Field(), ast.elements[i][0])
        

        # check methods
        #method = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, filter(lambda x: x.value == ast.name, c), c)

        c[-1].append(Symbol(name=ast.name, mtype=ast.name, value=ast.elements))


        return c

    def visitInterfaceType(self, ast, c: List[List[Symbol]]):
        pass

    # STATEMENT

    def visitBlock(self, ast, c: List[List[Symbol]]):
        return reduce(lambda acc, ele: self.visit(ele, acc), ast.member, c)

    def visitAssign(self, ast, c: List[List[Symbol]]):
        pass

    def visitIf(self, ast, c: List[List[Symbol]]):
        pass

    def visitForBasic(self, ast, c: List[List[Symbol]]):
        pass

    def visitForStep(self, ast, c: List[List[Symbol]]):
        pass

    def visitForEach(self, ast, c: List[List[Symbol]]):
        pass

    def visitBreak(self, ast, c: List[List[Symbol]]):
        pass

    def visitContinue(self, ast, c: List[List[Symbol]]):
        pass

    def visitReturn(self, ast, c: List[List[Symbol]]):
        pass

    # LHS

    def visitId(self, ast, c: List[List[Symbol]]):
        res = self.lookup(ast.name, reduce(lambda x, y: x + y, c, []), lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return ast
    
    def visitArrayCell(self, ast, c: List[List[Symbol]]):
        pass

    def visitFieldAccess(self, ast, c: List[List[Symbol]]):   
        pass

    # EXPRESSION
    def visitBinaryOp(self,ast,c: List[List[Symbol]]):
        pass

    def visitUnaryOp(self,ast,c: List[List[Symbol]]):
        pass

    def visitFuncCall(self,ast,c: List[List[Symbol]]):
        pass

    def visitMethCall(self,ast,c: List[List[Symbol]]):
        pass

    # LITERALS    
    def visitIntLiteral(self,ast, c: List[List[Symbol]]):
        return IntType()
    
    def visitFloatLiteral(self,ast, c: List[List[Symbol]]):
        return FloatType()
    
    def visitStringLiteral(self,ast, c: List[List[Symbol]]):
        return StringType()
    
    def visitBooleanLiteral(self,ast, c: List[List[Symbol]]):
        return BoolType()
    
    def visitArrayLiteral(self,ast, c: List[List[Symbol]]):
        pass

    def visitStructLiteral(self, ast, c):
        pass

    def visitNilLiteral(self, ast, c):
        pass
    
    
