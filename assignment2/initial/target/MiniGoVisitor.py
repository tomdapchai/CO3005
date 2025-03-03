# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#program_list.
    def visitProgram_list(self, ctx:MiniGoParser.Program_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl_or_stmt.
    def visitDecl_or_stmt(self, ctx:MiniGoParser.Decl_or_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#newlines.
    def visitNewlines(self, ctx:MiniGoParser.NewlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#eos.
    def visitEos(self, ctx:MiniGoParser.EosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logical_or_expr.
    def visitLogical_or_expr(self, ctx:MiniGoParser.Logical_or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logical_and_expr.
    def visitLogical_and_expr(self, ctx:MiniGoParser.Logical_and_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relational_expr.
    def visitRelational_expr(self, ctx:MiniGoParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additive_expr.
    def visitAdditive_expr(self, ctx:MiniGoParser.Additive_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicative_expr.
    def visitMultiplicative_expr(self, ctx:MiniGoParser.Multiplicative_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primary_expr.
    def visitPrimary_expr(self, ctx:MiniGoParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_access.
    def visitField_access(self, ctx:MiniGoParser.Field_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#atom_arr_access.
    def visitAtom_arr_access(self, ctx:MiniGoParser.Atom_arr_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#atom.
    def visitAtom(self, ctx:MiniGoParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#atom_value.
    def visitAtom_value(self, ctx:MiniGoParser.Atom_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_allow_lit.
    def visitArr_allow_lit(self, ctx:MiniGoParser.Arr_allow_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_init_list.
    def visitArr_init_list(self, ctx:MiniGoParser.Arr_init_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arr_init_list_body.
    def visitArr_init_list_body(self, ctx:MiniGoParser.Arr_init_list_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#int_number.
    def visitInt_number(self, ctx:MiniGoParser.Int_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#number.
    def visitNumber(self, ctx:MiniGoParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_access.
    def visitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_access_tail.
    def visitArray_access_tail(self, ctx:MiniGoParser.Array_access_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#index_expr.
    def visitIndex_expr(self, ctx:MiniGoParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logical_index_or_expr.
    def visitLogical_index_or_expr(self, ctx:MiniGoParser.Logical_index_or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#logical_index_and_expr.
    def visitLogical_index_and_expr(self, ctx:MiniGoParser.Logical_index_and_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#relational_index_expr.
    def visitRelational_index_expr(self, ctx:MiniGoParser.Relational_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#additive_index_expr.
    def visitAdditive_index_expr(self, ctx:MiniGoParser.Additive_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#multiplicative_index_expr.
    def visitMultiplicative_index_expr(self, ctx:MiniGoParser.Multiplicative_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#signed_index_expr.
    def visitSigned_index_expr(self, ctx:MiniGoParser.Signed_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primary_index_expr.
    def visitPrimary_index_expr(self, ctx:MiniGoParser.Primary_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#secondary_index_expr.
    def visitSecondary_index_expr(self, ctx:MiniGoParser.Secondary_index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#signed_tail.
    def visitSigned_tail(self, ctx:MiniGoParser.Signed_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal_tail3.
    def visitArray_literal_tail3(self, ctx:MiniGoParser.Array_literal_tail3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal_tail.
    def visitStruct_literal_tail(self, ctx:MiniGoParser.Struct_literal_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal_tail2.
    def visitStruct_literal_tail2(self, ctx:MiniGoParser.Struct_literal_tail2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_init.
    def visitField_init(self, ctx:MiniGoParser.Field_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field_access.
    def visitStruct_field_access(self, ctx:MiniGoParser.Struct_field_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field_access_head.
    def visitStruct_field_access_head(self, ctx:MiniGoParser.Struct_field_access_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field_access_no_func.
    def visitStruct_field_access_no_func(self, ctx:MiniGoParser.Struct_field_access_no_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_field_access_no_func_head.
    def visitStruct_field_access_no_func_head(self, ctx:MiniGoParser.Struct_field_access_no_func_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_in_block.
    def visitStmt_in_block(self, ctx:MiniGoParser.Stmt_in_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt_list.
    def visitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:MiniGoParser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_stmt_scalar.
    def visitAssignment_stmt_scalar(self, ctx:MiniGoParser.Assignment_stmt_scalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_operator.
    def visitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_expr.
    def visitAssignment_expr(self, ctx:MiniGoParser.Assignment_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt_tail.
    def visitIf_stmt_tail(self, ctx:MiniGoParser.If_stmt_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_stmt.
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_init.
    def visitFor_init(self, ctx:MiniGoParser.For_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_update.
    def visitFor_update(self, ctx:MiniGoParser.For_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_condition.
    def visitFor_condition(self, ctx:MiniGoParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_stmt.
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_stmt.
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl.
    def visitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_decl_no_init.
    def visitVar_decl_no_init(self, ctx:MiniGoParser.Var_decl_no_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_decl.
    def visitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#types.
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitiveType.
    def visitPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compositeType.
    def visitCompositeType(self, ctx:MiniGoParser.CompositeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_decl_with_init.
    def visitArray_decl_with_init(self, ctx:MiniGoParser.Array_decl_with_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_decl.
    def visitArray_decl(self, ctx:MiniGoParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimensions.
    def visitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_init.
    def visitArray_init(self, ctx:MiniGoParser.Array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_decl.
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_decl_list.
    def visitField_decl_list(self, ctx:MiniGoParser.Field_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_decl.
    def visitField_decl(self, ctx:MiniGoParser.Field_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_decl.
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_in_decl.
    def visitMethod_in_decl(self, ctx:MiniGoParser.Method_in_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_decl.
    def visitParam_decl(self, ctx:MiniGoParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_decl_tail.
    def visitParam_decl_tail(self, ctx:MiniGoParser.Param_decl_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param_call_list.
    def visitParam_call_list(self, ctx:MiniGoParser.Param_call_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_call.
    def visitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_decl.
    def visitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_decl.
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#GetIntCall.
    def visitGetIntCall(self, ctx:MiniGoParser.GetIntCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutIntCall.
    def visitPutIntCall(self, ctx:MiniGoParser.PutIntCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutIntLnCall.
    def visitPutIntLnCall(self, ctx:MiniGoParser.PutIntLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#GetFloatCall.
    def visitGetFloatCall(self, ctx:MiniGoParser.GetFloatCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutFloatCall.
    def visitPutFloatCall(self, ctx:MiniGoParser.PutFloatCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutFloatLnCall.
    def visitPutFloatLnCall(self, ctx:MiniGoParser.PutFloatLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#GetBoolCall.
    def visitGetBoolCall(self, ctx:MiniGoParser.GetBoolCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutBoolCall.
    def visitPutBoolCall(self, ctx:MiniGoParser.PutBoolCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutBoolLnCall.
    def visitPutBoolLnCall(self, ctx:MiniGoParser.PutBoolLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#GetStringCall.
    def visitGetStringCall(self, ctx:MiniGoParser.GetStringCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutStringCall.
    def visitPutStringCall(self, ctx:MiniGoParser.PutStringCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutStringLnCall.
    def visitPutStringLnCall(self, ctx:MiniGoParser.PutStringLnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#PutLnCall.
    def visitPutLnCall(self, ctx:MiniGoParser.PutLnCallContext):
        return self.visitChildren(ctx)



del MiniGoParser