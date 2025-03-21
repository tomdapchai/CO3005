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
        print("Var decl: ", ast)
        printEnv(c)
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
        
        
        c[0].append(Symbol(ast.conName, ast.conType, ast.iniExpr))

        return c

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        
        # create new scope for function
        
        env = [[]] + copy.deepcopy(c)

        # Param
        env = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, env)

        

        func_symbol = Symbol(name=ast.name, mtype=MType(partype=env[0], rettype=ast.retType))
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
        # only take list of method in appropriate struct
        env = list(filter(lambda x: x.value == ast.recType.name, c[-1]))

        res = self.lookup(ast.fun.name, env, lambda x: x.name)


        if not res is None:
            raise Redeclared(Method(), ast.fun.name)

        # check method for the same struct
        env = self.visit(ast.fun, [env])

        
        fun = env[-1][-1]

        c[-1].append(Symbol(name=ast.fun.name, mtype=MType(partype=fun.mtype.partype, rettype=fun.mtype.rettype), value=ast.recType.name))

        return c

    def visitPrototype(self, ast: Prototype, c: List[List[Symbol]]):
        # c here is a list of symbol of prototypes of an interface, with c[-1][-1] is the interface
        
        res = self.lookup(ast.name, list(filter(lambda x: x.value == c[-1][-1].name, c[-1])), lambda x: x.name)

        printEnv(c)

        
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        
        param = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, c)

        
        # add prototype in the 2nd last list of c[-1], so the last item of c[-1] (c[-1][-1]) is the interface
        c[-1] = c[-1][:-1] + [Symbol(name=ast.name, mtype=MType(partype=param, rettype=ast.retType), value=c[-1][-1].name)] + [c[-1][-1]]

        
        
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

    def visitArrayType(self, ast, c: List[List[Symbol]]):
        # looking for redeclared array name
        res = self.lookup(ast.eleType, c[0], lambda x: x.name)
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

    def visitInterfaceType(self, ast: InterfaceType, c: List[List[Symbol]]):
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            raise Redeclared(Type(), ast.name)
        
        # check prototypes
        # c here is a list of symbol of prototypes of an interface
        c[-1].append(Symbol(name=ast.name, mtype=type(ast)))

        reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, c)

        return c

    # STATEMENT

    def visitBlock(self, ast, c: List[List[Symbol]]):
        return reduce(lambda acc, ele: self.visit(ele, acc), ast.member, c)

    def visitAssign(self, ast, c: List[List[Symbol]]):
        return c

    def visitIf(self, ast: If, c: List[List[Symbol]]):
        print(ast)
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

        env = [[]] + copy.deepcopy(c)
        self.visit(ast.loop, env)

        return c

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]):


        env = [[]] + copy.deepcopy(c)

        env = self.visit(ast.init, env)

        self.visit(ast.loop, env)

        return c

    def visitForEach(self, ast: ForEach , c: List[List[Symbol]]):

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
        res = self.lookup(ast.name, reduce(lambda x, y: x + y, c, []), lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return c
    
    def visitArrayCell(self, ast, c: List[List[Symbol]]):
        return c

    def visitFieldAccess(self, ast, c: List[List[Symbol]]):   
        return c

    # EXPRESSION
    def visitBinaryOp(self,ast,c: List[List[Symbol]]):
        return c

    def visitUnaryOp(self,ast,c: List[List[Symbol]]):
        return c

    def visitFuncCall(self,ast,c: List[List[Symbol]]):
        return c

    def visitMethCall(self,ast,c: List[List[Symbol]]):
        return c

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
    
    
def printEnv(c: List[List[Symbol]]):
        tmp = c.copy()
        tmp = list(map(lambda x: list(map(lambda y: y.name, x)), tmp))

        print(tmp)