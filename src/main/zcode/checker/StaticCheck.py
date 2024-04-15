from functools import reduce

from src.main.zcode.utils.Utils import Utils
from src.main.zcode.utils.Visitor import BaseVisitor
from src.main.zcode.utils.AST import *


class Scope:
    def __init__(self, parent=None):
        self.symbols: list[Decl] = list()
        self.children: list[Scope] = list()
        self.parent: Scope | None = parent

    def add_symbol(self, name: Decl) -> None:
        if type(name) is not Decl:
            raise TypeError(f'{name} must be of type Decl')
        self.symbols.append(name)

    def validate(self, symbol: Decl) -> bool:
        for ele in self.symbols:
            if ele.name.name == symbol.name.name:
                return True
        return False

    def add_child_scope(self):
        pass

    def pop_scope(self):
        self.children.pop()


class GlobalScope(Scope):
    def add_child_scope(self):
        self.children.append(FunctionScope(parent=self))


class BlockScope(Scope):

    def add_child_scope(self):
        self.children.append(BlockScope(parent=self))


class FunctionScope(Scope):

    def add_child_scope(self):
        self.children.append(BlockScope(parent=self))


class StaticChecker(BaseVisitor, Utils):
    default_functions = [
        FuncDecl(name="readNumber", param=[], body=Return(NumberLiteral(1))),
        FuncDecl(name="writeNumber", param=[VarDecl(name=Id("anArg"), varType=NumberType())], body=Return()),
        FuncDecl(name="readBool", param=[], body=Return(BooleanLiteral(True))),
        FuncDecl(name="writeBool", param=[VarDecl(name=Id("anArg"), varType=BoolType())], body=Return()),
        FuncDecl(name="readString", param=[], body=Return(StringLiteral("foo"))),
        FuncDecl(name="writeString", param=[VarDecl(Id("anArg"), varType=StringType())], body=Return()),
    ]

    class ScopeManager:
        def __init__(self):
            self._global = GlobalScope()
            self._curr = self._global

    def visitProgram(self, ast: Program, param: ScopeManager):
        param = StaticChecker.ScopeManager()
        for default_func in self.default_functions:
            param.add_symbol(default_func)
        for decl in ast.decl:
            self.visit(decl, param)

    def visitVarDecl(self, ast: VarDecl, param: ScopeManager):
        pass

    def visitFuncDecl(self, ast: FuncDecl, param: ScopeManager):
        pass

    def visitNumberType(self, ast: NumberType, param: ScopeManager):
        return NumberType()

    def visitBoolType(self, ast: BoolType, param: ScopeManager):
        return BoolType()

    def visitStringType(self, ast: StringType, param: ScopeManager):
        return StringType()

    def visitArrayType(self, ast: ArrayType, param: ScopeManager):
        return ArrayType()

    def visitBinaryOp(self, ast: BinaryOp, param: ScopeManager):
        pass

    def visitUnaryOp(self, ast: UnaryOp, param: ScopeManager):
        pass

    def visitCallExpr(self, ast: CallExpr, param: ScopeManager):
        pass

    def visitId(self, ast: Id, param: ScopeManager):
        pass

    def visitArrayCell(self, ast: ArrayCell, param: ScopeManager):
        pass

    def visitBlock(self, ast: Block, param: ScopeManager):
        pass

    def visitIf(self, ast: If, param: ScopeManager):
        pass

    def visitFor(self, ast: For, param: ScopeManager):
        pass

    def visitContinue(self, ast: Continue, param: ScopeManager):
        pass

    def visitBreak(self, ast: Break, param: ScopeManager):
        pass

    def visitReturn(self, ast: Return, param: ScopeManager):
        pass

    def visitAssign(self, ast: Assign, param: ScopeManager):
        pass

    def visitCallStmt(self, ast: CallStmt, param: ScopeManager):
        pass

    def visitNumberLiteral(self, ast: NumberLiteral, param: ScopeManager):
        return NumberType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, param: ScopeManager):
        return BoolType()

    def visitStringLiteral(self, ast: StringLiteral, param: ScopeManager):
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, param: ScopeManager):
        return ArrayType()
