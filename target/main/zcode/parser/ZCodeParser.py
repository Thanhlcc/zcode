# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u017d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\3\2\3\2\3\2\3\3\6\3d\n\3\r\3\16\3e\3\4\7\4i\n")
        buf.write("\4\f\4\16\4l\13\4\3\5\3\5\3\5\3\5\5\5r\n\5\3\6\3\6\5\6")
        buf.write("v\n\6\3\7\3\7\5\7z\n\7\3\7\3\7\3\b\3\b\5\b\u0080\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u008f\n\13\3\13\3\13\3\13\3\13\5\13\u0095\n\13\3")
        buf.write("\f\3\f\3\r\3\r\5\r\u009b\n\r\3\16\3\16\5\16\u009f\n\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u00a9\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u00b7\n\21\3\22\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u00be\n\22\3\23\3\23\3\23\5\23\u00c3\n\23\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u00c9\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\5\25\u00d6\n\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u00e8\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\5\32\u00f4\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u010c")
        buf.write("\n\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\5\"\u011f\n\"\3#\3#\3#\3#\3#\5#\u0126")
        buf.write("\n#\3$\3$\3$\3$\3$\5$\u012d\n$\3%\3%\3%\3%\3%\5%\u0134")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\7&\u013c\n&\f&\16&\u013f\13&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\7\'\u0147\n\'\f\'\16\'\u014a\13\'")
        buf.write("\3(\3(\3(\3(\3(\3(\7(\u0152\n(\f(\16(\u0155\13(\3)\3)")
        buf.write("\3)\5)\u015a\n)\3*\3*\3*\5*\u015f\n*\3+\3+\3+\3+\3+\5")
        buf.write("+\u0166\n+\3,\3,\3,\3,\3,\3,\5,\u016e\n,\3-\3-\3-\3-\3")
        buf.write("-\5-\u0175\n-\3.\3.\3.\3.\3/\3/\3/\2\5JLN\60\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\\2\b\3\2\5\7\5\2\36\37!$&&\3\2\27\30")
        buf.write("\3\2\31\32\3\2\33\35\3\2\3\4\2\u0179\2^\3\2\2\2\4c\3\2")
        buf.write("\2\2\6j\3\2\2\2\bq\3\2\2\2\nu\3\2\2\2\fy\3\2\2\2\16\177")
        buf.write("\3\2\2\2\20\u0081\3\2\2\2\22\u0086\3\2\2\2\24\u0094\3")
        buf.write("\2\2\2\26\u0096\3\2\2\2\30\u009a\3\2\2\2\32\u009e\3\2")
        buf.write("\2\2\34\u00a8\3\2\2\2\36\u00aa\3\2\2\2 \u00b6\3\2\2\2")
        buf.write("\"\u00bd\3\2\2\2$\u00c2\3\2\2\2&\u00c8\3\2\2\2(\u00d5")
        buf.write("\3\2\2\2*\u00d7\3\2\2\2,\u00dc\3\2\2\2.\u00e7\3\2\2\2")
        buf.write("\60\u00e9\3\2\2\2\62\u00f3\3\2\2\2\64\u00f5\3\2\2\2\66")
        buf.write("\u00f9\3\2\2\28\u0102\3\2\2\2:\u0108\3\2\2\2<\u010f\3")
        buf.write("\2\2\2>\u0112\3\2\2\2@\u0115\3\2\2\2B\u011e\3\2\2\2D\u0125")
        buf.write("\3\2\2\2F\u012c\3\2\2\2H\u0133\3\2\2\2J\u0135\3\2\2\2")
        buf.write("L\u0140\3\2\2\2N\u014b\3\2\2\2P\u0159\3\2\2\2R\u015e\3")
        buf.write("\2\2\2T\u0165\3\2\2\2V\u016d\3\2\2\2X\u0174\3\2\2\2Z\u0176")
        buf.write("\3\2\2\2\\\u017a\3\2\2\2^_\5\6\4\2_`\5\b\5\2`a\7\2\2\3")
        buf.write("a\3\3\2\2\2bd\7+\2\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3")
        buf.write("\2\2\2f\5\3\2\2\2gi\7+\2\2hg\3\2\2\2il\3\2\2\2jh\3\2\2")
        buf.write("\2jk\3\2\2\2k\7\3\2\2\2lj\3\2\2\2mn\5\n\6\2no\5\b\5\2")
        buf.write("or\3\2\2\2pr\5\n\6\2qm\3\2\2\2qp\3\2\2\2r\t\3\2\2\2sv")
        buf.write("\5\36\20\2tv\5\f\7\2us\3\2\2\2ut\3\2\2\2v\13\3\2\2\2w")
        buf.write("z\5\16\b\2xz\5\24\13\2yw\3\2\2\2yx\3\2\2\2z{\3\2\2\2{")
        buf.write("|\5\4\3\2|\r\3\2\2\2}\u0080\5\20\t\2~\u0080\5\22\n\2\177")
        buf.write("}\3\2\2\2\177~\3\2\2\2\u0080\17\3\2\2\2\u0081\u0082\t")
        buf.write("\2\2\2\u0082\u0083\5\30\r\2\u0083\u0084\7 \2\2\u0084\u0085")
        buf.write("\5F$\2\u0085\21\3\2\2\2\u0086\u0087\t\2\2\2\u0087\u0088")
        buf.write("\5\30\r\2\u0088\23\3\2\2\2\u0089\u008e\7\n\2\2\u008a\u008f")
        buf.write("\7\62\2\2\u008b\u008c\7\62\2\2\u008c\u008d\7 \2\2\u008d")
        buf.write("\u008f\5F$\2\u008e\u008a\3\2\2\2\u008e\u008b\3\2\2\2\u008f")
        buf.write("\u0095\3\2\2\2\u0090\u0091\7\t\2\2\u0091\u0092\7\62\2")
        buf.write("\2\u0092\u0093\7 \2\2\u0093\u0095\5F$\2\u0094\u0089\3")
        buf.write("\2\2\2\u0094\u0090\3\2\2\2\u0095\25\3\2\2\2\u0096\u0097")
        buf.write("\5\22\n\2\u0097\27\3\2\2\2\u0098\u009b\7\62\2\2\u0099")
        buf.write("\u009b\5\32\16\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2")
        buf.write("\2\u009b\31\3\2\2\2\u009c\u009f\7\62\2\2\u009d\u009f\5")
        buf.write("@!\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a1\7)\2\2\u00a1\u00a2\5\34\17\2\u00a2")
        buf.write("\u00a3\7*\2\2\u00a3\33\3\2\2\2\u00a4\u00a5\7.\2\2\u00a5")
        buf.write("\u00a6\7,\2\2\u00a6\u00a9\5\34\17\2\u00a7\u00a9\7.\2\2")
        buf.write("\u00a8\u00a4\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\35\3\2")
        buf.write("\2\2\u00aa\u00ab\7\13\2\2\u00ab\u00ac\7\62\2\2\u00ac\u00ad")
        buf.write("\7\'\2\2\u00ad\u00ae\5 \21\2\u00ae\u00af\7(\2\2\u00af")
        buf.write("\u00b0\5\6\4\2\u00b0\u00b1\5$\23\2\u00b1\37\3\2\2\2\u00b2")
        buf.write("\u00b3\5\26\f\2\u00b3\u00b4\5\"\22\2\u00b4\u00b7\3\2\2")
        buf.write("\2\u00b5\u00b7\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7!\3\2\2\2\u00b8\u00b9\7,\2\2\u00b9\u00ba")
        buf.write("\5\26\f\2\u00ba\u00bb\5\"\22\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00be\3\2\2\2\u00bd\u00b8\3\2\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00be#\3\2\2\2\u00bf\u00c3\5:\36\2\u00c0\u00c3\58\35")
        buf.write("\2\u00c1\u00c3\5\4\3\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3%\3\2\2\2\u00c4\u00c5")
        buf.write("\5(\25\2\u00c5\u00c6\5&\24\2\u00c6\u00c9\3\2\2\2\u00c7")
        buf.write("\u00c9\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c8\u00c7\3\2\2\2")
        buf.write("\u00c9\'\3\2\2\2\u00ca\u00d6\5,\27\2\u00cb\u00d6\5\66")
        buf.write("\34\2\u00cc\u00d6\5:\36\2\u00cd\u00d6\58\35\2\u00ce\u00d6")
        buf.write("\5\f\7\2\u00cf\u00d6\5*\26\2\u00d0\u00d6\5<\37\2\u00d1")
        buf.write("\u00d6\5> \2\u00d2\u00d3\5@!\2\u00d3\u00d4\5\4\3\2\u00d4")
        buf.write("\u00d6\3\2\2\2\u00d5\u00ca\3\2\2\2\u00d5\u00cb\3\2\2\2")
        buf.write("\u00d5\u00cc\3\2\2\2\u00d5\u00cd\3\2\2\2\u00d5\u00ce\3")
        buf.write("\2\2\2\u00d5\u00cf\3\2\2\2\u00d5\u00d0\3\2\2\2\u00d5\u00d1")
        buf.write("\3\2\2\2\u00d5\u00d2\3\2\2\2\u00d6)\3\2\2\2\u00d7\u00d8")
        buf.write("\5\30\r\2\u00d8\u00d9\7 \2\2\u00d9\u00da\5F$\2\u00da\u00db")
        buf.write("\5\4\3\2\u00db+\3\2\2\2\u00dc\u00dd\7\21\2\2\u00dd\u00de")
        buf.write("\5\64\33\2\u00de\u00df\5\6\4\2\u00df\u00e0\5(\25\2\u00e0")
        buf.write("\u00e1\5.\30\2\u00e1\u00e2\5\62\32\2\u00e2-\3\2\2\2\u00e3")
        buf.write("\u00e4\5\60\31\2\u00e4\u00e5\5.\30\2\u00e5\u00e8\3\2\2")
        buf.write("\2\u00e6\u00e8\3\2\2\2\u00e7\u00e3\3\2\2\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8/\3\2\2\2\u00e9\u00ea\7\23\2\2\u00ea\u00eb")
        buf.write("\5\64\33\2\u00eb\u00ec\5\6\4\2\u00ec\u00ed\5(\25\2\u00ed")
        buf.write("\61\3\2\2\2\u00ee\u00ef\7\22\2\2\u00ef\u00f0\5\6\4\2\u00f0")
        buf.write("\u00f1\5(\25\2\u00f1\u00f4\3\2\2\2\u00f2\u00f4\3\2\2\2")
        buf.write("\u00f3\u00ee\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\63\3\2")
        buf.write("\2\2\u00f5\u00f6\7\'\2\2\u00f6\u00f7\5F$\2\u00f7\u00f8")
        buf.write("\7(\2\2\u00f8\65\3\2\2\2\u00f9\u00fa\7\f\2\2\u00fa\u00fb")
        buf.write("\7\62\2\2\u00fb\u00fc\7\r\2\2\u00fc\u00fd\5F$\2\u00fd")
        buf.write("\u00fe\7\16\2\2\u00fe\u00ff\5F$\2\u00ff\u0100\5\6\4\2")
        buf.write("\u0100\u0101\5(\25\2\u0101\67\3\2\2\2\u0102\u0103\7\24")
        buf.write("\2\2\u0103\u0104\5\4\3\2\u0104\u0105\5&\24\2\u0105\u0106")
        buf.write("\7\25\2\2\u0106\u0107\5\4\3\2\u01079\3\2\2\2\u0108\u010b")
        buf.write("\7\b\2\2\u0109\u010c\5F$\2\u010a\u010c\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u010e\5\4\3\2\u010e;\3\2\2\2\u010f\u0110\7\17\2\2\u0110")
        buf.write("\u0111\5\4\3\2\u0111=\3\2\2\2\u0112\u0113\7\20\2\2\u0113")
        buf.write("\u0114\5\4\3\2\u0114?\3\2\2\2\u0115\u0116\7\62\2\2\u0116")
        buf.write("\u0117\7\'\2\2\u0117\u0118\5B\"\2\u0118\u0119\7(\2\2\u0119")
        buf.write("A\3\2\2\2\u011a\u011b\5F$\2\u011b\u011c\5D#\2\u011c\u011f")
        buf.write("\3\2\2\2\u011d\u011f\3\2\2\2\u011e\u011a\3\2\2\2\u011e")
        buf.write("\u011d\3\2\2\2\u011fC\3\2\2\2\u0120\u0121\7,\2\2\u0121")
        buf.write("\u0122\5F$\2\u0122\u0123\5D#\2\u0123\u0126\3\2\2\2\u0124")
        buf.write("\u0126\3\2\2\2\u0125\u0120\3\2\2\2\u0125\u0124\3\2\2\2")
        buf.write("\u0126E\3\2\2\2\u0127\u0128\5H%\2\u0128\u0129\7%\2\2\u0129")
        buf.write("\u012a\5H%\2\u012a\u012d\3\2\2\2\u012b\u012d\5H%\2\u012c")
        buf.write("\u0127\3\2\2\2\u012c\u012b\3\2\2\2\u012dG\3\2\2\2\u012e")
        buf.write("\u012f\5J&\2\u012f\u0130\t\3\2\2\u0130\u0131\5J&\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0134\5J&\2\u0133\u012e\3\2\2\2\u0133")
        buf.write("\u0132\3\2\2\2\u0134I\3\2\2\2\u0135\u0136\b&\1\2\u0136")
        buf.write("\u0137\5L\'\2\u0137\u013d\3\2\2\2\u0138\u0139\f\4\2\2")
        buf.write("\u0139\u013a\t\4\2\2\u013a\u013c\5L\'\2\u013b\u0138\3")
        buf.write("\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013eK\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141")
        buf.write("\b\'\1\2\u0141\u0142\5N(\2\u0142\u0148\3\2\2\2\u0143\u0144")
        buf.write("\f\4\2\2\u0144\u0145\t\5\2\2\u0145\u0147\5N(\2\u0146\u0143")
        buf.write("\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149M\3\2\2\2\u014a\u0148\3\2\2\2\u014b")
        buf.write("\u014c\b(\1\2\u014c\u014d\5P)\2\u014d\u0153\3\2\2\2\u014e")
        buf.write("\u014f\f\4\2\2\u014f\u0150\t\6\2\2\u0150\u0152\5P)\2\u0151")
        buf.write("\u014e\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154O\3\2\2\2\u0155\u0153\3\2\2")
        buf.write("\2\u0156\u0157\7\26\2\2\u0157\u015a\5P)\2\u0158\u015a")
        buf.write("\5R*\2\u0159\u0156\3\2\2\2\u0159\u0158\3\2\2\2\u015aQ")
        buf.write("\3\2\2\2\u015b\u015c\7\32\2\2\u015c\u015f\5R*\2\u015d")
        buf.write("\u015f\5T+\2\u015e\u015b\3\2\2\2\u015e\u015d\3\2\2\2\u015f")
        buf.write("S\3\2\2\2\u0160\u0161\7\'\2\2\u0161\u0162\5F$\2\u0162")
        buf.write("\u0163\7(\2\2\u0163\u0166\3\2\2\2\u0164\u0166\5V,\2\u0165")
        buf.write("\u0160\3\2\2\2\u0165\u0164\3\2\2\2\u0166U\3\2\2\2\u0167")
        buf.write("\u016e\7.\2\2\u0168\u016e\7\61\2\2\u0169\u016e\5\\/\2")
        buf.write("\u016a\u016e\5Z.\2\u016b\u016e\5\30\r\2\u016c\u016e\5")
        buf.write("@!\2\u016d\u0167\3\2\2\2\u016d\u0168\3\2\2\2\u016d\u0169")
        buf.write("\3\2\2\2\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016c\3\2\2\2\u016eW\3\2\2\2\u016f\u0170\5F$\2\u0170")
        buf.write("\u0171\7,\2\2\u0171\u0172\5X-\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0175\5F$\2\u0174\u016f\3\2\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("Y\3\2\2\2\u0176\u0177\7)\2\2\u0177\u0178\5X-\2\u0178\u0179")
        buf.write("\7*\2\2\u0179[\3\2\2\2\u017a\u017b\t\7\2\2\u017b]\3\2")
        buf.write("\2\2!ejquy\177\u008e\u0094\u009a\u009e\u00a8\u00b6\u00bd")
        buf.write("\u00c2\u00c8\u00d5\u00e7\u00f3\u010b\u011e\u0125\u012c")
        buf.write("\u0133\u013d\u0148\u0153\u0159\u015e\u0165\u016d\u0174")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'bool'", "'number'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'!='", "'<-'", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "'\n'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "BOOLEAN", "NUMBER", 
                      "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
                      "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", "ASSIGN", 
                      "LT", "LTE", "GT", "GTE", "CONCAT", "Double_EQ", "LP", 
                      "RP", "LB", "RB", "NEWLINE", "COMMA", "COMMENT", "NUMBER_LIT", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRING_LIT", 
                      "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_newlines = 1
    RULE_nullable_newlines = 2
    RULE_decllist = 3
    RULE_decl = 4
    RULE_vardecl = 5
    RULE_explicit_vardecl = 6
    RULE_init_vardecl = 7
    RULE_simple_vardecl = 8
    RULE_implicit_vardecl = 9
    RULE_parameter_decl = 10
    RULE_varid = 11
    RULE_array_idx = 12
    RULE_dimensions = 13
    RULE_funcdecl = 14
    RULE_params = 15
    RULE_params_tail = 16
    RULE_body = 17
    RULE_nullable_stmtlist = 18
    RULE_stmt = 19
    RULE_asm_stmt = 20
    RULE_if_stmt = 21
    RULE_elif_clauses = 22
    RULE_elif_clause = 23
    RULE_else_clause = 24
    RULE_condition = 25
    RULE_for_stmt = 26
    RULE_block_stmt = 27
    RULE_return_stmt = 28
    RULE_break_stmt = 29
    RULE_continue_stmt = 30
    RULE_funcall_expr = 31
    RULE_nullbale_args = 32
    RULE_args_tail = 33
    RULE_expression = 34
    RULE_relational_expr = 35
    RULE_logical_expr = 36
    RULE_add_expr = 37
    RULE_multiply_expr = 38
    RULE_logical_not = 39
    RULE_sign_expr = 40
    RULE_subexpr = 41
    RULE_operand = 42
    RULE_expression_list = 43
    RULE_arraylit = 44
    RULE_booleanlit = 45

    ruleNames =  [ "program", "newlines", "nullable_newlines", "decllist", 
                   "decl", "vardecl", "explicit_vardecl", "init_vardecl", 
                   "simple_vardecl", "implicit_vardecl", "parameter_decl", 
                   "varid", "array_idx", "dimensions", "funcdecl", "params", 
                   "params_tail", "body", "nullable_stmtlist", "stmt", "asm_stmt", 
                   "if_stmt", "elif_clauses", "elif_clause", "else_clause", 
                   "condition", "for_stmt", "block_stmt", "return_stmt", 
                   "break_stmt", "continue_stmt", "funcall_expr", "nullbale_args", 
                   "args_tail", "expression", "relational_expr", "logical_expr", 
                   "add_expr", "multiply_expr", "logical_not", "sign_expr", 
                   "subexpr", "operand", "expression_list", "arraylit", 
                   "booleanlit" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    BOOLEAN=3
    NUMBER=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    PLUS=23
    MINUS=24
    MUL=25
    DIV=26
    MOD=27
    EQ=28
    NEQ=29
    ASSIGN=30
    LT=31
    LTE=32
    GT=33
    GTE=34
    CONCAT=35
    Double_EQ=36
    LP=37
    RP=38
    LB=39
    RB=40
    NEWLINE=41
    COMMA=42
    COMMENT=43
    NUMBER_LIT=44
    ILLEGAL_ESCAPE=45
    UNCLOSE_STRING=46
    STRING_LIT=47
    ID=48
    WS=49
    ERROR_CHAR=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullable_newlines(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlinesContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.nullable_newlines()
            self.state = 93
            self.decllist()
            self.state = 94
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newlines

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlines" ):
                return visitor.visitNewlines(self)
            else:
                return visitor.visitChildren(self)




    def newlines(self):

        localctx = ZCodeParser.NewlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_newlines)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.match(ZCodeParser.NEWLINE)
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_newlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_newlines

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_newlines" ):
                return visitor.visitNullable_newlines(self)
            else:
                return visitor.visitChildren(self)




    def nullable_newlines(self):

        localctx = ZCodeParser.Nullable_newlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nullable_newlines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 101
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decllist)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.decl()
                self.state = 108
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.funcdecl()
                pass
            elif token in [ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def explicit_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Explicit_vardeclContext,0)


        def implicit_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_vardeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 117
                self.explicit_vardecl()
                pass
            elif token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.state = 118
                self.implicit_vardecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 121
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Init_vardeclContext,0)


        def simple_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Simple_vardeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explicit_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_vardecl" ):
                return visitor.visitExplicit_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def explicit_vardecl(self):

        localctx = ZCodeParser.Explicit_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_explicit_vardecl)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.init_vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.simple_vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(ZCodeParser.VaridContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(ZCodeParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_init_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_vardecl" ):
                return visitor.visitInit_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def init_vardecl(self):

        localctx = ZCodeParser.Init_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_init_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 128
            self.varid()
            self.state = 129
            self.match(ZCodeParser.ASSIGN)
            self.state = 130
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(ZCodeParser.VaridContext,0)


        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(ZCodeParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_simple_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_vardecl" ):
                return visitor.visitSimple_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def simple_vardecl(self):

        localctx = ZCodeParser.Simple_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_simple_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 133
            self.varid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_vardecl" ):
                return visitor.visitImplicit_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def implicit_vardecl(self):

        localctx = ZCodeParser.Implicit_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_implicit_vardecl)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(ZCodeParser.DYNAMIC)
                self.state = 140
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 136
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 137
                    self.match(ZCodeParser.ID)
                    self.state = 138
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 139
                    self.expression()
                    pass


                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(ZCodeParser.VAR)
                self.state = 143
                self.match(ZCodeParser.ID)
                self.state = 144
                self.match(ZCodeParser.ASSIGN)
                self.state = 145
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Simple_vardeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_decl" ):
                return visitor.visitParameter_decl(self)
            else:
                return visitor.visitChildren(self)




    def parameter_decl(self):

        localctx = ZCodeParser.Parameter_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.simple_vardecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VaridContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_idx(self):
            return self.getTypedRuleContext(ZCodeParser.Array_idxContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarid" ):
                return visitor.visitVarid(self)
            else:
                return visitor.visitChildren(self)




    def varid(self):

        localctx = ZCodeParser.VaridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_varid)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.array_idx()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_idxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionsContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def funcall_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Funcall_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_idx

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_idx" ):
                return visitor.visitArray_idx(self)
            else:
                return visitor.visitChildren(self)




    def array_idx(self):

        localctx = ZCodeParser.Array_idxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 154
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 155
                self.funcall_expr()
                pass


            self.state = 158
            self.match(ZCodeParser.LB)
            self.state = 159
            self.dimensions()
            self.state = 160
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def dimensions(self):
            return self.getTypedRuleContext(ZCodeParser.DimensionsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = ZCodeParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dimensions)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(ZCodeParser.NUMBER_LIT)
                self.state = 163
                self.match(ZCodeParser.COMMA)
                self.state = 164
                self.dimensions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(ZCodeParser.NUMBER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def params(self):
            return self.getTypedRuleContext(ZCodeParser.ParamsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def nullable_newlines(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlinesContext,0)


        def body(self):
            return self.getTypedRuleContext(ZCodeParser.BodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ZCodeParser.FUNC)
            self.state = 169
            self.match(ZCodeParser.ID)
            self.state = 170
            self.match(ZCodeParser.LP)
            self.state = 171
            self.params()
            self.state = 172
            self.match(ZCodeParser.RP)
            self.state = 173
            self.nullable_newlines()
            self.state = 174
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_declContext,0)


        def params_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Params_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ZCodeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_params)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.parameter_decl()
                self.state = 177
                self.params_tail()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_declContext,0)


        def params_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Params_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_params_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_tail" ):
                return visitor.visitParams_tail(self)
            else:
                return visitor.visitChildren(self)




    def params_tail(self):

        localctx = ZCodeParser.Params_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_params_tail)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(ZCodeParser.COMMA)
                self.state = 183
                self.parameter_decl()
                self.state = 184
                self.params_tail()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = ZCodeParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_body)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.return_stmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.block_stmt()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.newlines()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullable_stmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def nullable_stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_stmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullable_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullable_stmtlist" ):
                return visitor.visitNullable_stmtlist(self)
            else:
                return visitor.visitChildren(self)




    def nullable_stmtlist(self):

        localctx = ZCodeParser.Nullable_stmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_nullable_stmtlist)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOLEAN, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.stmt()
                self.state = 195
                self.nullable_stmtlist()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def asm_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Asm_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def funcall_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Funcall_exprContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.return_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.block_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.vardecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 205
                self.asm_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 206
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 207
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 208
                self.funcall_expr()
                self.state = 209
                self.newlines()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asm_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(ZCodeParser.VaridContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_asm_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsm_stmt" ):
                return visitor.visitAsm_stmt(self)
            else:
                return visitor.visitChildren(self)




    def asm_stmt(self):

        localctx = ZCodeParser.Asm_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_asm_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.varid()
            self.state = 214
            self.match(ZCodeParser.ASSIGN)
            self.state = 215
            self.expression()
            self.state = 216
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def condition(self):
            return self.getTypedRuleContext(ZCodeParser.ConditionContext,0)


        def nullable_newlines(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlinesContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elif_clauses(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_clausesContext,0)


        def else_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Else_clauseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ZCodeParser.IF)
            self.state = 219
            self.condition()
            self.state = 220
            self.nullable_newlines()
            self.state = 221
            self.stmt()
            self.state = 222
            self.elif_clauses()
            self.state = 223
            self.else_clause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_clausesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_clause(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_clauseContext,0)


        def elif_clauses(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_clausesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_clauses

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_clauses" ):
                return visitor.visitElif_clauses(self)
            else:
                return visitor.visitChildren(self)




    def elif_clauses(self):

        localctx = ZCodeParser.Elif_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elif_clauses)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.elif_clause()
                self.state = 226
                self.elif_clauses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def condition(self):
            return self.getTypedRuleContext(ZCodeParser.ConditionContext,0)


        def nullable_newlines(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlinesContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_clause" ):
                return visitor.visitElif_clause(self)
            else:
                return visitor.visitChildren(self)




    def elif_clause(self):

        localctx = ZCodeParser.Elif_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elif_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(ZCodeParser.ELIF)
            self.state = 232
            self.condition()
            self.state = 233
            self.nullable_newlines()
            self.state = 234
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def nullable_newlines(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlinesContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_clause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = ZCodeParser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_clause)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(ZCodeParser.ELSE)
                self.state = 237
                self.nullable_newlines()
                self.state = 238
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = ZCodeParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ZCodeParser.LP)
            self.state = 244
            self.expression()
            self.state = 245
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def nullable_newlines(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_newlinesContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ZCodeParser.FOR)
            self.state = 248
            self.match(ZCodeParser.ID)
            self.state = 249
            self.match(ZCodeParser.UNTIL)
            self.state = 250
            self.expression()
            self.state = 251
            self.match(ZCodeParser.BY)
            self.state = 252
            self.expression()
            self.state = 253
            self.nullable_newlines()
            self.state = 254
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.NewlinesContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.NewlinesContext,i)


        def nullable_stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.Nullable_stmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(ZCodeParser.BEGIN)
            self.state = 257
            self.newlines()
            self.state = 258
            self.nullable_stmtlist()
            self.state = 259
            self.match(ZCodeParser.END)
            self.state = 260
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(ZCodeParser.RETURN)
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.ID]:
                self.state = 263
                self.expression()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 267
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ZCodeParser.BREAK)
            self.state = 270
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def newlines(self):
            return self.getTypedRuleContext(ZCodeParser.NewlinesContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.CONTINUE)
            self.state = 273
            self.newlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcall_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def nullbale_args(self):
            return self.getTypedRuleContext(ZCodeParser.Nullbale_argsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcall_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall_expr" ):
                return visitor.visitFuncall_expr(self)
            else:
                return visitor.visitChildren(self)




    def funcall_expr(self):

        localctx = ZCodeParser.Funcall_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcall_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(ZCodeParser.ID)
            self.state = 276
            self.match(ZCodeParser.LP)
            self.state = 277
            self.nullbale_args()
            self.state = 278
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nullbale_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def args_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Args_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullbale_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullbale_args" ):
                return visitor.visitNullbale_args(self)
            else:
                return visitor.visitChildren(self)




    def nullbale_args(self):

        localctx = ZCodeParser.Nullbale_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_nullbale_args)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.MINUS, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.expression()
                self.state = 281
                self.args_tail()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Args_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def args_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Args_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_args_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs_tail" ):
                return visitor.visitArgs_tail(self)
            else:
                return visitor.visitChildren(self)




    def args_tail(self):

        localctx = ZCodeParser.Args_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_args_tail)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(ZCodeParser.COMMA)
                self.state = 287
                self.expression()
                self.state = 288
                self.args_tail()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relational_exprContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.relational_expr()
                self.state = 294
                self.match(ZCodeParser.CONCAT)
                self.state = 295
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_exprContext,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def Double_EQ(self):
            return self.getToken(ZCodeParser.Double_EQ, 0)

        def NEQ(self):
            return self.getToken(ZCodeParser.NEQ, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = ZCodeParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.logical_expr(0)
                self.state = 301
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NEQ) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.Double_EQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 302
                self.logical_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.logical_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_exprContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.add_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.add_expr(0) 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiply_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multiply_exprContext,0)


        def add_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Add_exprContext,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_add_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_expr" ):
                return visitor.visitAdd_expr(self)
            else:
                return visitor.visitChildren(self)



    def add_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Add_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_add_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.multiply_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Add_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add_expr)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 323
                    self.multiply_expr(0) 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiply_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_not(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_notContext,0)


        def multiply_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multiply_exprContext,0)


        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiply_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply_expr" ):
                return visitor.visitMultiply_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiply_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multiply_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_multiply_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.logical_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiply_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiply_expr)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 334
                    self.logical_not() 
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def logical_not(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_notContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_not" ):
                return visitor.visitLogical_not(self)
            else:
                return visitor.visitChildren(self)




    def logical_not(self):

        localctx = ZCodeParser.Logical_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_logical_not)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(ZCodeParser.NOT)
                self.state = 341
                self.logical_not()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.MINUS, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(ZCodeParser.SubexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = ZCodeParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_sign_expr)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(ZCodeParser.MINUS)
                self.state = 346
                self.sign_expr()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LP, ZCodeParser.LB, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.subexpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = ZCodeParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_subexpr)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(ZCodeParser.LP)
                self.state = 351
                self.expression()
                self.state = 352
                self.match(ZCodeParser.RP)
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LB, ZCodeParser.NUMBER_LIT, ZCodeParser.STRING_LIT, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def booleanlit(self):
            return self.getTypedRuleContext(ZCodeParser.BooleanlitContext,0)


        def arraylit(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylitContext,0)


        def varid(self):
            return self.getTypedRuleContext(ZCodeParser.VaridContext,0)


        def funcall_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Funcall_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operand)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.match(ZCodeParser.NUMBER_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
                self.booleanlit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 360
                self.arraylit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 361
                self.varid()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 362
                self.funcall_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = ZCodeParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression_list)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.expression()
                self.state = 366
                self.match(ZCodeParser.COMMA)
                self.state = 367
                self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(ZCodeParser.LB, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def RB(self):
            return self.getToken(ZCodeParser.RB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = ZCodeParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(ZCodeParser.LB)
            self.state = 373
            self.expression_list()
            self.state = 374
            self.match(ZCodeParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanlitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_booleanlit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanlit" ):
                return visitor.visitBooleanlit(self)
            else:
                return visitor.visitChildren(self)




    def booleanlit(self):

        localctx = ZCodeParser.BooleanlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_booleanlit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TRUE or _la==ZCodeParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[36] = self.logical_expr_sempred
        self._predicates[37] = self.add_expr_sempred
        self._predicates[38] = self.multiply_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def add_expr_sempred(self, localctx:Add_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiply_expr_sempred(self, localctx:Multiply_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




