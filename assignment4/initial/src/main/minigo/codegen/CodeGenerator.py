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

class Symbol:
    def __init__(self,name,mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class SymbolType(Symbol): # for struct and interface
    def __init__(self, name, mtype, field: List[Symbol] = None, method: List[Symbol] = [], value = None, isDeclared = False, member: List[Symbol] = None):
        self.name = name
        self.mtype = mtype
        self.field = field # None if interface
        self.method = method
        self.isDeclared = isDeclared
        self.member = member # only struct would use this, for combination of field and method in ordered way based on there apprearance

    def __str__(self):
        return "SymbolType(" + str(self.name) + "," + str(self.mtype) + ")"

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class Access(Val):
    def __init__(self, frame: Frame, symbol: Symbol, env: List[List[Symbol]], isLeft: bool):
        #frame: Frame
        #symbol: Symbol
        #env: Env
        #isLeft: Bool
        self.frame = frame
        self.symbol = symbol
        self.env = env
        self.isLeft = isLeft

class CName(Val):
    # This is used to tell which class this symbol belongs to
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
        self.globalSym = []
        self.initCode = [] # List of tuples (name, type, expr) for delayed initialization

    def init(self):
        mem = [Symbol("getInt", MType([],IntType()), CName("io",True)),
                Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("getFloat",MType([],FloatType()),CName("io",True)),
                Symbol("putFloat",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("putFloatLn",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("getBool",MType([],BoolType()), CName("io", True)),
                Symbol("putBool",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("getString",MType([],StringType()), CName("io", True)),
                Symbol("putString",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putStringLn",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putLn",MType([],VoidType()),CName("io",True)),
                ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init() # builtin method
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)

    def genStructClass(self, structName, fields, methods, path):
        classFile = self.path + "/" + structName + ".j"
        structEmit = Emitter(classFile)
        
        # Generate class
        structEmit.printout(structEmit.emitPROLOG(structName, "java/lang/Object"))
        
        # Generate fields
        for field in fields:
            fieldName, fieldType = field
            structEmit.printout(structEmit.emitATTRIBUTE(fieldName, fieldType, False, None))
        
        # Generate constructor
        frame = Frame("<init>", VoidType())
        structEmit.printout(structEmit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        structEmit.printout(structEmit.emitVAR(frame.getNewIndex(), "this", ClassType(structName), frame.getStartLabel(), frame.getEndLabel(), frame))
        structEmit.printout(structEmit.emitLABEL(frame.getStartLabel(), frame))
        structEmit.printout(structEmit.emitREADVAR("this", ClassType(structName), 0, frame))
        structEmit.printout(structEmit.emitINVOKESPECIAL(frame))
        structEmit.printout(structEmit.emitLABEL(frame.getEndLabel(), frame))
        structEmit.printout(structEmit.emitRETURN(VoidType(), frame))
        structEmit.printout(structEmit.emitENDMETHOD(frame))
        frame.exitScope()
        
        # Generate methods
        for method in methods:
            self.genStructMethod(method, structName, structEmit)
        
        structEmit.emitEPILOG()
       
    # can use this for references on creating new method in class
    def emitObjectInit(self, name):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Start defining method <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(name), frame.getStartLabel(), frame.getEndLabel(), frame))  # create "this" variable in <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(name), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  

        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  
    
    def emitObjectClinitMain(self):
        # perform creating clinic instance here
        frame = Frame("<clinit>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))  # Start defining method <clinit>, static

        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Emit delayed initializations
        for name, typ, expr in self.initCode:
            eInit, tInit = self.visit(expr, {'frame': frame, 'env': [[]], 'isLeft': False})
            self.emit.printout(eInit)
            self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{name}", typ, frame))
        
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))  # End of <clinit>


    def visitProgram(self, ast, c):
        # first scan for function
        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]

        # var a int = foo() + 1
        # const a = 1 + 2 * 3

        env ={}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a,x: self.visit(x,a), ast.decl, env)
        self.emitObjectInit(self.className)
        self.emitObjectClinitMain()
        self.emit.printout(self.emit.emitEPILOG())
        return env

    # ====================================DECLARATIONS====================================
    # Workaround for basic literals for now
    def visitVarDecl(self, ast: VarDecl, o):
        if 'frame' not in o: # global var, need to be fixed as there is no frame to use
            if ast.varType:
                o['env'][-1].insert(0, Symbol(ast.varName, ast.varType, CName(self.className)))
                if isinstance(ast.varInit, (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral)):
                    # For simple literals, emit directly as attribute value
                    self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, str(ast.varInit.value) if ast.varInit else None))
                else:
                    # For complex expressions, delay initialization to <init>
                    self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, None))
                    self.initCode.append((ast.varName, ast.varType, ast.varInit))
            else:
                # For variables without explicit type, create a temporary frame to infer the type
                temp_frame = Frame("temp", VoidType())
                temp_env = o.copy()
                temp_env['frame'] = temp_frame
                _, tInit = self.visit(ast.varInit, temp_env)
                
                o['env'][-1].insert(0, Symbol(ast.varName, tInit, CName(self.className)))
                
                if isinstance(ast.varInit, (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral)):
                    # For simple literals, emit directly
                    self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, tInit, True, False, str(ast.varInit.value) if ast.varInit else None))
                else:
                    # For complex expressions, delay initialization to <clinit>
                    self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, tInit, True, False, None))
                    self.initCode.append((ast.varName, tInit, ast.varInit))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            if ast.varType:
                # Add the variable to environment first
                o['env'][0].insert(0, Symbol(ast.varName, ast.varType, Index(index)))
                
                # Emit variable declaration
                self.emit.printout(self.emit.emitVAR(index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
                
                if ast.varInit:
                    if isinstance(ast.varType, ArrayType) and isinstance(ast.varInit, ArrayLiteral):
                        # Handle array initialization - push array onto stack
                        eInit, _ = self.visit(ast.varInit, o)
                        self.emit.printout(eInit)
                    else:
                        eInit, _ = self.visit(ast.varInit, o)
                        self.emit.printout(eInit)
                    self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
                else:
                    if isinstance(ast.varType, ArrayType):
                        # Create empty array
                        if len(ast.varType.dimens) == 1:
                            # 1D array - use newarray/anewarray
                            dimCode, _ = self.visit(ast.varType.dimens[0], o)
                            self.emit.printout(dimCode)
                            
                            if isinstance(ast.varType.eleType, (IntType, FloatType, BoolType)):
                                eleTypeStr = self.emit.getFullType(ast.varType.eleType)
                                self.emit.printout(self.emit.jvm.emitNEWARRAY(eleTypeStr))
                            else:
                                self.emit.printout(self.emit.jvm.emitANEWARRAY(self.emit.getJVMType(ast.varType.eleType)))
                        else:
                            # Multi-dimensional array - use multianewarray
                            for dim in ast.varType.dimens:
                                dimCode, _ = self.visit(dim, o)
                                self.emit.printout(dimCode)
                            
                            self.emit.printout(self.emit.jvm.emitMULTIANEWARRAY(
                                self.emit.getJVMType(ast.varType), 
                                str(len(ast.varType.dimens))
                            ))
                        
                        self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
                    else:
                        # Use default value for non-array types
                        eInit = self.get_default_value(ast.varType)
                        self.emit.printout(self.emit.emitPUSHCONST(eInit, frame))
                        self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
            else:
                # there obviously is varInit if no varType here
                eInit, tInit = self.visit(ast.varInit, o)
                o['env'][0].insert(0, Symbol(ast.varName, tInit, Index(index)))
                self.emit.printout(self.emit.emitVAR(index, ast.varName, tInit, frame.getStartLabel(), frame.getEndLabel(), frame))
                self.emit.printout(eInit)
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, tInit, index,  frame))
                # self.printEnv(o['env'])
        
        return o
    
    def visitConstDecl(self, ast: ConstDecl, o):
        # would perform the exact global var in vardecl with isFinal = True
        if 'frame' not in o: # global const
            # For variables without explicit type, create a temporary frame to infer the type
            temp_frame = Frame("temp", VoidType())
            temp_env = o.copy()
            temp_env['frame'] = temp_frame
            
            _, tInit = self.visit(ast.iniExpr, temp_env)
            
            o['env'][-1].insert(0, Symbol(ast.conName, tInit, CName(self.className)))
            
            if isinstance(ast.iniExpr, (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral)):
                # For simple literals, emit directly
                self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, tInit, True, True, str(ast.iniExpr.value) ))
            else:
                initValue = self.inferValueConstant(ast.iniExpr)
                self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, tInit, True, True, str(initValue)))
        else:
            # when const declaration in local, treat is exactly the same as var
            frame = o['frame']
            e, typ = self.visit(ast.iniExpr, o)
            index = frame.getNewIndex()
            o['env'][0].insert(0, Symbol(ast.conName, typ, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.conName, typ, frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(e)
            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, typ, index, frame))
            # self.printEnv(o['env'])
        
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
        o['env'][-1].insert(0, Symbol(ast.name, mtype, CName(self.className)))
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
    

    def visitArrayType(self, ast: ArrayType, o):
        # @dimens: List[int]
        # @eleType: Type
        
        o['isLeft'] = False
        code = ""
        
        # Only emit dimension sizes for arrays without initialization
        # For arrays with initialization, this will be handled by visitArrayLiteral
        for dim in ast.dimens:
            e, t = self.visit(dim, o)
            code += e
        
        code += self.emit.emitNEWARRAY(ast, o['frame'])
        
        return code, ast

    def visitStructType(self, ast: StructType, o):
        # @name: str
        # @elements:List[Tuple[str,Type]]
        # @methods:List[MethodDecl]
        # @implements:List[InterfaceType] =  field(default_factory=list)

        frame = Frame(ast.name, VoidType())
        o['env'][-1].insert(0, Symbol(ast.name, ClassType(ast.name), None))


        # use emitPROLOG
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))

        # process field
        for element in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(element[0], element[1], True, False, None))

        # would be methods here, saved for later
        

        # init - constructor
        self.emitObjectInit(ast.name)

        
        return o
    
    def visitInterfaceType(self, ast, o):
        return o

    
    # ====================================EXPRESSIONS====================================
    
    def visitId(self, ast, o):
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        if sym is None:
            return "", None
        else:
            if type(sym.value) is Index:
                # local var
                if o['isLeft'] is False:
                    return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
                else:
                    return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:         
                # global var
                if o['isLeft'] is False:
                    return self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame']), sym.mtype
                else:
                    return self.emit.emitPUTSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame']), sym.mtype
    
    def visitArrayCell(self, ast: ArrayCell, o):
        code = ""
        mtype = None
        # find the symbol of array to get index
        if isinstance(ast.arr, Id):
            sym = next(filter(lambda x: x.name == ast.arr.name, [j for i in o['env'] for j in i]),None)
            if sym is None:
                return "", None
            else:
                if type(sym.value) is Index:
                    # local var
                    code += self.emit.emitREADVAR(ast.arr.name, sym.mtype, sym.value.value, o['frame'])
                else:         
                    # global var
                    code += self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame'])

            mtype = sym.mtype.eleType if isinstance(sym.mtype, ArrayType) else sym.mtype
        else:
            e, t = self.visit(ast.arr, o)
            code += e
        
        # for 1D array first
        if len(ast.idx) == 1:
            e, t = self.visit(ast.idx[0], o)
            code += e
            mtype = t
        else:
            # load each array
            for i in range(len(ast.idx)):
                e, t = self.visit(ast.idx[i], o)
                code += e
                if i < len(ast.idx) - 1:
                    code += self.emit.emitALOAD(ArrayType([None], t), o['frame'])

        if o['isLeft'] is False:
            # normal case first
            code += self.emit.emitALOAD(IntType(), o['frame'])
        else:
            # store would appear after RHS, so nothing here
            pass
        return code, mtype
    
    def visitFieldAccess(self, ast: FieldAccess, o):
        return o
    
    def visitBinaryOp(self, ast: BinaryOp, o):
        o['isLeft'] = False
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
        elif ast.op in ['==','!=','<','<=','>','>=']:
            code += self.emit.emitREOP(ast.op, mtype, o['frame'])
            return code, BoolType()
        elif ast.op in ['&&','||']:
            code += self.emit.emitANDOP( o['frame']) if ast.op == '&&' else self.emit.emitOROP(o['frame'])
            return code, BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, o):
        e, t = self.visit(ast.body, o)
        code = e
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
    
    def visitFuncCall(self, ast: FuncCall, o):
        # would be two case: being statement (voidtype) and expression, stmt would return o and exp return code + type
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function),None)

        env = o.copy()
        env['isLeft'] = False

        if type(sym.mtype.rettype) is VoidType:
            [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
            
            # sym.value.value is classname

            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame']))
            return o
        else:
            code = ""
            for arg in ast.args:
                code += self.visit(arg, env)[0]
            
            code += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])
            return code, sym.mtype.rettype
            
    
    def visitMethCall(self, ast, o):
        # likely invokestatic

        return o
        
    # ====================================LITERALS====================================

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitStringLiteral(self, ast: StringLiteral, o):
        # if 'frame' not in o:
        #     # global var
        #     strLabel = ast.value.replace(" ","_").replace("\n","_").replace("\t","_").replace("\"","")
        #     # self.emit.printout(self.emit.emitATTRIBUTE(strLabel, StringType(), False, True, ast.value))

        #     return self.emit.emitGETSTATIC(f"{self.className}/{strLabel}", StringType(), o['frame']), StringType()
        # else:
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()    

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(1 if ast.value else 0, o['frame']), BoolType()
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o):
        code = ""
        dimensions = ast.dimens
        eleType = ast.eleType
        values = ast.value
        
        # Handle array creation based on dimensions
        if len(dimensions) == 1:
            # 1D array - use newarray or anewarray
            dimValue = dimensions[0].value if hasattr(dimensions[0], 'value') else len(values)
            code += self.emit.emitPUSHICONST(dimValue, o['frame'])
            
            if isinstance(eleType, (IntType, FloatType, BoolType)):
                # For primitive types
                eleTypeStr = self.emit.getFullType(eleType)
                code += self.emit.jvm.emitNEWARRAY(eleTypeStr)
            else:
                # For reference types like String, arrays, or user-defined types
                code += self.emit.jvm.emitANEWARRAY(self.emit.getJVMType(eleType))
            
            # Initialize array elements
            for i, val in enumerate(values):
                code += self.emit.emitDUP(o['frame'])  # Duplicate array reference
                code += self.emit.emitPUSHICONST(i, o['frame'])  # Array index
                
                # Push value
                valCode, _ = self.visit(val, o)
                code += valCode
                
                # Store in array
                code += self.emit.emitASTORE(eleType, o['frame'])
        else:
            # Multi-dimensional array - use multianewarray
            for dim in dimensions:
                dimValue = dim.value if hasattr(dim, 'value') else len(values)
                code += self.emit.emitPUSHICONST(dimValue, o['frame'])
            
            # Create the multi-dimensional array
            code += self.emit.jvm.emitMULTIANEWARRAY(
                self.emit.getJVMType(ArrayType(dimensions, eleType)), 
                str(len(dimensions))
            )
            
            # For 2D arrays, we need to handle initialization differently
            if len(dimensions) == 2:
                # For each row
                for i, row in enumerate(values):
                    # For each column in this row
                    for j, val in enumerate(row):
                        code += self.emit.emitDUP(o['frame'])  # Duplicate array reference
                        code += self.emit.emitPUSHICONST(i, o['frame'])  # Row index
                        code += self.emit.jvm.emitAALOAD()  # Get row array
                        code += self.emit.emitPUSHICONST(j, o['frame'])  # Column index
                        
                        # Push value
                        valCode, _ = self.visit(val, o)
                        code += valCode
                        
                        # Store value
                        code += self.emit.emitASTORE(eleType, o['frame'])
            else:
                # For 3D+ arrays, use recursive initialization
                code += self.initMultiDimArray(values, [], dimensions, eleType, o)
        
        return code, ArrayType(dimensions, eleType)

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
    
    def visitAssign(self, ast: Assign, o):
        env = o.copy()
        env['isLeft'] = False
        rhs, rTyp = self.visit(ast.rhs, env)
        if not isinstance(ast.lhs, ArrayCell):
            self.emit.printout(rhs)

        # := quick declaration, so we need to check if the lhs is declared, else declare it

        env['isLeft'] = True
        lhs, lTyp = self.visit(ast.lhs, env)
        if isinstance(ast.lhs, Id) and lTyp is None:
            # if lhs is not declared, we need to declare it
            index = env['frame'].getNewIndex()
            env['env'][0].insert(0, Symbol(ast.lhs.name, rTyp, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.lhs.name, rTyp, env['frame'].getStartLabel(), env['frame'].getEndLabel(), env['frame']))
            self.emit.printout(self.emit.emitWRITEVAR(ast.lhs.name, rTyp, index, env['frame']))

        self.emit.printout(lhs)

        if isinstance(ast.lhs, ArrayCell):
            self.emit.printout(rhs)
            self.emit.printout(self.emit.emitASTORE(IntType(), o['frame']))

        # if type(lhs) is CName:
        #     self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{lhs}",rhs,o['frame']))
        # else:
        #     self.emit.printout(lhs)
        #     self.emit.printout(rhs)
        return o
    
    def visitIf(self, ast: If, o):
        env = o.copy()
        label0 = env['frame'].getNewLabel()
        label1 = env['frame'].getNewLabel()
        env['isLeft'] = False
        e, t = self.visit(ast.expr, env)
        self.emit.printout(e)
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
    
    def visitForBasic(self, ast: ForBasic, o):
        env = o.copy()
        env['frame'].enterLoop() # trigger enterLoop to get break and continue label
        Break = env['frame'].getBreakLabel()
        Continue = env['frame'].getContinueLabel()
        
        self.emit.printout(self.emit.emitLABEL(Continue, env['frame']))
        # only check condition here in for basic
        env['isLeft'] = False
        e = self.visit(ast.cond, env)[0]
        self.emit.printout(e)
        self.emit.printout(self.emit.emitIFFALSE(Break, env['frame']))

        # go to body of for loop
        env['isLeft'] = False

        self.visit(ast.loop, env)

        # go to continue label
        self.emit.printout(self.emit.emitGOTO(Continue, env['frame']))

        # emit break label
        self.emit.printout(self.emit.emitLABEL(Break, env['frame']))
        env['frame'].exitLoop()

        return o
    
    def visitForStep(self, ast: ForStep, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterLoop() # trigger enterLoop to get break and continue label
        Break = env['frame'].getBreakLabel()
        Continue = env['frame'].getContinueLabel()
        For = env['frame'].getNewLabel()

        # assign value init to the loop variable
        env['isLeft'] = True
        self.visit(ast.init, env)

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
        self.visit(ast.upda, env)

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

    # ====================================HELPER FUNCTIONS====================================

    def infer_type(self, ast, o): # this would be very likely to get type of global var
        pass

    def get_default_value(self, t):
        if isinstance(t, IntType):
            return 0
        elif isinstance(t, FloatType):
            return 0.0
        elif isinstance(t, BoolType):
            return False
        elif isinstance(t, StringType):
            return ""
        elif isinstance(t, ArrayType):
            return None
        else:
            return None
    
    def firstScan(self, ast: Program):
        for decl in ast.decl:
            if isinstance(decl, FuncDecl) or isinstance(decl, StructType) or isinstance(decl, InterfaceType):
                self.globalSym.append(decl)
    

    def inferValueConstant(self, ast): 
        if isinstance(ast, IntLiteral):
            if type(ast.value) is str:
                if ast.value.startswith("0x") or ast.value.startswith("0X"):
                    return int(ast.value, 16)
                elif ast.value.startswith("0b") or ast.value.startswith("0B"):
                    return int(ast.value, 2)
                elif ast.value.startswith("0o") or ast.value.startswith("0O"):
                    return int(ast.value, 8)
                return int(ast.value)
            return int(ast.value)
        elif isinstance(ast, FloatLiteral):
            return ast.value
        elif isinstance(ast, StringLiteral):
            return ast.value
        elif isinstance(ast, BooleanLiteral):
            return ast.value
        elif isinstance(ast, ArrayLiteral):
            return [self.inferValueConstant(x) for x in ast.value]
        elif isinstance(ast, BinaryOp):
            left = self.inferValueConstant(ast.left)
            right = self.inferValueConstant(ast.right)
            if ast.op == '+':
                return left + right
            elif ast.op == '-':
                return left - right
            elif ast.op == '*':
                return left * right
            elif ast.op == '/':
                return left / right
            elif ast.op == '%':
                return left % right
            elif ast.op == '==':
                return left == right
            elif ast.op == '!=':
                return left != right
            elif ast.op == '<':
                return left < right
            elif ast.op == '<=':
                return left <= right
            elif ast.op == '>':
                return left > right
            elif ast.op == '>=':
                return left >= right
        elif isinstance(ast, UnaryOp):
            value = self.inferValueConstant(ast.body)
            if ast.op == '-':
                return -value
            elif ast.op == '!':
                return not value
            
    
    def printEnv(self, c: List[List[Symbol]]):
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
                            "mtype": symbol.mtype,
                            "value": symbol.value.value
                        }
                    scope_info.append(symbol_info)
            result.append(scope_info)
        
        print(result)

    def initMultiDimArray(self, values, indices, dimensions, eleType, o):
        """Initialize elements in a multi-dimensional array"""
        if not values:
            return ""
        
        code = ""
        
        if len(indices) == len(dimensions) - 1:
            # At innermost level (1D array) - we need to get the row array first
            for i, val in enumerate(values):
                if i >= dimensions[-1].value if hasattr(dimensions[-1], 'value') else len(values):
                    break
                    
                code += self.emit.emitDUP(o['frame'])  # Duplicate main array reference
                
                # For 2D arrays, first get the row array
                if len(dimensions) == 2:
                    # Push row index
                    code += self.emit.emitPUSHICONST(indices[0], o['frame'])
                    # Get the row array (a[row])
                    code += self.emit.jvm.emitAALOAD()
                    # Push column index
                    code += self.emit.emitPUSHICONST(i, o['frame'])
                else:
                    # For deeper dimensions, push all indices except the last
                    for idx in indices:
                        code += self.emit.emitPUSHICONST(idx, o['frame'])
                        code += self.emit.jvm.emitAALOAD()  # Get the sub-array at each level
                    # Push final index
                    code += self.emit.emitPUSHICONST(i, o['frame'])
                
                # Push value
                valCode, _ = self.visit(val, o)
                code += valCode
                
                # Store using appropriate type
                if isinstance(eleType, IntType):
                    code += self.emit.jvm.emitIASTORE()
                elif isinstance(eleType, FloatType):
                    code += self.emit.jvm.emitFASTORE()
                elif isinstance(eleType, BoolType):
                    code += self.emit.jvm.emitBASTORE()
                else:
                    code += self.emit.jvm.emitAASTORE()
        else:
            # For higher dimensions, we need to handle nested arrays differently
            for i, subarray in enumerate(values):
                if i >= dimensions[len(indices)].value if hasattr(dimensions[len(indices)], 'value') else len(values):
                    break
                
                # For each sub-array at current dimension, we need to:
                # 1. Get the array at the current level of indices
                # 2. Then continue recursive initialization
                
                # Create path to the current sub-array
                new_indices = indices + [i]
                code += self.initMultiDimArray(subarray, new_indices, dimensions, eleType, o)
        
        return code

