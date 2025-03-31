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
    def __init__(self,name,mtype, isDeclared = False, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.isDeclared = isDeclared

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class SymbolType(Symbol): # for struct and interface
    def __init__(self, name, mtype, field: List[Symbol] = None, method: List[Symbol] = [], isDeclared = False, value = None):
        self.name = name
        self.mtype = mtype
        self.field = field # None if interface
        self.method = method
        self.isDeclared = isDeclared

    def __str__(self):
        return "SymbolType(" + str(self.name) + "," + str(self.mtype) + ")"


class StaticChecker(BaseVisitor,Utils):

    builtin_env = [
        Symbol("getInt",MType([],IntType()), isDeclared = True),
        Symbol("putInt",MType([IntType()],VoidType()),isDeclared = True),
        Symbol("putIntLn",MType([IntType()],VoidType()),isDeclared = True),
        Symbol("getFloat",MType([],FloatType()),isDeclared = True),
        Symbol("putFloat",MType([FloatType()],VoidType()),isDeclared = True),
        Symbol("putFloatLn",MType([FloatType()],VoidType()),isDeclared = True),
        Symbol("getBool",MType([],BoolType()),isDeclared = True),
        Symbol("putBool",MType([BoolType()],VoidType()),isDeclared = True),
        Symbol("putBoolLn",MType([BoolType()],VoidType()),isDeclared = True),
        Symbol("getString",MType([],StringType()),isDeclared = True),
        Symbol("putString",MType([StringType()],VoidType()),isDeclared = True),
        Symbol("putStringLn",MType([StringType()],VoidType()),isDeclared = True),
        Symbol("putLn",MType([],VoidType()), isDeclared = True),
    ]    
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = self.builtin_env.copy()
        self.global_types : List[SymbolType] = []
        self.global_funcs : List[Symbol] = []
        self.orphan_methods = [] # methods that cannot be assigned to any struct
        self.in_first_scan = False
 
    
    def check(self):
        self.in_first_scan = True
        self.first_scan(self.ast)

        self.process_orphan_methods()
        # if there is any methods cant be assign to the corresponding struct, add them to the struct methods, and remove them from the unassigned methods
        # after this, if there is still any methods that cannot be assigned to the struct, then skip

        # self.global_envi.extend(self.global_funcs)
        # self.global_envi.extend(self.global_types)
        
        # Regular checking
        self.in_first_scan = False

        return self.visit(self.ast, self.global_envi)
    
    def process_orphan_methods(self):
        """Associate methods that were declared before their struct types."""
        remaining_orphans = []
        
        for method_decl in self.orphan_methods:
            # Try to find the receiver type now that all structs are declared
            struct_sym = next((sym for sym in self.global_types if sym.name == method_decl.recType.name), None)
            
            if struct_sym:
                # Check if method with same name already exists
                existing_method = next((m for m in struct_sym.method if m.name == method_decl.fun.name), None)
                if existing_method:
                    # Skip this method if it already exists
                    # Later on will raise Redeclared error
                    continue
                
                # Add method to struct
                method_sym = Symbol(
                    name=method_decl.fun.name,
                    mtype=MType(
                        partype=[param.parType for param in method_decl.fun.params],
                        rettype=method_decl.fun.retType
                    ),
                    isDeclared=False  # Not fully declared yet
                )
                struct_sym.method.append(method_sym)
            else:
                # Keep in orphans for error reporting during regular visit
                remaining_orphans.append(method_decl)
        
        # Update orphan methods with those that still couldn't be associated
        self.orphan_methods = remaining_orphans
    
    def first_scan(self, ast):
        """Scan the program to collect all function, struct, and interface declarations."""
        # redeclaration of type and function and method will also be checked here
        # the later scan in program just check the body of the function and method, and the return type of the function and method
        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                # For functions, we just need a placeholder with signature
                # check if function is redeclared in global_envi:
                # res = self.lookup(decl.name, self.global_envi, lambda x: x.name)
                # if not res is None:
                #     raise Redeclared(Function(), decl.name)
                # check if function is redeclared in global_funcs:
                res = self.lookup(decl.name, self.global_funcs, lambda x: x.name)
                if not res is None:
                    continue

                func_symbol = Symbol(
                    name=decl.name, 
                    mtype=MType(
                        partype=[param.parType for param in decl.params],
                        rettype=decl.retType
                    ),
                    isDeclared=False
                )
                self.global_funcs.append(func_symbol)
            
            elif isinstance(decl, StructType):
                # For structs, create a SymbolType
                # check if struct is redeclared in global_types:
                res = self.lookup(decl.name, self.global_types, lambda x: x.name)
                if not res is None:
                    continue

                fields = [Symbol(name=elt[0], mtype=elt[1]) for elt in decl.elements]
                struct_sym = SymbolType(
                    name=decl.name,
                    mtype=type(decl),
                    field=fields,
                    method=[],
                    isDeclared=False
                )
                self.global_types.append(struct_sym)
            
            elif isinstance(decl, InterfaceType):
                # For interfaces, create a SymbolType
                # check if interface is redeclared in global_types:
                res = self.lookup(decl.name, self.global_types, lambda x: x.name)
                if not res is None:
                    continue

                # add method to the interface
                methods = []
                for method in decl.methods:
                    method_sym = Symbol(
                        name=method.name,
                        mtype=MType(
                            partype=[param for param in method.params],
                            rettype=method.retType
                        ),
                        isDeclared=False  # Not fully declared yet
                    )
                    methods.append(method_sym)

                interface_sym = SymbolType(
                    name=decl.name,
                    mtype=type(decl),
                    field=None,
                    method=methods,
                    isDeclared=False
                )
                self.global_types.append(interface_sym)
            
            elif isinstance(decl, MethodDecl):
                # Find the struct in the collected types
                struct_sym = next((sym for sym in self.global_types if sym.name == decl.recType.name), None)

                # if struct_sym not found, add method to somewhere else to store for later scan
                
                if struct_sym:
                    # Add method to the struct
                    print("method: ", decl.fun.retType)
                    method_sym = Symbol(
                        name=decl.fun.name,
                        mtype=MType(
                            partype=[param.parType for param in decl.fun.params],
                            rettype=decl.fun.retType
                        ),
                        isDeclared=False  # Not fully declared yet
                    )
                    struct_sym.method.append(method_sym)
                else:
                    # Store as an orphan method to be processed later
                    self.orphan_methods.append(decl)
    
    def checkArrayStructure(self, value, dimensions, level, eleType, c):
        """
        Recursively check that the array structure matches the dimensions.
        
        Args:
            value: Current array value or subarray
            dimensions: List of dimension expressions
            level: Current dimension level (0-indexed)
            eleType: Expected element type
            c: Symbol context
        """
        # If we've reached the end of dimensions, this should be a leaf element
        if level >= len(dimensions):
            # This should be a leaf element, check its type against eleType
            elemType = self.inferType(value, c)
            if not self.isSameType(elemType, eleType, c):
                raise TypeMismatch(value)
            return
        
        # At this level, value should be a list
        if not isinstance(value, list):
            raise TypeMismatch(value)
        
        # Check if dimension size is specified as a constant
        expected_size = None
        if isinstance(dimensions[level], IntLiteral):
            expected_size = int(dimensions[level].value)
            
            # Validate the array size at this level
            if len(value) > expected_size:
                raise TypeMismatch(value)
        # experimental
        elif isinstance(self.inferValue(dimensions[level], c), int):
            expected_size = self.inferValue(dimensions[level], c)
            if len(value) > expected_size:
                raise TypeMismatch(value)
        
        elif isinstance(dimensions[level], Id):
            # Look up the constant size
            size_sym = self.lookup(dimensions[level].name, sum(c, []), lambda x: x.name)
            if not size_sym:
                raise Undeclared(Identifier(), dimensions[level].name)
            if not isinstance(size_sym.mtype, IntType):
                raise TypeMismatch(dimensions[level])
            expected_size = size_sym.value
        
        # Recursively check each element at this level
        for elem in value:
            self.checkArrayStructure(elem, dimensions, level + 1, eleType, c)
    

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

    def inferType(self, expr: Expr, c: List[List[Symbol]], retType = None) -> AST.Type:
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
        
        elif isinstance(expr, StructLiteral):
            # Find the struct definition
            structSym = self.lookup(expr.name, sum(c, []) + self.global_types, lambda x: x.name)
            if not structSym or not isinstance(structSym, SymbolType):
                #raise TypeMismatch(expr)
                raise Undeclared(Identifier(), expr.name)
            # check if elements match the fields of the struct
            # and if they are redeclared
            field_declared = set()

            for field in expr.elements:
                if field[0] not in [f.name for f in structSym.field]:
                    raise Undeclared(Field(), field[0])
                if field[0] in field_declared:
                    raise Redeclared(Field(), field[0])
                if not self.isSameType(self.inferType(field[1], c), next(f.mtype for f in structSym.field if f.name == field[0]), c):
                    print("type 1: ", self.inferType(field[1], c))
                    print("type 2: ", next(f.mtype for f in structSym.field if f.name == field[0]))
                    raise TypeMismatch(expr)
                # check if field is redeclared
                
                field_declared.add(field[0])

            return Id(name=expr.name)


        elif isinstance(expr, NilLiteral):
            return TypeMismatch(expr)
        
        elif isinstance(expr, ArrayLiteral):
            # Infer type of elements, they must be the same and the same of eleType
            # there would be multi dimension array so need to check if all of them are the same
            
            self.checkArrayStructure(expr.value, expr.dimens, 0, expr.eleType, c)

            # check done, now infer the value of dimensions
            for i in range(len(expr.dimens)):
                value = self.inferValue(expr.dimens[i], c)
                if value is not None:
                    expr.dimens[i] = IntLiteral(int(value))
                

            return ArrayType(expr.dimens, expr.eleType)
        
        elif isinstance(expr, BinaryOp):
            ltype = self.inferType(expr.left, c)
            rtype = self.inferType(expr.right, c)
            
            # Arithmetic operators
            if expr.op in ['+', '-', '*', '/', '%']:
                if expr.op == '+':
                    if type(ltype) is StringType and type(rtype) is StringType:
                        return StringType()
                    elif type(ltype) in [IntType, FloatType] and type(rtype) in [IntType, FloatType]:
                        return FloatType() if type(ltype) is FloatType or type(rtype) is FloatType else IntType()
                    else:
                        raise TypeMismatch(expr)

                if expr.op in ['-', '*', '/']:
                    if type(ltype) is IntType and type(rtype) is IntType:
                        return IntType()
                    elif (type(ltype) in [IntType, FloatType] and 
                        type(rtype) in [IntType, FloatType]):
                        return FloatType()
                    else:
                        raise TypeMismatch(expr)
                
                if expr.op == '%':
                    if type(ltype) is IntType and type(rtype) is IntType:
                        return IntType()
                    else:
                        raise TypeMismatch(expr)
            
            # Comparison operators - result is boolean
            elif expr.op in ['==', '!=', '<', '<=', '>', '>=']:
                # Allow comparison between same types or between numeric types and string type, they have to be the same type
                if (type(ltype) is StringType and type(rtype) is StringType) or (type(ltype) is IntType and type(rtype) is IntType) or (type(ltype) is FloatType and type(rtype) is FloatType):
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
        
        # need further fix
        elif isinstance(expr, FieldAccess):
            # should be Id()
            receiverType = self.inferType(expr.receiver, c)
            print("receiverType: ", receiverType)

            # Find the struct or interface definition
            structSym = None
            for scope in [self.global_types]:
                for sym in scope:
                    if isinstance(sym, SymbolType) and sym.name == receiverType.name:
                        structSym = sym
                        break
                if structSym:
                    break
            
            if not structSym or not structSym.field:
                print("get here")
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
            print("here is func call ", expr)
            funcSym = self.lookup(expr.funName, sum(c, []) + self.global_funcs, lambda x: x.name)
            if not funcSym:
                raise Undeclared(Function(), expr.funName)
            
            if not isinstance(funcSym.mtype, MType):
                raise TypeMismatch(expr)
            
            # Check parameter types
            if len(expr.args) != len(funcSym.mtype.partype):
                raise TypeMismatch(expr)
            
            for i, arg in enumerate(expr.args):
                argType = self.inferType(arg, c)
                print("argType: ", argType)
                paramType = None
                if isinstance(funcSym.mtype.partype[i], Symbol):
                    paramType = funcSym.mtype.partype[i].mtype
                else:
                    paramType = funcSym.mtype.partype[i]
                if not self.isSameType(argType, paramType, c):
                    raise TypeMismatch(expr)
            
            # if rettype is not VoidType, raise TypeMismatch
            # if not isinstance(funcSym.mtype.rettype, VoidType):
            #     raise TypeMismatch(expr)
            

            return funcSym.mtype.rettype
        
        # need further fix
        elif isinstance(expr, MethCall):
            # Handle method calls similar to FuncCall but with receiver
            print("expr: ", expr)
            receiverType = self.inferType(expr.receiver, c)
            print("receiverType: ", receiverType)
            printEnv([self.global_types])
            if not isinstance(receiverType, Id):
                raise TypeMismatch(expr)

            # Find the struct or interface definition, only need to search in global_types
            typeSym = None
            for scope in [self.global_types]:
                for sym in scope:
                    if isinstance(sym, SymbolType) and sym.name == receiverType.name:
                        print("sym: ", sym)
                        typeSym = sym
                        break
                if typeSym:
                    break
            
            if not typeSym:
                print("typeSym: ", typeSym)
                raise Undeclared(Identifier(), receiverType.name)
            
            # Find the method
            methodSym = None
            print("typeSym.method: ")
            printEnv([typeSym.method])
            for method in typeSym.method:
                if method.name == expr.metName:
                    print("method: ", method)
                    methodSym = method
                    break
            
            if not methodSym:
                print("yoooo")
                raise Undeclared(Method(), expr.metName)

            # Check parameter types
            if len(expr.args) != len(methodSym.mtype.partype):
                print("len(expr.args): ", len(expr.args))
                print("len(methodSym.mtype.partype): ", len(methodSym.mtype.partype))
                raise TypeMismatch(expr)
            
            for i, arg in enumerate(expr.args):
                argType = self.inferType(arg, c)
                print("argType: ", argType)
                if isinstance(methodSym.mtype.partype[i], Symbol):
                    paramType = methodSym.mtype.partype[i].mtype
                else:
                    
                    paramType = methodSym.mtype.partype[i]
                    print("paramType: ", paramType)
                if not self.isSameType(argType, paramType, c):
                    
                    raise TypeMismatch(expr)
            
            print("methodSym.mtype.rettype: ", methodSym.mtype.rettype)

            return methodSym.mtype.rettype
        
        # probably good for now
        elif isinstance(expr, Block):
            # get return type of block (only function declaration call this one)
            # there would be multiple return type in a block, so we need to check if all of them are the same, if not raise TypeMismatch
            return_type = retType
            hasReturn = False
            # Helper function to process a block recursively

            def process_block(blk):
                nonlocal return_type
                nonlocal hasReturn
                for member in blk.member:
                    if isinstance(member, Return):
                        hasReturn = True
                        if member.expr is None:
                            current_type = VoidType()
                        else:
                            current_type = self.inferType(member.expr, c)
                        
                        if not self.isSameType(return_type, current_type, c):
                            raise TypeMismatch(member)
                    elif isinstance(member, If):
                        # Process then branch
                        if isinstance(member.thenStmt, Block):
                            process_block(member.thenStmt)
                        # Process else branch if it exists
                        if member.elseStmt:
                            if isinstance(member.elseStmt, Block):
                                process_block(member.elseStmt)
                            elif isinstance(member.elseStmt, If):
                                process_if(member.elseStmt)
                    elif isinstance(member, (ForBasic, ForStep, ForEach)):
                        if isinstance(member.loop, Block):
                            process_block(member.loop)
                    elif isinstance(member, Block):
                        process_block(member)
                
            
            # Helper for if statements (to handle nested if-else chains)
            def process_if(if_stmt):
                nonlocal return_type
                if isinstance(if_stmt.thenStmt, Block):
                    process_block(if_stmt.thenStmt)
                if if_stmt.elseStmt:
                    if isinstance(if_stmt.elseStmt, Block):
                        process_block(if_stmt.elseStmt)
                    elif isinstance(if_stmt.elseStmt, If):
                        process_if(if_stmt.elseStmt)
            
            # Start processing
            process_block(expr)
            
            # If no return statement found, it's void
            if return_type is None:
                return VoidType()
            
            # if there is return type (other than void), and there is no return statement, raise TypeMismatch
            if return_type is not None:
                if not hasReturn:
                    if not self.isSameType(return_type, VoidType(), c):
                        raise TypeMismatch(expr)

            return return_type


        raise TypeMismatch(expr)  # Default case if type can't be inferred

    def inferValue(self, expr: Expr, c: List[List[Symbol]]):
        # infer the value from the epxression, for now just IntType value, else pass
        if expr is None:
            return None
        if type(self.inferType(expr, c)) is IntType:
            if isinstance(expr, BinaryOp):
                leftVal = self.inferValue(expr.left, c)
                rightVal = self.inferValue(expr.right, c)
                
                # return None if any of the operands is None
                if leftVal is None or rightVal is None:
                    return None

                if expr.op == '+':
                    return leftVal + rightVal
                elif expr.op == '-':
                    return leftVal - rightVal
                elif expr.op == '*':
                    return leftVal * rightVal
                elif expr.op == '/':
                    return leftVal / rightVal
                elif expr.op == '%':
                    return leftVal % rightVal
            elif isinstance(expr, UnaryOp):
                if expr.op == '-':
                    return -self.inferValue(expr.body, c)
            elif isinstance(expr, IntLiteral):
                if type(expr.value) is str:
                    if expr.value.startswith('0x') or expr.value.startswith('0X'):
                        return int(expr.value, 16)
                    elif expr.value.startswith('0b') or expr.value.startswith('0B'):
                        return int(expr.value, 2)
                    elif expr.value.startswith('0o') or expr.value.startswith('0O'):
                        return int(expr.value, 8)
                    return int(expr.value)
                return int(expr.value)
            elif isinstance(expr, Id):
                sym = self.lookup(expr.name, sum(c, []), lambda x: x.name)
                if sym is None:
                    raise Undeclared(Identifier(), expr.name)
                if type(sym.mtype) is IntType:
                    print("sym.value: ", sym.value)
                    if type(sym.value) is int:
                        return sym.value
                
                return None
                

            return None # for now, only IntType value is supported     
        else:
            return None  # for now, only IntType value is supported  
    
    def isSameType(self, type1: AST.Type, type2: AST.Type, c = []) -> bool:
        """
        Check if two Types are exactly the same.
        """
        print("type1: ", type1)
        print("type2: ", type2)
        if type(type1) is ArrayType and type(type2) is ArrayType:
            if type(type1.eleType) is not type(type2.eleType):
                return False
            if len(type1.dimens) != len(type2.dimens):
                return False
            # print("checking dimens")
            # check dimension
            for i in range(len(type1.dimens)):
                print("dimens: ", type1.dimens[i], type2.dimens[i])
                value1 = self.inferValue(type1.dimens[i], c)
                value2 = self.inferValue(type2.dimens[i], c)
                if value1 is None or value2 is None:
                    return False
                if int(value1) != int(value2):
                    return False
                # if type(type1.dimens[i]) is not type(type2.dimens[i]) or (isinstance(type1.dimens[i], Id) or isinstance(type2.dimens[i], Id)):
                #     print("difff")

                #     if value1 is None or value2 is None:
                #         return False
                #     if value1 != value2:
                #         return False
                # # check if the dimension is the same, all IntType
                # elif not int(type1.dimens[i].value) == int(type2.dimens[i].value):
                #     print(type(type1.dimens[i].value), type(type2.dimens[i].value))
                #     return False


            # return all(int(type1.dimens[i].value) == int(type2.dimens[i].value) for i in range(len(type1.dimens)))
            # return all(type1.dimens[i] == type2.dimens[i] for i in range(len(type1.dimens)))
        if type(type1) is Id and type(type2) is Id:
            return type1.name == type2.name
        return type(type1) is type(type2)

    def visitProgram(self,ast: Program, c: List[Symbol]):
        
        return reduce(lambda acc, ele: self.visit(ele, acc), ast.decl, [c])

    # DECLARATION
    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]):
        print(ast)
        res = self.lookup(
            ast.varName,
            # filter out SymbolType
            list(filter(lambda x: not isinstance(x, SymbolType), c[0] + self.global_funcs)),
            lambda x: x.name)
        # lookup list of symbol in c, compare with varName
        if not res is None:
            raise Redeclared(Variable(), ast.varName) 
        if ast.varInit:
            initType = self.inferType(ast.varInit, c)
            if type(initType) is VoidType:
                print("initType: ", initType)
                raise TypeMismatch(ast)
            if ast.varType is None:
                # if varType is None, infer type from initType
                ast.varType = initType

            # Special handling for array
            # elif isinstance(ast.varType, ArrayType):
            #     for i in range(len(ast.varType.dimens)):
            #         value = self.inferValue(ast.varType.dimens[i], c)
            #         if value is not None:
            #             ast.varType.dimens[i] = IntLiteral(int(value))
                
                
            
            print("type: ", ast.varType, initType)

            # need special handling for StrucType and InterfaceType

            if not self.isSameType(ast.varType, initType, c):
                if isinstance(ast.varType, Id) and isinstance(initType, Id):
                    # check if the fields of the struct are the same
                    if ast.varType.name != initType.name:
                        # LHS can be interface, RHS can be struct IF the struct implements the interface methods
                        # check if the struct implements the interface
                        structSym = self.lookup(initType.name, self.global_types, lambda x: x.name)
                        if not structSym or not isinstance(structSym, SymbolType):
                            raise Undeclared(Identifier, initType.name)
                        interfaceSym = self.lookup(ast.varType.name, self.global_types, lambda x: x.name)

                        if not interfaceSym or not isinstance(interfaceSym, SymbolType):
                            raise Undeclared(Identifier, ast.varType.name)
                        
                        # check if the struct implements the interface
                        for method in interfaceSym.method:
                            
                            if not any(m.name == method.name for m in structSym.method):
                                raise TypeMismatch(ast)
                        
                        print("so lit")
                        ast.varType = initType
                elif type(initType) is IntType and type(ast.varType) is FloatType:
                    pass
                else:
                    raise TypeMismatch(ast)
        else:
            if isinstance(ast.varType, Id):
                try:
                    # for varType is user-defined (ID), visit it
                    # if Undeclared occurs, raise Undeclared(Type) because the Id visitor will raise Undeclared(Identifier)
                    self.visit(ast.varType, c + [self.global_types])
                except Undeclared:
                    raise Undeclared(Identifier(), ast.varType.name)
            # elif isinstance(ast.varType, ArrayType):
            #     self.visit(ast.varType, c)
            #     # infer value of dimensions if it is an expression
            #     for i in range(len(ast.varType.dimens)):
            #         if isinstance(ast.varType.dimens[i], Id):
            #             # # check if the dimension is declared
            #             # res = self.lookup(ast.varType.dimens[i].name, c[0] + self.global_funcs, lambda x: x.name)
            #             # if not res is None:
            #             #     raise Redeclared(Identifier(), ast.varType.dimens[i].name)
            #             # # check if the dimension is a constant
            #             # const = self.lookup(ast.varType.dimens[i].name, c[0] + self.global_types, lambda x: x.name)
            #             # if const is None or not isinstance(const.mtype, IntType):
            #             #     raise Undeclared(Identifier(), ast.varType.dimens[i].name)
            #             value = self.inferValue(ast.varType.dimens[i], c)
            #             if value is not None:
            #                 ast.varType.dimens[i] = IntLiteral(int(value))
                
            #     print("dimen varType: ", ast.varType.dimens)
                
        # try to get the value of varInit
        value = self.inferValue(ast.varInit, c)
        print("value calculated var: ", value)

        c[0].append(Symbol(ast.varName, ast.varType, ast.varInit if value is None else value))

        return c
    
    def visitParamDecl(self, ast: ParamDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.parName, c[0] + self.global_funcs, lambda x: x.name) 
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        
        self.visit(ast.parType, c + [self.global_types])

        # if parType is an array, check if the dimensions are declared
        # if isinstance(ast.parType, ArrayType):
        #     for i in range(len(ast.parType.dimens)):
        #         value = self.inferValue(ast.parType.dimens[i], c)
        #         if value is not None:
        #             ast.parType.dimens[i] = IntLiteral(int(value))

        c[0].append(Symbol(ast.parName, ast.parType, None))

        return c
    
    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.conName, c[0] + self.global_types, lambda x: x.name)
        if not res is None: # not int value, for now
            raise Redeclared(Constant(), ast.conName)
        
        value = self.inferValue(ast.iniExpr, c)
        print("value calculated const: ", value)

        

        c[0].append(Symbol(name=ast.conName, mtype=self.inferType(ast.iniExpr, c), value=ast.iniExpr if value is None else value))

        print("mtype const: ", c[0][-1].mtype)

        return c

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]):
        # might use isMethod to make sure the receiver cannot be used as a parameter, and being redeclared later in the function
        # in case of method, the receiver is the first parameter of the function
        res = self.lookup(
            ast.name, 
            list(filter(lambda x: not isinstance(x, SymbolType), c[-1] if hasattr(ast, 'isMethod') else self.global_funcs)),
            lambda x: x.name)
        if not res is None:            
            if res.isDeclared:
                raise Redeclared(Function(), ast.name)
            else:
                res.isDeclared = True

        # create new scope for function        
        env = [[]] + copy.deepcopy(c)

        # Param
        env = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, env)

        # check return type
        self.visit(ast.retType, c + [self.global_types])

        func_symbol = Symbol(name=ast.name, mtype=MType(partype=copy.deepcopy(env[0]), rettype=ast.retType))

        # Add function to the list of symbol, global
        env[-1].append(func_symbol)

        # check body, create new scope (other than params), as the body can redeclare the params
        env = [[]] + env

        print(ast.body)
        self.visit(ast.body, env)

        # if not self.isSameType(returnType, ast.retType):
        #     raise TypeMismatch(ast)
        # if isinstance(ast.retType, ArrayType):
        #     for i in range(len(ast.retType.dimens)):
        #         value = self.inferValue(ast.retType.dimens[i], c)
        #         if value is not None:
        #             ast.retType.dimens[i] = IntLiteral(int(value))

        try:
            self.inferType(ast.body, env, ast.retType)
        except TypeMismatch as e:
            if type(e.err) is Block:
                raise TypeMismatch(ast)
            else:
                raise e
        

        # just add the type of params instead of the whole symbol

        # c[-1].append(func_symbol)
        

        return c
    
    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]):
        # Find the struct in c[-1]
        struct : SymbolType = next((x for x in self.global_types if x.name == ast.recType.name), None)

        # print("methodDECL")
        # printEnv([self.global_types])

        # Check if struct was found
        if struct is None:
            raise Undeclared(Identifier(), ast.recType.name)

        env = struct.method

        # check if the method is redeclared in the struct
        # res = self.lookup(ast.fun.name, env, lambda x: x.name)
        # if not res is None:
        #     if res.isDeclared:
        #         raise Redeclared(Method(), ast.fun.name)
        #     else:
        #         res.isDeclared = True

        # if ast.fun.name in [method.name for method in env]:
        #     # then dont need to add the method to the struct, just check the body
        #     # will do later
        #     pass

        # res = self.lookup(ast.fun.name, env, lambda x: x.name)

        # if not res is None:
        #     raise Redeclared(Method(), ast.fun.name)

        # might need to add the receiver to the list of parameter
        ast.fun.params.insert(0, ParamDecl(ast.receiver, ast.recType))

        ast.fun.isMethod = True
        
        # check method for the same struct
        try:
            ret_env = self.visit(ast.fun, [env + c[-1]])
        except Redeclared as e:
            raise Redeclared(Method(), ast.fun.name)

        # take out the method body (the function)
        # fun = ret_env[-1][-1]

        # take out the receiver from the list of parameter
        # fun.mtype.partype.pop(0)

        # pop the last item of env
        # env.pop()

        # for i in fun.mtype.partype:
        #     print("method param: ", (i.name, i.mtype))

        # add method to the list of method of the struct
        # env.append(Symbol(name=ast.fun.name, mtype=MType(partype=fun.mtype.partype, rettype=fun.mtype.rettype)))
        
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
        
        # check return type
        self.visit(ast.retType, c + [self.global_types])

        # if isinstance(ast.retType, ArrayType):
        #     for i in range(len(ast.retType.dimens)):
        #         value = self.inferValue(ast.retType.dimens[i], c)
        #         if value is not None:
        #             ast.retType.dimens[i] = IntLiteral(int(value))

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
        # check if the dimension is IntType
        # inferType each dimension as it can be an expression
        for dim in ast.dimens:
            if type(self.inferType(dim, c)) is not IntType:
                raise TypeMismatch(ast)
        
        # check if the element type is valid
        if isinstance(ast.eleType, Id):
            self.visit(ast.eleType, c + [self.global_types])

        return c

    def visitStructType(self, ast, c: List[List[Symbol]]):
        res = self.lookup(ast.name, self.global_types, lambda x: x.name)
        if not res is None:
            if res.isDeclared:
                raise Redeclared(Type(), ast.name)
            else:
                res.isDeclared = True
        
        # check elements: list[Tuple[str, Type]], where str is the name of the field, Type is the type of the field, no visit, just check if there is two duplicate name in the elements

        # if valid add to field of struct

        fields : List[Symbol] = []
        seen_fields = set()
        
        for element in ast.elements:
            field_name = element[0]
            if field_name in seen_fields:
                raise Redeclared(Field(), field_name)
            
            seen_fields.add(field_name)
            # check if the type is valid
            self.visit(element[1], c + [self.global_types])
            fields.append(Symbol(name=field_name, mtype=element[1]))  

        # check methods
        #method = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, filter(lambda x: x.value == ast.name, c), c)
        # c[-1].append(SymbolType(name=ast.name, mtype=type(ast), method=[], field=fields))
        
        
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
        # First check all standalone function/method calls
        # but it hasnt had the environment yet
        env = c

        for member in ast.member:
            if isinstance(member, (FuncCall, MethCall)):
                member._is_standalone = True
            env = self.visit(member, env)
            

        return c

    def visitAssign(self, ast: Assign, c: List[List[Symbol]]):
        # check LHS
        print("assign")
        isDeclared = True
        lhsType = None
        try:
            lhsType = self.inferType(ast.lhs, c)
            print("lhsType: ", lhsType)
        except Undeclared as e:
            if isinstance(ast.lhs, Id):
                # make new declaration for the LHS
                isDeclared = False
                pass
            else:
                raise e
        # check RHS
        rhsType = self.inferType(ast.rhs, c)
        if not isDeclared:
            # add LHS to the list of symbol
            value = self.inferValue(ast.rhs, c)
            c[0].append(Symbol(name=ast.lhs.name, mtype=rhsType, value=ast.rhs if value is None else value))
            lhsType = rhsType

        elif not self.isSameType(lhsType, rhsType, c) and not (type(lhsType) is FloatType and type(rhsType) is IntType): 
            print("lhsType: ", lhsType)
            print("rhsType: ", rhsType)
            if type(lhsType) is Id and type(rhsType) is Id:
                # check if the fields of the struct are the same
                if lhsType.name != rhsType.name:
                    # LHS can be interface, RHS can be struct IF the struct implements the interface methods
                    # check if the struct implements the interface
                    structSym = self.lookup(rhsType.name, self.global_types, lambda x: x.name)
                    if not structSym or not isinstance(structSym, SymbolType):
                        raise Undeclared(Identifier(), rhsType.name)
                    interfaceSym = self.lookup(lhsType.name, self.global_types, lambda x: x.name)

                    if not interfaceSym or not isinstance(interfaceSym, SymbolType):
                        raise Undeclared(Identifier(), lhsType.name)
                    
                    # check if the struct implements the interface
                    for method in interfaceSym.method:
                        
                        if not any(m.name == method.name for m in structSym.method):
                            raise TypeMismatch(ast)

                    # change the type of LHS to the type of RHS
                    
                    pass
            else:
                raise TypeMismatch(ast)
        if isinstance(ast.lhs, Id):
            lhs_sym = self.lookup(ast.lhs.name, sum(c, []), lambda x: x.name)
            lhs_sym.value = self.inferValue(ast.rhs, c) if lhs_sym.value is None else lhs_sym.value

        return c

    def visitIf(self, ast: If, c: List[List[Symbol]]):
        # check condition
        print("here is if")
        condType = self.inferType(ast.expr, c)
        if type(condType) is not BoolType:
            raise TypeMismatch(ast.expr)

        # if condType is not BoolType():
        #     raise TypeMismatch(ast.expr)

        # then stmt is a block
        # create local scope for then stmt
        env = [[]] + copy.deepcopy(c)

        env = self.visit(ast.thenStmt, env)

        printEnv(env)

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
        condType = self.inferType(ast.cond, c)
        if type(condType) is not BoolType:
            raise TypeMismatch(ast.cond)

        env = [[]] + copy.deepcopy(c)
        self.visit(ast.loop, env)

        return c

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]):
        # checking init
        env = [[]] + copy.deepcopy(c)
        

        # basically just add the init variable to the scope
        if isinstance(ast.init, VarDecl):
            env[0].append(Symbol(name=ast.init.varName, mtype=self.inferType(ast.init.varType, c), value=ast.init.varInit))
        elif isinstance(ast.init, Assign):
            env[0].append(Symbol(name=ast.init.lhs.name, mtype=self.inferType(ast.init.rhs, c), value=ast.init.rhs))
        
        # checking condition
        self.visit(ast.cond, env)

        condType = self.inferType(ast.cond, env)
        if type(condType) is not BoolType:
            raise TypeMismatch(ast.cond)

        # checking update
        self.visit(ast.upda, env)

        # checking loop block
        self.visit(ast.loop, env)

        return c

    def visitForEach(self, ast: ForEach , c: List[List[Symbol]]):
        # this might just check the loop block and the arr (if it is an arrayType and declared)

        env = [[]] + copy.deepcopy(c)
        arrayTyp = self.inferType(ast.arr, c)
        if not isinstance(arrayTyp, ArrayType):
            raise TypeMismatch(ast.arr)

        # ignore if _ is used instead of index
        if ast.idx.name != '_':
            env[0].append(Symbol(name=ast.idx.name, mtype=IntType()))
        env[0].append(Symbol(name=ast.value.name, mtype=arrayTyp.eleType))

        
        
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
        # self.visit(ast.left, c)
        # self.visit(ast.right, c)
        self.inferType(ast, c)

        return c

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]):
        # self.visit(ast.body, c)
        self.inferType(ast, c)
        return c

    def visitFuncCall(self, ast: FuncCall,c: List[List[Symbol]]):
        retType = self.inferType(ast, c)

        is_standalone = ast._is_standalone if hasattr(ast, "_is_standalone") else False

        # If standalone, it must return void
        if is_standalone and not isinstance(retType, VoidType):
            raise TypeMismatch(ast)
        return c

    def visitMethCall(self,ast : MethCall,c: List[List[Symbol]]):
        # check if the caller exist
        # res = self.lookup(ast.receiver, sum(c, []) + self.global_types, lambda x: x.name)
        # if res is None:
        #     print("nothing")
        #     raise Undeclared(Identifier(), ast.receiver)
        
        retType = self.inferType(ast, c)

        is_standalone = ast._is_standalone if hasattr(ast, "_is_standalone") else False
    
        if is_standalone and not isinstance(retType, VoidType):
            raise TypeMismatch(ast)

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
    
    def visitArrayLiteral(self, ast, c: List[List[Symbol]]):
        self.inferType(ast, c)
        return c

    def visitStructLiteral(self, ast, c):
        self.inferType(ast, c)
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

