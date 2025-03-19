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
        return self.visit(self.ast,self.global_envi)
    
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

    def visitProgram(self,ast: Program, c):
        reduce(lambda acc, ele: [self.visit(ele, acc)] + acc , ast.decl,c)
        return c

    # DECLARATION
    def visitVarDecl(self, ast: VarDecl, c):
        res = self.lookup(ast.varName, c, lambda x: x.name)
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
        return Symbol(ast.varName, ast.varType,None)
    
    def visitParamDecl(self, ast: ParamDecl, c):
        res = self.lookup(ast.parName, c, lambda x: x.name) 
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        return Symbol(ast.parName, ast.parType,None)
    
    def visitConstDecl(self, ast: ConstDecl, c):
        res = self.lookup(ast.conName, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)
        

        if not type(ast.conType) is type(ast.iniExpr):
            raise TypeMismatch(ast)
        return Symbol(ast.conName, ast.conType,ast.constInit)

    def visitFuncDecl(self, ast: FuncDecl, c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        # check param
        param = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc , ast.params,[])

        for i in param:
            print(i.name)

        # check block body return type and function return type
        returnType = self.visit(ast.body, c)

        # will do later
        # if not self.isSameType(returnType, ast.retType):
        #     raise TypeMismatch(ast)


        return Symbol(name=ast.name, mtype=MType(partype=param, rettype=ast.retType))
    
    def visitMethodDecl(self, ast: MethodDecl, c):
        # only take list of method in appropriate struct
        env = filter(lambda x: x.value == ast.recType.name, c)

        res = self.lookup(ast.fun.name, env, lambda x: x.name)

        if not res is None:
            raise Redeclared(Method(), ast.fun.name)

        # check fun
        fun : FuncDecl = self.visit(ast.fun, env)

        return Symbol(name=ast.fun.name, mtype=MType(partype=fun.mtype.partype, rettype=fun.mtype.rettype), value=ast.recType.name)

    def visitPrototype(self, ast: Prototype, c):
        # c here is a list of symbol of prototypes of an interface
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        
        param = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc , ast.params, [])
        
        return Symbol(name=ast.name, mtype=MType(partype=param, rettype=ast.retType))

    
    # TYPE
    

    def visitIntType(self, ast, c):
        return ast

    def visitFloatType(self, ast, c):
        return ast

    def visitBoolType(self, ast, c):
        return ast

    def visitStringType(self, ast, c):
        return ast

    def visitVoidType(self, ast, c):
        return ast

    def visitArrayType(self, ast, c):
        # looking for redeclared array name
        res = self.lookup(ast.eleType, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.eleType)

        pass

    def visitStructType(self, ast, c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Type(), ast.name)
        
        # check elements: list[Tuple[str, Type]], where str is the name of the field, Type is the type of the field, no visit, just check if there is two duplicate name in the elements

        for i in range (len(ast.elements) - 1):
            for j in range(i + 1, len(ast.elements)):
                if ast.elements[i][0] == ast.elements[j][0]:
                    raise Redeclared(Field(), ast.elements[i][0])


        

        # check methods
        method = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, filter(lambda x: x.value == ast.name, c), [])

        return Symbol(name=ast.name, mtype=ast.name, value=ast.elements)

    def visitInterfaceType(self, ast, c):
        pass

    # STATEMENT

    def visitBlock(self, ast, c):
        pass

    def visitAssign(self, ast, c):
        pass

    def visitIf(self, ast, c):
        pass

    def visitForBasic(self, ast, c):
        pass

    def visitForStep(self, ast, c):
        pass

    def visitForEach(self, ast, c):
        pass

    def visitBreak(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitReturn(self, ast, c):
        pass

    # LHS

    def visitId(self,ast,c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype    
    
    def visitArrayCell(self,ast,c):
        pass

    def visitFieldAccess(self,ast,c):   
        pass

    # EXPRESSION
    def visitBinaryOp(self,ast,c):
        pass

    def visitUnaryOp(self,ast,c):
        pass

    def visitFuncCall(self,ast,c):
        pass

    def visitMethCall(self,ast,c):
        pass

    # LITERALS    
    def visitIntLiteral(self,ast, c):
        return IntType()
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()
    
    def visitStringLiteral(self,ast, c):
        return StringType()
    
    def visitBooleanLiteral(self,ast, c):
        return BoolType()
    
    def visitArrayLiteral(self,ast, c):
        pass

    def visitStructLiteral(self, ast, c):
        pass

    def visitNilLiteral(self, ast, c):
        pass
    
    
