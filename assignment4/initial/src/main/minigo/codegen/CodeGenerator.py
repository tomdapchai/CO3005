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
    def __init__(self, name, mtype, field: List[Symbol] = None, method: List[Symbol] = [], value = None):
        self.name = name
        self.mtype = mtype
        self.field = field # None if interface
        self.method = method

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
        self.structs = []
        self.interfaces = []
        self.list_function = [] # List of functions in the program
        self.firstscan = True

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
       
    # can use this for references on creating new method in class
    def emitObject(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Start defining method <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # create "this" variable in <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  

        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  
    
    def emitObjectClinit(self, env):
        # perform creating clinic instance here
        frame = Frame("<clinit>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))  # Start defining method <clinit>, static
        
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Emit delayed initializations
        for name, typ, expr in self.initCode:
            if isinstance(typ, Id) and expr is None: 
                # create new instance 
                isStruct = True
                struct = next(filter(lambda x: x.name == typ.name, self.structs),None)
                if struct is None:
                    isStruct = False
                if isStruct:
                    self.emit.printout(self.emit.emitNEW(typ.name, frame))
                    self.emit.printout(self.emit.emitDUP(frame))
                    self.emit.printout(self.emit.emitINVOKESPECIAL(lexeme=f"{typ.name}/<init>", in_=MType([], VoidType()), frame=frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{name}", typ, frame))
            elif isinstance(typ, ArrayType) and expr is None:
                pass
            else:
                eInit, tInit = self.visit(expr, {'frame': frame, 'env': env, 'isLeft': False})
                self.emit.printout(eInit)
                self.emit.printout(self.emit.emitPUTSTATIC(f"{self.className}/{name}", typ, frame))
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))  # End of <clinit>


    def visitProgram(self, ast: Program, c):
        # first scan for function
        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        decls = [item for item in ast.decl if isinstance(item, (VarDecl, ConstDecl))]

        # scan for methods
        self.MethScan(ast)
        for struct in self.structs:
            implemented = self.ImplementScan(struct)
            struct.implements = implemented
        
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # visit struct and interface
        env ={}
        env['env'] = [c]

        for decl in decls:
            self.visit(decl, env)

        for interface in self.interfaces:
            self.visit(interface, env)

        for struct in self.structs:
            self.visit(struct, env)
        
        self.firstscan = False
        env = reduce(lambda a,x: self.visit(x,a), ast.decl, env)
        self.emitObject()
        self.emitObjectClinit(env['env'])
        self.emit.printout(self.emit.emitEPILOG())
        return env

    # ====================================DECLARATIONS====================================
    # Workaround for basic literals for now
    def visitVarDecl(self, ast: VarDecl, o):
        if 'frame' not in o: # global var, need to be fixed as there is no frame to use
            if self.firstscan is True:
                if ast.varType:
                    o['env'][-1].insert(0, Symbol(ast.varName, ast.varType, CName(self.className)))
                    if ast.varInit:
                        if isinstance(ast.varInit, (IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral)):
                            # For simple literals, emit directly as attribute value
                            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, str(ast.varInit.value)))
                        else:
                            # For complex expressions, delay initialization to <init>
                            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, None))
                            self.initCode.append((ast.varName, ast.varType, ast.varInit))
                    else:
                        # For variables without explicit initialization, just emit the attribute
                        if isinstance(ast.varType, (IntType, FloatType, BoolType, StringType, Id)):
                            
                            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, None))
                            if isinstance(ast.varType, Id):
                                self.initCode.append((ast.varName, ast.varType, None))
                        elif isinstance(ast.varType, ArrayType):
                            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, None))
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
                pass
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            if ast.varType:
                # Add the variable to environment first
                o['env'][0].insert(0, Symbol(ast.varName, ast.varType, Index(index)))
                
                # Emit variable declaration
                self.emit.printout(self.emit.emitVAR(index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
                
                if ast.varInit:
                    o['isLeft'] = False
                    if isinstance(ast.varType, ArrayType) and isinstance(ast.varInit, ArrayLiteral):
                        # Handle array initialization - push array onto stack
                        eInit, t = self.visit(ast.varInit, o)
                        self.emit.printout(eInit)
                    else:
                        eInit, t = self.visit(ast.varInit, o)
                        self.emit.printout(eInit)
                        # very rare case, type is float and init is int, need to i2f
                        if isinstance(ast.varType, FloatType) and isinstance(t, IntType):
                            self.emit.printout(self.emit.emitI2F(frame))
                    self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))

                else:
                    if isinstance(ast.varType, ArrayType):
                        # Create empty array
                        if len(ast.varType.dimens) == 1:
                            # 1D array - use newarray/anewarray
                            o['isLeft'] = False
                            dimCode, _ = self.visit(ast.varType.dimens[0], o)
                            self.emit.printout(dimCode)
                            
                            if isinstance(ast.varType.eleType, (IntType, FloatType, BoolType)):
                                eleTypeStr = self.emit.getFullType(ast.varType.eleType)
                                self.emit.printout(self.emit.jvm.emitNEWARRAY(eleTypeStr))
                            else:
                                self.emit.printout(self.emit.jvm.emitANEWARRAY(self.emit.getFullType(ast.varType.eleType)))
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
                        if isinstance(ast.varType, (IntType, FloatType, StringType, BoolType)):
                            eInit = self.get_default_value(ast.varType)
                            self.emit.printout(self.emit.emitPUSHCONST(eInit, ast.varType ,frame))
                            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
                        elif isinstance(ast.varType, Id):
                            # check if Id is struct or interface from self.structs and self.interface
                            isStruct = True
                            struct = next(filter(lambda x: x.name == ast.varType.name, self.structs),None)

                            if struct is None:
                                isStruct = False
                                
                            if isStruct:
                                self.emit.printout(self.emit.emitNEW(ast.varType.name, frame))
                                self.emit.printout(self.emit.emitDUP(frame))
                                self.emit.printout(self.emit.emitINVOKESPECIAL(lexeme=f"{ast.varType.name}/<init>", in_=MType([], VoidType()), frame=frame))
                                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))
                            else:
                                # interface
                                pass
                            
                        
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
            if self.firstscan is True:
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
                pass
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
            for param in ast.params:
                paramName = param.parName
                paramType = param.parType
                index = frame.getNewIndex()
                env['env'][0].insert(0, Symbol(paramName, paramType, Index(index)))
                self.emit.printout(self.emit.emitVAR(index, paramName, paramType, frame.getStartLabel(), frame.getEndLabel(), frame))

        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        return o
    

    def visitMethodDecl(self, ast: MethodDecl, o):
        # o here has: 'env': List[List[Symbol]], 'frame': Frame, 'isLeft': bool, 'emit': Emitter
        # not gonna use self.emit here, so just use o['emit'] instead
        # would likely be the same as funcdecl
        if 'emit' not in o: # means this is accessed from global program
            return o
        mtype = MType(list(map(lambda x: x.parType, ast.fun.params)), ast.fun.retType)

        o['env'][-1].insert(0, Symbol(ast.fun.name, mtype, CName(ast.recType.name)))
        env = o.copy()
        env['frame'] = Frame(ast.fun.name, ast.fun.retType)
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, env['frame']))

        env['frame'].enterScope(True)
        # emit this
        self.emit.printout(self.emit.emitVAR(env['frame'].getNewIndex(), "this", ClassType(ast.recType.name), env['frame'].getStartLabel(), env['frame'].getEndLabel(), env['frame']))

        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        env['env'] = [[]] + env['env']

        # add receiver to env - workaround for now
        env['env'][0].insert(0, Symbol(ast.receiver, ast.recType, Index(0))) # "this" - receiver
        
        # add params to env
        env['env'] = [[]] + env['env']
        env = reduce(lambda acc,e: self.visit(e,acc),ast.fun.params,env)

        for param in ast.fun.params:
            paramName = param.parName
            paramType = param.parType
            index = env['frame'].getNewIndex()
            env['env'][0].insert(0, Symbol(paramName, paramType, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, paramName, paramType, env['frame'].getStartLabel(), env['frame'].getEndLabel(), env['frame']))

        env = self.visit(ast.fun.body, env)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), env['frame']))
        self.emit.printout(self.emit.emitENDMETHOD(env['frame']))
        env['frame'].exitScope()
        
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
        if self.firstscan is False:
            return o

        o['env'][-1].insert(0, SymbolType(ast.name, ast, ast.elements, ast.methods))

        classFile = self.path + "/" + ast.name + ".j"
        structEmit = Emitter(classFile)
        
        # Generate class
        structEmit.printout(structEmit.emitPROLOG(ast.name, "java/lang/Object"))
        
        # generate implements
        for implement in ast.implements:
            structEmit.printout(".implements " + implement + "\n")

        # Generate fields
        for field in ast.elements:
            fieldName, fieldType = field
            structEmit.printout(structEmit.emitATTRIBUTE(fieldName, fieldType, False, False, None))
        
        # Generate constructor
        frame = Frame("<init>", VoidType())
        structEmit.printout(structEmit.emitMETHOD("<init>", MType([x[1] for x in ast.elements], VoidType()), False, frame))
        frame.enterScope(True)
        structEmit.printout(structEmit.emitVAR(frame.getNewIndex(), "this", ClassType(ast.name), frame.getStartLabel(), frame.getEndLabel(), frame))
        
        # Generate fields variables
        # Convert each field tuple to include the index
        new_elements = []
        for field in ast.elements:
            fieldName, fieldType = field
            index = frame.getNewIndex()
            # Create new tuple with three elements: (name, type, index)
            new_elements.append((fieldName, fieldType, index))
            structEmit.printout(structEmit.emitVAR(index, fieldName, fieldType, frame.getStartLabel(), frame.getEndLabel(), frame))
        

        structEmit.printout(structEmit.emitLABEL(frame.getStartLabel(), frame))
        structEmit.printout(structEmit.emitREADVAR("this", ClassType(ast.name), 0, frame))
        structEmit.printout(structEmit.emitINVOKESPECIAL(frame))

        # Initialize fields
        for field in new_elements:
            fieldName, fieldType, index = field
            # frame.push()
            structEmit.printout(structEmit.emitREADVAR("this", ClassType(ast.name), 0, frame))
            # frame.push()
            structEmit.printout(structEmit.emitREADVAR(fieldName, fieldType, index, frame))
            # frame.pop() x 2
            structEmit.printout(structEmit.emitPUTFIELD(f"{ast.name}/{fieldName}", fieldType, frame))


        structEmit.printout(structEmit.emitLABEL(frame.getEndLabel(), frame))
        structEmit.printout(structEmit.emitRETURN(VoidType(), frame))
        structEmit.printout(structEmit.emitENDMETHOD(frame))
        frame.exitScope()

        # default constructor with no args
        frame = Frame("<init>", VoidType())
        structEmit.printout(structEmit.emitMETHOD("<init>", MType([], VoidType()), False, frame))
        frame.enterScope(True)
        structEmit.printout(structEmit.emitVAR(frame.getNewIndex(), "this", ClassType(ast.name), frame.getStartLabel(), frame.getEndLabel(), frame))
        structEmit.printout(structEmit.emitLABEL(frame.getStartLabel(), frame))
        structEmit.printout(structEmit.emitREADVAR("this", ClassType(ast.name), 0, frame))
        structEmit.printout(structEmit.emitINVOKESPECIAL(frame))
        structEmit.printout(structEmit.emitLABEL(frame.getEndLabel(), frame))
        structEmit.printout(structEmit.emitRETURN(VoidType(), frame))
        structEmit.printout(structEmit.emitENDMETHOD(frame))
        frame.exitScope()

        
        # Generate methods
        env = o.copy()
        env['emit'] = structEmit

        initEmit = self.emit
        self.emit = structEmit
        for method in ast.methods:
            self.visit(method, env)
        self.emit = initEmit
        
        structEmit.emitEPILOG()
        
        
        return o
    
    def visitInterfaceType(self, ast: InterfaceType, o):
        if self.firstscan is False:
            return o

        o['env'][-1].insert(0, SymbolType(ast.name, ast, None, ast.methods))

        classFile = self.path + "/" + ast.name + ".j"
        interfaceEmit = Emitter(classFile)

        # Generate class
        interfaceEmit.printout(interfaceEmit.emitINTERFACE(ast.name, "java/lang/Object", ast.methods))

        interfaceEmit.emitEPILOG()

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
        initLeft = o['isLeft']
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
            o['isLeft'] = False
            e, t = self.visit(ast.arr, o)
            o['isLeft'] = initLeft
            code += e
            mtype = t.eleType if isinstance(t, ArrayType) else t
        
        # for 1D array first
        if len(ast.idx) == 1:
            o['isLeft'] = False
            e, t = self.visit(ast.idx[0], o)
            o['isLeft'] = initLeft
            code += e
        else:
            # load each array
            for i in range(len(ast.idx)):
                o['isLeft'] = False
                e, t = self.visit(ast.idx[i], o)
                o['isLeft'] = initLeft
                code += e
                if i < len(ast.idx) - 1:
                    code += self.emit.emitALOAD(ArrayType([None], mtype), o['frame'])

        if o['isLeft'] is False:
            # normal case first
            code += self.emit.emitALOAD(mtype, o['frame'])
        else:
            # store would appear after RHS, so nothing here
            pass
        return code, mtype
    
    def visitFieldAccess(self, ast: FieldAccess, o):
        # find the symbol of caller to get index
        code = ""
        mtype = None
        initLeft = o['isLeft']
        
        if o['isLeft'] == False:
            if isinstance(ast.receiver, Id):
                sym = next(filter(lambda x: x.name == ast.receiver.name, [j for i in o['env'] for j in i]),None)

                # find the type of the field from sym.mtype - the struct

                # struct = next(filter(lambda x: isinstance(x, SymbolType) and x.name == sym.mtype.name, [j for i in o['env'] for j in i]),None)
                struct : StructType = next(filter(lambda x: x.name == sym.mtype.name, self.structs), None)

                # there will always be struct
                mtype = next(filter(lambda x: x[0] == ast.field, struct.elements),None)[1]
                
                if type(sym.value) is Index:
                    # local var
                    code += self.emit.emitREADVAR(ast.receiver.name, sym.mtype, sym.value.value , o['frame'])
                else:         
                    # global var
                    code += self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame'])
                code += self.emit.emitGETFIELD(f"{sym.mtype.name}/{ast.field}", mtype, o['frame'])
            else:
                o['isLeft'] = False
                e, t = self.visit(ast.receiver, o)
                o['isLeft'] = initLeft
                code += e

                # find struct
                struct : StructType = next(filter(lambda x: x.name == t.name, self.structs), None)

                # find the type of the field from struct
                mtype = next(filter(lambda x: x[0] == ast.field, struct.elements), None)[1]

                code += self.emit.emitGETFIELD(f"{t.name}/{ast.field}", mtype, o['frame'])
            
        else:
            if isinstance(ast.receiver, Id):
                sym = next(filter(lambda x: x.name == ast.receiver.name, [j for i in o['env'] for j in i]),None)

                struct = next(filter(lambda x: x.name == sym.mtype.name, self.structs),None)
                # struct = next(filter(lambda x: isinstance(x, SymbolType) and x.name == sym.mtype.name, [j for i in o['env'] for j in i]),None)

                # there will always be struct
                mtype = next(filter(lambda x: x[0] == ast.field, struct.elements),None)[1]
                if type(sym.value) is Index:
                    # local var
                    code += self.emit.emitREADVAR(ast.receiver.name, sym.mtype, sym.value.value , o['frame'])
                else:         
                    # global var
                    code += self.emit.emitGETSTATIC(f"{self.className}/{sym.name}",sym.mtype,o['frame'])
                
                code += self.emit.emitPUTFIELD(f"{sym.mtype.name}/{ast.field}", mtype, o['frame'])
            else: # it's field access again
                o['isLeft'] = False
                e, t = self.visit(ast.receiver, o)
                code += e
                o['isLeft'] = initLeft
                # find struct
                struct = next(filter(lambda x: x.name == t.name, self.structs), None)

                # find the type of the field from struct
                mtype = next(filter(lambda x: x[0] == ast.field, struct.elements),None)[1]

                code += self.emit.emitPUTFIELD(f"{t.name}/{ast.field}", mtype, o['frame'])
            

        return code, mtype
    
    def visitBinaryOp(self, ast: BinaryOp, o):
        o['isLeft'] = False
        e1, t1 = self.visit(ast.left, o)
        e2, t2 = self.visit(ast.right, o)

        if isinstance(t1, FloatType) or isinstance(t2, FloatType):
            mtype = FloatType()
        elif isinstance(t1, IntType) and isinstance(t2, IntType):
            mtype = IntType()
        elif isinstance(t1, StringType) and isinstance(t2, StringType):
            mtype = StringType()
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
            # Implement short-circuit evaluation
            result = ""
            labelEnd = o['frame'].getNewLabel()
            
            if ast.op == '&&':
                # For AND: if left is false, skip right operand
                labelFalse = o['frame'].getNewLabel()
                result += e1    # Evaluate left operand
                result += self.emit.emitIFFALSE(labelFalse, o['frame'])  # If left is false, jump to labelFalse
                result += e2    # Evaluate right operand
                result += self.emit.emitIFFALSE(labelFalse, o['frame'])  # If right is false, jump to labelFalse
                result += self.emit.emitPUSHCONST("true", BoolType(), o['frame'])  # Push true
                result += self.emit.emitGOTO(labelEnd, o['frame'])  # Jump to end
                result += self.emit.emitLABEL(labelFalse, o['frame'])  # Label for false case
                result += self.emit.emitPUSHCONST("false", BoolType(), o['frame'])  # Push false
                result += self.emit.emitLABEL(labelEnd, o['frame'])  # End label
            else:  # for OR
                # For OR: if left is true, skip right operand
                labelTrue = o['frame'].getNewLabel()
                result += e1    # Evaluate left operand
                result += self.emit.emitIFTRUE(labelTrue, o['frame'])  # If left is true, jump to labelTrue
                result += e2    # Evaluate right operand
                result += self.emit.emitIFTRUE(labelTrue, o['frame'])  # If right is true, jump to labelTrue
                result += self.emit.emitPUSHCONST("false", BoolType(), o['frame'])  # Push false
                result += self.emit.emitGOTO(labelEnd, o['frame'])  # Jump to end
                result += self.emit.emitLABEL(labelTrue, o['frame'])  # Label for true case
                result += self.emit.emitPUSHCONST("true", BoolType(), o['frame'])  # Push true
                result += self.emit.emitLABEL(labelEnd, o['frame'])  # End label
            
            return result, BoolType()
    
    def visitUnaryOp(self, ast: UnaryOp, o):
        o['isLeft'] = False
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

        # skip all get-related builtin functions
        if ast.funName in ["getInt", "getFloat", "getBoolean", "getString"]:
            return "", sym.mtype.rettype

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
            
    
    def visitMethCall(self, ast: MethCall, o):
        # likely invokestatic
        env = o.copy()
        sym = None # would store the method
        code = ""
        struct = None # would store the struct or interface
        isStruct = True # would check if this is struct or interface
        # check if caller is interface type or struct type, if interface type, use invokeinterface, else use invokevirtual

        if isinstance(ast.receiver, Id):
            caller = next(filter(lambda x: x.name == ast.receiver.name, [j for i in o['env'] for j in i]),None)

            callerType = caller.mtype.name
            isStruct = True
            struct = next(filter(lambda x: x.name == callerType, self.structs),None)
            if struct is None:
                isStruct = False
                struct = next(filter(lambda x: x.name == callerType, self.interfaces),None)
            
            if isStruct:
                sym = next(filter(lambda x: x.fun.name == ast.metName, struct.methods),None)
            else: # interface
                sym = next(filter(lambda x: x.name == ast.metName, struct.methods),None)

            if type(caller.value) is Index:
                code += self.emit.emitREADVAR(ast.receiver.name, caller.mtype, caller.value.value , env['frame'])
            else:
                code += self.emit.emitGETSTATIC(f"{self.className}/{caller.name}",caller.mtype,env['frame'])
        
        else:
            o['isLeft'] = False
            e, t = self.visit(ast.receiver, o)
            code += e
            # find struct
            struct = next(filter(lambda x: x.name == t.name, self.structs),None)
            if struct is None:
                isStruct = False
                struct = next(filter(lambda x: x.name == t.name, self.interfaces),None)
            
            if isStruct:
                # find the method from struct
                sym = next(filter(lambda x: x.fun.name == ast.metName, struct.methods),None)
            else:
                # find the method from interface
                sym = next(filter(lambda x: x.name == ast.metName, struct.methods),None)

        # args
        for arg in ast.args:
            e, t = self.visit(arg, o)
            code += e
        
        # invoke method
        if isStruct:
            code += self.emit.emitINVOKEVIRTUAL(f"{struct.name}/{ast.metName}", MType([x.parType for x in sym.fun.params], sym.fun.retType), env['frame'])
            if type(sym.fun.retType) is VoidType:
                self.emit.printout(code)
                return o
            else:
                return code, sym.fun.retType
        else:
            code += self.emit.emitINVOKEINTERFACE(f"{struct.name}/{ast.metName}", MType([x for x in sym.params], sym.retType), env['frame'], len(ast.args))
            if type(sym.retType) is VoidType:
                self.emit.printout(code)
                return o
            else:
                return code, sym.retType

    
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

    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        return self.emit.emitPUSHICONST(1 if ast.value == 'true' else 0, o['frame']), BoolType()
    
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
                code += self.emit.jvm.emitANEWARRAY(self.emit.getFullType(eleType))
            
            # Initialize array elements
            for i, val in enumerate(values):
                code += self.emit.emitDUP(o['frame'])  # Duplicate array reference
                code += self.emit.emitPUSHICONST(i, o['frame'])  # Array index
                
                # Push value
                valCode, tVal = self.visit(val, o)
                code += valCode
                if isinstance(eleType, FloatType) and isinstance(tVal, IntType):
                    code += self.emit.emitI2F(o['frame'])
                
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
                        valCode, tVal = self.visit(val, o)
                        code += valCode
                        if isinstance(eleType, FloatType) and isinstance(tVal, IntType):
                            code += self.emit.emitI2F(o['frame'])
                        
                        # Store value
                        code += self.emit.emitASTORE(eleType, o['frame'])
            else:
                # For 3D+ arrays, use recursive initialization
                code += self.initMultiDimArray(values, [], dimensions, eleType, o)
        
        return code, ArrayType(dimensions, eleType)

    def visitStructLiteral(self, ast: StructLiteral, o):
        
        # sym = next(filter(lambda x: isinstance(x, SymbolType) and x.name == ast.name, [j for i in o['env'] for j in i]),None)
        sym = next(filter(lambda x: x.name == ast.name, self.structs),None)
        # 
        code = ""

        code += self.emit.emitNEW(ast.name, o['frame'])
        code += self.emit.emitDUP(o['frame'])

        fields = sym.elements
        for field in fields:
            # need to make ast.elements that doesn't exist to be default value
            # find in ast.elements
            try:
                _, expr = next(filter(lambda x: x[0] == field[0], ast.elements), None)
                code += self.visit(expr, o)[0]
            except Exception:
                # if not found, set to default value
                val = self.get_default_value(field[1])
                if val is None:
                    code += self.emit.emitPUSHNULL(o['frame'])
                else:
                    code += self.emit.emitPUSHCONST(val, field[1], o['frame'])

        code += self.emit.emitINVOKESPECIAL(lexeme=f"{ast.name}/<init>", in_=MType([x[1] for x in fields], VoidType()), frame=o['frame'])

        return code, ClassType(ast.name)
    
    def visitNilLiteral(self, ast, o):
        return self.emit.emitPUSHNULL(o['frame']), None
    
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
        env = reduce(lambda acc,e: self.visit(e,acc),ast.member, env)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitAssign(self, ast: Assign, o):
        env = o.copy()
        env['isLeft'] = False
        rhs, rTyp = self.visit(ast.rhs, env)
        if isinstance(ast.rhs, BinaryOp) and isinstance(ast.lhs, FieldAccess):
            env['frame'].push()

        # this push to frame before reading the lhs is fieldaccess because of:
        # binary op would first push 2 times, and then, pop after the operation
        # as we just visit and not yet printout, this makes if the lhs is field access, it would have a aload_<index> or so, which would be the beginning of the assignment - before the rhs, which makes it less than 1 stack than it should be
        # Like a.x = n + m
        # aload_0 (this is visit later than the rhs), thus its stack size is now 2 (not 3)
        # iload_1 <stack size 1>
        # iload_2 <stack size 2>
        # (all of above need 3 stack size)
        # iadd <stack size 1>
        
        env['isLeft'] = True
        lhs, lTyp = self.visit(ast.lhs, env)
        putStatic = ""
        if not isinstance(ast.lhs, ArrayCell):
            if isinstance(ast.lhs, FieldAccess):
                load = '\n'.join(lhs.split("\n")[:-2])
                load += '\n'
                putStatic = lhs.split("\n")[-2]
                putStatic += '\n'
                self.emit.printout(load)
            self.emit.printout(rhs)    
            if isinstance(lTyp, FloatType) and isinstance(rTyp, IntType):
                self.emit.printout(self.emit.emitI2F(env['frame']))
                
            
        # all of this ugly code for field access is because:
        # an assign to field access is as follow
        """ 
        aload_<index>
        other stuffs goes here if it multi field access: getfield bla bla
        <lhs code here>
        putstatic <className>/<fieldName> <fieldType>
        """
        # and the lhs would return as follow
        """
        aload_<index>
        other stuffs goes here if it multi field access: getfield bla bla
        putstatic <className>/<fieldName> <fieldType>
        """
        # so we need to separate the lines of lhs, and the first part is the aload_<index> code, then the rhs, then the putstatic at bottom
        # we use [-2] because the last one is empty string, and the second last one is the putstatic code

        # := quick declaration, so we need to check if the lhs is declared, else declare it

        if isinstance(ast.lhs, Id) and lTyp is None:
            # if lhs is not declared, we need to declare it
            index = env['frame'].getNewIndex()
            env['env'][0].insert(0, Symbol(ast.lhs.name, rTyp, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.lhs.name, rTyp, env['frame'].getStartLabel(), env['frame'].getEndLabel(), env['frame']))
            self.emit.printout(self.emit.emitWRITEVAR(ast.lhs.name, rTyp, index, env['frame']))

        if not isinstance(ast.lhs, FieldAccess):
            self.emit.printout(lhs)

        if isinstance(ast.lhs, (ArrayCell)):
            self.emit.printout(rhs)
            self.emit.printout(self.emit.emitASTORE(lTyp, o['frame']))
        
        elif isinstance(ast.lhs, FieldAccess):
            self.emit.printout(putStatic)

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
        env['isLeft'] = False
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
        else:
            return None
    
    def MethScan(self, ast: Program):
        # get all methods to corresponding struct, would need two scan
        # the output of this function: ast with StructType would have their .methods filled
        
        structMethods = dict() # dictionary of struct name and their methods: "structName": [method1, method2]

        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                # create new struct type if not exist
                if decl.recType.name not in structMethods:
                    structMethods[decl.recType.name] = []
                structMethods[decl.recType.name].append(decl)
        
        for structName, methods in structMethods.items():
            # find the struct type
            struct: StructType = next(filter(lambda x: isinstance(x, StructType) and x.name == structName, ast.decl), None)
            for method in methods:
                struct.methods.append(method)

        # extras
        for decl in ast.decl:
            if isinstance(decl, StructType):
                self.structs.append(decl)
            elif isinstance(decl, InterfaceType):
                self.interfaces.append(decl)
    
    def ImplementScan(self, struct: StructType):
        Smethods = struct.methods

        implemented = []

        for interface in self.interfaces:
            name = interface.name
            Imethods = interface.methods
            isValid = True
            for proto in Imethods:
                if not any(self.cmpPrototype(meth.fun, proto) for meth in Smethods):
                    isValid = False
                    break
            if isValid:
                implemented.append(name)
        
        return implemented

    def cmpPrototype(self, meth: FuncDecl, proto: Prototype):
        if meth.name != proto.name:
            return False
        if len(meth.params) != len(proto.params):
            return False
        for i in range(len(meth.params)):
            if meth.params[i].parType != proto.params[i]:
                return False
        if  meth.retType != proto.retType:
            return False
        return True

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
                        "fields": symbol.field if symbol.field else None,
                        "methods": [method.fun.name for method in symbol.method] if symbol.method else None
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
                if i >= int(dimensions[-1].value) if hasattr(dimensions[-1], 'value') else len(values):
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
                valCode, tVal = self.visit(val, o)
                code += valCode
                if isinstance(eleType, FloatType) and isinstance(tVal, IntType):
                    code += self.emit.emitI2F(o['frame'])
                
                code += self.emit.emitASTORE(eleType, o['frame'])
        else:
            # For higher dimensions, we need to handle nested arrays differently
            for i, subarray in enumerate(values):
                if i >= int(dimensions[len(indices)].value) if hasattr(dimensions[len(indices)], 'value') else len(values):
                    break
                
                # For each sub-array at current dimension, we need to:
                # 1. Get the array at the current level of indices
                # 2. Then continue recursive initialization
                
                # Create path to the current sub-array
                new_indices = indices + [i]
                code += self.initMultiDimArray(subarray, new_indices, dimensions, eleType, o)
        
        return code

