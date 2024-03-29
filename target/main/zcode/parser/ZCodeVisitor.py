# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newlines.
    def visitNewlines(self, ctx:ZCodeParser.NewlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_newlines.
    def visitNullable_newlines(self, ctx:ZCodeParser.Nullable_newlinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decllist.
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explicit_vardecl.
    def visitExplicit_vardecl(self, ctx:ZCodeParser.Explicit_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#init_vardecl.
    def visitInit_vardecl(self, ctx:ZCodeParser.Init_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#simple_vardecl.
    def visitSimple_vardecl(self, ctx:ZCodeParser.Simple_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_vardecl.
    def visitImplicit_vardecl(self, ctx:ZCodeParser.Implicit_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_decl.
    def visitParameter_decl(self, ctx:ZCodeParser.Parameter_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varid.
    def visitVarid(self, ctx:ZCodeParser.VaridContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_idx.
    def visitArray_idx(self, ctx:ZCodeParser.Array_idxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dimensions.
    def visitDimensions(self, ctx:ZCodeParser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#params.
    def visitParams(self, ctx:ZCodeParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#params_tail.
    def visitParams_tail(self, ctx:ZCodeParser.Params_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body.
    def visitBody(self, ctx:ZCodeParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_stmtlist.
    def visitNullable_stmtlist(self, ctx:ZCodeParser.Nullable_stmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#asm_stmt.
    def visitAsm_stmt(self, ctx:ZCodeParser.Asm_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_clauses.
    def visitElif_clauses(self, ctx:ZCodeParser.Elif_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_clause.
    def visitElif_clause(self, ctx:ZCodeParser.Elif_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_clause.
    def visitElse_clause(self, ctx:ZCodeParser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#condition.
    def visitCondition(self, ctx:ZCodeParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcall_expr.
    def visitFuncall_expr(self, ctx:ZCodeParser.Funcall_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullbale_args.
    def visitNullbale_args(self, ctx:ZCodeParser.Nullbale_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#args_tail.
    def visitArgs_tail(self, ctx:ZCodeParser.Args_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_expr.
    def visitRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_expr.
    def visitLogical_expr(self, ctx:ZCodeParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#add_expr.
    def visitAdd_expr(self, ctx:ZCodeParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiply_expr.
    def visitMultiply_expr(self, ctx:ZCodeParser.Multiply_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_not.
    def visitLogical_not(self, ctx:ZCodeParser.Logical_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_expr.
    def visitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#subexpr.
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression_list.
    def visitExpression_list(self, ctx:ZCodeParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraylit.
    def visitArraylit(self, ctx:ZCodeParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#booleanlit.
    def visitBooleanlit(self, ctx:ZCodeParser.BooleanlitContext):
        return self.visitChildren(ctx)



del ZCodeParser