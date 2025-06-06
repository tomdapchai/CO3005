"""
 * @author 2213046
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
    def __init__(self,name,mtype, value = None, isDeclared = False,):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.isDeclared = isDeclared

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


class StaticChecker(BaseVisitor,Utils):

    builtin_env = [
        Symbol(name="getInt",mtype=MType([],IntType()), isDeclared = True),
        Symbol(name="putInt",mtype=MType([IntType()],VoidType()),isDeclared = True),
        Symbol(name="putIntLn",mtype=MType([IntType()],VoidType()),isDeclared = True),
        Symbol(name="getFloat",mtype=MType([],FloatType()),isDeclared = True),
        Symbol(name="putFloat",mtype=MType([FloatType()],VoidType()),isDeclared = True),
        Symbol(name="putFloatLn",mtype=MType([FloatType()],VoidType()),isDeclared = True),
        Symbol(name="getBool",mtype=MType([],BoolType()),isDeclared = True),
        Symbol(name="putBool",mtype=MType([BoolType()],VoidType()),isDeclared = True),
        Symbol(name="putBoolLn",mtype=MType([BoolType()],VoidType()),isDeclared = True),
        Symbol(name="getString",mtype=MType([],StringType()),isDeclared = True),
        Symbol(name="putString",mtype=MType([StringType()],VoidType()),isDeclared = True),
        Symbol(name="putStringLn",mtype=MType([StringType()],VoidType()),isDeclared = True),
        Symbol(name="putLn",mtype=MType([],VoidType()), isDeclared = True),
    ]    
    
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = []
        self.global_types : List[SymbolType] = []
        self.global_funcs : List[Symbol] = self.builtin_env.copy()
        self.orphan_methods = [] # methods that cannot be assigned to any struct
        self.in_first_scan = False
        # Add a field to track the current function return type
        self.current_function_rettype = None
        # Add a field to track if a return statement was found
        self.has_return = False
        # Add a field to track the current function
        self.current_function = None
 
    
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

        self.global_envi = self.global_funcs + self.global_types

        return self.visit(self.ast, self.global_envi)
    
    def process_orphan_methods(self):
        """Associate methods that were declared before their struct types."""
        remaining_orphans = []
        
        for method_decl in self.orphan_methods:
            # Try to find the receiver type now that all structs are declared
            struct_sym = next((sym for sym in self.global_types if sym.name == method_decl.recType.name), None)
            
            if struct_sym:
                # Check if method with same name already exists in struct.methods
                existing_method = next((m for m in struct_sym.method if m.name == method_decl.fun.name), None)
                if existing_method:
                    continue
                
                method_sym = Symbol(
                    name=method_decl.fun.name,
                    mtype=MType(
                        partype=[param.parType for param in method_decl.fun.params],
                        rettype=method_decl.fun.retType
                    ),
                    isDeclared=False  # Not fully declared yet
                )
                # Add method to struct
                struct_sym.method.insert(0, method_sym)

                # Check if method with same name already exists in struct.member
                existing_method_member = next((m for m in struct_sym.member if m.name == method_decl.fun.name), None)
                if existing_method_member:
                    # remove the existing method from member and add the new method to member to the head of the list
                    struct_sym.member.remove(existing_method_member)

                struct_sym.member.insert(0, method_sym)
                
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
                self.global_funcs.insert(0, func_symbol)
            
            elif isinstance(decl, StructType):
                # For structs, create a SymbolType
                # check if struct is redeclared in global_types:
                res = self.lookup(decl.name, self.global_types, lambda x: x.name)
                if not res is None:
                    continue

                members = []

                fields = []

                for elt in decl.elements:
                    # check if field is redeclared in the struct
                    res = self.lookup(elt[0], fields, lambda x: x.name)
                    if not res is None:
                        continue
                    # else add to the fields
                    field_sym = Symbol(
                        name=elt[0],
                        mtype=elt[1],
                        isDeclared=False  # Not fully declared yet
                    )
                    fields.append(field_sym)
                    members.append(field_sym)

                methods = []
                for method in decl.methods:
                    res = self.lookup(method.fun.name, methods, lambda x: x.name)
                    if not res is None:
                        continue
                    method_sym = Symbol(
                            name=method.fun.name,
                            mtype=MType(
                                partype=[param.parType for param in method.fun.params],
                                rettype=method.fun.retType
                            ),
                            isDeclared=False  # Not fully declared yet
                        )   
                    methods.append(method_sym)
                    members.append(method_sym)


                struct_sym = SymbolType(
                    name=decl.name,
                    mtype=type(decl),
                    field=fields,
                    method=methods,
                    isDeclared=False,
                    member=members
                )
                
                self.global_types.insert(0, struct_sym)
            
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
                    methods.insert(0, method_sym)

                interface_sym = SymbolType(
                    name=decl.name,
                    mtype=type(decl),
                    field=None,
                    method=methods,
                    isDeclared=False
                )
                self.global_types.insert(0, interface_sym)
            
            elif isinstance(decl, MethodDecl):
                # Find the struct in the collected types
                struct_sym = next((sym for sym in self.global_types if sym.name == decl.recType.name), None)

                # if struct_sym not found, add method to somewhere else to store for later scan
                
                if struct_sym:
                    # Add method to the struct
                    # print("method: ", decl.fun.retType)
                    # find the method in the struct
                    existing_method = next((m for m in struct_sym.method if m.name == decl.fun.name), None)
                    if existing_method:
                        # Skip this method if it already exists
                        # Later on will raise Redeclared error
                        continue

                    method_sym = Symbol(
                        name=decl.fun.name,
                        mtype=MType(
                            partype=[param.parType for param in decl.fun.params],
                            rettype=decl.fun.retType
                        ),
                        isDeclared=False  # Not fully declared yet
                    )
                    struct_sym.method.insert(0, method_sym)
                    struct_sym.member.append(method_sym)
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
            if type(dimensions[level].value) is str:
                if dimensions[level].value.startswith('0x') or dimensions[level].value.startswith('0X'):
                    expected_size = int(dimensions[level].value, 16)
                elif dimensions[level].value.startswith('0b') or dimensions[level].value.startswith('0B'):
                    expected_size = int(dimensions[level].value, 2)
                elif dimensions[level].value.startswith('0o') or dimensions[level].value.startswith('0O'):
                    expected_size = int(dimensions[level].value, 8)
                else:
                    expected_size = int(dimensions[level].value)
            else:
                expected_size = int(dimensions[level].value)    

            # print("expect_size: ", expected_size)
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
                    # print("type 1: ", self.inferType(field[1], c))
                    # print("type 2: ", next(f.mtype for f in structSym.field if f.name == field[0]))
                    raise TypeMismatch(expr)
                # check if field is redeclared
                
                field_declared.add(field[0])

            return Id(name=expr.name)


        elif isinstance(expr, NilLiteral):
            return TypeMismatch(expr)
        
        elif isinstance(expr, ArrayLiteral):
            # Infer type of elements, they must be the same and the same of eleType
            # there would be multi dimension array so need to check if all of them are the same
            try:
                self.checkArrayStructure(expr.value, expr.dimens, 0, expr.eleType, c)
            except TypeMismatch:
                raise TypeMismatch(expr)

            # check done, now infer the value of dimensions
            # for i in range(len(expr.dimens)):
            #     value = self.inferValue(expr.dimens[i], c)
            #     if value is not None:
            #         expr.dimens[i] = IntLiteral(int(value))
                

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
            # print("operandType: ", operandType)
            
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
        
        elif isinstance(expr, ArrayCell):
            arrType = self.inferType(expr.arr, c)
            
            if not isinstance(arrType, ArrayType):
                raise TypeMismatch(expr)
            
            # Validate index expressions
            for idx in expr.idx:
                idxType = self.inferType(idx, c)
                if type(idxType) is not IntType:
                    raise TypeMismatch(expr)
            
            # Check if indices are within bounds
            num_indices = len(expr.idx)
            total_dimensions = len(arrType.dimens)
            
            if num_indices > total_dimensions:
                # We're accessing more dimensions than the array has, which is an error
                raise TypeMismatch(expr)
            
            # Check if indices are within the declared bounds
            for i in range(min(num_indices, total_dimensions)):
                idx_value = self.inferValue(expr.idx[i], c)
                dim_value = self.inferValue(arrType.dimens[i], c)
                
                # If we can determine both values at compile time
                if idx_value is not None and dim_value is not None:
                    # Check if the index is out of bounds (negative or >= dimension size)
                    if idx_value < 0 or idx_value > dim_value:
                        raise TypeMismatch(expr)
            
            # Determine the return type based on dimensions accessed
            if num_indices < total_dimensions:
                # We're accessing a subset of dimensions, return an array type with remaining dimensions
                remaining_dimens = arrType.dimens[num_indices:]
                return ArrayType(dimens=remaining_dimens, eleType=arrType.eleType)
            else:  # num_indices == total_dimensions
                # We're accessing all dimensions, return the element type
                return arrType.eleType
        
        elif isinstance(expr, FieldAccess):
            # should be Id()
            receiverType = self.inferType(expr.receiver, c)
            # print("receiverType: ", receiverType)
            if not isinstance(receiverType, Id):
                raise TypeMismatch(expr)

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
                # print("get here")
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
            # funcSym = self.lookup(expr.funName, filter(lambda x: isinstance(x.mtype, MType) ,sum(c, []) + self.global_funcs), lambda x: x.name)

            funcSym = self.lookup(expr.funName, sum(c, []), lambda x: x.name)
            if not funcSym:
                raise Undeclared(Function(), expr.funName)
            
            if not isinstance(funcSym.mtype, MType):
                raise Undeclared(Function(), expr.funName)
            
            # Check parameter types
            if len(expr.args) != len(funcSym.mtype.partype):
                raise TypeMismatch(expr)
            
            for i, arg in enumerate(expr.args):
                argType = self.inferType(arg, c)
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
            receiverType = self.inferType(expr.receiver, c)
            if not isinstance(receiverType, Id):
                raise TypeMismatch(expr)

            # Find the struct or interface definition, only need to search in global_types
            typeSym = None
            for scope in [self.global_types]:
                for sym in scope:
                    if isinstance(sym, SymbolType) and sym.name == receiverType.name:
                        typeSym = sym
                        break
                if typeSym:
                    break
            
            if not typeSym:
                raise Undeclared(Identifier(), receiverType.name)
            
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
                if isinstance(methodSym.mtype.partype[i], Symbol):
                    paramType = methodSym.mtype.partype[i].mtype
                else:
                    
                    paramType = methodSym.mtype.partype[i]
                if not self.isSameType(argType, paramType, c):
                    
                    raise TypeMismatch(expr)

            return methodSym.mtype.rettype
        
        # probably good for now
        elif isinstance(expr, Block):
            # get return type of block (only function declaration call this one)
            # there would be multiple return type in a block, so we need to check if all of them are the same, if not raise TypeMismatch
            return_type = retType
            # hasReturn = False
            # # Helper function to process a block recursively

            # def process_block(blk):
            #     nonlocal return_type
            #     nonlocal hasReturn
            #     for member in blk.member:
            #         if isinstance(member, Return):
            #             hasReturn = True
            #             if member.expr is None:
            #                 current_type = VoidType()
            #             else:
            #                 current_type = self.inferType(member.expr, c)
                        
            #             if not self.isSameType(return_type, current_type, c):
            #                 raise TypeMismatch(member)
            #         elif isinstance(member, If):
            #             # Process then branch
            #             if isinstance(member.thenStmt, Block):
            #                 process_block(member.thenStmt)
            #             # Process else branch if it exists
            #             if member.elseStmt:
            #                 if isinstance(member.elseStmt, Block):
            #                     process_block(member.elseStmt)
            #                 elif isinstance(member.elseStmt, If):
            #                     process_if(member.elseStmt)
            #         elif isinstance(member, (ForBasic, ForStep, ForEach)):
            #             if isinstance(member.loop, Block):
            #                 process_block(member.loop)
            #         elif isinstance(member, Block):
            #             process_block(member)
                
            
            # # Helper for if statements (to handle nested if-else chains)
            # def process_if(if_stmt):
            #     nonlocal return_type
            #     if isinstance(if_stmt.thenStmt, Block):
            #         process_block(if_stmt.thenStmt)
            #     if if_stmt.elseStmt:
            #         if isinstance(if_stmt.elseStmt, Block):
            #             process_block(if_stmt.elseStmt)
            #         elif isinstance(if_stmt.elseStmt, If):
            #             process_if(if_stmt.elseStmt)
            
            # # Start processing
            # process_block(expr)
            
            # # If no return statement found, it's void
            # if return_type is None:
            #     return VoidType()
            
            # # if there is return type (other than void), and there is no return statement, raise TypeMismatch
            # if return_type is not None:
            #     if not hasReturn:
            #         if not self.isSameType(return_type, VoidType(), c):
            #             raise TypeMismatch(expr)

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
        if type(type1) is ArrayType and type(type2) is ArrayType:
            if type(type1.eleType) is not type(type2.eleType):
                return False
            if len(type1.dimens) != len(type2.dimens):
                return False
            # print("checking dimens")
            # check dimension
            for i in range(len(type1.dimens)):
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
        res = self.lookup(
            ast.varName,
            c[0],
            lambda x: x.name)
        # lookup list of symbol in c, compare with varName
        if not res is None:
            # check if the redeclared symbol is a function or type
            if isinstance(res.mtype, MType) or isinstance(res, SymbolType):
                if res.isDeclared:
                    raise Redeclared(Variable(), ast.varName)
            else:
                raise Redeclared(Variable(), ast.varName)

        if ast.varInit:
            # try: 
            #     self.inferType(ast.varInit, c)
            # except TypeMismatch:
            #     raise TypeMismatch(ast.varInit)
            self.inferType(ast.varInit, c)
            initType = self.inferType(ast.varInit, c)
            if type(initType) is VoidType:
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
                        
                        ast.varType = initType
                elif type(initType) is IntType and type(ast.varType) is FloatType:
                    pass
                elif type(initType) is ArrayType and type(ast.varType) is ArrayType and type(initType.eleType) is IntType and type(ast.varType.eleType) is FloatType:
                    if len(initType.dimens) != len(ast.varType.dimens):
                        raise TypeMismatch(ast)
                    # print("checking dimens")
                    # check dimension
                    for i in range(len(initType.dimens)):
                        value1 = self.inferValue(initType.dimens[i], c)
                        value2 = self.inferValue(ast.varType.dimens[i], c)
                        if value1 is None or value2 is None:
                            raise TypeMismatch(ast)
                        if int(value1) != int(value2):
                            raise TypeMismatch(ast)
                    pass
                else:
                    raise TypeMismatch(ast)
        else:
            if isinstance(ast.varType, Id):
                try:
                    # for varType is user-defined (ID), visit it
                    # if Undeclared occurs, raise Undeclared(Type) because the Id visitor will raise Undeclared(Identifier)
                    self.visit(ast.varType, c)
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

        c[0].insert(0, Symbol(name=ast.varName, mtype=ast.varType, value=ast.varInit if value is None else value))

        return c
    
    def visitParamDecl(self, ast: ParamDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.parName, c[0], lambda x: x.name) 
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)
        
        self.visit(ast.parType, c)

        # if parType is an array, check if the dimensions are declared
        # if isinstance(ast.parType, ArrayType):
        #     for i in range(len(ast.parType.dimens)):
        #         value = self.inferValue(ast.parType.dimens[i], c)
        #         if value is not None:
        #             ast.parType.dimens[i] = IntLiteral(int(value))

        c[0].insert(0, Symbol(ast.parName, ast.parType, None))

        return c
    
    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]):
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            # check if the redeclared symbol is a function or type
            if isinstance(res.mtype, MType) or isinstance(res, SymbolType):
                if res.isDeclared:
                    raise Redeclared(Constant(), ast.conName)
            else:
                raise Redeclared(Constant(), ast.conName)
        
        value = self.inferValue(ast.iniExpr, c)


        c[0].insert(0, Symbol(name=ast.conName, mtype=self.inferType(ast.iniExpr, c), value=ast.iniExpr if value is None else value))

        return c

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]):
        # might use isMethod to make sure the receiver cannot be used as a parameter, and being redeclared later in the function
        # in case of method, the receiver is the first parameter of the function

        # CASE: every declartion if different types are cool, even with same name
        # res = self.lookup(
        #     ast.name, 
        #     list(filter(lambda x: not isinstance(x, SymbolType), c[-1] if hasattr(ast, 'isMethod') else self.global_funcs)),
        #     lambda x: x.name)

        # CASE: things in global scope cannot have the same name, including structs, interfaces, and functions, and global variables as var decl and const decl

        # res = self.lookup(
        #     ast.name, 
        #     list(filter(lambda x: not isinstance(x, SymbolType), c[-1])),
        #     lambda x: x.name)
        # if not res is None:
        #     if isinstance(res.mtype, MType):          
        #         if res.isDeclared:
        #             raise Redeclared(Function(), ast.name)
        #         else:
        #             res.isDeclared = True
        #     else:
        #         raise Redeclared(Function(), ast.name)

        res = self.lookup(
            ast.name, 
            list(filter(lambda x: not isinstance(x, SymbolType), c[-1])),
            lambda x: x.name)
        if not res is None:
            if hasattr(ast, 'isMethod'):
                # The env now just have fields and methods of the struct        
                if res.isDeclared:
                    raise Redeclared(Method(), ast.name)
                elif isinstance(res.mtype, MType):
                    res.isDeclared = True
                
            else:
                if isinstance(res.mtype, MType):          
                    if res.isDeclared:
                        raise Redeclared(Function(), ast.name)
                    else:
                        res.isDeclared = True
                else:
                    raise Redeclared(Function(), ast.name)

        # create new scope for function        
        env = [[]] + copy.deepcopy(c)

        # Param
        env = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, env)

        # check return type
        self.visit(ast.retType, c)

        func_symbol = Symbol(name=ast.name, mtype=MType(partype=copy.deepcopy(env[0]), rettype=ast.retType))

        # Add function to the list of symbol, global
        env[-1].insert(0, func_symbol)

        # Store the current function's return type
        self.current_function_rettype = ast.retType
        
        # Reset return statement tracking
        self.has_return = False

        # check body, create new scope (other than params), as the body can redeclare the params
        env = [[]] + env

        self.visit(ast.body, env)

        # if not self.isSameType(returnType, ast.retType):
        #     raise TypeMismatch(ast)
        # if isinstance(ast.retType, ArrayType):
        #     for i in range(len(ast.retType.dimens)):
        #         value = self.inferValue(ast.retType.dimens[i], c)
        #         if value is not None:
        #             ast.retType.dimens[i] = IntLiteral(int(value))

        # try:
        #     self.inferType(ast.body, env, ast.retType)
        # except TypeMismatch as e:
        #     if type(e.err) is Block:
        #         raise TypeMismatch(ast)
        #     else:
        #         raise e
        

        # just add the type of params instead of the whole symbol

        # c[-1].append(func_symbol)
        # Check if a non-void function is missing a return statement

        if not isinstance(ast.retType, VoidType) and not self.has_return:
            raise TypeMismatch(ast)

        # Reset the current function's return type
        self.current_function_rettype = None
        

        return c
    
    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]):
        # Find the struct in c[-1]
        struct: SymbolType = next((x for x in self.global_types if x.name == ast.recType.name), None)

        # struct = self.lookup(ast.recType.name, c[-1], lambda x: x.name)

        # print("methodDECL")
        # printEnv([self.global_types])

        # Check if struct was found
        if struct is None:
            raise Undeclared(Identifier(), ast.recType.name)
        # if not hasattr(struct, 'field'):
        #     raise Undeclared(Identifier(), ast.recType.name)

        env = struct.member

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

        # receiver is first scope
        env = [Symbol(ast.receiver, ast.recType, None)] + env

        # ast.fun.params.insert(0, ParamDecl(ast.receiver, ast.recType))

        ast.fun.isMethod = True
        
        # check method for the same struct
        try:
            ret_env = self.visit(ast.fun, [env + c[-1]])
        except Redeclared as e:
            if isinstance(e.k, Function):
                raise Redeclared(Method(), ast.fun.name)
            else:
                raise e

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

        # since prototype is declared in the interface, there will be always interface, and it is the first item in c[-1]
        interface : SymbolType = c[-1][0]
        
        prototypes = interface.method

        res = self.lookup(ast.name, prototypes, lambda x: x.name)

        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        
        param = reduce(lambda acc, ele: self.visit(ele, acc), ast.params, c)
        
        # check return type
        self.visit(ast.retType, c)

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
            self.visit(ast.eleType, c)

        return c

    def visitStructType(self, ast : StructType, c: List[List[Symbol]]):
        # CASE: every declartion if different types are cool, even with same name
        # res = self.lookup(ast.name, self.global_types, lambda x: x.name)

        # CASE: things in global scope cannot have the same name, including structs, interfaces, and functions, and global variables as var decl and const decl
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            if isinstance(res, SymbolType): # then it is SymbolType
                if res.isDeclared:
                    raise Redeclared(Type(), ast.name)
                else:
                    res.isDeclared = True
            else:
                raise Redeclared(Type(), ast.name)
            
        
        # check elements: list[Tuple[str, Type]], where str is the name of the field, Type is the type of the field, no visit, just check if there is two duplicate name in the elements

        # if valid add to field of struct

        
        
        for element in ast.elements:
            field_name = element[0]
            # Check if field is already in fields list
            # existing_field = next((f for f in fields if f.name == field_name), None)
            existing_field = self.lookup(field_name, res.member, lambda x: x.name) # guarantee that there always be a result in the struct (field/method) as we have added in first scan
            
            if existing_field.isDeclared:
                raise Redeclared(Field(), field_name)
            else:
                self.visit(element[1], c)
                existing_field.isDeclared = True
           
        for method in ast.methods:
            self.visit(method, c)

        # check methods
        #method = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, filter(lambda x: x.value == ast.name, c), c)
        # c[-1].append(SymbolType(name=ast.name, mtype=type(ast), method=[], field=fields))
        
        
        return c

    def visitInterfaceType(self, ast: InterfaceType, c: List[List[Symbol]]):
        res = self.lookup(ast.name, c[-1], lambda x: x.name)
        if not res is None:
            if res.isDeclared:
                raise Redeclared(Type(), ast.name)
            else:
                res.isDeclared = True
        
        # check prototypes
        # c here is a list of symbol of prototypes of an interface
        # need to check more on this, as global_types already been added to c[-1]
        env = copy.deepcopy(c)

        env[-1].insert(0, SymbolType(name=ast.name, mtype=type(ast), field=None, method=[]))

        reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, env)

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
        isDeclared = True
        lhsType = None
        try:
            lhsType = self.inferType(ast.lhs, c)
        except Undeclared as e:
            if isinstance(ast.lhs, Id):
                # make new declaration for the LHS
                isDeclared = False
                pass
            else:
                raise e
        # check RHS
        # try:
        #     rhsType = self.inferType(ast.rhs, c)
        # except TypeMismatch as e:
        #     raise TypeMismatch(ast.rhs)
        rhsType = self.inferType(ast.rhs, c)
        
        if isinstance(rhsType, VoidType):
            raise TypeMismatch(ast)

        if not isDeclared:
            # add LHS to the list of symbol
            value = self.inferValue(ast.rhs, c)
            c[0].insert(0, Symbol(name=ast.lhs.name, mtype=rhsType, value=ast.rhs if value is None else value))
            lhsType = rhsType

        elif not self.isSameType(lhsType, rhsType, c) and not (type(lhsType) is FloatType and type(rhsType) is IntType): 
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
            elif type(lhsType) is ArrayType and type(rhsType) is ArrayType and type(lhsType.eleType) is FloatType and type(rhsType.eleType) is IntType:
                if len(lhsType.dimens) != len(rhsType.dimens):
                    raise TypeMismatch(ast)
                # print("checking dimens")
                # check dimension
                for i in range(len(lhsType.dimens)):
                    value1 = self.inferValue(lhsType.dimens[i], c)
                    value2 = self.inferValue(rhsType.dimens[i], c)
                    if value1 is None or value2 is None:
                        raise TypeMismatch(ast)
                    if int(value1) != int(value2):
                        raise TypeMismatch(ast)
            else:
                raise TypeMismatch(ast)
            
        if isinstance(ast.lhs, Id):
            lhs_sym = self.lookup(ast.lhs.name, sum(c, []), lambda x: x.name)
            value = self.inferValue(ast.rhs, c)
            
            lhs_sym.value = lhs_sym.value if value is None else value

        return c

    def visitIf(self, ast: If, c: List[List[Symbol]]):
        # check condition
        condType = self.inferType(ast.expr, c)
        if type(condType) is not BoolType:
            raise TypeMismatch(ast)

        # if condType is not BoolType():
        #     raise TypeMismatch(ast.expr)

        # then stmt is a block
        # create local scope for then stmt
        env = [[]] + copy.deepcopy(c)

        self.visit(ast.thenStmt, env)

        # printEnv(env)

        if ast.elseStmt is not None:
            # else stmt scope unrelated to then stmt
            if type(ast.elseStmt) is If:
                env = copy.deepcopy(c)
                self.visit(ast.elseStmt, env)
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
            varType = None
            if ast.init.varType is None:
                varType = self.inferType(ast.init.varInit, c)
            else:
                varType = ast.init.varType
            env[0].insert(0, Symbol(name=ast.init.varName, mtype=varType, value=ast.init.varInit))
        elif isinstance(ast.init, Assign):
            env[0].insert(0, Symbol(name=ast.init.lhs.name, mtype=self.inferType(ast.init.rhs, c), value=ast.init.rhs))
        
        
        # checking condition
        self.visit(ast.cond, env)
        
        condType = self.inferType(ast.cond, env)
        if type(condType) is not BoolType:
            
            raise TypeMismatch(ast.cond)

        # checking update
        self.visit(ast.upda, env)
        # check if the update is an assign statement, let not add it to the body scope - env[0]
        if isinstance(ast.upda, Assign):
            if len(env[0]) > 1: # means there is a new declaration in the update
            # then init would be at index 1, and update at index 0 because the declaration is added to the head of the list
                symUpda = env[0][0]
                symInit = env[0][1]
                if symUpda.name != symInit.name:
                    env[0].pop(0)
        

        # checking loop block
        self.visit(ast.loop, env)

        return c

    def visitForEach(self, ast: ForEach , c: List[List[Symbol]]):
        # this might just check the loop block and the arr (if it is an arrayType and declared)

        env = [[]] + copy.deepcopy(c)
        arrayTyp = self.inferType(ast.arr, c)
        if not isinstance(arrayTyp, ArrayType):
            raise TypeMismatch(ast)

        # ignore if _ is used instead of index
        if ast.idx.name != '_':
            # env[0].insert(0, Symbol(name=ast.idx.name, mtype=IntType()))
            self.visit(ast.idx, env)
            idxType = self.inferType(ast.idx, env)
            if not isinstance(idxType, IntType):
                raise TypeMismatch(ast)
        # env[0].insert(0, Symbol(name=ast.value.name, mtype=arrayTyp.eleType))
        self.visit(ast.value, env)

        valueType = self.inferType(ast.value, env)
        if not self.isSameType(valueType, arrayTyp.eleType, env):
            raise TypeMismatch(ast)
        
        self.visit(ast.loop, env)
        return c

    def visitBreak(self, ast, c: List[List[Symbol]]):
        return c

    def visitContinue(self, ast, c: List[List[Symbol]]):
        return c

    def visitReturn(self, ast, c: List[List[Symbol]]):
        # Mark that we found a return statement
        self.has_return = True
        
        # If there's no expression in the return statement
        if ast.expr is None:
            # If function expects a non-void return
            if not isinstance(self.current_function_rettype, VoidType):
                raise TypeMismatch(ast)
        else:
            # Return has an expression, get its type
            expr_type = self.inferType(ast.expr, c)
            
            # If function expects void
            if isinstance(self.current_function_rettype, VoidType):
                raise TypeMismatch(ast)
            
            # Check if return type matches function return type
            if not self.isSameType(expr_type, self.current_function_rettype, c):
                # Special case for int to float conversion
                # if not (isinstance(self.current_function_rettype, FloatType) and isinstance(expr_type, IntType)):
                #     raise TypeMismatch(ast)
                raise TypeMismatch(ast) 
        
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
                        "mtype": symbol.mtype,
                        "value": symbol.value
                    }
                scope_info.append(symbol_info)
        result.append(scope_info)
    
    print(result)

