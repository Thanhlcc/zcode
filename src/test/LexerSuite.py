import unittest
from TestUtils import TestLexer

EOF = '<EOF>'

def make_seq():
    for i in range(100,200):
        yield i

class LexerSuite(unittest.TestCase):
    seq = make_seq()
      
    def test_101(self):
        test = """##This is a comment
        """
        expected = f"{EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))
    
    def test_102(self):
        test = "This is a string"
        expected = f"This is a string,{EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_103(self):
        test = '''"This is a unclosed string'''
        expected = f"Unclosed String: This is a unclosed string"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_104(self):
        test = "This string has escape tab \t"
        expected = f"{test[1:-1]}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_105(self):
        test = '''He asked: \'\"This is a string\'\"'''
        expected = f"{test[1:-1]}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_106(self):
        test = """ "abc\nabc" """
        expected = f"""Unclosed String: abc"""
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_107(self):
        test = "This is a string\\"
        expected = f"Illegal Escape, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_108(self):
        test = "isPrime"
        expected = f"isPrime, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_109(self):
        test = "_isPrime"
        expected = f"_isPrime, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_110(self):
        test = "isPrime1"
        expected = f"isPrime1, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_111(self):
        test = "is_prime"
        expected = f"is_prime, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_112(self):
        test = "dec2oct"
        expected = f"dec2oct, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_113(self):
        test = "_dec2oct"
        expected = f"_dec2oct, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_114(self):
        test = "1"
        expected = f"1, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_115(self):
        test = "1.01"
        expected = f"1.01, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_116(self):
        test = "119"
        expected = f"119, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_117(self):
        test = "12."
        expected = f"12., {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_118(self):
        test = "12e3"
        expected = f"12e3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_119(self):
        test = "12E3"
        expected = f"12E3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_120(self):
        test = "12e-30"
        expected = f"12e-30, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_121(self):
        test = "12E-30"
        expected = f"12E-30, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))
    
    def test_122(self):
        test = "12.1E-30"
        expected = f"12.1E-30, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_123(self):
        test = "12.1e30"
        expected = f"12.1e30, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_124(self):
        test = ".10"
        expected = f"Error Token ., {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_125(self):
        test = "true"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_126(self):
        test = "false"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_127(self):
        test = "func"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_128(self):
        test = "number"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_129(self):
        test = "bool"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_130(self):
        test = "string"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_131(self):
        test = "var"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_132(self):
        test = "dynamic"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_133(self):
        test = "return"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_134(self):
        test = "for"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_135(self):
        test = "until"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_136(self):
        test = "by"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_137(self):
        test = "break"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_138(self):
        test = "continue"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_139(self):
        test = "if"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_140(self):
        test = "else"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))
    
    def test_141(self):
        test = "elif"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))
    
    def test_142(self):
        test = "begin"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_143(self):
        test = "end"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_144(self):
        test = "not"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_145(self):
        test = "and"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_146(self):
        test = "or"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_147(self):
        test = "+"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_148(self):
        test = "-"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_149(self):
        test = "*"
        expected = f"This is a string, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_150(self):
        test = "/"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_151(self):
        test = "%"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_152(self):
        test = "=="
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_153(self):
        test = "="
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_154(self):
        test = ">="
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_155(self):
        test = "<="
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_156(self):
        test = ">"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_157(self):
        test = "<"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_158(self):
        test = "..."
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_159(self):
        test = "<-"
        expected = f"{test}, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_160(self):
        test = "a+1"
        expected = f"a,+,1, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))
    
    def test_161(self):
        test = "1+1"
        expected = f"1,+,1, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))
    
    def test_162(self):
        test = "4-3"
        expected = f"4,-,3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_163(self):
        test = "a-3"
        expected = f"a,-,3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_164(self):
        test = "1*2"
        expected = f"1,*,2, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_165(self):
        test = "1/3"
        expected = f"1,/,3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_166(self):
        test = "1%3"
        expected = f"1,%,3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_167(self):
        test = "a+2*b"
        expected = f"a,,2+,*,b, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_168(self):
        test = "(a+2*b)"
        expected = f"(,a,+,2,*,b,), {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_169(self):
        test = "not true"
        expected = f"not, true, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_170(self):
        test = "-3"
        expected = f"-,3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_171(self):
        test = "-a"
        expected = f"-,a, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_172(self):
        test = "a>2 and b>1"
        expected = f"a,>,2,and,b,>,1, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_173(self):
        test = "true and true"
        expected = f"true, and, true, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_174(self):
        test = "This is a string"
        expected = f"This is a string, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_175(self):
        test = "b[1,2,3]"
        expected = f"b,[,1,2,3,], {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_176(self):
        test = "b[[1,2]]"
        expected = f"b,[,[,1,2,],], {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_177(self):
        test = "[[1,2],[3,4]]"
        expected = f"[,[,1,2,],[,3,4,],], {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_178(self):
        test = "3>3+1"
        expected = f"3,3,+,1, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_179(self):
        test = "---3"
        expected = f"-,-,-,3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_180(self):
        test = """ "ab"..."ab" """
        expected = f"ab,...,ab, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))
    
    def test_181(self):
        test = """ "ab"=="ab" """
        expected = f"ab,==,ab, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))
    
    def test_182(self):
        test = "a=b+c*2"
        expected = f"a,=,b,+,c,*,2, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_183(self):
        test = "funcCall()"
        expected = f"funcCall,(,), {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_184(self):
        test = "a[5]=1+2"
        expected = f"a,[,5,],=,1,+,2, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_185(self):
        test = "(1+2)/(3+4)"
        expected = f"(,1,+,2,),/,(,3,+,4,), {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_186(self):
        test = "(1=2) and (3=4)"
        expected = f"(,1,=,2,),and,(,3,=,4,), {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_187(self):
        test = """abc\\abc"""
        expected = f"""Illegal Escape In String: abc\\a, {EOF}"""
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_188(self):
        test = "(a+b*(2*c))"
        expected = f"(,a,+,b,*,(,2,*,c,),), {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_189(self):
        test = "a or true"
        expected = f"This is a string, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_190(self):
        test = "a or false"
        expected = f"a,or,false, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_191(self):
        test = "a or (true and b)"
        expected = f"a,or,(,true,and,b,), {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_192(self):
        test = '''""'''
        expected = f",{EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_193(self):
        test = '''"'''
        expected = f"Unclosed String: , {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_194(self):
        test = '''"this is a string'''
        expected = f"Unclosed String: this is a string, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_195(self):
        test = """##abc\n#abc"""
        expected = f"{EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_196(self):
        test = "##abc\nbc"
        expected = f"bc, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_197(self):
        test = "###comment"
        expected = f"{EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_198(self):
        test = "#abc"
        expected = f"Error Token #, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_199(self):
        test = "12\\3abc"
        expected = f"Illegal Escape In String 12\\3, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))

    def test_200(self):
        test = "var 2a <- 12"
        expected = f"var, Error Token 2, {EOF}"
        self.assertTrue(TestLexer.test(test, expected, next(self.seq)))