from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

# from src.main.zcode.utils.AST import *


class ASTGeneration(ZCodeVisitor):
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        """
        program: nullable_newlines decllist EOF;
        """
        return Program(self.visit(ctx.decllist()))

    def visitNewlines(self, ctx: ZCodeParser.NewlinesContext):
        return None

    def visitNullable_newlines(self, ctx: ZCodeParser.Nullable_newlinesContext):
        return None

    def visitNewlinetail(self, ctx: ZCodeParser.NewlinetailContext):
        return None

    def visitDecllist(self, ctx: ZCodeParser.DecllistContext) : #-> [Decl]
        """
            decllist: decl decllist
                    | decl;
        """
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decllist())

    def visitDecl(self, ctx: ZCodeParser.DeclContext) :#-> FuncDecl | VarDecl:
        """
            decl: funcdecl | vardecl ;
        """
        return self.visit(ctx.getChild(0))

    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        """
        vardecl: (scalar_decl | array_decl) newlines;
        """
        return self.visit(ctx.getChild(0))

    def visitPrimititve_types(self, ctx: ZCodeParser.Primititve_typesContext):
        """
            primititve_types: STRING | NUMBER | BOOLEAN
        """
        if ctx.STRING(): return StringType()
        if ctx.NUMBER(): return NumberType()
        if ctx.BOOLEAN(): return BoolType()
        #TODO: remove this later
        raise TypeError("Unknown type")
    def visitScalar_decl(self, ctx:ZCodeParser.Scalar_declContext):
        """
        scalar_decl: (primititve_types | DYNAMIC) ID (ASSIGN expression)?
                    | VAR ID ASSIGN expression;
        """
        modifier : string = None
        if ctx.DYNAMIC():
            modifier = ctx.DYNAMIC().getText()
        if ctx.VAR():
            modifier = ctx.VAR().getText()
        return VarDecl(
            name = Id(ctx.ID().getText()),
            varType = self.visit(ctx.primititve_types()) if ctx.primititve_types() else None,
            modifier = modifier,
            varInit = self.visit(ctx.expression()) if ctx.ASSIGN() else None
        )

    def visitArray_decl(self, ctx:ZCodeParser.Array_declContext):
        """
        array_decl: primititve_types array_id (ASSIGN expression)?;

        Because this is a declaration, ArrayCell.idx is [Expr] => [Float] with Expr is castable to Float and the ArrayCell.arr is an Id
        The capability is ensured by visitArray_id
        """
        arr_id = self.visit(ctx.array_id()) # ArrayCell(arr=Id(a), idx=[2.0])
        return VarDecl(
            name = arr_id.arr,
            varType = ArrayType(
                size = arr_id.idx,
                eleType = self.visit(ctx.primititve_types())
            ),
            varInit = self.visit(ctx.expression()) if ctx.ASSIGN() else None
        )
    def visitArray_id(self, ctx:ZCodeParser.Array_idContext) :#-> ArrayCell:
        """"
            array_id: ID LB numlist RB;
        """
        return ArrayCell(
            arr = Id(ctx.ID().getText()),
            idx = self.visit(ctx.numlist()) # List[float]
        )
    def visitNumlist(self, ctx:ZCodeParser.NumlistContext):# -> List[float]:
        """
        numlist: NUMBER_LIT numlisttail | NUMBER_LIT;
        """
        num = float(ctx.NUMBER_LIT().getText())
        if ctx.getChildCount() == 1:
            return [num]
        return [num] + self.visit(ctx.numlisttail())


    def visitNumlisttail(self, ctx:ZCodeParser.NumlisttailContext):# -> List[float]:
        """
        numlisttail: COMMA NUMBER_LIT numlisttail | ;
        """
        if ctx.getChildCount() == 0:
            return []
        return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.numlisttail())

    def visitSingle_vardecl(self, ctx: ZCodeParser.Single_vardeclContext):
        """
        single_vardecl: primititve_types varid;

        Visit a single parameter in the parameter list
        """
        id : Id | ArrayCell = self.visit(ctx.varid())
        if isinstance(id, Id):
            return VarDecl(
                name = id,
                varType =  self.visit(ctx.primititve_types())
            )
        if isinstance(id, ArrayCell):
            return VarDecl(
                name = id.arr,
                varType =  ArrayType(
                    size = id.idx,
                    eleType = self.visit(ctx.primititve_types())
                )
            )
    def visitParams(self, ctx: ZCodeParser.ParamsContext) :#-> [VarDecl]:
        """
        params: single_vardecl params_tail | ;
        """
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.single_vardecl())] + self.visit(ctx.params_tail())


    def visitParams_tail(self, ctx: ZCodeParser.Params_tailContext):#-> list:
        """
        params_tail: COMMA single_vardecl params_tail | ;
        """
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.single_vardecl())] + self.visit(ctx.params_tail())
    def visitVarid(self, ctx: ZCodeParser.VaridContext) :#-> Id | ArrayType:
        """
            varid: ID | array_id;
        """
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.array_id())

    def visitArray_access(self, ctx: ZCodeParser.Array_accessContext) :#-> ArrayCell:
        """
        array_access: ( ID | funcall_expr ) LB dimensions RB;
        """
        arr = Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.funcall_expr())
        return ArrayCell(
            arr = arr,
            idx = self.visit(ctx.dimensions())
        )

    def visitDimensions(self, ctx: ZCodeParser.DimensionsContext):# -> [Expr]:
        """
        dimensions: expression COMMA dimensions | expression;
        """
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.dimensions())

    def visitFuncdecl(self, ctx: ZCodeParser.FuncdeclContext): #-> FuncDecl:
        """
        funcdecl: FUNC ID LP params RP nullable_newlines body;
        """
        return FuncDecl(
            name    = Id(ctx.ID().getText()),
            param   = self.visit(ctx.params()),
            body    = self.visit(ctx.body())
        )


    def visitBody(self, ctx: ZCodeParser.BodyContext): #-> Stmt | None:
        """
        body: return_stmt | block_stmt | newlines;
        """
        if ctx.newlines(): return None
        return self.visit(ctx.getChild(0))


    def visitNullable_stmtlist(self, ctx: ZCodeParser.Nullable_stmtlistContext):
        """
        nullable_stmtlist: stmt nullable_stmtlist | ;
        """
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.nullable_stmtlist())
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
        """
            stmt: if_stmt
                | for_stmt
                | return_stmt
                | block_stmt
                | vardecl
                | asm_stmt
                | break_stmt
                | continue_stmt
                | funcall_expr newlines;
        """
        if ctx.getChildCount() == 2:
            callexpr = self.visit(ctx.funcall_expr())
            return CallStmt(
                name = callexpr.name,
                args = callexpr.args
            )
        return self.visit(ctx.getChild(0))

    def visitAsm_stmt(self, ctx: ZCodeParser.Asm_stmtContext):
        """
        asm_stmt: ( ID | array_access ) ASSIGN expression newlines;
        """
        lhs : LHS = None
        if ctx.ID():
            lhs = Id(ctx.ID().getText())
        else:
            lhs = self.visit(ctx.array_access())
        return Assign(lhs, self.visit(ctx.expression()))


    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        """
        if_stmt: IF condition nullable_newlines stmt
                elif_clauses
                else_clause;
        """
        return If(
            expr = self.visit(ctx.condition()),
            thenStmt = self.visit(ctx.stmt()),
            elifStmt = self.visit(ctx.elif_clauses()), # [(Expr, Stmt)]
            elseStmt = self.visit(ctx.else_clause())
        )

    def visitElif_clauses(self, ctx: ZCodeParser.Elif_clausesContext):#-> [(Expr, Stmt)]:
        """
        elif_clauses: elif_clause elif_clauses | ;
        """
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.elif_clause())] + self.visit(ctx.elif_clauses())


    def visitElif_clause(self, ctx: ZCodeParser.Elif_clauseContext): #-> (Expr, Stmt):
        """
        elif_clause: ELIF condition nullable_newlines stmt;
        """
        return (self.visit(ctx.condition()), self.visit(ctx.stmt()))


    def visitElse_clause(self, ctx: ZCodeParser.Else_clauseContext):# -> Stmt:
        """
        else_clause: (ELSE nullable_newlines stmt) | ;
        """
        return self.visit(ctx.stmt()) if ctx.getChildCount() != 0 else None


    def visitCondition(self, ctx: ZCodeParser.ConditionContext):
        """
        condition: LP expression RP;
        """
        return self.visit(ctx.expression())

    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        """
            for_stmt: FOR ID UNTIL expression BY expression nullable_newlines stmt;
        """
        return For(
            name = Id(ctx.ID().getText()),
            condExpr = self.visit(ctx.expression(0)),
            updExpr = self.visit(ctx.expression(1)),
            body = self.visit(ctx.stmt())
        )

    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        """
            block_stmt: BEGIN newlines nullable_stmtlist END newlines;
        """
        return Block(self.visit(ctx.nullable_stmtlist()))

    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        """
            return_stmt: RETURN (expression | ) newlines;
        """
        return Return(self.visit(ctx.expression())) if ctx.expression() else Return()


    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        """
            continue_stmt: CONTINUE newlines;
        """
        return Continue()

    def visitFuncall_expr(self, ctx: ZCodeParser.Funcall_exprContext):
        """
            funcall_expr: ID LP nullbale_args RP;
        """
        return CallExpr(
            name = Id(ctx.ID().getText()),
            args = self.visit(ctx.nullbale_args())
        )


    def visitNullbale_args(self, ctx: ZCodeParser.Nullbale_argsContext):# -> list:
        """
            nullbale_args: expression args_tail
                            | ;
        """
        if ctx.getChildCount() == 0: return []
        return [self.visit(ctx.expression())] + self.visit(ctx.args_tail())

    def visitArgs_tail(self, ctx: ZCodeParser.Args_tailContext): # -> list:
        """
            args_tail: COMMA expression args_tail
                        | ;
        """
        return [self.visit(ctx.expression())] + self.visit(ctx.args_tail()) if ctx.getChildCount() != 0 else []


    def visitExpression(self, ctx: ZCodeParser.ExpressionContext):# -> BinaryOp | UnaryOp | Literal:
        """
        expression: relational_expr CONCAT relational_expr
                    | relational_expr;
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relational_expr(0))
        lhs = self.visit(ctx.relational_expr(0))
        rhs = self.visit(ctx.relational_expr(1))
        return BinaryOp(ctx.getChild(1).getText(), lhs, rhs)


    def visitRelational_expr(self, ctx: ZCodeParser.Relational_exprContext): # -> BinaryOp:
        """
            relational_expr: logical_expr (EQ | Double_EQ | NEQ | LT | LTE | GT | GTE) logical_expr
                            | logical_expr;
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logical_expr(0))
        return BinaryOp(
            op=ctx.getChild(1).getText(),
            left=self.visit(ctx.logical_expr(0)),
            right=self.visit(ctx.logical_expr(1))
        )

    def visitLogical_expr(self, ctx: ZCodeParser.Logical_exprContext): # -> BinaryOp:
        """
        logical_expr: logical_expr (AND | OR) add_expr
                        | add_expr;
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.add_expr())
        return BinaryOp(
            op=ctx.getChild(1).getText(),
            left=self.visit(ctx.logical_expr()),
            right=self.visit(ctx.add_expr())
        )

    def visitAdd_expr(self, ctx: ZCodeParser.Add_exprContext): # -> BinaryOp:
        """
        add_expr: add_expr (PLUS| MINUS) multiply_expr
                | multiply_expr;
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiply_expr())
        return BinaryOp(
            op=ctx.getChild(1).getText(),
            left=self.visit(ctx.add_expr()),
            right=self.visit(ctx.multiply_expr())
        )

    def visitMultiply_expr(self, ctx: ZCodeParser.Multiply_exprContext): # -> Expr:
        """
            multiply_expr: multiply_expr (DIV | MUL | MOD) logical_not
                            | logical_not;
        """
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logical_not())
        return BinaryOp(
            op=ctx.getChild(1).getText(),
            left=self.visit(ctx.multiply_expr()),
            right=self.visit(ctx.logical_not())
        )

    def visitLogical_not(self, ctx: ZCodeParser.Logical_notContext): # -> UnaryOp:
        """
            logical_not: NOT logical_not
                        | sign_expr;
        """
        return UnaryOp(
            op=ctx.NOT().getText(),
            operand=self.visit(ctx.logical_not())
        ) if ctx.getChildCount() == 2 else self.visit(ctx.sign_expr())


    def visitSign_expr(self, ctx: ZCodeParser.Sign_exprContext): #-> UnaryOp:
        """
        sign_expr: MINUS sign_expr
                | subexpr;
        """
        if ctx.subexpr():
            return self.visit(ctx.subexpr())
        return UnaryOp(
            op=ctx.MINUS().getText(),
            operand=self.visit(ctx.sign_expr())
        )


    def visitSubexpr(self, ctx: ZCodeParser.SubexprContext) :#-> Literal | Expr:
        """
            subexpr: LP expression RP
                    | operand;
        """
        if ctx.operand():
            return self.visit(ctx.operand())
        return self.visit(ctx.expression())

    def visitOperand(self, ctx: ZCodeParser.OperandContext):# -> Literal:
        """
        operand:
            NUMBER_LIT
            | STRING_LIT
            | ID
            | booleanlit
            | arraylit
            | array_access
            | funcall_expr;
        """
        if ctx.NUMBER_LIT(): return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        if ctx.STRING_LIT(): return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.ID(): return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))

    def visitExpression_list(self, ctx: ZCodeParser.Expression_listContext): #-> List[Expr]:
        """
            expression_list: expression COMMA expression_list | expression;
        """
        expression = self.visit(ctx.expression())
        if ctx.getChildCount() == 1:
            return [expression]
        return [expression] + self.visit(ctx.expression_list())


    def visitArraylit(self, ctx: ZCodeParser.ArraylitContext): #-> ArrayLiteral:
        """
            arraylit: LB expression_list RB;
        """
        return ArrayLiteral(self.visit(ctx.expression_list()))

    def visitBooleanlit(self, ctx: ZCodeParser.BooleanlitContext):# -> BooleanLiteral:
        """
            booleanlit: TRUE | FALSE;
        """
        return BooleanLiteral(
            value = ctx.getChild(0).getText() == "true"
        )
