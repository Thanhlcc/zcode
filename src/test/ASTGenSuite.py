# 2052256
import unittest
from TestUtils import TestAST
from AST import *


# from src.main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    # Test Declarations
    def test_300(self):
        _input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(), None, None)]))
        self.assertTrue(TestAST.test(_input, expect, 300))

    def test_301(self):
        _input = '''
number arr[2,313.716,51]

'''
        expect = str(
            Program([
                VarDecl(
                    name=Id("arr"),
                    varType=ArrayType([
                        2.0, 313.716, 51.0
                    ],
                        NumberType()))
            ]))
        self.assertTrue(TestAST.test(_input, expect, 301))

    def test_302(self):
        _input = '''
var a <- true
'''
        expect = str(Program([VarDecl(Id("a"), None, "var", BooleanLiteral(True))]))
        self.assertTrue(TestAST.test(_input, expect, 302))

    def test_303(self):
        _input = '''
string a[2,2] <- [["Hi","Hello"],["Bye", "Seeya"]]
'''
        expect = str(Program([
            VarDecl(
                name=Id("a"),
                varType=ArrayType([2.0, 2.0], StringType()),
                modifier=None,
                varInit=ArrayLiteral([
                    ArrayLiteral([
                        StringLiteral("Hi"),
                        StringLiteral("Hello")
                    ]),
                    ArrayLiteral([
                        StringLiteral("Bye"),
                        StringLiteral("Seeya")
                    ])
                ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 303))

    def test_304(self):
        _input = '''
func nums() return [1, 2]
dynamic o6 <- foo(2, nums()[0])
'''
        expect = str(Program([
            FuncDecl(
                name=Id("nums"),
                param=[],
                body=Return(
                    expr=ArrayLiteral([
                        NumberLiteral(1.0),
                        NumberLiteral(2.0)
                    ])
                )
            ),
            VarDecl(
                name=Id("o6"),
                varType=None,
                modifier="dynamic",
                varInit=CallExpr(
                    name=Id("foo"),
                    args=[
                        NumberLiteral(2.0),
                        ArrayCell(
                            arr=CallExpr(name=Id("nums"), args=[]),
                            idx=[NumberLiteral(0.0)]
                        )
                    ]
                )
            )
        ]))
        self.assertTrue(TestAST.test(_input, expect, 304))

    def test_305(self):
        _input = '''

func foo(number a[2], number size, bool flag)
func main() begin
    foo([1, 2], 2, false)
end
'''
        expect = str(Program([
            FuncDecl(
                name=Id("foo"),
                param=[
                    VarDecl(Id("a"), ArrayType([2.0], NumberType())),
                    VarDecl(Id("size"), NumberType()),
                    VarDecl(Id("flag"), BoolType())
                ]
            ),
            FuncDecl(
                name=Id("main"),
                param=[],
                body=Block([CallStmt(
                    name=Id("foo"),
                    args=[
                        ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)]),
                        NumberLiteral(2.0),
                        BooleanLiteral(False)
                    ]
                )])
            )
        ]))
        self.assertTrue(TestAST.test(_input, expect, 305))

    def test_306(self):
        _input = '''
##
func getOrderByCustomer(number accountId) return ["apple", "bannana"]
func main() begin
    var accountId <- 12.E12
    var products <- getOrderByCustomer(accountId)
    products[b[2, 3]] <- "dump"
end
'''
        expect = str(Program([
            FuncDecl(
                name=Id("getOrderByCustomer"),
                param=[VarDecl(name=Id("accountId"), varType=NumberType())],
                body=Return(ArrayLiteral([StringLiteral("apple"), StringLiteral("bannana")]))
            ),
            FuncDecl(
                name=Id("main"),
                param=[],
                body=Block([
                    VarDecl(
                        name=Id("accountId"),
                        varType=None,
                        modifier="var",
                        varInit=NumberLiteral(12.E12)
                    ),
                    VarDecl(
                        name=Id("products"),
                        varType=None,
                        modifier="var",
                        varInit=CallExpr(
                            name=Id("getOrderByCustomer"),
                            args=[Id("accountId")]
                        )
                    ),
                    Assign(
                        lhs=ArrayCell(
                            arr=Id("products"),
                            idx=[
                                ArrayCell(
                                    arr=Id("b"),
                                    idx=[
                                        NumberLiteral(2.0),
                                        NumberLiteral(3.0)
                                    ])
                            ]),
                        rhs=StringLiteral("dump")
                    ),
                ])
            )
        ]))
        self.assertTrue(TestAST.test(_input, expect, 306))

        def test_307(self):
            _input = """func inc(number a) return a + 1
func main() begin
var a <- 1
inc(a)
writeNumber(a)
end
"""
            expect = str(Program([
                FuncDecl(
                    Id("inc"),
                    [
                        VarDecl(Id("a"), NumberType(), None, None)
                    ],
                    Return(
                        BinaryOp("+", Id("a"), NumberLiteral(1.0))
                    )),
                FuncDecl(
                    Id("main"), [], Block(
                        [VarDecl(Id("a"), None, "var", NumberLiteral(1.0)), CallStmt(Id("inc"), [Id("a")]),
                         CallStmt(Id("writeNumber"), [Id("a")])])
                )]))
            self.assertTrue(TestAST.test(_input, expect, 307))

    def test_308(self):
        _input = """func main() begin
number a
if (5 < 2) a <- 1
elif (not true) a <- 2
elif ("h" == "6") a <- 3
end
"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [],
                Block([
                    VarDecl(Id("a"), NumberType(), None, None),
                    If(
                        expr=BinaryOp("<", NumberLiteral(5.0), NumberLiteral(2.0)),
                        thenStmt=Assign(Id("a"), NumberLiteral(1.0)),
                        elifStmt=[
                            (
                                UnaryOp("not", BooleanLiteral(True)),
                                Assign(Id("a"), NumberLiteral(2.0))
                            ),
                            (
                                BinaryOp("==", StringLiteral("h"), StringLiteral("6")),
                                Assign(Id("a"), NumberLiteral(3.0))
                            )],
                        elseStmt=None
                    )
                ]))]))
        self.assertTrue(TestAST.test(_input, expect, 308))

    def test_309(self):
        _input = '''
func main() begin
    if (1 <= 2) a <- 1
    else a <- 2
end
'''
        one, two = NumberLiteral(1.0), NumberLiteral(2.0)
        a = Id("a")
        expect = str(Program([
            FuncDecl(name=Id("main"), param=[], body=Block([
                If(
                    expr=BinaryOp("<=", one, two),
                    thenStmt=Assign(a, one),
                    elseStmt=Assign(a, two)
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 309))

    def test_310(self):
        _input = '''
func main() begin
    if(1 > 2) a <- 2
    elif (2 == 1) a <- 3
    else a <- 0
end
'''
        zero, one, two, three = NumberLiteral(0.0), NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)
        expect = str(Program([
            FuncDecl(name=Id("main"), param=[], body=Block([
                If(
                    expr=BinaryOp(">", one, two),
                    thenStmt=Assign(Id("a"), two),
                    elifStmt=[
                        (BinaryOp("==", two, one), Assign(Id("a"), three))
                    ],
                    elseStmt=Assign(Id("a"), zero)
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 310))

    def test_311(self):
        _input = '''
func main() begin
    if(1 > 2) a <- 2
end
'''
        expect = str(Program([
            FuncDecl(name=Id("main"), param=[], body=Block([
                If(
                    expr=BinaryOp(">", NumberLiteral(1.0), NumberLiteral(2.0)),
                    thenStmt=Assign(Id("a"), NumberLiteral(2.0))
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 311))

    def test_312(self):
        _input = '''
func main() begin
    if ( 1 + 2 = 3 ) print("Correct")
    if ( 2 * 2 = 4 ) print("Correct")
    if ( 2 and 2 = 4 ) print("Correct")


    else print("Incorrect")
    if ( "hello" ... "world" == "world") print("Correct")
end

'''
        one = NumberLiteral(1.0)
        two = NumberLiteral(2.0)
        three = NumberLiteral(3.0)
        four = NumberLiteral(4.0)
        expect = str(Program([
            FuncDecl(name=Id("main"), param=[], body=Block([
                If(
                    expr=BinaryOp("=", BinaryOp("+", one, two), three),
                    thenStmt=CallStmt(Id("print"), args=[StringLiteral("Correct")]),
                ),
                If(
                    expr=BinaryOp("=", BinaryOp("*", two, two), four),
                    thenStmt=CallStmt(Id("print"), args=[StringLiteral("Correct")]),
                ),
                If(
                    expr=BinaryOp("=", BinaryOp("and", two, two), four),
                    thenStmt=CallStmt(Id("print"), args=[StringLiteral("Correct")]),
                    elseStmt=CallStmt(Id("print"), args=[StringLiteral("Incorrect")])
                ),
                If(
                    expr=BinaryOp("...", StringLiteral("hello"),
                                  BinaryOp("==", StringLiteral("world"), StringLiteral("world"))),
                    thenStmt=CallStmt(Id("print"), args=[StringLiteral("Correct")]),
                ),
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 312))

    def test_313(self):
        _input = '''
func main() begin
    var flag <- false
    if(1 > 2) return 1 + 2
    elif (flag or true) return 1 / 2
    elif (flag and not false) return 1 - 2
    if (flag) return 1 * 2 
    else return 1 % -2
end
'''
        flag = Id("flag")
        one = NumberLiteral(1.0)
        two = NumberLiteral(2.0)
        true = BooleanLiteral(True)
        false = BooleanLiteral(False)
        expect = str(Program([
            FuncDecl(name=Id("main"), param=[], body=Block([
                VarDecl(name=Id("flag"), modifier="var", varInit=false),
                If(
                    expr=BinaryOp(">", one, two),
                    thenStmt=Return(BinaryOp("+", one, two)),
                    elifStmt=[
                        (BinaryOp("or", flag, true), Return(BinaryOp("/", one, two))),
                        (BinaryOp("and", flag, UnaryOp("not", false)), Return(BinaryOp("-", one, two)))
                    ]
                ),
                If(
                    expr=flag,
                    thenStmt=Return(BinaryOp("*", one, two)),
                    elseStmt=Return(BinaryOp("%", one, UnaryOp("-", two)))
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 313))

    def test_314(self):
        _input = '''
## *DN3;jJ/>l{E(.vsK+
func compute(number seed) return goo[1] % 100 + foo() * ( 1 = 1 ) and not (--1)
'''
        one = NumberLiteral(1.0)
        expect = str(Program([
            FuncDecl(
                name=Id("compute"),
                param=[VarDecl(Id("seed"), NumberType())],
                body=Return(BinaryOp(
                    "and",
                    BinaryOp(
                        "+",
                        BinaryOp(
                            "%",
                            ArrayCell(Id("goo"), [one]),
                            NumberLiteral(100.0)
                        ),
                        BinaryOp("*", CallExpr(Id("foo"), []), BinaryOp("=", one, one))
                    ),
                    UnaryOp("not", UnaryOp("-", UnaryOp("-", one)))
                ))
            )
        ]))
        self.assertTrue(TestAST.test(_input, expect, 314))

    def test_315(self):
        _input = '''
var a <- b[foo(2,4),b[1,get((a + foo(2)),a)]]
'''
        a, b = Id("a"), Id("b")
        one, two, four = NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(4.0)
        expect = str(Program([
            VarDecl(
                name=a,
                modifier="var",
                varInit=ArrayCell(
                    arr=b,
                    idx=[
                        CallExpr(
                            name=Id("foo"),
                            args=[two, four]),
                        ArrayCell(
                            arr=b,
                            idx=[
                                one,
                                CallExpr(
                                    name=Id("get"),
                                    args=[BinaryOp("+", a, CallExpr(Id("foo"), [two])), a])
                            ]
                        )
                    ]
                )
            )
        ]))
        self.assertTrue(TestAST.test(_input, expect, 315))

    def test_316(self):
        _input = '''
    func main() begin
        begin
            a[3] <- [1,2,3]
        end
    end
    '''
        expect = str(Program([
            FuncDecl(Id("main"), param=[], body=Block([
                Block([
                    Assign(ArrayCell(Id("a"), [NumberLiteral(3.0)]),
                           ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]))
                ])
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 316))

    def test_317(self):
        _input = '''
number i <- ("hello" == "hello")
var x <- "hello"
func main(string args) begin
    for i until i < 2 by 1
    begin
       print(x)
    end
end
'''
        hello = StringLiteral("hello")
        i, x = Id("i"), Id("x")
        expect = str(Program([
            VarDecl(name=i, varType=NumberType(), varInit=BinaryOp("==", hello, hello)),
            VarDecl(name=x, modifier="var", varInit=hello),
            FuncDecl(name=Id("main"), param=[VarDecl(Id("args"), StringType())], body=Block([
                For(
                    name=i,
                    condExpr=BinaryOp("<", i, NumberLiteral(2.0)),
                    updExpr=NumberLiteral(1.0),
                    body=Block([
                        CallStmt(name=Id("print"), args=[x])
                    ]))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 317))

    def test_318(self):
        _input = '''
## wpT;sK
## S%PB>6Yy}6]<_C
func main(string args[5]) begin
    number i <- 0.1
    for i until i < 2 by 1
    if (i % 2 = 0) break
    else continue
end
'''
        i = Id("i")
        expect = str(Program([
            FuncDecl(name=Id("main"), param=[VarDecl(name=Id("args"), varType=ArrayType([5.0], StringType()))],
                     body=Block([
                         VarDecl(name=i, varType=NumberType(), varInit=NumberLiteral(0.1)),
                         For(i, BinaryOp("<", i, NumberLiteral(2.0)), NumberLiteral(1.0), body=If(
                             expr=BinaryOp("=", BinaryOp("%", i, NumberLiteral(2.0)), NumberLiteral(0.0)),
                             thenStmt=Break(),
                             elseStmt=Continue()
                         ))
                     ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 318))

    def test_319(self):
        _input = '''
func Imain (string message, string validations[1,2,3])
            return
dynamic mJ
string HW <- 7.642 ## ewfsfdc sd;fd
'''
        expect = str(Program([
            FuncDecl(name=Id("Imain"), param=[
                VarDecl(Id("message"), StringType()),
                VarDecl(
                    Id("validations"),
                    ArrayType(
                        size=[1.0, 2.0, 3.0],
                        eleType=StringType()
                    )
                )
            ],
                     body=Return()),
            VarDecl(name=Id("mJ"), modifier="dynamic"),
            VarDecl(name=Id("HW"), varType=StringType(), varInit=NumberLiteral(7.642))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 319))

    def test_320(self):
        _input = '''
dynamic a <- 3
var result <- (a = b) + 2 + n or 4 + 5 - a and 2 - 9
'''
        two = NumberLiteral(2.0);
        four = NumberLiteral(4.0);
        five = NumberLiteral(5.0);
        nine = NumberLiteral(9.0);
        three = NumberLiteral(3.0)
        a, b, result, n = Id("a"), Id("b"), Id("result"), Id("n")
        expect = str(Program([
            VarDecl(name=a, modifier="dynamic", varInit=three),
            VarDecl(name=result, modifier='var', varInit=BinaryOp(
                op="and",
                left=BinaryOp(
                    "or",
                    BinaryOp("+", BinaryOp("+", BinaryOp("=", a, b), two), n),
                    BinaryOp("-", BinaryOp("+", four, five), a)
                ),
                right=BinaryOp("-", two, nine)
            ))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 320))

    def test_321(self):
        _input = '''
func iK ( bool GD, string zO[993.096e45,2.222e11] )
        begin
            var a <- (((1 + 2))) % 2
        end
'''
        one, two = NumberLiteral(1.0), NumberLiteral(2.0)
        expect = str(Program([
            FuncDecl(
                name=Id("iK"),
                param=[
                    VarDecl(Id("GD"), BoolType()),
                    VarDecl(Id("zO"), ArrayType([993.096e45, 2.222e11], StringType()))
                ],
                body=Block([
                    VarDecl(name=Id("a"), modifier="var", varInit=BinaryOp("%", BinaryOp("+", one, two), two))
                ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 321))

    def test_322(self):
        _input = '''
func main (number km) return
## <dqhOb},TL*?
func foo () return 537

number arr[5] ## 0O+HF:
'''
        expect = str(Program([
            FuncDecl(Id("main"), [VarDecl(Id("km"), NumberType())], Return()),
            FuncDecl(Id("foo"), [], Return(NumberLiteral(537.0))),
            VarDecl(Id("arr"), ArrayType([5.0], NumberType()))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 322))

    def test_323(self):
        _input = '''
func main()
begin
    if ( 1 >= 1 ) return [1,2]
    elif ( 1 <= 1 ) return [[1,2], [1,2]]
    else return
end
'''
        one, two = NumberLiteral(1.0), NumberLiteral(2.0)
        expect = str(Program([
            FuncDecl(Id("main"), [], body=Block([
                If(
                    BinaryOp(">=", one, one),
                    Return(ArrayLiteral([one, two])),
                    [
                        (
                            BinaryOp("<=", one, one),
                            Return(ArrayLiteral([
                                ArrayLiteral([one, two]),
                                ArrayLiteral([one, two])
                            ]))
                        )
                    ],
                    Return()
                ),
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 323))

    def test_324(self):
        _input = '''
number arr[2] <- [1,2]
func main() begin
    if (not true)
        if (false)
            if(-2 < 1) print(arr[1,2])
end
'''
        one, two = NumberLiteral(1.0), NumberLiteral(2.0)
        expect = str(Program([
            VarDecl(Id("arr"), ArrayType([2.0], NumberType()), None, ArrayLiteral([one, two])),
            FuncDecl(Id("main"), [], Block([
                If(UnaryOp("not", BooleanLiteral(True)),
                   If(BooleanLiteral(False),
                      If(BinaryOp("<", UnaryOp("-", two), one),
                         CallStmt(Id("print"), [ArrayCell(Id("arr"), [one, two])]))))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 324))

    def test_325(self):
        _input = '''
func foo() return [1]
var a <- foo()[0]
number b[1, 2] <- [[a], [a]]
'''
        a, b = Id("a"), Id("b")
        one, two = NumberLiteral(1.0), NumberLiteral(2.0)
        expect = str(Program([
            FuncDecl(Id("foo"), [], Return(ArrayLiteral([one]))),
            VarDecl(a, None, "var", ArrayCell(CallExpr(Id("foo"), []), [NumberLiteral(0.0)])),
            VarDecl(b, ArrayType([1.0, 2.0], NumberType()), None, ArrayLiteral([ArrayLiteral([a]), ArrayLiteral([a])]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 325))

    def test_326(self):
        _input = '''
## N7:n@:7$fk
func foo() begin
    a[(1 + 2) * 1 -- 2, 2] <- 1
end

'''
        one, two = NumberLiteral(1.0), NumberLiteral(2.0)
        expect = str(Program([
            FuncDecl(Id("foo"), [], Block([
                Assign(
                    ArrayCell(Id("a"), [
                        BinaryOp("-",
                                 BinaryOp("*", BinaryOp("+", one, two), one)
                                 , UnaryOp("-", two)),
                        two
                    ]), one),
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 326))

    def test_327(self):
        _input = '''
func foo() begin
    begin
        var a <- 1
    end
    begin
        var a <- foo()
    end
    return
end
'''
        expect = str(Program([
            FuncDecl(Id("foo"), [], Block([
                Block([VarDecl(Id("a"), None, "var", NumberLiteral(1.0))]),
                Block([VarDecl(Id("a"), None, "var", CallExpr(Id("foo"), []))]),
                Return()
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 327))

    def test_328(self):
        _input = '''
func BB (string jo[68,922E+59])        return 88.0

'''
        expect = str(Program([
            FuncDecl(Id("BB"), [VarDecl(Id("jo"), ArrayType([68., 922E+59], StringType()))],
                     Return(NumberLiteral(88.0)))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 328))

    def test_329(self):
        _input = '''
dynamic dfd
var df <- dfd ## O~Q
func LL (number KBE, bool pe[38], string WB)        return 92

bool sdfdsa[64,427.813]
string QNj ## %1gcFupGCbG%9T<ozn6
'''
        expect = str(Program([
            VarDecl(Id("dfd"), None, "dynamic"),
            VarDecl(Id("df"), None, "var", Id("dfd")),
            FuncDecl(Id("LL"), [VarDecl(Id("KBE"), NumberType()), VarDecl(Id("pe"), ArrayType([38.0], BoolType())),
                                VarDecl(Id("WB"), StringType())], Return(NumberLiteral(92.))),
            VarDecl(Id("sdfdsa"), ArrayType([64.0, 427.813], BoolType())),
            VarDecl(Id("QNj"), StringType())
        ]))
        self.assertTrue(TestAST.test(_input, expect, 329))

    def test_330(self):
        _input = '''
func main() begin
    a[(1+2+3)-(4+5*6/abc and (123))] <- 1 
    a[(((-5)))] <- 1
    a[(((--5))), a[0]] <- 1
end
'''
        one, two, three, four, five, six = NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(
            4.0), NumberLiteral(5.0), NumberLiteral(6.0)
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                Assign(ArrayCell(Id("a"), [
                    BinaryOp("-",
                             BinaryOp("+",
                                      BinaryOp("+", one, two),
                                      three),
                             BinaryOp("and",
                                      BinaryOp("+",
                                               four,
                                               BinaryOp("/",
                                                        BinaryOp("*", five, six),
                                                        Id("abc"))
                                               ),
                                      NumberLiteral(123.0)
                                      ))
                ]), one),
                Assign(ArrayCell(Id("a"), [UnaryOp("-", five)]), one),
                Assign(ArrayCell(Id("a"), [UnaryOp("-", UnaryOp("-", five)), ArrayCell(Id("a"), [NumberLiteral(0.0)])]),
                       one)
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 330))

    def test_331(self):
        _input = '''
func main() begin
end
'''
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 331))

    def test_332(self):
        _input = '''
func main() begin
    for i until false by 1 + 2 begin
    end

    return foo()
end

'''
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                For(Id("i"), BooleanLiteral(False), BinaryOp("+", NumberLiteral(1.0), NumberLiteral(2.0)), Block([])),
                Return(CallExpr(Id("foo"), []))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 332))

    def test_333(self):
        _input = '''
bool DYKL[4] <- true ## |[wW
string VEv
dynamic JJdF
string NHbK <- false
func RI (number Sg0b[83.181,0E37])        return

'''
        expect = str(Program([
            VarDecl(Id("DYKL"), ArrayType([4.0], BoolType()), None, BooleanLiteral(True)),
            VarDecl(Id("VEv"), StringType()),
            VarDecl(Id("JJdF"), None, "dynamic"),
            VarDecl(Id("NHbK"), StringType(), None, BooleanLiteral(False)),
            FuncDecl(Id("RI"), [VarDecl(Id("Sg0b"), ArrayType([83.181, 0E37], NumberType()))], Return())
        ]))
        self.assertTrue(TestAST.test(_input, expect, 333))

    def test_334(self):
        _input = '''

        string clients[2] <- [newClient[2], foo(---2)[2 + 1, not true]]

'''
        expect = str(Program([
            VarDecl(Id("clients"), ArrayType([2.0], StringType()), None, ArrayLiteral([
                ArrayCell(Id("newClient"), [NumberLiteral(2.0)]),
                ArrayCell(
                    arr=CallExpr(Id("foo"), [UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(2.0))))]),
                    idx=[
                        BinaryOp("+", NumberLiteral(2.0), NumberLiteral(1.0)),
                        UnaryOp("not", BooleanLiteral(True))
                    ])
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 334))

    def test_335(self):
        _input = '''
func main() begin
return 2
end
'''
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                Return(NumberLiteral(2.0))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 335))

    def test_336(self):
        _input = '''
bool ssT[61.415E-76,869.242,3e+34] <- 9E-96
string fd[64.e+74,0.546e89,592.E+09]
'''
        expect = str(Program([
            VarDecl(Id("ssT"), ArrayType([61.415E-76, 869.242, 3e+34], BoolType()), None, NumberLiteral(9E-96)),
            VarDecl(Id("fd"), ArrayType([64.e+74, 0.546e89, 592.E+09], StringType()))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 336))

    def test_337(self):
        _input = '''
func main(string vargs[10]) begin
    begin
        var a <- 12
    end
    var a <- not false
    for a until a <= 100 by 1 begin
        if (a) print("ping")
        else print("pong")
    end
end

dynamic ab <- 12
dynamic bb <- false
'''
        expect = str(Program([
            FuncDecl(Id("main"), [VarDecl(Id("vargs"), ArrayType([10.0], StringType()))], Block([
                Block([VarDecl(Id("a"), None, "var", NumberLiteral(12.0))]),
                VarDecl(Id("a"), None, "var", UnaryOp("not", BooleanLiteral(False))),
                For(Id("a"), BinaryOp("<=", Id("a"), NumberLiteral(100.0)), NumberLiteral(1.0), Block([
                    If(Id("a"), CallStmt(Id("print"), [StringLiteral("ping")]),
                       elseStmt=CallStmt(Id("print"), [StringLiteral("pong")]))
                ]))
            ])),
            VarDecl(Id("ab"), None, "dynamic", NumberLiteral(12.0)),
            VarDecl(Id("bb"), None, "dynamic", BooleanLiteral(False))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 337))

    def test_338(self):
        _input = '''
func main() begin
    for i until i < 100 by 1
        for j until j < i by 1
            print(j)
end
'''
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(100.0)), NumberLiteral(1.0),
                    For(Id("j"), BinaryOp("<", Id("j"), Id("i")), NumberLiteral(1.0), CallStmt(Id("print"), [Id("j")])))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 338))

    def test_339(self):
        _input = '''
## M]r&}5noBNHp2i[72
var a <- true
func main() return [1,2] ##hello
'''
        expect = str(Program([
            VarDecl(Id("a"), None, "var", BooleanLiteral(True)),
            FuncDecl(Id("main"), [], Return(ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 339))

    def test_340(self):
        _input = '''
func AfJ (string asd9, number NH[464.337e-67,727.734,59.122])
        begin
        end
'''
        expect = str(Program([
            FuncDecl(Id("AfJ"), [
                VarDecl(Id("asd9"), StringType()),
                VarDecl(Id("NH"), ArrayType([464.337e-67, 727.734, 59.122], NumberType()))
            ], Block([]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 340))

    def test_341(self):
        _input = '''
func helo_func(bool flags[2]) return flags
    ## For nothingsfdsffsfsaf!@#!@
        bool foo[2] <- helo_func([false, true, false])
'''
        expect = str(Program([
            FuncDecl(Id("helo_func"), [VarDecl(Id("flags"), ArrayType([2.0], BoolType()))], Return(Id("flags"))),
            VarDecl(Id("foo"), ArrayType([2.0], BoolType()), None, CallExpr(Id("helo_func"), [ArrayLiteral([
                BooleanLiteral(False),
                BooleanLiteral(True),
                BooleanLiteral(False),
            ])]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 341))

    def test_342(self):
        _input = '''
func foo() begin
    break
end
'''
        expect = str(Program([
            FuncDecl(Id("foo"), [], Block([
                Break()
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 342))

    def test_343(self):
        _input = '''
func foo() begin
    continue
end
'''
        expect = str(Program([
            FuncDecl(Id("foo"), [], Block([
                Continue()
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 343))

    def test_344(self):
        _input = '''

        func yoo() return [false]
    var greeting <- "nothing"

func foo() return yoo()
'''
        expect = str(Program([
            FuncDecl(Id("yoo"), [], Return(ArrayLiteral([BooleanLiteral(False)]))),
            VarDecl(Id("greeting"), None, "var", StringLiteral("nothing")),
            FuncDecl(Id("foo"), [], Return(CallExpr(Id("yoo"), [])))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 344))

    def test_345(self):
        _input = '''
func foo()
'''
        expect = str(Program([
            FuncDecl(Id("foo"), [], None)
        ]))
        self.assertTrue(TestAST.test(_input, expect, 345))

    def test_346(self):
        _input = '''
func main(string firstname, string lastname, number age)


return create_new_user(firstname, lastname, age)


'''
        firstname, lastname, age = Id("firstname"), Id("lastname"), Id("age")
        expect = str(Program([
            FuncDecl(Id("main"), [
                VarDecl(firstname, StringType()),
                VarDecl(lastname, StringType()),
                VarDecl(age, NumberType()),
            ], Return(CallExpr(Id("create_new_user"), [firstname, lastname, age])))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 346))

    def test_347(self):
        _input = '''
var sfsd <- dsfsaf ## ibLjm_IXs%k{[k;r~Q
string YXO <- 12.12
dynamic QbHD ## )u
dynamic hoo <- "e"
'''
        expect = str(Program([
            VarDecl(Id("sfsd"), None, "var", Id("dsfsaf")),
            VarDecl(Id('YXO'), StringType(), None, NumberLiteral(12.12)),
            VarDecl(Id('QbHD'), None, "dynamic"),
            VarDecl(Id('hoo'), None, "dynamic", StringLiteral("e"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 347))

    def test_348(self):
        _input = '''
number jp[74.674,560.496e-25,655.410] <- false ## g{4D9>EI]p3{?wxJ;n
func glIg ()        begin
                de[false] <- hk
        end

number iE[68.339e-27,85E31] <- 57E30
'''
        expect = str(Program([
            VarDecl(Id("jp"), ArrayType([74.674, 560.496e-25, 655.410], NumberType()), None, BooleanLiteral(False)),
            FuncDecl(Id("glIg"), [], Block([
                Assign(ArrayCell(Id("de"), [BooleanLiteral(False)]), Id("hk"))
            ])),
            VarDecl(Id("iE"), ArrayType([68.339e-27, 85E31], NumberType()), None, NumberLiteral(57E30))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 348))

    def test_349(self):
        _input = '''
func main ()
begin
    if (1.0)
        a()
    elif (2.0)
        if (3.0)
            b()
        elif (4.0)
            c()
        else
            d()
end
## 6?
'''
        one, two, three, four = NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0), NumberLiteral(4.0)
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                If(one, CallStmt(Id("a"), []), elifStmt=[
                    (two, If(three, CallStmt(Id("b"), []), [
                        (four, CallStmt(Id("c"), []))
                    ], CallStmt(Id("d"), [])))
                ])
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 349))

    def test_350(self):
        _input = """
    func main() begin
        if (1)
            if (2)
                a()
            elif (3)
                if (4)
                    b()
                elif (5)
                    c()
                else d()
            elif(6)
                e()
            else g()
        elif (7) f()
    end
"""
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                If(NumberLiteral(1.0),
                   If(
                       NumberLiteral(2.0), CallStmt(Id("a"), []),
                       elifStmt=[
                           (NumberLiteral(3.0),
                            If(NumberLiteral(4.0), CallStmt(Id("b"), []),
                               elifStmt=[(NumberLiteral(5.0), CallStmt(Id("c"), []))],
                               elseStmt=CallStmt(Id("d"), [])
                               )
                            ),
                           (NumberLiteral(6.0),
                            CallStmt(Id("e"), [])
                            )
                       ],
                       elseStmt=CallStmt(Id("g"), [])),
                   elifStmt=[(NumberLiteral(7.0), CallStmt(Id("f"), []))]
                   )
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 350))

    def test_351(self):
        _input = '''
var hi <- [[[2]]]
'''
        expect = str(Program([
            VarDecl(Id("hi"), None, "var", ArrayLiteral([ArrayLiteral([ArrayLiteral([NumberLiteral(2.0)])])]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 351))

    def test_352(self):
        _input = '''
        func foo() begin
            begin
                var a <- 1
            end
            begin
                var a <- foo()
            end
            return
        end
        '''
        expect = str(Program([
            FuncDecl(Id("foo"), [], Block([
                Block([VarDecl(Id("a"), None, "var", NumberLiteral(1.0))]),
                Block([VarDecl(Id("a"), None, "var", CallExpr(Id("foo"), []))]),
                Return()
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 352))

    def test_353(self):
        _input = '''

                string clients[2] <- [newClient[2], foo(---2)[2 + 1, not true]]

        '''
        expect = str(Program([
            VarDecl(Id("clients"), ArrayType([2.0], StringType()), None, ArrayLiteral([
                ArrayCell(Id("newClient"), [NumberLiteral(2.0)]),
                ArrayCell(
                    arr=CallExpr(Id("foo"), [UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(2.0))))]),
                    idx=[
                        BinaryOp("+", NumberLiteral(2.0), NumberLiteral(1.0)),
                        UnaryOp("not", BooleanLiteral(True))
                    ])
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 353))

    def test_354(self):
        _input = '''
        func main() begin
            if ( 1 + 2 = 3 ) return print["Correct"]
            if ( 2 * 2 = 4 ) return print["Correct"]
            if ( 2 and 2 = 4 ) return print["Correct"]


            else print("Incorrect")
            if ( "hello" ... "world" == "world") print("Correct")
        end

        '''
        one = NumberLiteral(1.0)
        two = NumberLiteral(2.0)
        three = NumberLiteral(3.0)
        four = NumberLiteral(4.0)
        expect = str(Program([
            FuncDecl(name=Id("main"), param=[], body=Block([
                If(
                    expr=BinaryOp("=", BinaryOp("+", one, two), three),
                    thenStmt=Return(ArrayCell(Id("print"), [StringLiteral("Correct")])),
                ),
                If(
                    expr=BinaryOp("=", BinaryOp("*", two, two), four),
                    thenStmt=Return(ArrayCell(Id("print"), [StringLiteral("Correct")])),
                ),
                If(
                    expr=BinaryOp("=", BinaryOp("and", two, two), four),
                    thenStmt=Return(ArrayCell(Id("print"), [StringLiteral("Correct")])),
                    elseStmt=CallStmt(Id("print"), args=[StringLiteral("Incorrect")])
                ),
                If(
                    expr=BinaryOp("...", StringLiteral("hello"),
                                  BinaryOp("==", StringLiteral("world"), StringLiteral("world"))),
                    thenStmt=CallStmt(Id("print"), args=[StringLiteral("Correct")]),
                ),
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 354))

    def test_355(self):
        _input = '''
## ftU1
string nFey[0.586,1E-98]
bool ZK_ <- "c{" ## 9 5Cr>bM>eO,"#b`
func qd0 ()
        return
number bR <- false
'''
        expect = str(Program([
            VarDecl(Id("nFey"), ArrayType([0.586, 1E-98], StringType())),
            VarDecl(Id("ZK_"), BoolType(), None, StringLiteral("c{")),
            FuncDecl(Id("qd0"), [], Return()),
            VarDecl(Id("bR"), NumberType(), None, BooleanLiteral(False))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 355))

    def test_356(self):
        _input = '''
        func main() begin
            if(1 = 2) a <- 2
            elif (2 == 1) a <- 3
            else a <- 3
        end
        '''
        one, two, three = NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)
        expect = str(Program([
            FuncDecl(name=Id("main"), param=[], body=Block([
                If(
                    expr=BinaryOp("=", one, two),
                    thenStmt=Assign(Id("a"), two),
                    elifStmt=[
                        (BinaryOp("==", two, one), Assign(Id("a"), three))
                    ],
                    elseStmt=Assign(Id("a"), three)
                )
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 356))

    def test_357(self):
        _input = '''
func gfhf ()
        begin

        end


number fdsf

    func dsfsd ()
                return
'''
        expect = str(Program([
            FuncDecl(Id("gfhf"), [], Block([])),
            VarDecl(Id("fdsf"), NumberType()),
            FuncDecl(Id("dsfsd"), [], Return())
        ]))
        self.assertTrue(TestAST.test(_input, expect, 357))

    def test_358(self):
        _input = '''
func lY (bool nAo[83.412], string gH, string rTF0)
        begin
                I7()
                ## !DSC
                ## #@%$#
        end

'''
        expect = str(Program([
            FuncDecl(Id("lY"), [
                VarDecl(Id("nAo"), ArrayType([83.412], BoolType())),
                VarDecl(Id("gH"), StringType()),
                VarDecl(Id("rTF0"), StringType())
            ], Block([CallStmt(Id("I7"), [])]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 358))

    def test_359(self):
        _input = '''
        func foo() begin
            begin
                var a <- 1
            end
            begin
                dynamic a <- goo(12)
            end
            return
        end
        '''
        expect = str(Program([
            FuncDecl(Id("foo"), [], Block([
                Block([VarDecl(Id("a"), None, "var", NumberLiteral(1.0))]),
                Block([VarDecl(Id("a"), None, "dynamic", CallExpr(Id("goo"), [NumberLiteral(12.0)]))]),
                Return()
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 359))

    def test_360(self):
        _input = '''
bool Q32[586.368,8.107,96e+74] <- N29W
func X2 ()
        return
## $u:MV"4
number AbC <- 5 ## OPX5:wg&YSmsbl
## m6JdJK^YM&LW
'''
        expect = str(Program([
            VarDecl(Id("Q32"), ArrayType([586.368, 8.107, 96e+74], BoolType()), None, Id("N29W")),
            FuncDecl(Id("X2"), [], Return()),
            VarDecl(Id("AbC"), NumberType(), None, NumberLiteral(5.0))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 360))

    def test_361(self):
        _input = '''
## G3{@~%p/t
## uY($4&7
var a <- 1
'''
        expect = str(Program([
            VarDecl(Id("a"), None, "var", NumberLiteral(1.0))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 261))

    def test_362(self):
        _input = '''
func NM57 (bool Qu[88], string KUNB, string wWv)        begin
                ## aE~&fTb
                ## =_/Kw=#!th6*@c
                ## rW4=9g/h62
        end
'''
        expect = str(Program([
            FuncDecl(Id("NM57"), [
                VarDecl(Id("Qu"), ArrayType([88.0], BoolType())),
                VarDecl(Id("KUNB"), StringType()),
                VarDecl(Id("wWv"), StringType())
            ], Block([]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 362))

    def test_363(self):
        _input = '''
        dynamic a <- 3
        var result <- (a = b) + 2 + n or 4 + 5 - a and 2 - 9
        '''
        two = NumberLiteral(2.0);
        four = NumberLiteral(4.0);
        five = NumberLiteral(5.0);
        nine = NumberLiteral(9.0);
        three = NumberLiteral(3.0)
        a, b, result, n = Id("a"), Id("b"), Id("result"), Id("n")
        expect = str(Program([
            VarDecl(name=a, modifier="dynamic", varInit=three),
            VarDecl(name=result, modifier='var', varInit=BinaryOp(
                op="and",
                left=BinaryOp(
                    "or",
                    BinaryOp("+", BinaryOp("+", BinaryOp("=", a, b), two), n),
                    BinaryOp("-", BinaryOp("+", four, five), a)
                ),
                right=BinaryOp("-", two, nine)
            ))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 363))

    def test_364(self):
        _input = '''
string SDF[4.630E+24,310] <- true
func main ()
        return
'''
        expect = str(Program([
            VarDecl(Id("SDF"), ArrayType([4.630E+24, 310.], StringType()), None, BooleanLiteral(True)),
            FuncDecl(Id("main"), [], Return())
        ]))
        self.assertTrue(TestAST.test(_input, expect, 364))

    def test_365(self):
        _input = '''

                string clients[2] <- [newClient[2], foo(---2)[2 + 1, not true]]

        '''
        expect = str(Program([
            VarDecl(Id("clients"), ArrayType([2.0], StringType()), None, ArrayLiteral([
                ArrayCell(Id("newClient"), [NumberLiteral(2.0)]),
                ArrayCell(
                    arr=CallExpr(Id("foo"), [UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(2.0))))]),
                    idx=[
                        BinaryOp("+", NumberLiteral(2.0), NumberLiteral(1.0)),
                        UnaryOp("not", BooleanLiteral(True))
                    ])
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 365))

    def test_366(self):
        _input = '''
number dsf <- 32.063
number ghg <- true
'''
        expect = str(Program([
            VarDecl(Id("dsf"), NumberType(), None, NumberLiteral(32.063)),
            VarDecl(Id("ghg"), NumberType(), None, BooleanLiteral(True))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 366))

    def test_367(self):
        _input = '''
bool XvPW[36e42] <- PE ## =U}tS~.o_LoJ<C;0l^
## B,
bool ri[39.356,7] <- true ##  2PwIbQq+IW1$t}
string ve[6,7] <- "'"5'"U'"" ## ;3N!SI=IyZn
dynamic qtrG
'''
        expect = str(Program([
            VarDecl(Id("XvPW"), ArrayType([36e42], BoolType()), varInit=Id("PE")),
            VarDecl(Id("ri"), ArrayType([39.356, 7.], BoolType()), varInit=BooleanLiteral(True)),
            VarDecl(Id("ve"), ArrayType([6.0, 7.0], StringType()), varInit=StringLiteral("'\"5'\"U'\"")),
            VarDecl(Id("qtrG"), None, "dynamic")
        ]))
        self.assertTrue(TestAST.test(_input, expect, 367))

    def test_368(self):
        _input = '''
        func main(string firstname, string lastname, number age)


        return create_new_user(firstname, lastname, age)


        '''
        firstname, lastname, age = Id("firstname"), Id("lastname"), Id("age")
        expect = str(Program([
            FuncDecl(Id("main"), [
                VarDecl(firstname, StringType()),
                VarDecl(lastname, StringType()),
                VarDecl(age, NumberType()),
            ], Return(CallExpr(Id("create_new_user"), [firstname, lastname, age])))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 368))

    def test_369(self):
        _input = '''
func Zj (string H7, string tFZ)        return id

## }9L4*O=/
'''
        expect = str(Program([
            FuncDecl(Id("Zj"), [
                VarDecl(Id("H7"), StringType()),
                VarDecl(Id("tFZ"), StringType())
            ], Return(Id("id")))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 369))

    def test_370(self):
        _input = '''

        func main() begin
            for i until i < 10 by 1 begin
                if(i=1) print(i)
                else break
            end

    end
'''
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                For(Id("i"), BinaryOp("<", Id("i"), NumberLiteral(10.0)), NumberLiteral(1.0), Block([
                    If(BinaryOp("=", Id("i"), NumberLiteral(1.0)), CallStmt(Id("print"), [Id("i")]), [], Break())
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 370))

    def test_371(self):
        _input = '''
## {
bool dfds
## dffghhnkuy
##24325436
## $#$#
'''
        expect = str(Program([
            VarDecl(Id("dfds"), BoolType())
        ]))
        self.assertTrue(TestAST.test(_input, expect, 371))

    def test_372(self):
        _input = '''
func zK ()        begin
                ## greg45234
                for v until 48 by dfsd
                        continue
        end 
## 5?;AJ>4kn;s
## $lcCOG6@4Pf;
'''
        expect = str(Program([
            FuncDecl(Id("zK"), [], Block([
                For(Id("v"), NumberLiteral(48.0), Id("dfsd"), Continue())
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 372))

    def test_373(self):
        _input = '''
## wdsfdsp
## 7_pU)sdf
## i:sdfds6 V.q^Z|r
string sf[52,2] <- dsf ## 4tergfdb
## safd~b
'''
        expect = str(Program([
            VarDecl(Id("sf"), ArrayType([52., 2.], StringType()), None, Id("dsf"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 373))

    def test_374(self):
        _input = '''
## ^ewfdb`G%0,dsaf
var cgFY <- 3.073 ## 575637
string wz[0e43, 12] <- 12
bool Mu <- fgfd ## gfdf
'''
        expect = str(Program([
            VarDecl(Id("cgFY"), None, "var", NumberLiteral(3.073)),
            VarDecl(Id("wz"), ArrayType([0e43, 12.], StringType()), None, NumberLiteral(12.)),
            VarDecl(Id("Mu"), BoolType(), None, Id("fgfd"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 374))

    def test_375(self):
        _input = '''
func sdf (string name)        return nothing
'''
        expect = str(Program([
            FuncDecl(Id("sdf"), [VarDecl(Id("name"), StringType())], Return(Id("nothing")))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 375))

    def test_376(self):
        _input = '''
## iaa)<>3Ej2/ tD
## Vv$BjP7*J.>x:aeC
dynamic fs
number nums <- false
'''
        expect = str(Program([
            VarDecl(Id("fs"), None, "dynamic"),
            VarDecl(Id("nums"), NumberType(), None, BooleanLiteral(False))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 376))

    def test_377(self):
        _input = """    
            func b() 
        begin
                if (true)  return true
                elif (false) return true


            end
        """
        expect = str(Program([
            FuncDecl(Id('b'), [], Block([
                If(BooleanLiteral(True), Return(BooleanLiteral(True)),
                   [(BooleanLiteral(False), Return(BooleanLiteral(True)))])
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 377))

    def test_378(self):
        _input = '''
func foo (bool dsf[4.385,66E-06,48.482], bool fds, number dsf)        begin
                for on until true by 782.500e+95
                        begin
                        for BF until true by sIvR
                                begin
                                end
                        end
        end
'''
        expect = str(Program([
            FuncDecl(Id("foo"), [
                VarDecl(Id('dsf'), ArrayType([4.385, 66E-06, 48.482], BoolType())),
                VarDecl(Id("fds"), BoolType()),
                VarDecl(Id("dsf"), NumberType())
            ], Block([
                For(Id("on"), BooleanLiteral(True), NumberLiteral(782.500e+95), Block([
                    For(Id("BF"), BooleanLiteral(True), Id("sIvR"), Block([]))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 378))

    def test_379(self):
        _input = '''
func oib ()        begin
                ## CULt1;^V.+2J 

                if (true) if(true) if(true) print(i)
        end

## ,&F=)N7(b5p>BK3
'''
        expect = str(Program([
            FuncDecl(Id("oib"), [], Block([
                If(BooleanLiteral(True),
                   If(BooleanLiteral(True), If(BooleanLiteral(True), CallStmt(Id("print"), [Id("i")]))))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 379))

    def test_380(self):
        _input = """    
            func a()
            begin
                if (not false)  return true
            end
        """
        expect = str(Program([
            FuncDecl(Id('a'), [], Block([
                If(UnaryOp("not", BooleanLiteral(False)), Return(BooleanLiteral(True)))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 380))

    def test_381(self):
        _input = '''
## <|wQ&5
func dmiG (string dsfs, bool Ig[7E+72,61], string P3) begin
    if (true) begin
        if(not false)
            print(i)
    end
end
## ?p,!bv
'''
        expect = str(Program([
            FuncDecl(Id("dmiG"), [
                VarDecl(Id("dsfs"), StringType()),
                VarDecl(Id("Ig"), ArrayType([7E+72, 61.], BoolType())),
                VarDecl(Id("P3"), StringType())
            ], Block([
                If(BooleanLiteral(True), Block([
                    If(UnaryOp("not", BooleanLiteral(False)), CallStmt(Id("print"), [Id("i")]))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 381))

    def test_382(self):
        _input = '''
## !dsafsad
func U123 ()        return 915.556
'''
        expect = str(Program([
            FuncDecl(Id("U123"), [], Return(NumberLiteral(915.556)))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 382))

    def test_383(self):
        _input = '''
var hello <- [1,2] ## heflafdsdfs
func foo() return hello 
## sdfsd
'''
        expect = str(Program([
            VarDecl(Id("hello"), None, "var", ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0)])),
            FuncDecl(Id("foo"), [], Return(Id("hello")))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 383))

    def test_384(self):
        _input = '''
## dsaf
## )q=fdsa
number dump ## u(/sadf^asfaP
'''
        expect = str(Program([
            VarDecl(Id("dump"), NumberType())
        ]))
        self.assertTrue(TestAST.test(_input, expect, 384))

    def test_385(self):
        _input = '''
func foo(bool ofyo[8.208,72.527e75,595.926E-20], string XZ)
        return

bool ZI4[6.410,24,3.419] <- 59e12 ## _(>}3uMgZz
## T^F&0fW:=yLq!Zo^F
string u0 ## _+rAd
bool cVzR[687.690E+66,4]
'''
        expect = str(Program([
            FuncDecl(Id("foo"), [VarDecl(Id("ofyo"), ArrayType([8.208, 72.527e75, 595.926E-20], BoolType())),
                                 VarDecl(Id("XZ"), StringType())], Return()),
            VarDecl(Id("ZI4"), ArrayType([6.410, 24., 3.419], BoolType()), varInit=NumberLiteral(59e12)),
            VarDecl(Id("u0"), StringType()),
            VarDecl(Id("cVzR"), ArrayType([687.690E+66, 4.], BoolType()))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 385))

    def test_386(self):
        _input = '''
dynamic uwv
## ,eTA;hzU
## qr^.gj;oJp3nD1x9
'''
        expect = str(Program([VarDecl(Id("uwv"), None, "dynamic")]))
        self.assertTrue(TestAST.test(_input, expect, 386))

    def test_387(self):
        _input = '''
func foo ()
        return [not false, not not true]

func fd ()        begin
                for bF until "hello" by false
                    a2I <- [632, true, "8f;'"@"]
        end

'''
        false = BooleanLiteral(False)
        true = BooleanLiteral(True)
        expect = str(Program([
            FuncDecl(Id("foo"), [],
                     Return(ArrayLiteral([UnaryOp("not", false), UnaryOp("not", UnaryOp("not", true))]))),
            FuncDecl(Id("fd"), [], Block([
                For(Id('bF'), StringLiteral("hello"), false,
                    Assign(Id("a2I"), ArrayLiteral([NumberLiteral(632.), true, StringLiteral("8f;'\"@")])))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 387))

    def test_388(self):
        _input = '''
## !!]j~z7u
func foo ()
        begin
                ## ##################################
                ## COMMENT
                ## ####################################
        end
##  
'''
        expect = str(Program([
            FuncDecl(Id("foo"), [], Block([]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 388))

    def test_389(self):
        _input = '''
        var a <- b
'''
        expect = str(Program([
            VarDecl(Id("a"), None, "var", Id("b"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 389))

    def test_390(self):
        _input = '''

        func hello(string name) return "hello" ... name

'''
        expect = str(Program([
            FuncDecl(Id("hello"), [VarDecl(Id("name"), StringType())],
                     Return(BinaryOp("...", StringLiteral("hello"), Id("name"))))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 390))

    def test_391(self):
        _input = '''
## dsf
## fdsa
bool PK[59,79.259,7]
'''
        expect = str(Program([
            VarDecl(Id('PK'), ArrayType([59., 79.259, 7.], BoolType()))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 391))

    def test_392(self):
        _input = '''
var dump <- "'"'"'""
'''
        expect = str(Program([
            VarDecl(Id("dump"), None, "var", StringLiteral("'\"'\"'\""))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 392))

    def test_393(self):
        _input = '''
number df[17E53,666,230.502] <- [1---2]
'''
        expect = str(Program([
            VarDecl(Id("df"), ArrayType([17E53, 666., 230.502], NumberType()), None, ArrayLiteral([
                BinaryOp("-", NumberLiteral(1.0), UnaryOp("-", UnaryOp("-", NumberLiteral(2.))))
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 393))

    def test_394(self):
        _input = '''
func main(string df[708,6], number fe)        begin
                return

        end
## $k1GIOj+
## "I {ua
'''
        expect = str(Program([
            FuncDecl(Id("main"),
                     [VarDecl(Id("df"), ArrayType([708., 6.], StringType())), VarDecl(Id("fe"), NumberType())],
                     Block([Return()]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 394))

    def test_395(self):
        _input = '''

        ## sdfsadjfoewij
        var main <- foo(foo(), foo()) ## sdfindsaf

'''
        call_foo = CallExpr(Id("foo"), [])
        expect = str(Program([
            VarDecl(Id("main"), None, "var", CallExpr(Id("foo"), [call_foo, call_foo]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 395))

    def test_396(self):
        _input = '''
func main (string MI_[12])        begin
        end

'''
        expect = str(Program([
            FuncDecl(Id("main"), [VarDecl(Id("MI_"), ArrayType([12.], StringType()))], Block([]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 396))

    def test_397(self):
        _input = '''
number age <- (((("string"..."string")+ "string" ... "string")))
'''
        _str = StringLiteral("string")
        expect = str(Program([
            VarDecl(Id("age"), NumberType(), None,
                    BinaryOp("...", BinaryOp("+", BinaryOp("...", _str, _str), _str), _str))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 397))

    def test_398(self):
        _input = '''
func main() return call([1,2,3])
## =2v>q)*^qw-oe/
## :Cw
'''
        expect = str(Program([
            FuncDecl(Id("main"), [], Return(
                CallExpr(Id("call"), [ArrayLiteral([NumberLiteral(1.), NumberLiteral(2.), NumberLiteral(3.)])])))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 398))

    def test_399(self):
        _input = '''

        ## abfzvcx
        func main() begin
            for i until 1 + 2 by false return
        end
'''
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                For(Id("i"), BinaryOp("+", NumberLiteral(1.), NumberLiteral(2.)), BooleanLiteral(False), Return())
            ]))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 399))


def test_400(self):
    _input = '''
    number jp[74.674,560.496e-25,655.410] <- false ## g{4D9>EI]p3{?wxJ;n
    func glIg ()        begin
                    de[false] <- hk
            end

    number iE[68.339e-27,85E31] <- 57E30
    '''
    expect = str(Program([
        VarDecl(Id("jp"), ArrayType([74.674, 560.496e-25, 655.410], NumberType()), None, BooleanLiteral(False)),
        FuncDecl(Id("glIg"), [], Block([
            Assign(ArrayCell(Id("de"), [BooleanLiteral(False)]), Id("hk"))
        ])),
        VarDecl(Id("iE"), ArrayType([68.339e-27, 85E31], NumberType()), None, NumberLiteral(57E30))
    ]))
    self.assertTrue(TestAST.test(_input, expect, 400))