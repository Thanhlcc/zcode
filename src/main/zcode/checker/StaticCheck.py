from functools import reduce
# from Visitor import Visitor
# from StaticError import *
# from AST import *
from src.main.zcode.utils.Utils import Utils
from src.main.zcode.utils.Visitor import BaseVisitor
from src.main.zcode.utils.AST import *
from src.main.zcode.checker.StaticError import *

class FunctionType(FuncDecl):
    def __init__(self, name: Id, params = [], return_type = None, body: Stmt = None):
        super().__init__(name, params, body)
        self.return_type = return_type
    def __init__(self, sample: FuncDecl):
        super().__init__(sample.name, sample.param, sample.body)
        self.return_type = None

class Scope:
    def __init__(self, receiver: VoidType | FunctionType | Block =VoidType()):
        """
        :param receiver: the statement or declaration that initiates the scope creation
        - type(receiver) == VoidType        ----> global scope
        - type(receiver) == FunctionType    ----> function scope
        - type(receiver) ==  Block          ----> block scope
        """
        self.receiver: VoidType | FunctionType | Block = receiver
        self.symbols = []

    def update_type(self, symbol: Id, typ: Type):
        param_names = map(lambda x: x.name, self.symbols)
        for idx, name in enumerate(param_names):
            if symbol.name == name:
                if type(symbol) is FunctionType:
                    self.symbols[idx].return_type = typ
                elif type(symbol) is VarDecl:
                    self.symbols[idx].varType = typ
                else: raise Exception(f"Unexpected type {type(symbol)}")
                return self.symbols
    def add_symbol(self, symbol: FunctionType | VarDecl):
        if type(symbol) not in [FunctionType | VarDecl]:
            raise Exception(f"Unexpected type {type(symbol)}")
        if self.is_redundant(symbol.name):
            if type(symbol) is FunctionType:
                raise Redeclared(Function(), symbol.name)
            if type(symbol) is VarDecl:
                raise Redeclared(Variable(), symbol.name)

        self.symbols.append(symbol)
        return self.symbols
    def is_redundant(self, _id: Id) -> bool:
        return _id.name in [symbol.name for symbol in self.symbols]
    @staticmethod
    def get_symbol_type(symbol: FunctionType | VarDecl) -> Function | Variable | None:
        if type(symbol) is FunctionType:
            return symbol.return_type
        return symbol.varType

    @staticmethod
    def hoisting(lst: list[Stmt]) -> tuple[list[VarDecl], list[Stmt]]:
        """
        Collect the declarations inside a scope
        :param lst: the statements inside the scope
        :return: declarations and the remaining statements
        """
        decl = list(filter(lambda stmt: type(stmt) is VarDecl, lst))
        return decl, list(set(lst) - set(decl))

class StaticChecker(BaseVisitor, Utils):
    DEFAULT_FUNCTIONS = [
        FunctionType(
            name="readNumber",
            return_type=VoidType()
        ),
        FunctionType(
            name="writeNumber",
            param=[VarDecl(name=Id("anArg"), varType=NumberType())], return_type=VoidType()
        ),
        FunctionType(
            name="readBool",
            return_type=BoolType()
        ),
        FunctionType(
            name="writeBool",
            param=[VarDecl(name=Id("anArg"), varType=BoolType())], return_type=VoidType()
        ),
        FunctionType(
            name="readString",
            return_type=StringType()
        ),
        FunctionType(
            name="writeString",
            param=[VarDecl(Id("anArg"), varType=StringType())],
            return_type=VoidType()
        ),
    ]

    def visitProgram(self, ast: Program, param: list[Scope]):
        param = [Scope()]
        param = reduce(lambda symbols, func:
                       symbols[0].add_symbols(func),
                       StaticChecker.DEFAULT_FUNCTIONS,
                       param)
        reduce(lambda symbols, decl: self.visit(decl, symbols), ast.decl, param)

    def visitVarDecl(self, ast: VarDecl, param: list[Scope]):
        param[0].add_symbol(ast)
        if ast.varInit:
            rhs_type = self.visit(ast.varInit, param)
            self.visit(Assign(ast.name, rhs_type), param)
        return param


    def visitFuncDecl(self, ast: FuncDecl, param: list[Scope]):
        func_type = FunctionType(ast)
        param[0].add_symbol(func_type)
        param = [Scope(receiver=func_type)] + param
        if ast.body:
            self.visit(ast.body, param)

        local_env = reduce(lambda symbols, decl: self.visit(decl, symbols), ast.param + f_locals, )


    def visitBlock(self, ast: Block, param: list[Scope]):
        pass

    def visitBinaryOp(self, ast: BinaryOp, param: list[Scope]):
        pass

    def visitUnaryOp(self, ast: UnaryOp, param: list[Scope]):
        pass

    def visitCallExpr(self, ast: CallExpr, param: list[Scope]):
        pass

    def visitId(self, ast: Id, param: list[Scope]):
        target: VarDecl | FunctionType \
            = self.lookup(ast.name, param[0].symbols, lambda symbol: symbol.name)
        if target:
            return Scope.get_symbol_type(target)
        raise Undeclared(Variable(), ast.name)

    def visitArrayCell(self, ast: ArrayCell, param: list[Scope]):
        pass



    def visitIf(self, ast: If, param: list[Scope]):
        pass

    def visitFor(self, ast: For, param: list[Scope]):
        pass

    def visitContinue(self, ast: Continue, param: list[Scope]):
        if type(param[0].receiver) is not For:
            raise MustInLoop(ast)

    def visitBreak(self, ast: Break, param: list[Scope]):
        if type(param[0].receiver) is not For:
            raise MustInLoop(ast)

    def visitReturn(self, ast: Return, param: list[Scope]):
        """
        Assumption: return statement is declared inside a function scope
        """
        scope = None
        for scope in param: # Get the scope of enclosing function
            if type(scope.receiver) is FunctionType: break

        enclosing_func = scope.receiver
        return_type = self.visit(ast.expr, param) if ast.expr else VoidType()
        if enclosing_func.return_type is None: # function return type is not defined yet
            enclosing_func.return_type = return_type
        elif type(enclosing_func.return_type) != type(return_type):
            raise TypeMismatchInStatement(ast)
    def visitAssign(self, ast: Assign, param: list[Scope]):
        pass

    def visitCallStmt(self, ast: CallStmt, param: list[Scope]):
        pass

    def visitNumberLiteral(self, ast: NumberLiteral, param: list[Scope]): return NumberType()
    def visitBooleanLiteral(self, ast: BooleanLiteral, param: list[Scope]): return BoolType()
    def visitStringLiteral(self, ast: StringLiteral, param: list[Scope]): return StringType()
    def visitArrayLiteral(self, ast: ArrayLiteral, param: list[Scope]): return ArrayType()
    def visitNumberType(self, ast: NumberType, param: list[Scope]): return self
    def visitBoolType(self, ast: BoolType, param: list[Scope]): return BoolType()
    def visitStringType(self, ast: StringType, param: list[Scope]): return self
    def visitArrayType(self, ast: ArrayType, param: list[Scope]): return self