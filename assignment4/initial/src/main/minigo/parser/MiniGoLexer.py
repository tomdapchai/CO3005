# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01f1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\5\26")
        buf.write("\u0102\n\26\3\26\3\26\3\26\3\27\3\27\7\27\u0109\n\27\f")
        buf.write("\27\16\27\u010c\13\27\3\30\3\30\3\31\3\31\3\32\3\32\3")
        buf.write("\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\3\67\7\67\u015b\n\67\f\67\16\67\u015e\13\67\5\67")
        buf.write("\u0160\n\67\38\38\38\68\u0165\n8\r8\168\u0166\39\39\3")
        buf.write("9\69\u016c\n9\r9\169\u016d\3:\3:\3:\6:\u0173\n:\r:\16")
        buf.write(":\u0174\3;\3;\3<\3<\5<\u017b\n<\3<\6<\u017e\n<\r<\16<")
        buf.write("\u017f\3=\6=\u0183\n=\r=\16=\u0184\3=\3=\7=\u0189\n=\f")
        buf.write("=\16=\u018c\13=\3=\5=\u018f\n=\3=\6=\u0192\n=\r=\16=\u0193")
        buf.write("\3=\3=\3=\3=\6=\u019a\n=\r=\16=\u019b\3=\3=\5=\u01a0\n")
        buf.write("=\3>\6>\u01a3\n>\r>\16>\u01a4\3>\3>\3?\3?\3@\3@\3@\3@")
        buf.write("\3@\3@\7@\u01b1\n@\f@\16@\u01b4\13@\3@\3@\3A\3A\3A\3A")
        buf.write("\7A\u01bc\nA\fA\16A\u01bf\13A\3A\3A\3B\3B\3B\3B\3B\7B")
        buf.write("\u01c8\nB\fB\16B\u01cb\13B\3B\3B\3B\3B\3B\3C\3C\3C\3D")
        buf.write("\3D\3D\3D\7D\u01d9\nD\fD\16D\u01dc\13D\3D\3D\3D\3D\3E")
        buf.write("\3E\3E\3E\3E\3E\7E\u01e8\nE\fE\16E\u01eb\13E\3E\5E\u01ee")
        buf.write("\nE\3E\3E\3\u01c9\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u\2w\2y<{=}\2\177>\u0081?\u0083@\u0085")
        buf.write("A\u0087B\u0089C\3\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\63")
        buf.write(";\3\2\62;\4\2ZZzz\5\2\62;CHch\4\2QQqq\3\2\629\4\2DDdd")
        buf.write("\3\2\62\63\4\2GGgg\4\2--//\5\2\13\13\16\17\"\"\5\2\f\f")
        buf.write("$$^^\7\2$$^^ppttvv\4\2\f\f\17\17\6\2\f\f\17\17$$^^\3\3")
        buf.write("\f\f\2\u0209\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u008b\3\2\2")
        buf.write("\2\5\u008e\3\2\2\2\7\u0093\3\2\2\2\t\u0097\3\2\2\2\13")
        buf.write("\u009e\3\2\2\2\r\u00a3\3\2\2\2\17\u00a8\3\2\2\2\21\u00af")
        buf.write("\3\2\2\2\23\u00b9\3\2\2\2\25\u00c0\3\2\2\2\27\u00c4\3")
        buf.write("\2\2\2\31\u00ca\3\2\2\2\33\u00d2\3\2\2\2\35\u00d8\3\2")
        buf.write("\2\2\37\u00dc\3\2\2\2!\u00e5\3\2\2\2#\u00eb\3\2\2\2%\u00f1")
        buf.write("\3\2\2\2\'\u00f5\3\2\2\2)\u00fa\3\2\2\2+\u0101\3\2\2\2")
        buf.write("-\u0106\3\2\2\2/\u010d\3\2\2\2\61\u010f\3\2\2\2\63\u0111")
        buf.write("\3\2\2\2\65\u0113\3\2\2\2\67\u0115\3\2\2\29\u0117\3\2")
        buf.write("\2\2;\u011a\3\2\2\2=\u011d\3\2\2\2?\u011f\3\2\2\2A\u0122")
        buf.write("\3\2\2\2C\u0124\3\2\2\2E\u0127\3\2\2\2G\u012a\3\2\2\2")
        buf.write("I\u012d\3\2\2\2K\u012f\3\2\2\2M\u0131\3\2\2\2O\u0134\3")
        buf.write("\2\2\2Q\u0137\3\2\2\2S\u013a\3\2\2\2U\u013d\3\2\2\2W\u0140")
        buf.write("\3\2\2\2Y\u0143\3\2\2\2[\u0145\3\2\2\2]\u0147\3\2\2\2")
        buf.write("_\u0149\3\2\2\2a\u014b\3\2\2\2c\u014d\3\2\2\2e\u014f\3")
        buf.write("\2\2\2g\u0151\3\2\2\2i\u0153\3\2\2\2k\u0155\3\2\2\2m\u015f")
        buf.write("\3\2\2\2o\u0161\3\2\2\2q\u0168\3\2\2\2s\u016f\3\2\2\2")
        buf.write("u\u0176\3\2\2\2w\u0178\3\2\2\2y\u019f\3\2\2\2{\u01a2\3")
        buf.write("\2\2\2}\u01a8\3\2\2\2\177\u01aa\3\2\2\2\u0081\u01b7\3")
        buf.write("\2\2\2\u0083\u01c2\3\2\2\2\u0085\u01d1\3\2\2\2\u0087\u01d4")
        buf.write("\3\2\2\2\u0089\u01e1\3\2\2\2\u008b\u008c\7k\2\2\u008c")
        buf.write("\u008d\7h\2\2\u008d\4\3\2\2\2\u008e\u008f\7g\2\2\u008f")
        buf.write("\u0090\7n\2\2\u0090\u0091\7u\2\2\u0091\u0092\7g\2\2\u0092")
        buf.write("\6\3\2\2\2\u0093\u0094\7h\2\2\u0094\u0095\7q\2\2\u0095")
        buf.write("\u0096\7t\2\2\u0096\b\3\2\2\2\u0097\u0098\7t\2\2\u0098")
        buf.write("\u0099\7g\2\2\u0099\u009a\7v\2\2\u009a\u009b\7w\2\2\u009b")
        buf.write("\u009c\7t\2\2\u009c\u009d\7p\2\2\u009d\n\3\2\2\2\u009e")
        buf.write("\u009f\7h\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1\7p\2\2\u00a1")
        buf.write("\u00a2\7e\2\2\u00a2\f\3\2\2\2\u00a3\u00a4\7v\2\2\u00a4")
        buf.write("\u00a5\7{\2\2\u00a5\u00a6\7r\2\2\u00a6\u00a7\7g\2\2\u00a7")
        buf.write("\16\3\2\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa\7v\2\2\u00aa")
        buf.write("\u00ab\7t\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7e\2\2\u00ad")
        buf.write("\u00ae\7v\2\2\u00ae\20\3\2\2\2\u00af\u00b0\7k\2\2\u00b0")
        buf.write("\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7g\2\2\u00b3")
        buf.write("\u00b4\7t\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6\7c\2\2\u00b6")
        buf.write("\u00b7\7e\2\2\u00b7\u00b8\7g\2\2\u00b8\22\3\2\2\2\u00b9")
        buf.write("\u00ba\7u\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7t\2\2\u00bc")
        buf.write("\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7i\2\2\u00bf")
        buf.write("\24\3\2\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2")
        buf.write("\u00c3\7v\2\2\u00c3\26\3\2\2\2\u00c4\u00c5\7h\2\2\u00c5")
        buf.write("\u00c6\7n\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8\7c\2\2\u00c8")
        buf.write("\u00c9\7v\2\2\u00c9\30\3\2\2\2\u00ca\u00cb\7d\2\2\u00cb")
        buf.write("\u00cc\7q\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7n\2\2\u00ce")
        buf.write("\u00cf\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7p\2\2\u00d1")
        buf.write("\32\3\2\2\2\u00d2\u00d3\7e\2\2\u00d3\u00d4\7q\2\2\u00d4")
        buf.write("\u00d5\7p\2\2\u00d5\u00d6\7u\2\2\u00d6\u00d7\7v\2\2\u00d7")
        buf.write("\34\3\2\2\2\u00d8\u00d9\7x\2\2\u00d9\u00da\7c\2\2\u00da")
        buf.write("\u00db\7t\2\2\u00db\36\3\2\2\2\u00dc\u00dd\7e\2\2\u00dd")
        buf.write("\u00de\7q\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7v\2\2\u00e0")
        buf.write("\u00e1\7k\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7w\2\2\u00e3")
        buf.write("\u00e4\7g\2\2\u00e4 \3\2\2\2\u00e5\u00e6\7d\2\2\u00e6")
        buf.write("\u00e7\7t\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9\7c\2\2\u00e9")
        buf.write("\u00ea\7m\2\2\u00ea\"\3\2\2\2\u00eb\u00ec\7t\2\2\u00ec")
        buf.write("\u00ed\7c\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7i\2\2\u00ef")
        buf.write("\u00f0\7g\2\2\u00f0$\3\2\2\2\u00f1\u00f2\7p\2\2\u00f2")
        buf.write("\u00f3\7k\2\2\u00f3\u00f4\7n\2\2\u00f4&\3\2\2\2\u00f5")
        buf.write("\u00f6\7v\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7w\2\2\u00f8")
        buf.write("\u00f9\7g\2\2\u00f9(\3\2\2\2\u00fa\u00fb\7h\2\2\u00fb")
        buf.write("\u00fc\7c\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe\7u\2\2\u00fe")
        buf.write("\u00ff\7g\2\2\u00ff*\3\2\2\2\u0100\u0102\7\17\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0103\3\2\2\2")
        buf.write("\u0103\u0104\7\f\2\2\u0104\u0105\b\26\2\2\u0105,\3\2\2")
        buf.write("\2\u0106\u010a\t\2\2\2\u0107\u0109\t\3\2\2\u0108\u0107")
        buf.write("\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b.\3\2\2\2\u010c\u010a\3\2\2\2\u010d")
        buf.write("\u010e\7-\2\2\u010e\60\3\2\2\2\u010f\u0110\7/\2\2\u0110")
        buf.write("\62\3\2\2\2\u0111\u0112\7,\2\2\u0112\64\3\2\2\2\u0113")
        buf.write("\u0114\7\61\2\2\u0114\66\3\2\2\2\u0115\u0116\7\'\2\2\u0116")
        buf.write("8\3\2\2\2\u0117\u0118\7?\2\2\u0118\u0119\7?\2\2\u0119")
        buf.write(":\3\2\2\2\u011a\u011b\7#\2\2\u011b\u011c\7?\2\2\u011c")
        buf.write("<\3\2\2\2\u011d\u011e\7>\2\2\u011e>\3\2\2\2\u011f\u0120")
        buf.write("\7>\2\2\u0120\u0121\7?\2\2\u0121@\3\2\2\2\u0122\u0123")
        buf.write("\7@\2\2\u0123B\3\2\2\2\u0124\u0125\7@\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126D\3\2\2\2\u0127\u0128\7(\2\2\u0128\u0129")
        buf.write("\7(\2\2\u0129F\3\2\2\2\u012a\u012b\7~\2\2\u012b\u012c")
        buf.write("\7~\2\2\u012cH\3\2\2\2\u012d\u012e\7#\2\2\u012eJ\3\2\2")
        buf.write("\2\u012f\u0130\7?\2\2\u0130L\3\2\2\2\u0131\u0132\7<\2")
        buf.write("\2\u0132\u0133\7?\2\2\u0133N\3\2\2\2\u0134\u0135\7-\2")
        buf.write("\2\u0135\u0136\7?\2\2\u0136P\3\2\2\2\u0137\u0138\7/\2")
        buf.write("\2\u0138\u0139\7?\2\2\u0139R\3\2\2\2\u013a\u013b\7,\2")
        buf.write("\2\u013b\u013c\7?\2\2\u013cT\3\2\2\2\u013d\u013e\7\61")
        buf.write("\2\2\u013e\u013f\7?\2\2\u013fV\3\2\2\2\u0140\u0141\7\'")
        buf.write("\2\2\u0141\u0142\7?\2\2\u0142X\3\2\2\2\u0143\u0144\7\60")
        buf.write("\2\2\u0144Z\3\2\2\2\u0145\u0146\7.\2\2\u0146\\\3\2\2\2")
        buf.write("\u0147\u0148\7=\2\2\u0148^\3\2\2\2\u0149\u014a\7<\2\2")
        buf.write("\u014a`\3\2\2\2\u014b\u014c\7*\2\2\u014cb\3\2\2\2\u014d")
        buf.write("\u014e\7+\2\2\u014ed\3\2\2\2\u014f\u0150\7}\2\2\u0150")
        buf.write("f\3\2\2\2\u0151\u0152\7\177\2\2\u0152h\3\2\2\2\u0153\u0154")
        buf.write("\7]\2\2\u0154j\3\2\2\2\u0155\u0156\7_\2\2\u0156l\3\2\2")
        buf.write("\2\u0157\u0160\7\62\2\2\u0158\u015c\t\4\2\2\u0159\u015b")
        buf.write("\t\5\2\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u0160\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0157\3\2\2\2\u015f\u0158\3")
        buf.write("\2\2\2\u0160n\3\2\2\2\u0161\u0162\7\62\2\2\u0162\u0164")
        buf.write("\t\6\2\2\u0163\u0165\t\7\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167p\3\2\2\2\u0168\u0169\7\62\2\2\u0169\u016b\t\b\2")
        buf.write("\2\u016a\u016c\t\t\2\2\u016b\u016a\3\2\2\2\u016c\u016d")
        buf.write("\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("r\3\2\2\2\u016f\u0170\7\62\2\2\u0170\u0172\t\n\2\2\u0171")
        buf.write("\u0173\t\13\2\2\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2")
        buf.write("\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175t\3\2")
        buf.write("\2\2\u0176\u0177\t\5\2\2\u0177v\3\2\2\2\u0178\u017a\t")
        buf.write("\f\2\2\u0179\u017b\t\r\2\2\u017a\u0179\3\2\2\2\u017a\u017b")
        buf.write("\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u017e\5u;\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180x\3\2\2\2\u0181\u0183\5u;\2\u0182")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u018a\7")
        buf.write("\60\2\2\u0187\u0189\5u;\2\u0188\u0187\3\2\2\2\u0189\u018c")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018f\5w<\2\u018e")
        buf.write("\u018d\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u01a0\3\2\2\2")
        buf.write("\u0190\u0192\5u;\2\u0191\u0190\3\2\2\2\u0192\u0193\3\2")
        buf.write("\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\7\60\2\2\u0196\u0197\5w<\2\u0197")
        buf.write("\u01a0\3\2\2\2\u0198\u019a\5u;\2\u0199\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2")
        buf.write("\u019c\u019d\3\2\2\2\u019d\u019e\7\60\2\2\u019e\u01a0")
        buf.write("\3\2\2\2\u019f\u0182\3\2\2\2\u019f\u0191\3\2\2\2\u019f")
        buf.write("\u0199\3\2\2\2\u01a0z\3\2\2\2\u01a1\u01a3\t\16\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\b")
        buf.write(">\3\2\u01a7|\3\2\2\2\u01a8\u01a9\7$\2\2\u01a9~\3\2\2\2")
        buf.write("\u01aa\u01b2\7$\2\2\u01ab\u01b1\n\17\2\2\u01ac\u01ad\7")
        buf.write("^\2\2\u01ad\u01b1\t\20\2\2\u01ae\u01af\7)\2\2\u01af\u01b1")
        buf.write("\7$\2\2\u01b0\u01ab\3\2\2\2\u01b0\u01ac\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2")
        buf.write("\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3")
        buf.write("\2\2\2\u01b5\u01b6\7$\2\2\u01b6\u0080\3\2\2\2\u01b7\u01b8")
        buf.write("\7\61\2\2\u01b8\u01b9\7\61\2\2\u01b9\u01bd\3\2\2\2\u01ba")
        buf.write("\u01bc\n\21\2\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf\3\2\2")
        buf.write("\2\u01bd\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0\u01c1\bA\3\2\u01c1")
        buf.write("\u0082\3\2\2\2\u01c2\u01c3\7\61\2\2\u01c3\u01c4\7,\2\2")
        buf.write("\u01c4\u01c9\3\2\2\2\u01c5\u01c8\5\u0083B\2\u01c6\u01c8")
        buf.write("\13\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8")
        buf.write("\u01cb\3\2\2\2\u01c9\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01ca\u01cc\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd\7")
        buf.write(",\2\2\u01cd\u01ce\7\61\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0")
        buf.write("\bB\3\2\u01d0\u0084\3\2\2\2\u01d1\u01d2\13\2\2\2\u01d2")
        buf.write("\u01d3\bC\4\2\u01d3\u0086\3\2\2\2\u01d4\u01da\7$\2\2\u01d5")
        buf.write("\u01d6\7^\2\2\u01d6\u01d9\t\20\2\2\u01d7\u01d9\n\22\2")
        buf.write("\2\u01d8\u01d5\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc")
        buf.write("\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("\u01dd\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01de\7^\2\2")
        buf.write("\u01de\u01df\n\20\2\2\u01df\u01e0\bD\5\2\u01e0\u0088\3")
        buf.write("\2\2\2\u01e1\u01e9\7$\2\2\u01e2\u01e8\n\17\2\2\u01e3\u01e4")
        buf.write("\7^\2\2\u01e4\u01e8\t\20\2\2\u01e5\u01e6\7)\2\2\u01e6")
        buf.write("\u01e8\7$\2\2\u01e7\u01e2\3\2\2\2\u01e7\u01e3\3\2\2\2")
        buf.write("\u01e7\u01e5\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3")
        buf.write("\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01ec\u01ee\t\23\2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f0\bE\6\2\u01f0\u008a\3\2\2\2")
        buf.write("\35\2\u0101\u010a\u015c\u015f\u0166\u016d\u0174\u017a")
        buf.write("\u017f\u0184\u018a\u018e\u0193\u019b\u019f\u01a4\u01b0")
        buf.write("\u01b2\u01bd\u01c7\u01c9\u01d8\u01da\u01e7\u01e9\u01ed")
        buf.write("\7\3\26\2\b\2\2\3C\3\3D\4\3E\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    CONST = 13
    VAR = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    NIL = 18
    TRUE = 19
    FALSE = 20
    NEWLINE = 21
    ID = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQ = 28
    NEQ = 29
    LT = 30
    LE = 31
    GT = 32
    GE = 33
    AND = 34
    OR = 35
    NOT = 36
    ASSIGN = 37
    SHORT_ASSIGN = 38
    ADD_ASSIGN = 39
    SUB_ASSIGN = 40
    MUL_ASSIGN = 41
    DIV_ASSIGN = 42
    MOD_ASSIGN = 43
    DOT = 44
    COMMA = 45
    SEMICOLON = 46
    COLON = 47
    LPAREN = 48
    RPAREN = 49
    LBRACE = 50
    RBRACE = 51
    LBRACKET = 52
    RBRACKET = 53
    INT_LIT = 54
    HEX_LIT = 55
    OCT_LIT = 56
    BIN_LIT = 57
    FLOAT_LIT = 58
    WS = 59
    STRING_LIT = 60
    LINE_COMMENT = 61
    BLOCK_COMMENT = 62
    ERROR_CHAR = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "','", "';'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "NEWLINE", "ID", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", 
            "AND", "OR", "NOT", "ASSIGN", "SHORT_ASSIGN", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", 
            "COMMA", "SEMICOLON", "COLON", "LPAREN", "RPAREN", "LBRACE", 
            "RBRACE", "LBRACKET", "RBRACKET", "INT_LIT", "HEX_LIT", "OCT_LIT", 
            "BIN_LIT", "FLOAT_LIT", "WS", "STRING_LIT", "LINE_COMMENT", 
            "BLOCK_COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", 
                  "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", "FALSE", 
                  "NEWLINE", "ID", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "NEQ", "LT", "LE", "GT", "GE", "AND", "OR", "NOT", "ASSIGN", 
                  "SHORT_ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "COMMA", "SEMICOLON", 
                  "COLON", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                  "RBRACKET", "INT_LIT", "HEX_LIT", "OCT_LIT", "BIN_LIT", 
                  "Digit", "Exponent", "FLOAT_LIT", "WS", "DOUBTED_QUOTE", 
                  "STRING_LIT", "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        self.lastTokenType = self.type
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[20] = self.NEWLINE_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                if hasattr(self, 'lastTokenType') and self.lastTokenType in [
                    self.ID, self.INT_LIT, self.HEX_LIT, self.BIN_LIT, self.OCT_LIT, self.FLOAT_LIT, self.BOOLEAN, self.STRING_LIT, 
                    self.RPAREN, self.RBRACKET, self.RBRACE, self.STRING, self.INT, self.FLOAT, self.BOOLEAN, self.NIL, self.TRUE, self.FALSE,
                    self.RETURN, self.CONTINUE, self.BREAK
                ]:
                    self.type = self.SEMICOLON
                    self.text = ';'
                else:
                    self.skip()

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                        raise IllegalEscape(self.text);
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[0:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[0:-1])
                else:
                    raise UncloseString(self.text)

     


