# Generated from w:/CO3005/assignment4/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#program_list.
    def enterProgram_list(self, ctx:MiniGoParser.Program_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program_list.
    def exitProgram_list(self, ctx:MiniGoParser.Program_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decl_or_stmt.
    def enterDecl_or_stmt(self, ctx:MiniGoParser.Decl_or_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decl_or_stmt.
    def exitDecl_or_stmt(self, ctx:MiniGoParser.Decl_or_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decl.
    def enterDecl(self, ctx:MiniGoParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decl.
    def exitDecl(self, ctx:MiniGoParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#newlines.
    def enterNewlines(self, ctx:MiniGoParser.NewlinesContext):
        pass

    # Exit a parse tree produced by MiniGoParser#newlines.
    def exitNewlines(self, ctx:MiniGoParser.NewlinesContext):
        pass


    # Enter a parse tree produced by MiniGoParser#eos.
    def enterEos(self, ctx:MiniGoParser.EosContext):
        pass

    # Exit a parse tree produced by MiniGoParser#eos.
    def exitEos(self, ctx:MiniGoParser.EosContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr.
    def enterExpr(self, ctx:MiniGoParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expr.
    def exitExpr(self, ctx:MiniGoParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#logical_or_expr.
    def enterLogical_or_expr(self, ctx:MiniGoParser.Logical_or_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#logical_or_expr.
    def exitLogical_or_expr(self, ctx:MiniGoParser.Logical_or_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#logical_and_expr.
    def enterLogical_and_expr(self, ctx:MiniGoParser.Logical_and_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#logical_and_expr.
    def exitLogical_and_expr(self, ctx:MiniGoParser.Logical_and_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#relational_expr.
    def enterRelational_expr(self, ctx:MiniGoParser.Relational_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#relational_expr.
    def exitRelational_expr(self, ctx:MiniGoParser.Relational_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#additive_expr.
    def enterAdditive_expr(self, ctx:MiniGoParser.Additive_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#additive_expr.
    def exitAdditive_expr(self, ctx:MiniGoParser.Additive_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#multiplicative_expr.
    def enterMultiplicative_expr(self, ctx:MiniGoParser.Multiplicative_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#multiplicative_expr.
    def exitMultiplicative_expr(self, ctx:MiniGoParser.Multiplicative_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primary_expr.
    def enterPrimary_expr(self, ctx:MiniGoParser.Primary_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primary_expr.
    def exitPrimary_expr(self, ctx:MiniGoParser.Primary_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_access.
    def enterField_access(self, ctx:MiniGoParser.Field_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_access.
    def exitField_access(self, ctx:MiniGoParser.Field_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#atom_arr_access.
    def enterAtom_arr_access(self, ctx:MiniGoParser.Atom_arr_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#atom_arr_access.
    def exitAtom_arr_access(self, ctx:MiniGoParser.Atom_arr_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#atom.
    def enterAtom(self, ctx:MiniGoParser.AtomContext):
        pass

    # Exit a parse tree produced by MiniGoParser#atom.
    def exitAtom(self, ctx:MiniGoParser.AtomContext):
        pass


    # Enter a parse tree produced by MiniGoParser#atom_value.
    def enterAtom_value(self, ctx:MiniGoParser.Atom_valueContext):
        pass

    # Exit a parse tree produced by MiniGoParser#atom_value.
    def exitAtom_value(self, ctx:MiniGoParser.Atom_valueContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arr_allow_lit.
    def enterArr_allow_lit(self, ctx:MiniGoParser.Arr_allow_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arr_allow_lit.
    def exitArr_allow_lit(self, ctx:MiniGoParser.Arr_allow_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arr_init_list.
    def enterArr_init_list(self, ctx:MiniGoParser.Arr_init_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arr_init_list.
    def exitArr_init_list(self, ctx:MiniGoParser.Arr_init_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arr_init_list_body.
    def enterArr_init_list_body(self, ctx:MiniGoParser.Arr_init_list_bodyContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arr_init_list_body.
    def exitArr_init_list_body(self, ctx:MiniGoParser.Arr_init_list_bodyContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal.
    def enterLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal.
    def exitLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#int_number.
    def enterInt_number(self, ctx:MiniGoParser.Int_numberContext):
        pass

    # Exit a parse tree produced by MiniGoParser#int_number.
    def exitInt_number(self, ctx:MiniGoParser.Int_numberContext):
        pass


    # Enter a parse tree produced by MiniGoParser#number.
    def enterNumber(self, ctx:MiniGoParser.NumberContext):
        pass

    # Exit a parse tree produced by MiniGoParser#number.
    def exitNumber(self, ctx:MiniGoParser.NumberContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_access.
    def enterArray_access(self, ctx:MiniGoParser.Array_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_access.
    def exitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_access_tail.
    def enterArray_access_tail(self, ctx:MiniGoParser.Array_access_tailContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_access_tail.
    def exitArray_access_tail(self, ctx:MiniGoParser.Array_access_tailContext):
        pass


    # Enter a parse tree produced by MiniGoParser#index_expr.
    def enterIndex_expr(self, ctx:MiniGoParser.Index_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#index_expr.
    def exitIndex_expr(self, ctx:MiniGoParser.Index_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#logical_index_or_expr.
    def enterLogical_index_or_expr(self, ctx:MiniGoParser.Logical_index_or_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#logical_index_or_expr.
    def exitLogical_index_or_expr(self, ctx:MiniGoParser.Logical_index_or_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#logical_index_and_expr.
    def enterLogical_index_and_expr(self, ctx:MiniGoParser.Logical_index_and_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#logical_index_and_expr.
    def exitLogical_index_and_expr(self, ctx:MiniGoParser.Logical_index_and_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#relational_index_expr.
    def enterRelational_index_expr(self, ctx:MiniGoParser.Relational_index_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#relational_index_expr.
    def exitRelational_index_expr(self, ctx:MiniGoParser.Relational_index_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#additive_index_expr.
    def enterAdditive_index_expr(self, ctx:MiniGoParser.Additive_index_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#additive_index_expr.
    def exitAdditive_index_expr(self, ctx:MiniGoParser.Additive_index_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#multiplicative_index_expr.
    def enterMultiplicative_index_expr(self, ctx:MiniGoParser.Multiplicative_index_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#multiplicative_index_expr.
    def exitMultiplicative_index_expr(self, ctx:MiniGoParser.Multiplicative_index_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#signed_index_expr.
    def enterSigned_index_expr(self, ctx:MiniGoParser.Signed_index_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#signed_index_expr.
    def exitSigned_index_expr(self, ctx:MiniGoParser.Signed_index_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primary_index_expr.
    def enterPrimary_index_expr(self, ctx:MiniGoParser.Primary_index_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primary_index_expr.
    def exitPrimary_index_expr(self, ctx:MiniGoParser.Primary_index_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#secondary_index_expr.
    def enterSecondary_index_expr(self, ctx:MiniGoParser.Secondary_index_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#secondary_index_expr.
    def exitSecondary_index_expr(self, ctx:MiniGoParser.Secondary_index_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#signed_tail.
    def enterSigned_tail(self, ctx:MiniGoParser.Signed_tailContext):
        pass

    # Exit a parse tree produced by MiniGoParser#signed_tail.
    def exitSigned_tail(self, ctx:MiniGoParser.Signed_tailContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_literal.
    def enterArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_literal.
    def exitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_literal_tail3.
    def enterArray_literal_tail3(self, ctx:MiniGoParser.Array_literal_tail3Context):
        pass

    # Exit a parse tree produced by MiniGoParser#array_literal_tail3.
    def exitArray_literal_tail3(self, ctx:MiniGoParser.Array_literal_tail3Context):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_literal.
    def enterStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_literal.
    def exitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_literal_tail.
    def enterStruct_literal_tail(self, ctx:MiniGoParser.Struct_literal_tailContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_literal_tail.
    def exitStruct_literal_tail(self, ctx:MiniGoParser.Struct_literal_tailContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_literal_tail2.
    def enterStruct_literal_tail2(self, ctx:MiniGoParser.Struct_literal_tail2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_literal_tail2.
    def exitStruct_literal_tail2(self, ctx:MiniGoParser.Struct_literal_tail2Context):
        pass


    # Enter a parse tree produced by MiniGoParser#field_init.
    def enterField_init(self, ctx:MiniGoParser.Field_initContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_init.
    def exitField_init(self, ctx:MiniGoParser.Field_initContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_field_access.
    def enterStruct_field_access(self, ctx:MiniGoParser.Struct_field_accessContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_field_access.
    def exitStruct_field_access(self, ctx:MiniGoParser.Struct_field_accessContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_field_access_head.
    def enterStruct_field_access_head(self, ctx:MiniGoParser.Struct_field_access_headContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_field_access_head.
    def exitStruct_field_access_head(self, ctx:MiniGoParser.Struct_field_access_headContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_field_access_no_func.
    def enterStruct_field_access_no_func(self, ctx:MiniGoParser.Struct_field_access_no_funcContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_field_access_no_func.
    def exitStruct_field_access_no_func(self, ctx:MiniGoParser.Struct_field_access_no_funcContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_field_access_no_func_head.
    def enterStruct_field_access_no_func_head(self, ctx:MiniGoParser.Struct_field_access_no_func_headContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_field_access_no_func_head.
    def exitStruct_field_access_no_func_head(self, ctx:MiniGoParser.Struct_field_access_no_func_headContext):
        pass


    # Enter a parse tree produced by MiniGoParser#stmt_in_block.
    def enterStmt_in_block(self, ctx:MiniGoParser.Stmt_in_blockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#stmt_in_block.
    def exitStmt_in_block(self, ctx:MiniGoParser.Stmt_in_blockContext):
        pass


    # Enter a parse tree produced by MiniGoParser#stmt_list.
    def enterStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#stmt_list.
    def exitStmt_list(self, ctx:MiniGoParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:MiniGoParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:MiniGoParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignment_stmt_scalar.
    def enterAssignment_stmt_scalar(self, ctx:MiniGoParser.Assignment_stmt_scalarContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignment_stmt_scalar.
    def exitAssignment_stmt_scalar(self, ctx:MiniGoParser.Assignment_stmt_scalarContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignment_operator.
    def enterAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignment_operator.
    def exitAssignment_operator(self, ctx:MiniGoParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignment_expr.
    def enterAssignment_expr(self, ctx:MiniGoParser.Assignment_exprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignment_expr.
    def exitAssignment_expr(self, ctx:MiniGoParser.Assignment_exprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#lhs.
    def enterLhs(self, ctx:MiniGoParser.LhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#lhs.
    def exitLhs(self, ctx:MiniGoParser.LhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_stmt.
    def enterIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_stmt.
    def exitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_stmt_tail.
    def enterIf_stmt_tail(self, ctx:MiniGoParser.If_stmt_tailContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_stmt_tail.
    def exitIf_stmt_tail(self, ctx:MiniGoParser.If_stmt_tailContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_stmt.
    def enterFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_stmt.
    def exitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_init.
    def enterFor_init(self, ctx:MiniGoParser.For_initContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_init.
    def exitFor_init(self, ctx:MiniGoParser.For_initContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_update.
    def enterFor_update(self, ctx:MiniGoParser.For_updateContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_update.
    def exitFor_update(self, ctx:MiniGoParser.For_updateContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_condition.
    def enterFor_condition(self, ctx:MiniGoParser.For_conditionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_condition.
    def exitFor_condition(self, ctx:MiniGoParser.For_conditionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#return_stmt.
    def enterReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#return_stmt.
    def exitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continue_stmt.
    def enterContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continue_stmt.
    def exitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#break_stmt.
    def enterBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#break_stmt.
    def exitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl.
    def enterVar_decl(self, ctx:MiniGoParser.Var_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl.
    def exitVar_decl(self, ctx:MiniGoParser.Var_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_decl_no_init.
    def enterVar_decl_no_init(self, ctx:MiniGoParser.Var_decl_no_initContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_decl_no_init.
    def exitVar_decl_no_init(self, ctx:MiniGoParser.Var_decl_no_initContext):
        pass


    # Enter a parse tree produced by MiniGoParser#const_decl.
    def enterConst_decl(self, ctx:MiniGoParser.Const_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#const_decl.
    def exitConst_decl(self, ctx:MiniGoParser.Const_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#types.
    def enterTypes(self, ctx:MiniGoParser.TypesContext):
        pass

    # Exit a parse tree produced by MiniGoParser#types.
    def exitTypes(self, ctx:MiniGoParser.TypesContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primitiveType.
    def enterPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primitiveType.
    def exitPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arrayType.
    def enterArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arrayType.
    def exitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#compositeType.
    def enterCompositeType(self, ctx:MiniGoParser.CompositeTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#compositeType.
    def exitCompositeType(self, ctx:MiniGoParser.CompositeTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_decl_with_init.
    def enterArray_decl_with_init(self, ctx:MiniGoParser.Array_decl_with_initContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_decl_with_init.
    def exitArray_decl_with_init(self, ctx:MiniGoParser.Array_decl_with_initContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_decl.
    def enterArray_decl(self, ctx:MiniGoParser.Array_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_decl.
    def exitArray_decl(self, ctx:MiniGoParser.Array_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#dimensions.
    def enterDimensions(self, ctx:MiniGoParser.DimensionsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#dimensions.
    def exitDimensions(self, ctx:MiniGoParser.DimensionsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_init.
    def enterArray_init(self, ctx:MiniGoParser.Array_initContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_init.
    def exitArray_init(self, ctx:MiniGoParser.Array_initContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_decl.
    def enterStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_decl.
    def exitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_decl_list.
    def enterField_decl_list(self, ctx:MiniGoParser.Field_decl_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_decl_list.
    def exitField_decl_list(self, ctx:MiniGoParser.Field_decl_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#field_decl.
    def enterField_decl(self, ctx:MiniGoParser.Field_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#field_decl.
    def exitField_decl(self, ctx:MiniGoParser.Field_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_decl.
    def enterInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_decl.
    def exitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_in_decl.
    def enterMethod_in_decl(self, ctx:MiniGoParser.Method_in_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_in_decl.
    def exitMethod_in_decl(self, ctx:MiniGoParser.Method_in_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param_decl.
    def enterParam_decl(self, ctx:MiniGoParser.Param_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param_decl.
    def exitParam_decl(self, ctx:MiniGoParser.Param_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param_decl_tail.
    def enterParam_decl_tail(self, ctx:MiniGoParser.Param_decl_tailContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param_decl_tail.
    def exitParam_decl_tail(self, ctx:MiniGoParser.Param_decl_tailContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param_call_list.
    def enterParam_call_list(self, ctx:MiniGoParser.Param_call_listContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param_call_list.
    def exitParam_call_list(self, ctx:MiniGoParser.Param_call_listContext):
        pass


    # Enter a parse tree produced by MiniGoParser#function_call.
    def enterFunction_call(self, ctx:MiniGoParser.Function_callContext):
        pass

    # Exit a parse tree produced by MiniGoParser#function_call.
    def exitFunction_call(self, ctx:MiniGoParser.Function_callContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_decl.
    def enterFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_decl.
    def exitFunc_decl(self, ctx:MiniGoParser.Func_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_decl.
    def enterMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_decl.
    def exitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        pass


    # Enter a parse tree produced by MiniGoParser#block.
    def enterBlock(self, ctx:MiniGoParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniGoParser#block.
    def exitBlock(self, ctx:MiniGoParser.BlockContext):
        pass



del MiniGoParser