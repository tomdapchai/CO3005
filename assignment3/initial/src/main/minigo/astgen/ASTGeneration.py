from typing import Tuple
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.program_list()))

    def visitProgram_list(self, ctx:MiniGoParser.Program_listContext):
        # If there are leading newlines, visit the rest of the program_list
        if ctx.NEWLINE():
            return self.visit(ctx.program_list())
        
        # Visit the decl_or_stmt
        return self.visit(ctx.decl_or_stmt())

    def visitDecl_or_stmt(self, ctx:MiniGoParser.Decl_or_stmtContext):
        # Initialize an empty list to collect nodes
        nodes = []

        # Recursively visit the left part first if it exists
        if ctx.decl_or_stmt():
            left_nodes = self.visit(ctx.decl_or_stmt())
            
            # If left_nodes is a list, extend our nodes
            # If it's a single node, append it
            if isinstance(left_nodes, list):
                nodes.extend(left_nodes)
            else:
                nodes.append(left_nodes)

        # Now add current node based on its type
        # Base case: declaration
        if ctx.decl():
            nodes.append(self.visit(ctx.decl()))

        # Ignore newlines
        # if ctx.NEWLINE():
        #     pass
        
        return nodes
        

    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        # Check for struct declaration
        if ctx.struct_decl():
            return self.visit(ctx.struct_decl())
        # Check for interface declaration
        if ctx.interface_decl():
            return self.visit(ctx.interface_decl())
        # Check for constant declaration
        if ctx.const_decl():
            return self.visit(ctx.const_decl())
        # Check for variable declaration with initialization
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        # Check for array declaration
        if ctx.array_decl():
            return self.visit(ctx.array_decl())
        # Check for variable declaration without initialization
        if ctx.var_decl_no_init():
            return self.visit(ctx.var_decl_no_init())
        # Check for function declaration
        if ctx.func_decl():
            return self.visit(ctx.func_decl())
        # Check for method declaration
        if ctx.method_decl():
            return self.visit(ctx.method_decl())
        if ctx.array_decl_with_init():
            return self.visit(ctx.array_decl_with_init())
        # Fallback to visiting all children if none found (though unlikely)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_in_block.
    """ def visitDecl_in_block(self, ctx:MiniGoParser.Decl_in_blockContext):
        # Check for struct declaration
        if ctx.struct_decl():
            return self.visit(ctx.struct_decl())
        # Check for interface declaration
        if ctx.interface_decl():
            return self.visit(ctx.interface_decl())
        # Check for constant declaration
        if ctx.const_decl():
            return self.visit(ctx.const_decl())
        # Check for variable declaration with initialization
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        # Check for array declaration
        if ctx.array_decl():
            return self.visit(ctx.array_decl())
        # Check for variable declaration without initialization
        if ctx.var_decl_no_init():
            return self.visit(ctx.var_decl_no_init())
        # Check for short variable declaration
        if ctx.short_decl():
            return self.visit(ctx.short_decl())
        # Check for function declaration
        if ctx.func_decl():
            return self.visit(ctx.func_decl())
        # Check for method declaration
        if ctx.method_decl():
            return self.visit(ctx.method_decl())
        # Fallback to visiting all children if none found (though unlikely)
        return self.visitChildren(ctx) """


    # Visit a parse tree produced by MiniGoParser#newlines.
    def visitNewlines(self, ctx:MiniGoParser.NewlinesContext):
        pass

    def visitEos(self, ctx:MiniGoParser.EosContext):
        pass

    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visit(ctx.logical_or_expr())

    # Visit a parse tree produced by MiniGoParser#logical_or_expr.
    def visitLogical_or_expr(self, ctx:MiniGoParser.Logical_or_exprContext):
        if ctx.logical_or_expr():
            left = self.visit(ctx.logical_or_expr())
            right = self.visit(ctx.logical_and_expr())
            return BinaryOp(ctx.OR().getText(), left, right)
        return self.visit(ctx.logical_and_expr())
        


    # Visit a parse tree produced by MiniGoParser#logical_and_expr.
    def visitLogical_and_expr(self, ctx:MiniGoParser.Logical_and_exprContext):
        if ctx.logical_and_expr():
            left = self.visit(ctx.logical_and_expr())
            right = self.visit(ctx.relational_expr())
            return BinaryOp(ctx.AND().getText(), left, right)
        return self.visit(ctx.relational_expr())


    # Visit a parse tree produced by MiniGoParser#logical_expr.
    # def visitLogical_expr(self, ctx: MiniGoParser.Logical_exprContext):
    #     """Visit logical expression (AND/OR operations - version 1)."""
    #     if ctx.logical_expr():  # Check if there's a left logical_expr
    #         left = self.visit(ctx.logical_expr())  # Visit the left side
    #         op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()  # Get the operator
    #         right = self.visit(ctx.equality_expr())  # Visit the right side (higher precedence)
    #         return BinaryOp(op, left, right)
        
    #     # If no left logical_expr, just visit the equality_expr
    #     return self.visit(ctx.equality_expr())
    
    # def visitEquality_expr(self, ctx: MiniGoParser.Equality_exprContext):
    #     """Visit equality expression (EQ/NEQ operations)."""
    #     if ctx.equality_expr():  # Check if there's a left equality_expr
    #         left = self.visit(ctx.equality_expr())  # Visit the left side
    #         op = ctx.EQ().getText() if ctx.EQ() else ctx.NEQ().getText()  # Get the operator
    #         right = self.visit(ctx.relational_expr())  # Visit the right side (higher precedence)
    #         return BinaryOp(op, left, right)
        
    #     # If no left equality_expr, just visit the relational_expr
    #     return self.visit(ctx.relational_expr())

    def visitRelational_expr(self, ctx: MiniGoParser.Relational_exprContext):
        """Visit relational expression (LT/LE/GT/GE operations)."""
        if ctx.relational_expr():  # Check if there's a left relational_expr
            left = self.visit(ctx.relational_expr())  # Visit the left side
            op = None
            if ctx.LT():
                op = ctx.LT().getText()
            elif ctx.LE():
                op = ctx.LE().getText()
            elif ctx.GT():
                op = ctx.GT().getText()
            elif ctx.GE():
                op = ctx.GE().getText()
            elif ctx.EQ():
                op = ctx.EQ().getText()
            elif ctx.NEQ():
                op = ctx.NEQ().getText()
            
            right = self.visit(ctx.additive_expr())  # Visit the right side (higher precedence)
            return BinaryOp(op, left, right)
        
        # If no left relational_expr, just visit the additive_expr
        return self.visit(ctx.additive_expr())

    def visitAdditive_expr(self, ctx: MiniGoParser.Additive_exprContext):
        """Visit additive expression (ADD/SUB operations)."""
        if ctx.additive_expr():  # Check if there's a left additive_expr
            left = self.visit(ctx.additive_expr())  # Visit the left side
            op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()  # Get the operator
            right = self.visit(ctx.multiplicative_expr())  # Visit the right side (higher precedence)
            return BinaryOp(op, left, right)
        
        # If no left additive_expr, just visit the multiplicative_expr
        return self.visit(ctx.multiplicative_expr())

    def visitMultiplicative_expr(self, ctx: MiniGoParser.Multiplicative_exprContext):
        """Visit multiplicative expression (MUL/DIV/MOD operations)."""
        if ctx.multiplicative_expr():  # Check if there's a left multiplicative_expr
            left = self.visit(ctx.multiplicative_expr())  # Visit the left side
            op = None
            if ctx.MUL():
                op = ctx.MUL().getText()
            elif ctx.DIV():
                op = ctx.DIV().getText()
            elif ctx.MOD():
                op = ctx.MOD().getText()
            
            right = self.visit(ctx.primary_expr())  # Visit the right side (higher precedence)
            return BinaryOp(op, left, right)
        
        # If no left multiplicative_expr, just visit the primary_expr
        return self.visit(ctx.primary_expr())

    def visitPrimary_expr(self, ctx: MiniGoParser.Primary_exprContext):
        operator = self.visit(ctx.signed_tail())  # This will return a list of operators
        expr = self.visit(ctx.field_access()) if ctx.field_access() else self.visit(ctx.atom_arr_access())  # Visit the atom
        if operator:  # If we have an operator
            for op in operator: # might remove reversed later
                expr = UnaryOp(op, expr)

        return expr  
        

     # Visit a parse tree produced by MiniGoParser#field_access.
    def visitField_access(self, ctx:MiniGoParser.Field_accessContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.atom_arr_access())
        else:
            if ctx.function_call():
                function_call = self.visit(ctx.function_call())
                return MethCall(self.visit(ctx.field_access()), function_call.funName, function_call.args)
            elif ctx.ID():
                return FieldAccess(receiver=self.visit(ctx.field_access()), field=ctx.ID().getText())
            else:
                arr = self.visit(ctx.array_access())
                res = self.visit(ctx.field_access())
                if isinstance(arr.arr, MethCall):
                    arr.arr.receiver = res
                    return ArrayCell(arr.arr, arr.idx)
                elif isinstance(arr.arr, FuncCall):
                    return ArrayCell(arr=MethCall(receiver=res,metName=arr.arr.funName, args=arr.arr.args), idx=arr.idx)
                return ArrayCell(FieldAccess(receiver=self.visit(ctx.field_access()), field=getArrName(arr)), arr.idx)


    # Visit a parse tree produced by MiniGoParser#atom_arr_access.
    def visitAtom_arr_access(self, ctx:MiniGoParser.Atom_arr_accessContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.atom())
        else:
            indices = []
            arr = self.visit(ctx.atom_arr_access())
            idx = self.visit(ctx.index_expr())
            indices.append(idx)
            if arr != None:
                if isinstance(arr, ArrayCell):
                    arr.idx.extend(indices)
                    return arr
                else:
                    return ArrayCell(arr, indices)


    # Visit a parse tree produced by MiniGoParser#atom.
    def visitAtom(self, ctx:MiniGoParser.AtomContext):
        
        if ctx.atom_value():
            return self.visit(ctx.atom_value())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        elif ctx.struct_field_access():
            return self.visit(ctx.struct_field_access())
        else:
            return self.visit(ctx.struct_field_access_no_func())


    # Visit a parse tree produced by MiniGoParser#atom_value.
    def visitAtom_value(self, ctx:MiniGoParser.Atom_valueContext):
        if ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        elif ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.NIL():
            return NilLiteral()
        else:
            return self.visit(ctx.number())

    # Visit a parse tree produced by MiniGoParser#arr_allow_lit.
    def visitArr_allow_lit(self, ctx:MiniGoParser.Arr_allow_litContext):
        if ctx.int_number():
            return self.visit(ctx.int_number())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(ctx.TRUE().getText())
        elif ctx.FALSE():
            return BooleanLiteral(ctx.FALSE().getText())
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        else:
            return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#arr_init_list.
    def visitArr_init_list(self, ctx:MiniGoParser.Arr_init_listContext):
        return self.visit(ctx.arr_init_list_body())


    # Visit a parse tree produced by MiniGoParser#arr_init_list_body.
    def visitArr_init_list_body(self, ctx:MiniGoParser.Arr_init_list_bodyContext):
        if ctx.getChildCount() == 1:
            if ctx.arr_allow_lit():
                return [self.visit(ctx.arr_allow_lit())]
            else:
                return [self.visit(ctx.arr_init_list())]
        else:
            first = self.visit(ctx.getChild(0))
            rest = self.visit(ctx.arr_init_list_body())
            return [first] + rest



    # Visit a parse tree produced by MiniGoParser#atom_list.
    # def visitAtom_list(self, ctx: MiniGoParser.Atom_listContext):
    #     """Visit atom list (parenthesized or braced expression list)."""
    #     # Visit the expression list within the braces/parentheses
    #     return self.visit(ctx.expr_list())

    # def visitExpr_list(self, ctx: MiniGoParser.Expr_listContext):
    #     """Visit expression list."""
    #     expressions = []
        
    #     # Handle the first expression or struct_init
    #     if ctx.expr():
    #         expressions.append(self.visit(ctx.expr()))
    #     elif ctx.struct_literal():
    #         expressions.append(self.visit(ctx.struct_literal()))
        
    #     # If there's a recursive expr_list after the comma, visit it
    #     if ctx.expr_list():
    #         expressions.extend(self.visit(ctx.expr_list()))
        
    #     return expressions


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    #* int_number: INT_LIT | HEX_LIT | OCT_LIT | BIN_LIT;
    def visitInt_number(self, ctx:MiniGoParser.Int_numberContext):
        return IntLiteral(ctx.getText())
        

    # Visit a parse tree produced by MiniGoParser#number.
    def visitNumber(self, ctx:MiniGoParser.NumberContext):
        if ctx.int_number():
            return self.visit(ctx.int_number())
        return FloatLiteral(ctx.FLOAT_LIT().getText())


    def visitArray_access(self, ctx: MiniGoParser.Array_accessContext):
        """Visit array access."""
        base = self.visit(ctx.secondary_index_expr())
        indices = self.visit(ctx.array_access_tail())  # Get the list of indices

        if indices:  # If there are indices, build the nested ArrayCell structure
            """ current = ArrayCell(arr=base, idx=indices[0])
            for i in range(1, len(indices)):
                current = ArrayCell(arr=current, idx=indices[i])
            return current """
            return ArrayCell(arr=base, idx=indices)
        else:
            return base  # No indices, just the base

    def visitArray_access_tail(self, ctx: MiniGoParser.Array_access_tailContext):
        """Visit array access tail and return a list of indices."""
        index_expr = self.visit(ctx.index_expr())
        if ctx.array_access_tail():
            tail_indices = self.visit(ctx.array_access_tail())
            return [index_expr] + tail_indices  # Combine current index with tail indices
        else:
            return [index_expr]  # Return a list containing the single index

    def visitIndex_expr(self, ctx: MiniGoParser.Index_exprContext):
        """Top-level index expression."""
        return self.visit(ctx.logical_index_or_expr())

    def visitLogical_index_or_expr(self, ctx:MiniGoParser.Logical_index_or_exprContext):
        if ctx.logical_index_or_expr():
            left = self.visit(ctx.logical_index_or_expr())
            right = self.visit(ctx.logical_index_and_expr())
            return BinaryOp(ctx.OR().getText(), left, right)
        return self.visit(ctx.logical_index_and_expr())


    # Visit a parse tree produced by MiniGoParser#logical_index_and_expr.
    def visitLogical_index_and_expr(self, ctx:MiniGoParser.Logical_index_and_exprContext):
        if ctx.logical_index_and_expr():
            left = self.visit(ctx.logical_index_and_expr())
            right = self.visit(ctx.relational_index_expr())
            return BinaryOp(ctx.AND().getText(), left, right)
        return self.visit(ctx.relational_index_expr())

    # def visitLogical_index_expr(self, ctx: MiniGoParser.Logical_index_exprContext):
    #     """Visit logical index expression (AND/OR operations)."""
    #     if ctx.logical_index_expr():
    #         left = self.visit(ctx.logical_index_expr())
    #         op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
    #         right = self.visit(ctx.logical_index_tail())
    #         return BinaryOp(op, left, right)
        
    #     return self.visit(ctx.equality_index_expr())

    # def visitEquality_index_expr(self, ctx: MiniGoParser.Equality_index_exprContext):
    #     if ctx.equality_index_expr():
    #         left = self.visit(ctx.equality_index_expr())
    #         op = ctx.EQ().getText() if ctx.EQ() else ctx.NEQ().getText()
    #         right = self.visit(ctx.relational_index_expr())
    #         return BinaryOp(op, left, right)
        
    #     return self.visit(ctx.relational_index_expr())

    def visitRelational_index_expr(self, ctx: MiniGoParser.Relational_index_exprContext):
        if ctx.relational_index_expr():
            left = self.visit(ctx.relational_index_expr())
            op = None
            if ctx.LT():
                op = ctx.LT().getText()
            elif ctx.LE():
                op = ctx.LE().getText()
            elif ctx.GT():
                op = ctx.GT().getText()
            elif ctx.GE():
                op = ctx.GE().getText()
            elif ctx.EQ():
                op = ctx.EQ().getText()
            elif ctx.NEQ():
                op = ctx.NEQ().getText()
            right = self.visit(ctx.additive_index_expr())
            return BinaryOp(op, left, right)
        
        return self.visit(ctx.additive_index_expr())

    def visitAdditive_index_expr(self, ctx: MiniGoParser.Additive_index_exprContext):
        if ctx.additive_index_expr():
            left = self.visit(ctx.additive_index_expr())
            op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
            right = self.visit(ctx.multiplicative_index_expr())
            return BinaryOp(op, left, right)
        
        return self.visit(ctx.multiplicative_index_expr())

    def visitMultiplicative_index_expr(self, ctx: MiniGoParser.Multiplicative_index_exprContext):
        if ctx.multiplicative_index_expr():
            left = self.visit(ctx.multiplicative_index_expr())
            op = None
            if ctx.MUL():
                op = ctx.MUL().getText()
            elif ctx.DIV():
                op = ctx.DIV().getText()
            elif ctx.MOD():
                op = ctx.MOD().getText()
            right = self.visit(ctx.signed_index_expr())
            return BinaryOp(op, left, right)
        
        return self.visit(ctx.signed_index_expr())
    
    # Visit a parse tree produced by MiniGoParser#signed_index_expr.
    def visitSigned_index_expr(self, ctx:MiniGoParser.Signed_index_exprContext):
        operator = self.visit(ctx.signed_tail())
        expr = self.visit(ctx.primary_index_expr())
        if operator:
            for op in operator:
                expr = UnaryOp(op, expr)
        return expr
    
    def visitPrimary_index_expr(self, ctx: MiniGoParser.Primary_index_exprContext):
        """Visit primary index expression with all its possible forms."""
        if ctx.secondary_index_expr():
            return self.visit(ctx.secondary_index_expr())
        elif ctx.array_access():
            return self.visit(ctx.array_access())
        elif ctx.int_number():
            return self.visit(ctx.int_number())
        elif ctx.LPAREN():
            return self.visit(ctx.index_expr())
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        elif ctx.struct_literal():
            return self.visit(ctx.
            struct_literal())
        elif ctx.struct_field_access():
            return self.visit(ctx.struct_field_access())
        else:
            return self.visit(ctx.struct_field_access_no_func())

    def visitSecondary_index_expr(self, ctx: MiniGoParser.Secondary_index_exprContext):
        """Visit secondary index expression (base of array access)."""
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        else:
            return self.visit(ctx.function_call())


    # Visit a parse tree produced by MiniGoParser#signed_tail.
    def visitSigned_tail(self, ctx: MiniGoParser.Signed_tailContext):
        if not ctx.getChildCount():  # Empty case
            return []  # Return an empty list

        operators = self.visit(ctx.signed_tail())  # Recursive call
        if operators is None:
            operators = []

        elif ctx.SUB():
            operators.append('-')
        elif ctx.NOT():
            operators.append('!')

        return operators


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx: MiniGoParser.Array_literalContext):
        """Visit array literal."""
        typ = self.visit(ctx.getChild(1))  # Visit the type of the array
        dimensions = self.visit(ctx.array_literal_tail3())  # Visit the list of dimensions
        values = self.visit(ctx.arr_init_list())  # Visit the list of values

        return ArrayLiteral(dimens=dimensions, eleType=typ, value=values)

    # def visitArray_literal_tail(self, ctx: MiniGoParser.Array_literal_tailContext):
    #     """Visit array literal tail (list of values)."""
    #     values = []
        
    #     # Handle the first value - could be either an expr or atom_list
    #     first_child = ctx.getChild(0)
    #     if isinstance(first_child, MiniGoParser.Atom_listContext):
    #         # If it's an atom_list, recursively visit it
    #         first_value = self.visit(first_child)
    #         values.append(first_value)
    #     else:
    #         # If it's a single expression
    #         expr = self.visit(first_child)
    #         values.append(expr)

    #     # Recursively process the tail if it exists
    #     if ctx.array_literal_tail():
    #         tail_values = self.visit(ctx.array_literal_tail())
    #         values.extend(tail_values)

    #     return values

    def visitArray_literal_tail3(self, ctx: MiniGoParser.Array_literal_tail3Context):
        """Visit array literal tail3 (multi-dimensional brackets)."""
        if not ctx.index_expr():
            return []
        dimensions = []
        dimensions.append(self.visit(ctx.index_expr()))
        if ctx.array_literal_tail3():
            dimensions.extend(self.visit(ctx.array_literal_tail3()))
        return dimensions


    def visitStruct_literal(self, ctx: MiniGoParser.Struct_literalContext):
        """Visit struct literal."""
        # Get the struct name as Id
        struct_name = ctx.ID().getText()
        
        # Visit struct_literal_tail to get the list of field initializations
        field_inits = self.visit(ctx.struct_literal_tail()) or []
        
        return StructLiteral(name=struct_name, elements=field_inits)

    def visitStruct_literal_tail(self, ctx: MiniGoParser.Struct_literal_tailContext):
        """Visit struct literal tail."""
        if not ctx.field_init():  # If there's no field_init, return empty list
            return []
        
        # Get the first field initialization
        field_init = self.visit(ctx.field_init())
        
        # Get any additional field initializations from tail2
        additional_fields = self.visit(ctx.struct_literal_tail2()) or []
        
        # Combine the first field with additional fields
        return [field_init] + additional_fields

    def visitStruct_literal_tail2(self, ctx: MiniGoParser.Struct_literal_tail2Context):
        """Visit struct literal tail2."""
        if not ctx.field_init():  # If there's no field_init, return empty list
            return []
        
        # Get the current field initialization
        field_init = self.visit(ctx.field_init())
        
        # Recursively get any additional field initializations
        additional_fields = self.visit(ctx.struct_literal_tail2()) or []
        
        # Return current field plus additional fields
        return [field_init] + additional_fields

    def visitField_init(self, ctx: MiniGoParser.Field_initContext):
        """Visit field initialization."""
        # Create Id for field name
        field_name = ctx.ID().getText()
        
        # Visit the expression for the field value
        field_value = self.visit(ctx.expr())
        
        # Return tuple of (field_name, field_value)
        return (field_name, field_value)

    def visitStruct_field_access(self, ctx: MiniGoParser.Struct_field_accessContext):
        head = self.visit(ctx.struct_field_access_head())
        if ctx.function_call():
            function_call = self.visit(ctx.function_call())
            return MethCall(head, function_call.funName, function_call.args)
        elif ctx.ID():
            return FieldAccess(receiver=head, field=ctx.ID().getText())
        else:
            arr = self.visit(ctx.array_access())
            if isinstance(arr.arr, MethCall):
                arr.arr.receiver = head
                return ArrayCell(arr.arr, arr.idx)
            elif isinstance(arr.arr, FuncCall):
                return ArrayCell(arr=MethCall(receiver=head,metName=arr.arr.funName, args=arr.arr.args), idx=arr.idx)
            return ArrayCell(arr=FieldAccess(receiver=head, field=getArrName(arr)), idx=arr.idx)

    def visitStruct_field_access_head(self, ctx: MiniGoParser.Struct_field_access_headContext):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.function_call():
                return self.visit(ctx.function_call())
            else:
                return self.visit(ctx.array_access())
        else: # count == 3
            if ctx.function_call():
                function_call = self.visit(ctx.function_call())
                return MethCall(self.visit(ctx.struct_field_access_head()), function_call.funName, function_call.args)
            elif ctx.ID():
                return FieldAccess(receiver=self.visit(ctx.struct_field_access_head()), field=ctx.ID().getText())
            else:
                arr = self.visit(ctx.array_access())
                head = self.visit(ctx.struct_field_access_head())
                if isinstance(arr.arr, MethCall):
                    arr.arr.receiver = head
                    return ArrayCell(arr.arr, arr.idx)
                elif isinstance(arr.arr, FuncCall):
                    return ArrayCell(arr=MethCall(receiver=head,metName=arr.arr.funName, args=arr.arr.args), idx=arr.idx)
                return ArrayCell(FieldAccess(receiver=self.visit(ctx.struct_field_access_head()), field=getArrName(arr)), arr.idx)
                
    def visitStruct_field_access_no_func(self, ctx: MiniGoParser.Struct_field_access_no_funcContext):
        head = self.visit(ctx.struct_field_access_no_func_head())
        if ctx.ID():
            return FieldAccess(receiver=head, field=ctx.ID().getText())
        else:
            arr = self.visit(ctx.array_access())
            return ArrayCell(arr=FieldAccess(receiver=head, field=getArrName(arr)), idx=arr.idx)

    def visitStruct_field_access_no_func_head(self, ctx: MiniGoParser.Struct_field_access_no_func_headContext):
        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            else:
                return self.visit(ctx.array_access())
        else:
            if ctx.ID():
                return FieldAccess(receiver=self.visit(ctx.struct_field_access_no_func_head()), field=ctx.ID().getText())
            else:
                arr = self.visit(ctx.array_access())
                return ArrayCell(FieldAccess(receiver=self.visit(ctx.struct_field_access_no_func_head()), field=getArrName(arr)), arr.idx)


    # Visit a parse tree produced by MiniGoParser#stmt_primary.
    """ def visitStmt_primary(self, ctx:MiniGoParser.Stmt_primaryContext):
        if ctx.function_call():
            res = self.visit(ctx.function_call())
            return CallStmt(res.obj, res.method, res.param)
        elif ctx.array_access():
            return self.visit(ctx.array_access())
        elif ctx.struct_field_access():
            res = self.visit(ctx.struct_field_access())
            if isinstance(res, CallExpr):
                return CallStmt(res.obj, res.method, res.param)
            return res
        elif ctx.struct_field_access_no_func():
            return self.visit(ctx.struct_field_access_no_func())
        elif ctx.assignment_stmt():
            return self.visit(ctx.assignment_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        else:
            return self.visit(ctx.assignment_stmt()) """

    # Visit a parse tree produced by MiniGoParser#stmt_in_block.
    def visitStmt_in_block(self, ctx:MiniGoParser.Stmt_in_blockContext):
        if ctx.array_access():
            return self.visit(ctx.array_access())
        elif ctx.struct_field_access():
            return self.visit(ctx.struct_field_access())
        elif ctx.struct_field_access_no_func():
            return self.visit(ctx.struct_field_access_no_func())
        elif ctx.const_decl():
            return self.visit(ctx.const_decl())
        elif ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.var_decl_no_init():
            return self.visit(ctx.var_decl_no_init())
        elif ctx.array_decl():
            return self.visit(ctx.array_decl())
        elif ctx.array_decl_with_init():
            return self.visit(ctx.array_decl_with_init())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.assignment_stmt():
            return self.visit(ctx.assignment_stmt())
        elif ctx.function_call():
            return self.visit(ctx.function_call())


    # Visit a parse tree produced by MiniGoParser#stmt_list.
    def visitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        results = []
        
        if ctx.getChildCount() == 1:  # Base case
            results.append(self.visit(ctx.stmt_in_block()))
            return results
            
        # Since the rule is stmt_list stmt_in_block, both will exist together
        # Get statements from previous stmt_list
        results.extend(self.visit(ctx.stmt_list()))
        # Add the current stmt_in_block
        stmt = self.visit(ctx.stmt_in_block())
        if stmt is not None:
            results.append(stmt)
        
        return results


    # Visit a parse tree produced by MiniGoParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:MiniGoParser.Assignment_stmtContext):
        lhs = self.visit(ctx.lhs())
        operator = self.visit(ctx.assignment_operator())
        rhs = self.visit(ctx.expr())
        # if assign operator is +=, rhs is BinaryOp(+,lhs,rhs), similar to -=,*=,/=,%=
        if operator == '+=' or operator == '-=' or operator == '*=' or operator == '/=' or operator == '%=':
            rhs = BinaryOp(operator[0], lhs, rhs)
        return Assign(lhs, rhs)

    # Visit a parse tree produced by MiniGoParser#assignment_stmt_scalar.
    def visitAssignment_stmt_scalar(self, ctx:MiniGoParser.Assignment_stmt_scalarContext):
        lhs = ctx.ID().getText()
        operator = self.visit(ctx.assignment_operator())
        rhs = self.visit(ctx.expr())
        # if assign operator is +=, rhs is BinaryOp(+,lhs,rhs), similar to -=,*=,/=,%=
        if operator == '+=' or operator == '-=' or operator == '*=' or operator == '/=' or operator == '%=':
            rhs = BinaryOp(operator[0], Id(lhs), rhs)
        return Assign(Id(lhs), rhs)

    # Visit a parse tree produced by MiniGoParser#assignment_operator.
    def visitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        if ctx.SHORT_ASSIGN():
            return ':='
        elif ctx.ADD_ASSIGN():
            return '+='
        elif ctx.SUB_ASSIGN():
            return '-='
        elif ctx.MUL_ASSIGN():
            return '*='
        elif ctx.DIV_ASSIGN():
            return '/='
        else:
            return '%='


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    # Missing else if in AST - gonna ask teacher later
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        condition = self.visit(ctx.expr())
        
        # Get the main if block
        then_block = self.visit(ctx.block())
        
        else_block = None
        if ctx.if_stmt_tail():
            else_block = self.visit(ctx.if_stmt_tail())
        
        return If(condition, then_block, else_block)

    def visitIf_stmt_tail(self, ctx:MiniGoParser.If_stmt_tailContext):
        if not ctx.getChildCount():
            return None
            
        # Check if this is an else-if branch
        if ctx.ELSE() and ctx.IF():
            condition = self.visit(ctx.expr())
            block = self.visit(ctx.block())
            
            # Recursively visit the rest of the tail
            else_block = self.visit(ctx.if_stmt_tail())
            
            return If(condition, block, else_block)
            
        # This must be the else branch
        elif ctx.ELSE():
            else_block = self.visit(ctx.block())
            return else_block
            
        return None


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        """ if ctx.for_init():
            return For(initStmt=self.visit(ctx.for_init()), expr=self.visit(ctx.expr()), postStmt=self.visit(ctx.for_update()), loop=self.visit(ctx.block()))
        elif ctx.RANGE():
            return ForArray(index=Id(ctx.ID(0).getText()), value=Id(ctx.ID(1).getText()), array=self.visit(ctx.atom()), loop=self.visit(ctx.block()))
        else:
            return For(initStmt=None, expr=self.visit(ctx.expr()), postStmt=None, loop=self.visit(ctx.block())) """
        if ctx.getChildCount() == 3: # For basic
            return ForBasic(cond=self.visit(ctx.expr()), loop=self.visit(ctx.block()))
        elif ctx.getChildCount() == 8: # For each
            return ForEach(idx=Id(ctx.ID(0).getText()), value=Id(ctx.ID(1).getText()), arr=self.visit(ctx.getChild(6)), loop=self.visit(ctx.block()))
        else: # child count 7, For step
            return ForStep(init=self.visit(ctx.for_init()), cond=self.visit(ctx.expr()), upda=self.visit(ctx.for_update()), loop=self.visit(ctx.block()))


    # Visit a parse tree produced by MiniGoParser#for_init. done
    def visitFor_init(self, ctx:MiniGoParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_update. done
    def visitFor_update(self, ctx:MiniGoParser.For_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        """ if ctx.types():
            return VariablesDecl(Id(ctx.ID().getText()), self.visit(ctx.types()), self.visit(ctx.expr()))
        return VariablesDecl(Id(ctx.ID().getText()), None, self.visit(ctx.expr())) """
        if ctx.primitiveType() or ctx.compositeType():
            return VarDecl(varName=ctx.ID().getText(), varType=self.visit(ctx.getChild(2)), varInit=self.visit(ctx.expr()))
        else:
            return VarDecl(varName=ctx.ID().getText(), varType=None, varInit=self.visit(ctx.expr()))


    # Visit a parse tree produced by MiniGoParser#var_decl_no_init.
    def visitVar_decl_no_init(self, ctx:MiniGoParser.Var_decl_no_initContext):
        """ return VariablesDecl(Id(ctx.ID().getText()), self.visit(ctx.types()), None) """
        return VarDecl(varName=ctx.ID().getText(), varType=self.visit(ctx.getChild(2)), varInit=None)



    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return ConstDecl(ctx.ID().getText(), None, self.visit(ctx.expr()))


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitiveType.
    def visitPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        # primitiveType: INT | FLOAT | STRING | BOOLEAN ;
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return BoolType()


    # Visit a parse tree produced by MiniGoParser#compositeType.
    def visitCompositeType(self, ctx:MiniGoParser.CompositeTypeContext):
        # return ClassType(Id(ctx.ID().getText()))
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        indices = self.visit(ctx.dimensions())
        # get only value
        # for i in range(len(indices)):
        #     indices[i] = indices[i].value
        return ArrayType(dimens=indices,eleType=self.visit(ctx.getChild(1)),)

    # Visit a parse tree produced by MiniGoParser#array_decl_with_init.
    def visitArray_decl_with_init(self, ctx:MiniGoParser.Array_decl_with_initContext):
        return VarDecl(varName=ctx.ID().getText(), varType=self.visit(ctx.arrayType()), varInit=self.visit(ctx.array_init()))

    # Visit a parse tree produced by MiniGoParser#array_decl.
    def visitArray_decl(self, ctx:MiniGoParser.Array_declContext):
        return VarDecl(varName=ctx.ID().getText(), varType=self.visit(ctx.arrayType()), varInit=None)
        # indices = self.visit(ctx.dimensions())
        # # get only value
        # for i in range(len(indices)):
        #     indices[i] = indices[i].value
        # return VariablesDecl(Id(ctx.ID().getText()), ArrayType(self.visit(ctx.types()), indices), self.visit(ctx.array_init()) if ctx.array_init() else None)



    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        dim = []
        # dim.append(IntLiteral(int(ctx.INT_LIT().getText())))
        if ctx.int_number():
            dim.append(self.visit(ctx.int_number()))
        elif ctx.ID():
            dim.append(Id(ctx.ID().getText()))
        if ctx.dimensions():
            dim.extend(self.visit(ctx.dimensions()))
        return dim


    # Visit a parse tree produced by MiniGoParser#array_init.
    def visitArray_init(self, ctx:MiniGoParser.Array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_init_tail.
    """ def visitArray_init_tail(self, ctx:MiniGoParser.Array_init_tailContext):
        init = []
        if ctx.expr():
            init.append(self.visit(ctx.expr()))
        if ctx.atom_list():
            init.append(self.visit(ctx.atom_list()))
        if ctx.array_init_tail():
            init.extend(self.visit(ctx.array_init_tail()))
        return init """


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return StructType(name=ctx.ID().getText(), elements=self.visit(ctx.field_decl_list()), methods=[])


    # Visit a parse tree produced by MiniGoParser#field_decl_list.
    def visitField_decl_list(self, ctx:MiniGoParser.Field_decl_listContext):
        fields = []
        if ctx.field_decl():
            fields.append(self.visit(ctx.field_decl()))
        if ctx.field_decl_list():
            fields.extend(self.visit(ctx.field_decl_list()))
        return fields


    # Visit a parse tree produced by MiniGoParser#field_decl.
    def visitField_decl(self, ctx:MiniGoParser.Field_declContext):
        return [ctx.ID().getText(), self.visit(ctx.types())]


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return InterfaceType(name=ctx.ID().getText(), methods=self.visit(ctx.method_in_decl()))


    # Visit a parse tree produced by MiniGoParser#method_in_decl.
    def visitMethod_in_decl(self, ctx:MiniGoParser.Method_in_declContext):
        methods = []
        if ctx.ID():
            params_list = []
            if ctx.param_decl():
                params_list = self.visit(ctx.param_decl())
                # takes only the type out
                for i in range(len(params_list)):
                    params_list[i] = params_list[i].parType
            methods.append(Prototype(name=ctx.ID().getText(), retType=(self.visit(ctx.types()) if ctx.types() else VoidType()), params=params_list))
        if ctx.method_in_decl():
            methods.extend(self.visit(ctx.method_in_decl()))
        return methods


    # Visit a parse tree produced by MiniGoParser#param_in_decl.
    def visitParam_decl(self, ctx:MiniGoParser.Param_declContext):
        params = []
        params.append(ParamDecl(ctx.ID().getText(), self.visit(ctx.types())))
        if ctx.param_decl_tail():
            extended_params = self.visit(ctx.param_decl_tail())
            for p in extended_params:
                params.append(ParamDecl(p, self.visit(ctx.types())))
        if ctx.param_decl():
            params.extend(self.visit(ctx.param_decl()))
        return params


    # Visit a parse tree produced by MiniGoParser#param_in_decl_tail.
    def visitParam_decl_tail(self, ctx:MiniGoParser.Param_decl_tailContext):
        params = []
        if ctx.getChildCount() > 0:
            params.append(ctx.ID().getText())
            params.extend(self.visit(ctx.param_decl_tail()))
        return params

    # Visit a parse tree produced by MiniGoParser#param_call_list.
    def visitParam_call_list(self, ctx:MiniGoParser.Param_call_listContext):
        list = []
        list.append(self.visit(ctx.expr()))
        if ctx.param_call_list():
            list.extend(self.visit(ctx.param_call_list()))
        return list

    # Visit a parse tree produced by MiniGoParser#param_decl.
    """ def visitParam_decl(self, ctx:MiniGoParser.Param_declContext):
        params = []
        params.append(VariablesDecl(Id(ctx.ID().getText()), self.visit(ctx.types()), None))
        if ctx.param_decl():
            params.extend(self.visit(ctx.param_decl()))
        return params """

    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        if not ctx.built_in_function_call():
            if ctx.param_call_list():
                return FuncCall(funName=ctx.ID().getText(), args=self.visit(ctx.param_call_list()))
            return FuncCall(funName=ctx.ID().getText(), args=[])
        return self.visit(ctx.built_in_function_call())


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return FuncDecl(name=ctx.ID().getText(), retType=(self.visit(ctx.types()) if ctx.types() else VoidType()), params=(self.visit(ctx.param_decl()) if ctx.param_decl() else []), body=self.visit(ctx.block()))


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        # return MethodDecl(name=Id(ctx.ID(1).getText()), returnType=(self.visit(ctx.types()) if ctx.types() else VoidType()), methodReceiver=VarDecl(Id(ctx.ID(0).getText()), self.visit(ctx.compositeType()), None), param=(self.visit(ctx.param_decl()) if ctx.param_decl() else []), stmts=self.visit(ctx.block()))
        return MethodDecl(receiver=ctx.ID(0).getText(), recType=self.visit(ctx.compositeType()), fun=FuncDecl(name=ctx.ID(1).getText(), retType=self.visit(ctx.types()) if ctx.types() else VoidType(), params=(self.visit(ctx.param_decl()) if ctx.param_decl() else []), body=self.visit(ctx.block())))
        

    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return Block(self.visit(ctx.stmt_list()))


    # Visit a parse tree produced by MiniGoParser#GetIntCall.
    def visitGetIntCall(self, ctx:MiniGoParser.GetIntCallContext):
        return FuncCall(funName=ctx.GET_INT().getText(), args=[])


    # Visit a parse tree produced by MiniGoParser#PutIntCall.
    def visitPutIntCall(self, ctx:MiniGoParser.PutIntCallContext):
        return FuncCall(funName=ctx.PUT_INT().getText(), args=[self.visit(ctx.expr())])


    # Visit a parse tree produced by MiniGoParser#PutIntLnCall.
    def visitPutIntLnCall(self, ctx:MiniGoParser.PutIntLnCallContext):
        return FuncCall(funName=ctx.PUT_INT_LN().getText(), args=[self.visit(ctx.expr())])  


    # Visit a parse tree produced by MiniGoParser#GetFloatCall.
    def visitGetFloatCall(self, ctx:MiniGoParser.GetFloatCallContext):
        return FuncCall(funName=ctx.GET_FLOAT().getText(), args=[])


    # Visit a parse tree produced by MiniGoParser#PutFloatCall.
    def visitPutFloatCall(self, ctx:MiniGoParser.PutFloatCallContext):
        return FuncCall(funName=ctx.PUT_FLOAT().getText(), args=[self.visit(ctx.expr())])


    # Visit a parse tree produced by MiniGoParser#PutFloatLnCall.
    def visitPutFloatLnCall(self, ctx:MiniGoParser.PutFloatLnCallContext):
        return FuncCall(funName=ctx.PUT_FLOAT_LN().getText(), args=[self.visit(ctx.expr())])


    # Visit a parse tree produced by MiniGoParser#GetBoolCall.
    def visitGetBoolCall(self, ctx:MiniGoParser.GetBoolCallContext):
        return FuncCall(funName=ctx.GET_BOOL().getText(), args=[])


    # Visit a parse tree produced by MiniGoParser#PutBoolCall.
    def visitPutBoolCall(self, ctx:MiniGoParser.PutBoolCallContext):
        return FuncCall(funName=ctx.PUT_BOOL().getText(), args=[self.visit(ctx.expr())])


    # Visit a parse tree produced by MiniGoParser#PutBoolLnCall.
    def visitPutBoolLnCall(self, ctx:MiniGoParser.PutBoolLnCallContext):
        return FuncCall(funName=ctx.PUT_BOOL_LN().getText(), args=[self.visit(ctx.expr())])


    # Visit a parse tree produced by MiniGoParser#GetStringCall.
    def visitGetStringCall(self, ctx:MiniGoParser.GetStringCallContext):
        return FuncCall(funName=ctx.GET_STRING().getText(), args=[])


    # Visit a parse tree produced by MiniGoParser#PutStringCall.
    def visitPutStringCall(self, ctx:MiniGoParser.PutStringCallContext):
        return FuncCall(funName=ctx.PUT_STRING().getText(), args=[self.visit(ctx.expr())])


    # Visit a parse tree produced by MiniGoParser#PutStringLnCall.
    def visitPutStringLnCall(self, ctx:MiniGoParser.PutStringLnCallContext):
        return FuncCall(funName=ctx.PUT_STRING_LN().getText(), args=[self.visit(ctx.expr())])


    # Visit a parse tree produced by MiniGoParser#PutLnCall.
    def visitPutLnCall(self, ctx:MiniGoParser.PutLnCallContext):
        return FuncCall(funName=ctx.PUT_LN().getText(), args=[])
    
    
# HELPER FUNCTIONS
def getArrName(arr: ArrayCell):
        while isinstance(arr, ArrayCell):
            arr = arr.arr
        if isinstance(arr, Id):
            return arr.name
        elif isinstance(arr, FuncCall):
            return arr.funName
        elif isinstance(arr, MethCall):
            return arr.metName

    

