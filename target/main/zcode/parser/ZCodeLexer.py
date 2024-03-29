# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0184\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3,\3,\7,\u011d\n,\f,\16,\u0120\13,\3,\5,\u0123\n,\3")
        buf.write(",\3,\3-\3-\7-\u0129\n-\f-\16-\u012c\13-\3.\3.\3.\5.\u0131")
        buf.write("\n.\3.\6.\u0134\n.\r.\16.\u0135\3/\6/\u0139\n/\r/\16/")
        buf.write("\u013a\3/\5/\u013e\n/\3/\5/\u0141\n/\3\60\3\60\3\60\3")
        buf.write("\60\5\60\u0147\n\60\5\60\u0149\n\60\3\61\3\61\7\61\u014d")
        buf.write("\n\61\f\61\16\61\u0150\13\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\7\62\u0158\n\62\f\62\16\62\u015b\13\62\3\62\3\62")
        buf.write("\3\63\3\63\5\63\u0161\n\63\3\63\3\63\3\63\3\64\3\64\5")
        buf.write("\64\u0168\n\64\3\64\3\64\3\64\7\64\u016d\n\64\f\64\16")
        buf.write("\64\u0170\13\64\3\65\6\65\u0173\n\65\r\65\16\65\u0174")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3:\2\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write("I&K\'M(O)Q*S+U,W-Y\2[\2]._\2a/c\60e\61g\62i\63k\2m\2o")
        buf.write("\2q\2s\64\3\2\f\3\2\f\f\4\2GGgg\6\2\f\f\17\17$$^^\3\2")
        buf.write("))\3\2$$\n\2$$))^^ddhhppttvv\5\2\n\13\16\16\"\"\t\2))")
        buf.write("^^ddhhppttvv\4\2C\\c|\3\2\62;\2\u0190\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2]\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5z\3\2\2")
        buf.write("\2\7\u0080\3\2\2\2\t\u0085\3\2\2\2\13\u008c\3\2\2\2\r")
        buf.write("\u0093\3\2\2\2\17\u009a\3\2\2\2\21\u009e\3\2\2\2\23\u00a6")
        buf.write("\3\2\2\2\25\u00ab\3\2\2\2\27\u00af\3\2\2\2\31\u00b5\3")
        buf.write("\2\2\2\33\u00b8\3\2\2\2\35\u00be\3\2\2\2\37\u00c7\3\2")
        buf.write("\2\2!\u00ca\3\2\2\2#\u00cf\3\2\2\2%\u00d4\3\2\2\2\'\u00da")
        buf.write("\3\2\2\2)\u00de\3\2\2\2+\u00e2\3\2\2\2-\u00e6\3\2\2\2")
        buf.write("/\u00e9\3\2\2\2\61\u00eb\3\2\2\2\63\u00ed\3\2\2\2\65\u00ef")
        buf.write("\3\2\2\2\67\u00f1\3\2\2\29\u00f3\3\2\2\2;\u00f5\3\2\2")
        buf.write("\2=\u00f8\3\2\2\2?\u00fb\3\2\2\2A\u00fd\3\2\2\2C\u0100")
        buf.write("\3\2\2\2E\u0102\3\2\2\2G\u0105\3\2\2\2I\u0109\3\2\2\2")
        buf.write("K\u010c\3\2\2\2M\u010e\3\2\2\2O\u0110\3\2\2\2Q\u0112\3")
        buf.write("\2\2\2S\u0114\3\2\2\2U\u0116\3\2\2\2W\u0118\3\2\2\2Y\u0126")
        buf.write("\3\2\2\2[\u012d\3\2\2\2]\u0138\3\2\2\2_\u0148\3\2\2\2")
        buf.write("a\u014a\3\2\2\2c\u0155\3\2\2\2e\u015e\3\2\2\2g\u0167\3")
        buf.write("\2\2\2i\u0172\3\2\2\2k\u0178\3\2\2\2m\u017b\3\2\2\2o\u017d")
        buf.write("\3\2\2\2q\u017f\3\2\2\2s\u0181\3\2\2\2uv\7v\2\2vw\7t\2")
        buf.write("\2wx\7w\2\2xy\7g\2\2y\4\3\2\2\2z{\7h\2\2{|\7c\2\2|}\7")
        buf.write("n\2\2}~\7u\2\2~\177\7g\2\2\177\6\3\2\2\2\u0080\u0081\7")
        buf.write("d\2\2\u0081\u0082\7q\2\2\u0082\u0083\7q\2\2\u0083\u0084")
        buf.write("\7n\2\2\u0084\b\3\2\2\2\u0085\u0086\7p\2\2\u0086\u0087")
        buf.write("\7w\2\2\u0087\u0088\7o\2\2\u0088\u0089\7d\2\2\u0089\u008a")
        buf.write("\7g\2\2\u008a\u008b\7t\2\2\u008b\n\3\2\2\2\u008c\u008d")
        buf.write("\7u\2\2\u008d\u008e\7v\2\2\u008e\u008f\7t\2\2\u008f\u0090")
        buf.write("\7k\2\2\u0090\u0091\7p\2\2\u0091\u0092\7i\2\2\u0092\f")
        buf.write("\3\2\2\2\u0093\u0094\7t\2\2\u0094\u0095\7g\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096\u0097\7w\2\2\u0097\u0098\7t\2\2\u0098\u0099")
        buf.write("\7p\2\2\u0099\16\3\2\2\2\u009a\u009b\7x\2\2\u009b\u009c")
        buf.write("\7c\2\2\u009c\u009d\7t\2\2\u009d\20\3\2\2\2\u009e\u009f")
        buf.write("\7f\2\2\u009f\u00a0\7{\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2")
        buf.write("\7c\2\2\u00a2\u00a3\7o\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7e\2\2\u00a5\22\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8")
        buf.write("\7w\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7e\2\2\u00aa\24")
        buf.write("\3\2\2\2\u00ab\u00ac\7h\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\26\3\2\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1")
        buf.write("\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\30\3\2\2\2\u00b5\u00b6\7d\2\2\u00b6\u00b7")
        buf.write("\7{\2\2\u00b7\32\3\2\2\2\u00b8\u00b9\7d\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd")
        buf.write("\7m\2\2\u00bd\34\3\2\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\36\3\2\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9 \3\2\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc")
        buf.write("\7n\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7g\2\2\u00ce\"")
        buf.write("\3\2\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7h\2\2\u00d3$\3\2\2\2\u00d4\u00d5")
        buf.write("\7d\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7i\2\2\u00d7\u00d8")
        buf.write("\7k\2\2\u00d8\u00d9\7p\2\2\u00d9&\3\2\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7f\2\2\u00dd(\3")
        buf.write("\2\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1*\3\2\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7p\2\2\u00e4\u00e5\7f\2\2\u00e5,\3\2\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7t\2\2\u00e8.\3\2\2\2\u00e9\u00ea")
        buf.write("\7-\2\2\u00ea\60\3\2\2\2\u00eb\u00ec\7/\2\2\u00ec\62\3")
        buf.write("\2\2\2\u00ed\u00ee\7,\2\2\u00ee\64\3\2\2\2\u00ef\u00f0")
        buf.write("\7\61\2\2\u00f0\66\3\2\2\2\u00f1\u00f2\7\'\2\2\u00f28")
        buf.write("\3\2\2\2\u00f3\u00f4\7?\2\2\u00f4:\3\2\2\2\u00f5\u00f6")
        buf.write("\7#\2\2\u00f6\u00f7\7?\2\2\u00f7<\3\2\2\2\u00f8\u00f9")
        buf.write("\7>\2\2\u00f9\u00fa\7/\2\2\u00fa>\3\2\2\2\u00fb\u00fc")
        buf.write("\7>\2\2\u00fc@\3\2\2\2\u00fd\u00fe\7>\2\2\u00fe\u00ff")
        buf.write("\7?\2\2\u00ffB\3\2\2\2\u0100\u0101\7@\2\2\u0101D\3\2\2")
        buf.write("\2\u0102\u0103\7@\2\2\u0103\u0104\7?\2\2\u0104F\3\2\2")
        buf.write("\2\u0105\u0106\7\60\2\2\u0106\u0107\7\60\2\2\u0107\u0108")
        buf.write("\7\60\2\2\u0108H\3\2\2\2\u0109\u010a\7?\2\2\u010a\u010b")
        buf.write("\7?\2\2\u010bJ\3\2\2\2\u010c\u010d\7*\2\2\u010dL\3\2\2")
        buf.write("\2\u010e\u010f\7+\2\2\u010fN\3\2\2\2\u0110\u0111\7]\2")
        buf.write("\2\u0111P\3\2\2\2\u0112\u0113\7_\2\2\u0113R\3\2\2\2\u0114")
        buf.write("\u0115\7\f\2\2\u0115T\3\2\2\2\u0116\u0117\7.\2\2\u0117")
        buf.write("V\3\2\2\2\u0118\u0119\7%\2\2\u0119\u011a\7%\2\2\u011a")
        buf.write("\u011e\3\2\2\2\u011b\u011d\n\2\2\2\u011c\u011b\3\2\2\2")
        buf.write("\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3")
        buf.write("\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0123")
        buf.write("\7\2\2\3\u0122\u0121\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u0124\3\2\2\2\u0124\u0125\b,\2\2\u0125X\3\2\2\2\u0126")
        buf.write("\u012a\7\60\2\2\u0127\u0129\5q9\2\u0128\u0127\3\2\2\2")
        buf.write("\u0129\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3")
        buf.write("\2\2\2\u012bZ\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u0130")
        buf.write("\t\3\2\2\u012e\u0131\5/\30\2\u012f\u0131\5\61\31\2\u0130")
        buf.write("\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write("\u0131\u0133\3\2\2\2\u0132\u0134\5q9\2\u0133\u0132\3\2")
        buf.write("\2\2\u0134\u0135\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\\\3\2\2\2\u0137\u0139\5q9\2\u0138\u0137")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u013d\3\2\2\2\u013c\u013e\5Y-\2\u013d")
        buf.write("\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2")
        buf.write("\u013f\u0141\5[.\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2")
        buf.write("\2\2\u0141^\3\2\2\2\u0142\u0149\n\4\2\2\u0143\u0149\5")
        buf.write("k\66\2\u0144\u0146\t\5\2\2\u0145\u0147\t\6\2\2\u0146\u0145")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148")
        buf.write("\u0142\3\2\2\2\u0148\u0143\3\2\2\2\u0148\u0144\3\2\2\2")
        buf.write("\u0149`\3\2\2\2\u014a\u014e\t\6\2\2\u014b\u014d\5_\60")
        buf.write("\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0151\u0152\7^\2\2\u0152\u0153\n\7\2\2")
        buf.write("\u0153\u0154\b\61\3\2\u0154b\3\2\2\2\u0155\u0159\t\6\2")
        buf.write("\2\u0156\u0158\5_\60\2\u0157\u0156\3\2\2\2\u0158\u015b")
        buf.write("\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015c\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\b\62\4")
        buf.write("\2\u015dd\3\2\2\2\u015e\u0160\5c\62\2\u015f\u0161\7^\2")
        buf.write("\2\u0160\u015f\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162\u0163\t\6\2\2\u0163\u0164\b\63\5\2\u0164")
        buf.write("f\3\2\2\2\u0165\u0168\5o8\2\u0166\u0168\5m\67\2\u0167")
        buf.write("\u0165\3\2\2\2\u0167\u0166\3\2\2\2\u0168\u016e\3\2\2\2")
        buf.write("\u0169\u016d\5m\67\2\u016a\u016d\5o8\2\u016b\u016d\5q")
        buf.write("9\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016fh\3\2\2\2\u0170\u016e\3\2\2\2\u0171")
        buf.write("\u0173\t\b\2\2\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0177\b\65\2\2\u0177j\3\2\2\2\u0178\u0179")
        buf.write("\7^\2\2\u0179\u017a\t\t\2\2\u017al\3\2\2\2\u017b\u017c")
        buf.write("\7a\2\2\u017cn\3\2\2\2\u017d\u017e\t\n\2\2\u017ep\3\2")
        buf.write("\2\2\u017f\u0180\t\13\2\2\u0180r\3\2\2\2\u0181\u0182\13")
        buf.write("\2\2\2\u0182\u0183\b:\6\2\u0183t\3\2\2\2\24\2\u011e\u0122")
        buf.write("\u012a\u0130\u0135\u013a\u013d\u0140\u0146\u0148\u014e")
        buf.write("\u0159\u0160\u0167\u016c\u016e\u0174\7\b\2\2\3\61\2\3")
        buf.write("\62\3\3\63\4\3:\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    BOOLEAN = 3
    NUMBER = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    PLUS = 23
    MINUS = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQ = 28
    NEQ = 29
    ASSIGN = 30
    LT = 31
    LTE = 32
    GT = 33
    GTE = 34
    CONCAT = 35
    Double_EQ = 36
    LP = 37
    RP = 38
    LB = 39
    RB = 40
    NEWLINE = 41
    COMMA = 42
    COMMENT = 43
    NUMBER_LIT = 44
    ILLEGAL_ESCAPE = 45
    UNCLOSE_STRING = 46
    STRING_LIT = 47
    ID = 48
    WS = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'bool'", "'number'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'!='", "'<-'", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "'\n'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "BOOLEAN", "NUMBER", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
            "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", "ASSIGN", "LT", "LTE", 
            "GT", "GTE", "CONCAT", "Double_EQ", "LP", "RP", "LB", "RB", 
            "NEWLINE", "COMMA", "COMMENT", "NUMBER_LIT", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "STRING_LIT", "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "BOOLEAN", "NUMBER", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", 
                  "NEQ", "ASSIGN", "LT", "LTE", "GT", "GTE", "CONCAT", "Double_EQ", 
                  "LP", "RP", "LB", "RB", "NEWLINE", "COMMA", "COMMENT", 
                  "Decimal_Part", "Exponent_Part", "NUMBER_LIT", "Allowed_Character", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING_LIT", "ID", 
                  "WS", "Escape_Char", "Underscore", "Charset", "Digit", 
                  "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[47] = self.ILLEGAL_ESCAPE_action 
            actions[48] = self.UNCLOSE_STRING_action 
            actions[49] = self.STRING_LIT_action 
            actions[56] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


