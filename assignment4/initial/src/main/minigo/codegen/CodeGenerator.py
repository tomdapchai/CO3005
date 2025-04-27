'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce


class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None

    def init(self):
        mem = [Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True))]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
        
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def visitProgram(self, ast, c):
        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        env ={}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a,x: self.visit(x,a), ast.decl, env)
        self.emitObjectInit()
        self.emit.printout(self.emit.emitEPILOG())
        return env

    # ====================================DECLARATIONS====================================
    def visitVarDecl(self, ast, o):
        if 'frame' not in o: # global var
            o['env'][0].append(Symbol(ast.varName, ast.varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, str(ast.varInit.value) if ast.varInit else None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, ast.varType, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            if ast.varInit:
                self.emit.printout(self.emit.emitPUSHICONST(ast.varInit.value, frame))
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index,  frame))
        return o
    
    def visitConstDecl(self, ast, o):
        return o
    
    def visitParamDecl(self, ast, o):
        return o

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        o['env'][0].append(Symbol(ast.name, mtype, CName(self.className)))
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    

    def visitMethodDecl(self, ast, o):
        return o
    
    def visitPrototype(self, ast, o):
        return o
    

    
    # ====================================EXPRESSIONS====================================
    
    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        if type(sym.value) is Index:
            # local var
            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']),sym.mtype
        else:         
            # global var
            return self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame']),sym.mtype
    
    def visitArrayCell(self, ast, o):
        return o
    
    def visitFieldAccess(self, ast, o):
        return o
    
    def visitBinaryOp(self, ast: BinaryOp, o):
        e1, t1 = self.visit(ast.left, o)
        e2, t2 = self.visit(ast.right, o)

        if isinstance(t1, FloatType) or isinstance(t2, FloatType):
            mtype = FloatType()
        else:
            mtype = IntType()
        if type(t1) is IntType and type(mtype) != type(t1):
            e1 = e1 + self.emit.emitI2F(o['frame'])
        if type(t2) is IntType and type(mtype) != type(t2):
            e2 = e2 + self.emit.emitI2F(o['frame'])
        
        # store codes of left and right expressions
        code = e1 + e2
        if ast.op in ['+','-']:
            if isinstance(t1, StringType) and isinstance(t2, StringType):
                code += self.emit.emitADDOP(ast.op, mtype, o['frame'])
                return code, StringType()
            code += self.emit.emitADDOP(ast.op, mtype, o['frame'])
            return code, mtype
        elif ast.op in ['*','/']:
            code += self.emit.emitMULOP(ast.op, mtype, o['frame'])
            return code, mtype
        elif ast.op in ['%']:
            code += self.emit.emitMOD(o['frame'])
            return code, IntType()
        elif ast.op in ['&&','||','==','!=','<','<=','>','>=']:
            code += self.emit.emitREOP(ast.op, mtype, o['frame'])
            return code, BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, o):
        e, t = self.visit(ast.body, o)
        if isinstance(t, FloatType):
            mtype = FloatType()
        else:
            mtype = IntType()
        
        if ast.op in ['-']:
            code += self.emit.emitNEGOP(mtype, o['frame'])
            return code, mtype
        elif ast.op in ['!']:
            code += self.emit.emitNOT(BoolType(), o['frame'])
            return code, BoolType()
    
    def visitFuncCall(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
        env = o.copy()
        env['isLeft'] = False
        [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
        self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
        return o
    
    def visitMethCall(self, ast, o):
        # likely invokestatic

        return o
        
    # ====================================LITERALS====================================

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitStringLiteral(self, ast, o):
        strLabel = ast.value.replace(" ","_").replace("\n","_").replace("\t","_")
        self.emit.printout(self.emit.emitATTRIBUTE(strLabel, StringType(), False, True, ast.value))
        return self.emit.emitGETSTATIC(f"{self.className}/{strLabel}", StringType(), o['frame']), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(1 if ast.value else 0, o['frame']), BoolType()
    
    def visitArrayLiteral(self, ast, o):
        return o
    
    def visitStructLiteral(self, ast, o):
        return o
    
    def visitNilLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(0, o['frame']), None
    
    # ====================================TYPES====================================

    def visitInttype(self, ast, o):
        return o
    
    def visitFloatType(self, ast, o):
        return o
    
    def visitStringType(self, ast, o):
        return o
    
    def visitBoolType(self, ast, o):
        return o
    
    def visitVoidType(self, ast, o):
        return o
    
    def visitArrayType(self, ast, o):
        return o
    
    def visitStructType(self, ast, o):
        return o
    
    def visitInterfaceType(self, ast, o):
        return o
    
    # ====================================STATEMENTS====================================

    def visitBlock(self, ast, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        env = reduce(lambda acc,e: self.visit(e,acc),ast.member,env)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitAssign(self, ast, o):
        env = o.copy()
        env['isLeft'] = True
        lhs = self.visit(ast.lhs,env)[0]
        rhs = self.visit(ast.rhs,env)[0]
        if type(lhs) is CName:
            self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{lhs}",rhs,o['frame']))
        else:
            self.emit.printout(lhs)
            self.emit.printout(rhs)
        return o
    
    def visitIf(self, ast: If, o):
        env = o.copy()
        env['isLeft'] = False
        e, t = self.visit(ast.expr, env)
        self.emit.printout(e)
        label0 = env['frame'].getNewLabel()
        label1 = env['frame'].getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(label0, env['frame']))
        self.visit(ast.thenStmt, env)
        
        if ast.elseStmt:
            self.emit.printout(self.emit.emitGOTO(label1, env['frame']))
            self.emit.printout(self.emit.emitLABEL(label0, env['frame']))
            self.visit(ast.elseStmt, env)
            self.emit.printout(self.emit.emitLABEL(label1, env['frame']))
        else:
            self.emit.printout(self.emit.emitLABEL(label0, env['frame']))
        return o
    
    def visitForBasic(self, ast, o):
        return o
    
    def visitForStep(self, ast: ForStep, o):
        env = o.copy()
        env['frame'].enterLoop() # trigger enterLoop to get break and continue label
        Break = env['frame'].getBreakLabel()
        Continue = env['frame'].getContinueLabel()
        For = env['frame'].getNewLabel()

        # assign value init to the loop variable
        env['isLeft'] = True
        iniAssign = self.visit(ast.init, env)[0]
        self.emit.printout(iniAssign)

        # for start
        env['isLeft'] = False
        self.emit.printout(self.emit.emitLABEL(For, env['frame']))

        # check condition
        e = self.visit(ast.cond, env)[0]
        self.emit.printout(e)
        self.emit.printout(self.emit.emitIFFALSE(Break, env['frame'])) # if false, jump to break label

        # go to body of for loop
        self.visit(ast.loop, env)

        # go to continue label
        self.emit.printout(self.emit.emitLABEL(Continue, env['frame']))

        # update loop variable
        env['isLeft'] = True
        update = self.visit(ast.upda, env)[0]
        self.emit.printout(update)

        # go to for label
        self.emit.printout(self.emit.emitGOTO(For, env['frame']))

        # go to break label
        self.emit.printout(self.emit.emitLABEL(Break, env['frame']))
        env['frame'].exitLoop()

        return o
    
    # No need to do forEach, just declare here for completed program
    def visitForEach(self, ast, o):
        return o
    
    def visitBreak(self, ast, o):
        env = o.copy()
        breakLabel = env["frame"].getBreakLabel()
        
        self.emit.printout(self.emit.emitGOTO(breakLabel, env['frame']))
        return o
    
    def visitContinue(self, ast, o):
        env = o.copy()
        continueLabel = env["frame"].getContinueLabel()

        self.emit.printout(self.emit.emitGOTO(continueLabel, env['frame']))
        return o
    
    def visitReturn(self, ast, o):
        env = o.copy()
        e, t = self.visit(ast.expr, env)
        # printout the expr of the return
        self.emit.printout(e)
        # printout the return statement
        self.emit.printout(self.emit.emitRETURN(t, env['frame']))
        return o

    
    

