# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0332\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\5\3\u00b1\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\7\4\u00ba\n\4\f\4\16\4\u00bd\13\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00c8\n\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\7\6\u00d1\n\6\f\6\16\6\u00d4\13\6\3\7\3\7")
        buf.write("\5\7\u00d8\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00e2")
        buf.write("\n\t\f\t\16\t\u00e5\13\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00ed")
        buf.write("\n\n\f\n\16\n\u00f0\13\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\7\13\u00f8\n\13\f\13\16\13\u00fb\13\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\7\f\u0103\n\f\f\f\16\f\u0106\13\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\7\r\u010e\n\r\f\r\16\r\u0111\13\r\3\16")
        buf.write("\3\16\3\16\5\16\u0116\n\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u0120\n\17\7\17\u0122\n\17\f\17\16")
        buf.write("\17\u0125\13\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\7\20\u012f\n\20\f\20\16\20\u0132\13\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u013f\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\5\22\u0146\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0150\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u015a\n\25\3\25")
        buf.write("\3\25\3\25\5\25\u015f\n\25\3\26\3\26\5\26\u0163\n\26\3")
        buf.write("\27\3\27\3\30\3\30\5\30\u0169\n\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u0172\n\32\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\7\34\u017c\n\34\f\34\16\34\u017f\13")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0187\n\35\f\35")
        buf.write("\16\35\u018a\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36")
        buf.write("\u0192\n\36\f\36\16\36\u0195\13\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\7\37\u019d\n\37\f\37\16\37\u01a0\13\37\3 \3")
        buf.write(" \3 \3 \3 \3 \7 \u01a8\n \f \16 \u01ab\13 \3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01bb\n")
        buf.write("\"\3#\3#\3#\5#\u01c0\n#\3$\3$\3$\3$\3$\5$\u01c7\n$\3%")
        buf.write("\3%\3%\5%\u01cc\n%\3%\3%\3&\3&\3&\3&\5&\u01d4\n&\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\5(\u01de\n(\3)\3)\3)\3)\5)\u01e4")
        buf.write("\n)\3*\3*\3*\3*\3+\3+\3+\3+\3+\5+\u01ef\n+\3,\3,\3,\3")
        buf.write(",\5,\u01f5\n,\3,\3,\3,\3,\3,\5,\u01fc\n,\7,\u01fe\n,\f")
        buf.write(",\16,\u0201\13,\3-\3-\3-\3-\5-\u0207\n-\3.\3.\3.\5.\u020c")
        buf.write("\n.\3.\3.\3.\3.\5.\u0212\n.\7.\u0214\n.\f.\16.\u0217\13")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u0228")
        buf.write("\n/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u0233")
        buf.write("\n\60\f\60\16\60\u0236\13\60\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\5\64\u0246")
        buf.write("\n\64\3\65\3\65\3\65\5\65\u024b\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\5\67\u025f\n\67\38\38\38\38\38\3")
        buf.write("8\38\38\38\38\38\38\38\38\38\38\58\u0271\n8\38\38\38\3")
        buf.write("8\38\38\58\u0279\n8\39\39\39\59\u027e\n9\3:\3:\3;\3;\3")
        buf.write("<\3<\5<\u0286\n<\3=\3=\3>\3>\3?\3?\3?\3?\5?\u0290\n?\3")
        buf.write("?\3?\3?\3@\3@\3@\3@\5@\u0299\n@\3A\3A\3A\3A\3A\3B\3B\3")
        buf.write("B\5B\u02a3\nB\3C\3C\3D\3D\3D\5D\u02aa\nD\3E\3E\3F\3F\3")
        buf.write("F\3F\3F\3F\3G\3G\3G\3G\3H\3H\3H\5H\u02bb\nH\3H\3H\5H\u02bf")
        buf.write("\nH\3I\3I\5I\u02c3\nI\3J\3J\3J\3J\3J\5J\u02ca\nJ\3J\3")
        buf.write("J\3J\3K\3K\3K\3K\5K\u02d3\nK\3K\5K\u02d6\nK\3L\3L\3L\3")
        buf.write("M\3M\3M\3M\3M\5M\u02e0\nM\3M\3M\3M\3N\3N\3N\5N\u02e8\n")
        buf.write("N\3N\3N\5N\u02ec\nN\3N\3N\5N\u02f0\nN\3N\5N\u02f3\nN\3")
        buf.write("O\3O\3O\3O\3O\3O\5O\u02fb\nO\3P\3P\3P\3P\5P\u0301\nP\3")
        buf.write("Q\3Q\3Q\5Q\u0306\nQ\3R\3R\3R\5R\u030b\nR\3R\3R\3S\3S\3")
        buf.write("S\3S\5S\u0313\nS\3S\3S\5S\u0317\nS\3S\3S\3T\3T\3T\3T\3")
        buf.write("T\3T\3T\3T\5T\u0323\nT\3T\3T\5T\u0327\nT\3T\3T\3U\3U\5")
        buf.write("U\u032d\nU\3U\3U\3U\3U\2\23\6\n\20\22\24\26\30\34\36\66")
        buf.write("8:<>VZ^V\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write("\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4")
        buf.write("\u00a6\u00a8\2\t\3\2\36#\3\2\31\32\3\2\33\35\3\28;\3\2")
        buf.write("(-\3\2\'(\3\2\13\16\2\u0360\2\u00aa\3\2\2\2\4\u00b0\3")
        buf.write("\2\2\2\6\u00b2\3\2\2\2\b\u00c7\3\2\2\2\n\u00cb\3\2\2\2")
        buf.write("\f\u00d7\3\2\2\2\16\u00d9\3\2\2\2\20\u00db\3\2\2\2\22")
        buf.write("\u00e6\3\2\2\2\24\u00f1\3\2\2\2\26\u00fc\3\2\2\2\30\u0107")
        buf.write("\3\2\2\2\32\u0112\3\2\2\2\34\u0117\3\2\2\2\36\u0126\3")
        buf.write("\2\2\2 \u013e\3\2\2\2\"\u0145\3\2\2\2$\u014f\3\2\2\2&")
        buf.write("\u0151\3\2\2\2(\u015e\3\2\2\2*\u0162\3\2\2\2,\u0164\3")
        buf.write("\2\2\2.\u0168\3\2\2\2\60\u016a\3\2\2\2\62\u016d\3\2\2")
        buf.write("\2\64\u0173\3\2\2\2\66\u0175\3\2\2\28\u0180\3\2\2\2:\u018b")
        buf.write("\3\2\2\2<\u0196\3\2\2\2>\u01a1\3\2\2\2@\u01ac\3\2\2\2")
        buf.write("B\u01ba\3\2\2\2D\u01bf\3\2\2\2F\u01c6\3\2\2\2H\u01c8\3")
        buf.write("\2\2\2J\u01cf\3\2\2\2L\u01d5\3\2\2\2N\u01dd\3\2\2\2P\u01e3")
        buf.write("\3\2\2\2R\u01e5\3\2\2\2T\u01e9\3\2\2\2V\u01f4\3\2\2\2")
        buf.write("X\u0202\3\2\2\2Z\u020b\3\2\2\2\\\u0227\3\2\2\2^\u022b")
        buf.write("\3\2\2\2`\u0237\3\2\2\2b\u023b\3\2\2\2d\u023f\3\2\2\2")
        buf.write("f\u0241\3\2\2\2h\u024a\3\2\2\2j\u024c\3\2\2\2l\u025e\3")
        buf.write("\2\2\2n\u0278\3\2\2\2p\u027d\3\2\2\2r\u027f\3\2\2\2t\u0281")
        buf.write("\3\2\2\2v\u0283\3\2\2\2x\u0287\3\2\2\2z\u0289\3\2\2\2")
        buf.write("|\u028b\3\2\2\2~\u0294\3\2\2\2\u0080\u029a\3\2\2\2\u0082")
        buf.write("\u02a2\3\2\2\2\u0084\u02a4\3\2\2\2\u0086\u02a6\3\2\2\2")
        buf.write("\u0088\u02ab\3\2\2\2\u008a\u02ad\3\2\2\2\u008c\u02b3\3")
        buf.write("\2\2\2\u008e\u02b7\3\2\2\2\u0090\u02c2\3\2\2\2\u0092\u02c4")
        buf.write("\3\2\2\2\u0094\u02d2\3\2\2\2\u0096\u02d7\3\2\2\2\u0098")
        buf.write("\u02da\3\2\2\2\u009a\u02ef\3\2\2\2\u009c\u02f4\3\2\2\2")
        buf.write("\u009e\u0300\3\2\2\2\u00a0\u0302\3\2\2\2\u00a2\u0307\3")
        buf.write("\2\2\2\u00a4\u030e\3\2\2\2\u00a6\u031a\3\2\2\2\u00a8\u032a")
        buf.write("\3\2\2\2\u00aa\u00ab\5\4\3\2\u00ab\u00ac\7\2\2\3\u00ac")
        buf.write("\3\3\2\2\2\u00ad\u00ae\7\27\2\2\u00ae\u00b1\5\4\3\2\u00af")
        buf.write("\u00b1\5\6\4\2\u00b0\u00ad\3\2\2\2\u00b0\u00af\3\2\2\2")
        buf.write("\u00b1\5\3\2\2\2\u00b2\u00b3\b\4\1\2\u00b3\u00b4\5\b\5")
        buf.write("\2\u00b4\u00bb\3\2\2\2\u00b5\u00b6\f\4\2\2\u00b6\u00ba")
        buf.write("\7\27\2\2\u00b7\u00b8\f\3\2\2\u00b8\u00ba\5\b\5\2\u00b9")
        buf.write("\u00b5\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bd\3\2\2\2")
        buf.write("\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\7\3\2\2")
        buf.write("\2\u00bd\u00bb\3\2\2\2\u00be\u00c8\5\u0092J\2\u00bf\u00c8")
        buf.write("\5\u0098M\2\u00c0\u00c8\5\u0080A\2\u00c1\u00c8\5|?\2\u00c2")
        buf.write("\u00c8\5\u008cG\2\u00c3\u00c8\5\u008aF\2\u00c4\u00c8\5")
        buf.write("~@\2\u00c5\u00c8\5\u00a4S\2\u00c6\u00c8\5\u00a6T\2\u00c7")
        buf.write("\u00be\3\2\2\2\u00c7\u00bf\3\2\2\2\u00c7\u00c0\3\2\2\2")
        buf.write("\u00c7\u00c1\3\2\2\2\u00c7\u00c2\3\2\2\2\u00c7\u00c3\3")
        buf.write("\2\2\2\u00c7\u00c4\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\5\f\7\2\u00ca")
        buf.write("\t\3\2\2\2\u00cb\u00cc\b\6\1\2\u00cc\u00cd\7\27\2\2\u00cd")
        buf.write("\u00d2\3\2\2\2\u00ce\u00cf\f\3\2\2\u00cf\u00d1\7\27\2")
        buf.write("\2\u00d0\u00ce\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0")
        buf.write("\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\13\3\2\2\2\u00d4\u00d2")
        buf.write("\3\2\2\2\u00d5\u00d8\7\60\2\2\u00d6\u00d8\5\n\6\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\r\3\2\2\2\u00d9")
        buf.write("\u00da\5\20\t\2\u00da\17\3\2\2\2\u00db\u00dc\b\t\1\2\u00dc")
        buf.write("\u00dd\5\22\n\2\u00dd\u00e3\3\2\2\2\u00de\u00df\f\4\2")
        buf.write("\2\u00df\u00e0\7%\2\2\u00e0\u00e2\5\22\n\2\u00e1\u00de")
        buf.write("\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\21\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e7\b\n\1\2\u00e7\u00e8\5\24\13\2\u00e8\u00ee\3\2\2")
        buf.write("\2\u00e9\u00ea\f\4\2\2\u00ea\u00eb\7$\2\2\u00eb\u00ed")
        buf.write("\5\24\13\2\u00ec\u00e9\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\23\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f1\u00f2\b\13\1\2\u00f2\u00f3\5\26\f")
        buf.write("\2\u00f3\u00f9\3\2\2\2\u00f4\u00f5\f\4\2\2\u00f5\u00f6")
        buf.write("\t\2\2\2\u00f6\u00f8\5\26\f\2\u00f7\u00f4\3\2\2\2\u00f8")
        buf.write("\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2")
        buf.write("\u00fa\25\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\b\f")
        buf.write("\1\2\u00fd\u00fe\5\30\r\2\u00fe\u0104\3\2\2\2\u00ff\u0100")
        buf.write("\f\4\2\2\u0100\u0101\t\3\2\2\u0101\u0103\5\30\r\2\u0102")
        buf.write("\u00ff\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0104\u0105\3\2\2\2\u0105\27\3\2\2\2\u0106\u0104\3\2")
        buf.write("\2\2\u0107\u0108\b\r\1\2\u0108\u0109\5\32\16\2\u0109\u010f")
        buf.write("\3\2\2\2\u010a\u010b\f\4\2\2\u010b\u010c\t\4\2\2\u010c")
        buf.write("\u010e\5\32\16\2\u010d\u010a\3\2\2\2\u010e\u0111\3\2\2")
        buf.write("\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\31\3")
        buf.write("\2\2\2\u0111\u010f\3\2\2\2\u0112\u0115\5F$\2\u0113\u0116")
        buf.write("\5\34\17\2\u0114\u0116\5\36\20\2\u0115\u0113\3\2\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116\33\3\2\2\2\u0117\u0118\b\17\1\2\u0118")
        buf.write("\u0119\5\36\20\2\u0119\u0123\3\2\2\2\u011a\u011b\f\4\2")
        buf.write("\2\u011b\u011f\7.\2\2\u011c\u0120\7\30\2\2\u011d\u0120")
        buf.write("\5\u00a2R\2\u011e\u0120\5\60\31\2\u011f\u011c\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120\u0122\3")
        buf.write("\2\2\2\u0121\u011a\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0121")
        buf.write("\3\2\2\2\u0123\u0124\3\2\2\2\u0124\35\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0126\u0127\b\20\1\2\u0127\u0128\5 \21\2\u0128")
        buf.write("\u0130\3\2\2\2\u0129\u012a\f\4\2\2\u012a\u012b\7\66\2")
        buf.write("\2\u012b\u012c\5\64\33\2\u012c\u012d\7\67\2\2\u012d\u012f")
        buf.write("\3\2\2\2\u012e\u0129\3\2\2\2\u012f\u0132\3\2\2\2\u0130")
        buf.write("\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\37\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0133\u013f\5\"\22\2\u0134\u0135\7\62\2")
        buf.write("\2\u0135\u0136\5\16\b\2\u0136\u0137\7\63\2\2\u0137\u013f")
        buf.write("\3\2\2\2\u0138\u013f\7\30\2\2\u0139\u013f\5\u00a2R\2\u013a")
        buf.write("\u013f\5H%\2\u013b\u013f\5L\'\2\u013c\u013f\5T+\2\u013d")
        buf.write("\u013f\5X-\2\u013e\u0133\3\2\2\2\u013e\u0134\3\2\2\2\u013e")
        buf.write("\u0138\3\2\2\2\u013e\u0139\3\2\2\2\u013e\u013a\3\2\2\2")
        buf.write("\u013e\u013b\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013d\3")
        buf.write("\2\2\2\u013f!\3\2\2\2\u0140\u0146\5.\30\2\u0141\u0146")
        buf.write("\7\25\2\2\u0142\u0146\7\26\2\2\u0143\u0146\7\24\2\2\u0144")
        buf.write("\u0146\7>\2\2\u0145\u0140\3\2\2\2\u0145\u0141\3\2\2\2")
        buf.write("\u0145\u0142\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0144\3")
        buf.write("\2\2\2\u0146#\3\2\2\2\u0147\u0150\5,\27\2\u0148\u0150")
        buf.write("\7<\2\2\u0149\u0150\7>\2\2\u014a\u0150\7\25\2\2\u014b")
        buf.write("\u0150\7\26\2\2\u014c\u0150\7\24\2\2\u014d\u0150\5L\'")
        buf.write("\2\u014e\u0150\7\30\2\2\u014f\u0147\3\2\2\2\u014f\u0148")
        buf.write("\3\2\2\2\u014f\u0149\3\2\2\2\u014f\u014a\3\2\2\2\u014f")
        buf.write("\u014b\3\2\2\2\u014f\u014c\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u014f\u014e\3\2\2\2\u0150%\3\2\2\2\u0151\u0152\7\64\2")
        buf.write("\2\u0152\u0153\5(\25\2\u0153\u0154\7\65\2\2\u0154\'\3")
        buf.write("\2\2\2\u0155\u015f\5$\23\2\u0156\u015f\5&\24\2\u0157\u015a")
        buf.write("\5$\23\2\u0158\u015a\5&\24\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\7/\2\2")
        buf.write("\u015c\u015d\5(\25\2\u015d\u015f\3\2\2\2\u015e\u0155\3")
        buf.write("\2\2\2\u015e\u0156\3\2\2\2\u015e\u0159\3\2\2\2\u015f)")
        buf.write("\3\2\2\2\u0160\u0163\5H%\2\u0161\u0163\5L\'\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0161\3\2\2\2\u0163+\3\2\2\2\u0164\u0165")
        buf.write("\t\5\2\2\u0165-\3\2\2\2\u0166\u0169\5,\27\2\u0167\u0169")
        buf.write("\7<\2\2\u0168\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("/\3\2\2\2\u016a\u016b\5D#\2\u016b\u016c\5\62\32\2\u016c")
        buf.write("\61\3\2\2\2\u016d\u016e\7\66\2\2\u016e\u016f\5\64\33\2")
        buf.write("\u016f\u0171\7\67\2\2\u0170\u0172\5\62\32\2\u0171\u0170")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172\63\3\2\2\2\u0173\u0174")
        buf.write("\5\66\34\2\u0174\65\3\2\2\2\u0175\u0176\b\34\1\2\u0176")
        buf.write("\u0177\58\35\2\u0177\u017d\3\2\2\2\u0178\u0179\f\4\2\2")
        buf.write("\u0179\u017a\7%\2\2\u017a\u017c\58\35\2\u017b\u0178\3")
        buf.write("\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\67\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181")
        buf.write("\b\35\1\2\u0181\u0182\5:\36\2\u0182\u0188\3\2\2\2\u0183")
        buf.write("\u0184\f\4\2\2\u0184\u0185\7$\2\2\u0185\u0187\5:\36\2")
        buf.write("\u0186\u0183\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0188\u0189\3\2\2\2\u01899\3\2\2\2\u018a\u0188")
        buf.write("\3\2\2\2\u018b\u018c\b\36\1\2\u018c\u018d\5<\37\2\u018d")
        buf.write("\u0193\3\2\2\2\u018e\u018f\f\4\2\2\u018f\u0190\t\2\2\2")
        buf.write("\u0190\u0192\5<\37\2\u0191\u018e\3\2\2\2\u0192\u0195\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194;")
        buf.write("\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0197\b\37\1\2\u0197")
        buf.write("\u0198\5> \2\u0198\u019e\3\2\2\2\u0199\u019a\f\4\2\2\u019a")
        buf.write("\u019b\t\3\2\2\u019b\u019d\5> \2\u019c\u0199\3\2\2\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f=\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\b \1\2")
        buf.write("\u01a2\u01a3\5@!\2\u01a3\u01a9\3\2\2\2\u01a4\u01a5\f\4")
        buf.write("\2\2\u01a5\u01a6\t\4\2\2\u01a6\u01a8\5@!\2\u01a7\u01a4")
        buf.write("\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa?\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01ad\5F$\2\u01ad\u01ae\5B\"\2\u01aeA\3\2\2\2\u01af\u01bb")
        buf.write("\5D#\2\u01b0\u01bb\5\60\31\2\u01b1\u01bb\5,\27\2\u01b2")
        buf.write("\u01b3\7\62\2\2\u01b3\u01b4\5\64\33\2\u01b4\u01b5\7\63")
        buf.write("\2\2\u01b5\u01bb\3\2\2\2\u01b6\u01bb\5H%\2\u01b7\u01bb")
        buf.write("\5L\'\2\u01b8\u01bb\5T+\2\u01b9\u01bb\5X-\2\u01ba\u01af")
        buf.write("\3\2\2\2\u01ba\u01b0\3\2\2\2\u01ba\u01b1\3\2\2\2\u01ba")
        buf.write("\u01b2\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3\2\2\2")
        buf.write("\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bbC\3\2\2")
        buf.write("\2\u01bc\u01c0\7\30\2\2\u01bd\u01c0\7>\2\2\u01be\u01c0")
        buf.write("\5\u00a2R\2\u01bf\u01bc\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0E\3\2\2\2\u01c1\u01c7\3\2\2\2\u01c2")
        buf.write("\u01c3\7\32\2\2\u01c3\u01c7\5F$\2\u01c4\u01c5\7&\2\2\u01c5")
        buf.write("\u01c7\5F$\2\u01c6\u01c1\3\2\2\2\u01c6\u01c2\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c7G\3\2\2\2\u01c8\u01cb\5J&\2\u01c9")
        buf.write("\u01cc\5\u0084C\2\u01ca\u01cc\5\u0088E\2\u01cb\u01c9\3")
        buf.write("\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce")
        buf.write("\5&\24\2\u01ceI\3\2\2\2\u01cf\u01d0\7\66\2\2\u01d0\u01d1")
        buf.write("\5\64\33\2\u01d1\u01d3\7\67\2\2\u01d2\u01d4\5J&\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4K\3\2\2\2\u01d5")
        buf.write("\u01d6\7\30\2\2\u01d6\u01d7\7\64\2\2\u01d7\u01d8\5N(\2")
        buf.write("\u01d8\u01d9\7\65\2\2\u01d9M\3\2\2\2\u01da\u01db\5R*\2")
        buf.write("\u01db\u01dc\5P)\2\u01dc\u01de\3\2\2\2\u01dd\u01da\3\2")
        buf.write("\2\2\u01dd\u01de\3\2\2\2\u01deO\3\2\2\2\u01df\u01e0\7")
        buf.write("/\2\2\u01e0\u01e1\5R*\2\u01e1\u01e2\5P)\2\u01e2\u01e4")
        buf.write("\3\2\2\2\u01e3\u01df\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write("Q\3\2\2\2\u01e5\u01e6\7\30\2\2\u01e6\u01e7\7\61\2\2\u01e7")
        buf.write("\u01e8\5\16\b\2\u01e8S\3\2\2\2\u01e9\u01ea\5V,\2\u01ea")
        buf.write("\u01ee\7.\2\2\u01eb\u01ef\7\30\2\2\u01ec\u01ef\5\u00a2")
        buf.write("R\2\u01ed\u01ef\5\60\31\2\u01ee\u01eb\3\2\2\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ee\u01ed\3\2\2\2\u01efU\3\2\2\2\u01f0\u01f1")
        buf.write("\b,\1\2\u01f1\u01f5\7\30\2\2\u01f2\u01f5\5\u00a2R\2\u01f3")
        buf.write("\u01f5\5\60\31\2\u01f4\u01f0\3\2\2\2\u01f4\u01f2\3\2\2")
        buf.write("\2\u01f4\u01f3\3\2\2\2\u01f5\u01ff\3\2\2\2\u01f6\u01f7")
        buf.write("\f\6\2\2\u01f7\u01fb\7.\2\2\u01f8\u01fc\7\30\2\2\u01f9")
        buf.write("\u01fc\5\u00a2R\2\u01fa\u01fc\5\60\31\2\u01fb\u01f8\3")
        buf.write("\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01fe")
        buf.write("\3\2\2\2\u01fd\u01f6\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200W\3\2\2\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0202\u0203\5Z.\2\u0203\u0206\7.\2\2\u0204")
        buf.write("\u0207\7\30\2\2\u0205\u0207\5\60\31\2\u0206\u0204\3\2")
        buf.write("\2\2\u0206\u0205\3\2\2\2\u0207Y\3\2\2\2\u0208\u0209\b")
        buf.write(".\1\2\u0209\u020c\7\30\2\2\u020a\u020c\5\60\31\2\u020b")
        buf.write("\u0208\3\2\2\2\u020b\u020a\3\2\2\2\u020c\u0215\3\2\2\2")
        buf.write("\u020d\u020e\f\5\2\2\u020e\u0211\7.\2\2\u020f\u0212\7")
        buf.write("\30\2\2\u0210\u0212\5\60\31\2\u0211\u020f\3\2\2\2\u0211")
        buf.write("\u0210\3\2\2\2\u0212\u0214\3\2\2\2\u0213\u020d\3\2\2\2")
        buf.write("\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3")
        buf.write("\2\2\2\u0216[\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u0228")
        buf.write("\5\60\31\2\u0219\u0228\5T+\2\u021a\u0228\5X-\2\u021b\u0228")
        buf.write("\5\u0080A\2\u021c\u0228\5|?\2\u021d\u0228\5\u008cG\2\u021e")
        buf.write("\u0228\5\u008aF\2\u021f\u0228\5~@\2\u0220\u0228\5z>\2")
        buf.write("\u0221\u0228\5x=\2\u0222\u0228\5j\66\2\u0223\u0228\5n")
        buf.write("8\2\u0224\u0228\5`\61\2\u0225\u0228\5\u00a2R\2\u0226\u0228")
        buf.write("\5v<\2\u0227\u0218\3\2\2\2\u0227\u0219\3\2\2\2\u0227\u021a")
        buf.write("\3\2\2\2\u0227\u021b\3\2\2\2\u0227\u021c\3\2\2\2\u0227")
        buf.write("\u021d\3\2\2\2\u0227\u021e\3\2\2\2\u0227\u021f\3\2\2\2")
        buf.write("\u0227\u0220\3\2\2\2\u0227\u0221\3\2\2\2\u0227\u0222\3")
        buf.write("\2\2\2\u0227\u0223\3\2\2\2\u0227\u0224\3\2\2\2\u0227\u0225")
        buf.write("\3\2\2\2\u0227\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229")
        buf.write("\u022a\5\f\7\2\u022a]\3\2\2\2\u022b\u022c\b\60\1\2\u022c")
        buf.write("\u022d\5\\/\2\u022d\u0234\3\2\2\2\u022e\u022f\f\4\2\2")
        buf.write("\u022f\u0233\5\\/\2\u0230\u0231\f\3\2\2\u0231\u0233\7")
        buf.write("\27\2\2\u0232\u022e\3\2\2\2\u0232\u0230\3\2\2\2\u0233")
        buf.write("\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2")
        buf.write("\u0235_\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u0238\5h\65")
        buf.write("\2\u0238\u0239\5d\63\2\u0239\u023a\5\16\b\2\u023aa\3\2")
        buf.write("\2\2\u023b\u023c\7\30\2\2\u023c\u023d\5d\63\2\u023d\u023e")
        buf.write("\5\16\b\2\u023ec\3\2\2\2\u023f\u0240\t\6\2\2\u0240e\3")
        buf.write("\2\2\2\u0241\u0242\5h\65\2\u0242\u0245\t\7\2\2\u0243\u0246")
        buf.write("\5\16\b\2\u0244\u0246\5L\'\2\u0245\u0243\3\2\2\2\u0245")
        buf.write("\u0244\3\2\2\2\u0246g\3\2\2\2\u0247\u024b\7\30\2\2\u0248")
        buf.write("\u024b\5\60\31\2\u0249\u024b\5X-\2\u024a\u0247\3\2\2\2")
        buf.write("\u024a\u0248\3\2\2\2\u024a\u0249\3\2\2\2\u024bi\3\2\2")
        buf.write("\2\u024c\u024d\7\3\2\2\u024d\u024e\7\62\2\2\u024e\u024f")
        buf.write("\5\16\b\2\u024f\u0250\7\63\2\2\u0250\u0251\5\u00a8U\2")
        buf.write("\u0251\u0252\5l\67\2\u0252k\3\2\2\2\u0253\u0254\7\4\2")
        buf.write("\2\u0254\u0255\7\3\2\2\u0255\u0256\7\62\2\2\u0256\u0257")
        buf.write("\5\16\b\2\u0257\u0258\7\63\2\2\u0258\u0259\5\u00a8U\2")
        buf.write("\u0259\u025a\5l\67\2\u025a\u025f\3\2\2\2\u025b\u025c\7")
        buf.write("\4\2\2\u025c\u025f\5\u00a8U\2\u025d\u025f\3\2\2\2\u025e")
        buf.write("\u0253\3\2\2\2\u025e\u025b\3\2\2\2\u025e\u025d\3\2\2\2")
        buf.write("\u025fm\3\2\2\2\u0260\u0261\7\5\2\2\u0261\u0262\5p9\2")
        buf.write("\u0262\u0263\7\60\2\2\u0263\u0264\5\16\b\2\u0264\u0265")
        buf.write("\7\60\2\2\u0265\u0266\5r:\2\u0266\u0267\5\u00a8U\2\u0267")
        buf.write("\u0279\3\2\2\2\u0268\u0269\7\5\2\2\u0269\u026a\7\30\2")
        buf.write("\2\u026a\u026b\7/\2\2\u026b\u026c\7\30\2\2\u026c\u026d")
        buf.write("\7(\2\2\u026d\u0270\7\23\2\2\u026e\u0271\5 \21\2\u026f")
        buf.write("\u0271\5\60\31\2\u0270\u026e\3\2\2\2\u0270\u026f\3\2\2")
        buf.write("\2\u0271\u0272\3\2\2\2\u0272\u0273\5\u00a8U\2\u0273\u0279")
        buf.write("\3\2\2\2\u0274\u0275\7\5\2\2\u0275\u0276\5\16\b\2\u0276")
        buf.write("\u0277\5\u00a8U\2\u0277\u0279\3\2\2\2\u0278\u0260\3\2")
        buf.write("\2\2\u0278\u0268\3\2\2\2\u0278\u0274\3\2\2\2\u0279o\3")
        buf.write("\2\2\2\u027a\u027e\5|?\2\u027b\u027e\5b\62\2\u027c\u027e")
        buf.write("\5\u008aF\2\u027d\u027a\3\2\2\2\u027d\u027b\3\2\2\2\u027d")
        buf.write("\u027c\3\2\2\2\u027eq\3\2\2\2\u027f\u0280\5b\62\2\u0280")
        buf.write("s\3\2\2\2\u0281\u0282\5\16\b\2\u0282u\3\2\2\2\u0283\u0285")
        buf.write("\7\6\2\2\u0284\u0286\5\16\b\2\u0285\u0284\3\2\2\2\u0285")
        buf.write("\u0286\3\2\2\2\u0286w\3\2\2\2\u0287\u0288\7\21\2\2\u0288")
        buf.write("y\3\2\2\2\u0289\u028a\7\22\2\2\u028a{\3\2\2\2\u028b\u028c")
        buf.write("\7\20\2\2\u028c\u028f\7\30\2\2\u028d\u0290\5\u0084C\2")
        buf.write("\u028e\u0290\5\u0088E\2\u028f\u028d\3\2\2\2\u028f\u028e")
        buf.write("\3\2\2\2\u028f\u0290\3\2\2\2\u0290\u0291\3\2\2\2\u0291")
        buf.write("\u0292\7\'\2\2\u0292\u0293\5\16\b\2\u0293}\3\2\2\2\u0294")
        buf.write("\u0295\7\20\2\2\u0295\u0298\7\30\2\2\u0296\u0299\5\u0084")
        buf.write("C\2\u0297\u0299\5\u0088E\2\u0298\u0296\3\2\2\2\u0298\u0297")
        buf.write("\3\2\2\2\u0299\177\3\2\2\2\u029a\u029b\7\17\2\2\u029b")
        buf.write("\u029c\7\30\2\2\u029c\u029d\7\'\2\2\u029d\u029e\5\16\b")
        buf.write("\2\u029e\u0081\3\2\2\2\u029f\u02a3\5\u0084C\2\u02a0\u02a3")
        buf.write("\5\u0088E\2\u02a1\u02a3\5\u0086D\2\u02a2\u029f\3\2\2\2")
        buf.write("\u02a2\u02a0\3\2\2\2\u02a2\u02a1\3\2\2\2\u02a3\u0083\3")
        buf.write("\2\2\2\u02a4\u02a5\t\b\2\2\u02a5\u0085\3\2\2\2\u02a6\u02a9")
        buf.write("\5\u008eH\2\u02a7\u02aa\5\u0084C\2\u02a8\u02aa\5\u0088")
        buf.write("E\2\u02a9\u02a7\3\2\2\2\u02a9\u02a8\3\2\2\2\u02aa\u0087")
        buf.write("\3\2\2\2\u02ab\u02ac\7\30\2\2\u02ac\u0089\3\2\2\2\u02ad")
        buf.write("\u02ae\7\20\2\2\u02ae\u02af\7\30\2\2\u02af\u02b0\5\u0086")
        buf.write("D\2\u02b0\u02b1\7\'\2\2\u02b1\u02b2\5\u0090I\2\u02b2\u008b")
        buf.write("\3\2\2\2\u02b3\u02b4\7\20\2\2\u02b4\u02b5\7\30\2\2\u02b5")
        buf.write("\u02b6\5\u0086D\2\u02b6\u008d\3\2\2\2\u02b7\u02ba\7\66")
        buf.write("\2\2\u02b8\u02bb\5,\27\2\u02b9\u02bb\7\30\2\2\u02ba\u02b8")
        buf.write("\3\2\2\2\u02ba\u02b9\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bc")
        buf.write("\u02be\7\67\2\2\u02bd\u02bf\5\u008eH\2\u02be\u02bd\3\2")
        buf.write("\2\2\u02be\u02bf\3\2\2\2\u02bf\u008f\3\2\2\2\u02c0\u02c3")
        buf.write("\5H%\2\u02c1\u02c3\5\16\b\2\u02c2\u02c0\3\2\2\2\u02c2")
        buf.write("\u02c1\3\2\2\2\u02c3\u0091\3\2\2\2\u02c4\u02c5\7\b\2\2")
        buf.write("\u02c5\u02c6\7\30\2\2\u02c6\u02c7\7\t\2\2\u02c7\u02c9")
        buf.write("\7\64\2\2\u02c8\u02ca\5\n\6\2\u02c9\u02c8\3\2\2\2\u02c9")
        buf.write("\u02ca\3\2\2\2\u02ca\u02cb\3\2\2\2\u02cb\u02cc\5\u0094")
        buf.write("K\2\u02cc\u02cd\7\65\2\2\u02cd\u0093\3\2\2\2\u02ce\u02cf")
        buf.write("\5\u0096L\2\u02cf\u02d0\5\f\7\2\u02d0\u02d3\3\2\2\2\u02d1")
        buf.write("\u02d3\7\27\2\2\u02d2\u02ce\3\2\2\2\u02d2\u02d1\3\2\2")
        buf.write("\2\u02d3\u02d5\3\2\2\2\u02d4\u02d6\5\u0094K\2\u02d5\u02d4")
        buf.write("\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6\u0095\3\2\2\2\u02d7")
        buf.write("\u02d8\7\30\2\2\u02d8\u02d9\5\u0082B\2\u02d9\u0097\3\2")
        buf.write("\2\2\u02da\u02db\7\b\2\2\u02db\u02dc\7\30\2\2\u02dc\u02dd")
        buf.write("\7\n\2\2\u02dd\u02df\7\64\2\2\u02de\u02e0\5\n\6\2\u02df")
        buf.write("\u02de\3\2\2\2\u02df\u02e0\3\2\2\2\u02e0\u02e1\3\2\2\2")
        buf.write("\u02e1\u02e2\5\u009aN\2\u02e2\u02e3\7\65\2\2\u02e3\u0099")
        buf.write("\3\2\2\2\u02e4\u02e5\7\30\2\2\u02e5\u02e7\7\62\2\2\u02e6")
        buf.write("\u02e8\5\u009cO\2\u02e7\u02e6\3\2\2\2\u02e7\u02e8\3\2")
        buf.write("\2\2\u02e8\u02e9\3\2\2\2\u02e9\u02eb\7\63\2\2\u02ea\u02ec")
        buf.write("\5\u0082B\2\u02eb\u02ea\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec")
        buf.write("\u02ed\3\2\2\2\u02ed\u02f0\5\f\7\2\u02ee\u02f0\7\27\2")
        buf.write("\2\u02ef\u02e4\3\2\2\2\u02ef\u02ee\3\2\2\2\u02f0\u02f2")
        buf.write("\3\2\2\2\u02f1\u02f3\5\u009aN\2\u02f2\u02f1\3\2\2\2\u02f2")
        buf.write("\u02f3\3\2\2\2\u02f3\u009b\3\2\2\2\u02f4\u02f5\7\30\2")
        buf.write("\2\u02f5\u02f6\5\u009eP\2\u02f6\u02f7\5\u0082B\2\u02f7")
        buf.write("\u02fa\3\2\2\2\u02f8\u02f9\7/\2\2\u02f9\u02fb\5\u009c")
        buf.write("O\2\u02fa\u02f8\3\2\2\2\u02fa\u02fb\3\2\2\2\u02fb\u009d")
        buf.write("\3\2\2\2\u02fc\u02fd\7/\2\2\u02fd\u02fe\7\30\2\2\u02fe")
        buf.write("\u0301\5\u009eP\2\u02ff\u0301\3\2\2\2\u0300\u02fc\3\2")
        buf.write("\2\2\u0300\u02ff\3\2\2\2\u0301\u009f\3\2\2\2\u0302\u0305")
        buf.write("\5\16\b\2\u0303\u0304\7/\2\2\u0304\u0306\5\u00a0Q\2\u0305")
        buf.write("\u0303\3\2\2\2\u0305\u0306\3\2\2\2\u0306\u00a1\3\2\2\2")
        buf.write("\u0307\u0308\7\30\2\2\u0308\u030a\7\62\2\2\u0309\u030b")
        buf.write("\5\u00a0Q\2\u030a\u0309\3\2\2\2\u030a\u030b\3\2\2\2\u030b")
        buf.write("\u030c\3\2\2\2\u030c\u030d\7\63\2\2\u030d\u00a3\3\2\2")
        buf.write("\2\u030e\u030f\7\7\2\2\u030f\u0310\7\30\2\2\u0310\u0312")
        buf.write("\7\62\2\2\u0311\u0313\5\u009cO\2\u0312\u0311\3\2\2\2\u0312")
        buf.write("\u0313\3\2\2\2\u0313\u0314\3\2\2\2\u0314\u0316\7\63\2")
        buf.write("\2\u0315\u0317\5\u0082B\2\u0316\u0315\3\2\2\2\u0316\u0317")
        buf.write("\3\2\2\2\u0317\u0318\3\2\2\2\u0318\u0319\5\u00a8U\2\u0319")
        buf.write("\u00a5\3\2\2\2\u031a\u031b\7\7\2\2\u031b\u031c\7\62\2")
        buf.write("\2\u031c\u031d\7\30\2\2\u031d\u031e\5\u0088E\2\u031e\u031f")
        buf.write("\7\63\2\2\u031f\u0320\7\30\2\2\u0320\u0322\7\62\2\2\u0321")
        buf.write("\u0323\5\u009cO\2\u0322\u0321\3\2\2\2\u0322\u0323\3\2")
        buf.write("\2\2\u0323\u0324\3\2\2\2\u0324\u0326\7\63\2\2\u0325\u0327")
        buf.write("\5\u0082B\2\u0326\u0325\3\2\2\2\u0326\u0327\3\2\2\2\u0327")
        buf.write("\u0328\3\2\2\2\u0328\u0329\5\u00a8U\2\u0329\u00a7\3\2")
        buf.write("\2\2\u032a\u032c\7\64\2\2\u032b\u032d\7\27\2\2\u032c\u032b")
        buf.write("\3\2\2\2\u032c\u032d\3\2\2\2\u032d\u032e\3\2\2\2\u032e")
        buf.write("\u032f\5^\60\2\u032f\u0330\7\65\2\2\u0330\u00a9\3\2\2")
        buf.write("\2O\u00b0\u00b9\u00bb\u00c7\u00d2\u00d7\u00e3\u00ee\u00f9")
        buf.write("\u0104\u010f\u0115\u011f\u0123\u0130\u013e\u0145\u014f")
        buf.write("\u0159\u015e\u0162\u0168\u0171\u017d\u0188\u0193\u019e")
        buf.write("\u01a9\u01ba\u01bf\u01c6\u01cb\u01d3\u01dd\u01e3\u01ee")
        buf.write("\u01f4\u01fb\u01ff\u0206\u020b\u0211\u0215\u0227\u0232")
        buf.write("\u0234\u0245\u024a\u025e\u0270\u0278\u027d\u0285\u028f")
        buf.write("\u0298\u02a2\u02a9\u02ba\u02be\u02c2\u02c9\u02d2\u02d5")
        buf.write("\u02df\u02e7\u02eb\u02ef\u02f2\u02fa\u0300\u0305\u030a")
        buf.write("\u0312\u0316\u0322\u0326\u032c")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "','", 
                     "';'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "NEWLINE", "ID", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LE", "GT", 
                      "GE", "AND", "OR", "NOT", "ASSIGN", "SHORT_ASSIGN", 
                      "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                      "MOD_ASSIGN", "DOT", "COMMA", "SEMICOLON", "COLON", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "INT_LIT", "HEX_LIT", "OCT_LIT", "BIN_LIT", 
                      "FLOAT_LIT", "WS", "STRING_LIT", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_program_list = 1
    RULE_decl_or_stmt = 2
    RULE_decl = 3
    RULE_newlines = 4
    RULE_eos = 5
    RULE_expr = 6
    RULE_logical_or_expr = 7
    RULE_logical_and_expr = 8
    RULE_relational_expr = 9
    RULE_additive_expr = 10
    RULE_multiplicative_expr = 11
    RULE_primary_expr = 12
    RULE_field_access = 13
    RULE_atom_arr_access = 14
    RULE_atom = 15
    RULE_atom_value = 16
    RULE_arr_allow_lit = 17
    RULE_arr_init_list = 18
    RULE_arr_init_list_body = 19
    RULE_literal = 20
    RULE_int_number = 21
    RULE_number = 22
    RULE_array_access = 23
    RULE_array_access_tail = 24
    RULE_index_expr = 25
    RULE_logical_index_or_expr = 26
    RULE_logical_index_and_expr = 27
    RULE_relational_index_expr = 28
    RULE_additive_index_expr = 29
    RULE_multiplicative_index_expr = 30
    RULE_signed_index_expr = 31
    RULE_primary_index_expr = 32
    RULE_secondary_index_expr = 33
    RULE_signed_tail = 34
    RULE_array_literal = 35
    RULE_array_literal_tail3 = 36
    RULE_struct_literal = 37
    RULE_struct_literal_tail = 38
    RULE_struct_literal_tail2 = 39
    RULE_field_init = 40
    RULE_struct_field_access = 41
    RULE_struct_field_access_head = 42
    RULE_struct_field_access_no_func = 43
    RULE_struct_field_access_no_func_head = 44
    RULE_stmt_in_block = 45
    RULE_stmt_list = 46
    RULE_assignment_stmt = 47
    RULE_assignment_stmt_scalar = 48
    RULE_assignment_operator = 49
    RULE_assignment_expr = 50
    RULE_lhs = 51
    RULE_if_stmt = 52
    RULE_if_stmt_tail = 53
    RULE_for_stmt = 54
    RULE_for_init = 55
    RULE_for_update = 56
    RULE_for_condition = 57
    RULE_return_stmt = 58
    RULE_continue_stmt = 59
    RULE_break_stmt = 60
    RULE_var_decl = 61
    RULE_var_decl_no_init = 62
    RULE_const_decl = 63
    RULE_types = 64
    RULE_primitiveType = 65
    RULE_arrayType = 66
    RULE_compositeType = 67
    RULE_array_decl_with_init = 68
    RULE_array_decl = 69
    RULE_dimensions = 70
    RULE_array_init = 71
    RULE_struct_decl = 72
    RULE_field_decl_list = 73
    RULE_field_decl = 74
    RULE_interface_decl = 75
    RULE_method_in_decl = 76
    RULE_param_decl = 77
    RULE_param_decl_tail = 78
    RULE_param_call_list = 79
    RULE_function_call = 80
    RULE_func_decl = 81
    RULE_method_decl = 82
    RULE_block = 83

    ruleNames =  [ "program", "program_list", "decl_or_stmt", "decl", "newlines", 
                   "eos", "expr", "logical_or_expr", "logical_and_expr", 
                   "relational_expr", "additive_expr", "multiplicative_expr", 
                   "primary_expr", "field_access", "atom_arr_access", "atom", 
                   "atom_value", "arr_allow_lit", "arr_init_list", "arr_init_list_body", 
                   "literal", "int_number", "number", "array_access", "array_access_tail", 
                   "index_expr", "logical_index_or_expr", "logical_index_and_expr", 
                   "relational_index_expr", "additive_index_expr", "multiplicative_index_expr", 
                   "signed_index_expr", "primary_index_expr", "secondary_index_expr", 
                   "signed_tail", "array_literal", "array_literal_tail3", 
                   "struct_literal", "struct_literal_tail", "struct_literal_tail2", 
                   "field_init", "struct_field_access", "struct_field_access_head", 
                   "struct_field_access_no_func", "struct_field_access_no_func_head", 
                   "stmt_in_block", "stmt_list", "assignment_stmt", "assignment_stmt_scalar", 
                   "assignment_operator", "assignment_expr", "lhs", "if_stmt", 
                   "if_stmt_tail", "for_stmt", "for_init", "for_update", 
                   "for_condition", "return_stmt", "continue_stmt", "break_stmt", 
                   "var_decl", "var_decl_no_init", "const_decl", "types", 
                   "primitiveType", "arrayType", "compositeType", "array_decl_with_init", 
                   "array_decl", "dimensions", "array_init", "struct_decl", 
                   "field_decl_list", "field_decl", "interface_decl", "method_in_decl", 
                   "param_decl", "param_decl_tail", "param_call_list", "function_call", 
                   "func_decl", "method_decl", "block" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    NEWLINE=21
    ID=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    EQ=28
    NEQ=29
    LT=30
    LE=31
    GT=32
    GE=33
    AND=34
    OR=35
    NOT=36
    ASSIGN=37
    SHORT_ASSIGN=38
    ADD_ASSIGN=39
    SUB_ASSIGN=40
    MUL_ASSIGN=41
    DIV_ASSIGN=42
    MOD_ASSIGN=43
    DOT=44
    COMMA=45
    SEMICOLON=46
    COLON=47
    LPAREN=48
    RPAREN=49
    LBRACE=50
    RBRACE=51
    LBRACKET=52
    RBRACKET=53
    INT_LIT=54
    HEX_LIT=55
    OCT_LIT=56
    BIN_LIT=57
    FLOAT_LIT=58
    WS=59
    STRING_LIT=60
    LINE_COMMENT=61
    BLOCK_COMMENT=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65

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

        def program_list(self):
            return self.getTypedRuleContext(MiniGoParser.Program_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.program_list()
            self.state = 169
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def program_list(self):
            return self.getTypedRuleContext(MiniGoParser.Program_listContext,0)


        def decl_or_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_or_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_list" ):
                return visitor.visitProgram_list(self)
            else:
                return visitor.visitChildren(self)




    def program_list(self):

        localctx = MiniGoParser.Program_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_list)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(MiniGoParser.NEWLINE)
                self.state = 172
                self.program_list()
                pass
            elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.decl_or_stmt(0)
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


    class Decl_or_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decl_or_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_or_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_or_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_or_stmt" ):
                return visitor.visitDecl_or_stmt(self)
            else:
                return visitor.visitChildren(self)



    def decl_or_stmt(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Decl_or_stmtContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_decl_or_stmt, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 183
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 179
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 180
                        self.match(MiniGoParser.NEWLINE)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 181
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 182
                        self.decl()
                        pass

             
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def array_decl_with_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_decl_with_initContext,0)


        def var_decl_no_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_no_initContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 188
                self.struct_decl()
                pass

            elif la_ == 2:
                self.state = 189
                self.interface_decl()
                pass

            elif la_ == 3:
                self.state = 190
                self.const_decl()
                pass

            elif la_ == 4:
                self.state = 191
                self.var_decl()
                pass

            elif la_ == 5:
                self.state = 192
                self.array_decl()
                pass

            elif la_ == 6:
                self.state = 193
                self.array_decl_with_init()
                pass

            elif la_ == 7:
                self.state = 194
                self.var_decl_no_init()
                pass

            elif la_ == 8:
                self.state = 195
                self.func_decl()
                pass

            elif la_ == 9:
                self.state = 196
                self.method_decl()
                pass


            self.state = 199
            self.eos()
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

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_newlines

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewlines" ):
                return visitor.visitNewlines(self)
            else:
                return visitor.visitChildren(self)



    def newlines(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.NewlinesContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_newlines, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MiniGoParser.NEWLINE)
            self._ctx.stop = self._input.LT(-1)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.NewlinesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_newlines)
                    self.state = 204
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 205
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_eos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEos" ):
                return visitor.visitEos(self)
            else:
                return visitor.visitChildren(self)




    def eos(self):

        localctx = MiniGoParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_eos)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(MiniGoParser.SEMICOLON)
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.newlines(0)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_or_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_or_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniGoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.logical_or_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_and_exprContext,0)


        def logical_or_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_or_exprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logical_or_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_or_expr" ):
                return visitor.visitLogical_or_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Logical_or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_logical_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.logical_and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 225
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_or_expr)
                    self.state = 220
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 221
                    self.match(MiniGoParser.OR)
                    self.state = 222
                    self.logical_and_expr(0) 
                self.state = 227
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_and_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_exprContext,0)


        def logical_and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_and_exprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logical_and_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_and_expr" ):
                return visitor.visitLogical_and_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Logical_and_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_logical_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.relational_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_and_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_and_expr)
                    self.state = 231
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 232
                    self.match(MiniGoParser.AND)
                    self.state = 233
                    self.relational_expr(0) 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Additive_exprContext,0)


        def relational_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_exprContext,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)



    def relational_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Relational_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_relational_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.additive_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Relational_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 244
                    self.additive_expr(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Additive_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Multiplicative_exprContext,0)


        def additive_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Additive_exprContext,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_additive_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_expr" ):
                return visitor.visitAdditive_expr(self)
            else:
                return visitor.visitChildren(self)



    def additive_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Additive_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_additive_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.multiplicative_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Additive_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expr)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 255
                    self.multiplicative_expr(0) 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplicative_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_exprContext,0)


        def multiplicative_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Multiplicative_exprContext,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplicative_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_expr" ):
                return visitor.visitMultiplicative_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplicative_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Multiplicative_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_multiplicative_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.primary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Multiplicative_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expr)
                    self.state = 264
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 265
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 266
                    self.primary_expr() 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Signed_tailContext,0)


        def field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Field_accessContext,0)


        def atom_arr_access(self):
            return self.getTypedRuleContext(MiniGoParser.Atom_arr_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primary_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expr" ):
                return visitor.visitPrimary_expr(self)
            else:
                return visitor.visitChildren(self)




    def primary_expr(self):

        localctx = MiniGoParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primary_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.signed_tail()
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 273
                self.field_access(0)
                pass

            elif la_ == 2:
                self.state = 274
                self.atom_arr_access(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_arr_access(self):
            return self.getTypedRuleContext(MiniGoParser.Atom_arr_accessContext,0)


        def field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Field_accessContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_access" ):
                return visitor.visitField_access(self)
            else:
                return visitor.visitChildren(self)



    def field_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Field_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_field_access, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.atom_arr_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 289
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Field_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_field_access)
                    self.state = 280
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 281
                    self.match(MiniGoParser.DOT)
                    self.state = 285
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        self.state = 282
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 283
                        self.function_call()
                        pass

                    elif la_ == 3:
                        self.state = 284
                        self.array_access()
                        pass

             
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Atom_arr_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(MiniGoParser.AtomContext,0)


        def atom_arr_access(self):
            return self.getTypedRuleContext(MiniGoParser.Atom_arr_accessContext,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Index_exprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_atom_arr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom_arr_access" ):
                return visitor.visitAtom_arr_access(self)
            else:
                return visitor.visitChildren(self)



    def atom_arr_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Atom_arr_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_atom_arr_access, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Atom_arr_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_atom_arr_access)
                    self.state = 295
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 296
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 297
                    self.index_expr()
                    self.state = 298
                    self.match(MiniGoParser.RBRACKET) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_value(self):
            return self.getTypedRuleContext(MiniGoParser.Atom_valueContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def struct_field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_accessContext,0)


        def struct_field_access_no_func(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_no_funcContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = MiniGoParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atom)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.atom_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(MiniGoParser.LPAREN)
                self.state = 307
                self.expr()
                self.state = 308
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 311
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 312
                self.array_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 313
                self.struct_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 314
                self.struct_field_access()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 315
                self.struct_field_access_no_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atom_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MiniGoParser.NumberContext,0)


        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_atom_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom_value" ):
                return visitor.visitAtom_value(self)
            else:
                return visitor.visitChildren(self)




    def atom_value(self):

        localctx = MiniGoParser.Atom_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_atom_value)
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.number()
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 320
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 321
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 322
                self.match(MiniGoParser.STRING_LIT)
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


    class Arr_allow_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_number(self):
            return self.getTypedRuleContext(MiniGoParser.Int_numberContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_allow_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_allow_lit" ):
                return visitor.visitArr_allow_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_allow_lit(self):

        localctx = MiniGoParser.Arr_allow_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arr_allow_lit)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.int_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 330
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 331
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 332
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_init_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def arr_init_list_body(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_init_list_bodyContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_init_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_init_list" ):
                return visitor.visitArr_init_list(self)
            else:
                return visitor.visitChildren(self)




    def arr_init_list(self):

        localctx = MiniGoParser.Arr_init_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arr_init_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MiniGoParser.LBRACE)
            self.state = 336
            self.arr_init_list_body()
            self.state = 337
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_init_list_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_allow_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_allow_litContext,0)


        def arr_init_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_init_listContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arr_init_list_body(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_init_list_bodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_init_list_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_init_list_body" ):
                return visitor.visitArr_init_list_body(self)
            else:
                return visitor.visitChildren(self)




    def arr_init_list_body(self):

        localctx = MiniGoParser.Arr_init_list_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arr_init_list_body)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.arr_allow_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.arr_init_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                    self.state = 341
                    self.arr_allow_lit()
                    pass
                elif token in [MiniGoParser.LBRACE]:
                    self.state = 342
                    self.arr_init_list()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 345
                self.match(MiniGoParser.COMMA)
                self.state = 346
                self.arr_init_list_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_literal)
        try:
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.struct_literal()
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


    class Int_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(MiniGoParser.HEX_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(MiniGoParser.OCT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(MiniGoParser.BIN_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_int_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_number" ):
                return visitor.visitInt_number(self)
            else:
                return visitor.visitChildren(self)




    def int_number(self):

        localctx = MiniGoParser.Int_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_int_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.BIN_LIT))) != 0)):
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


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_number(self):
            return self.getTypedRuleContext(MiniGoParser.Int_numberContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = MiniGoParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_number)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.int_number()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(MiniGoParser.FLOAT_LIT)
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


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def secondary_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Secondary_index_exprContext,0)


        def array_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_access_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.secondary_index_expr()
            self.state = 361
            self.array_access_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_access_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Index_exprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def array_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_access_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access_tail" ):
                return visitor.visitArray_access_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_access_tail(self):

        localctx = MiniGoParser.Array_access_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_array_access_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(MiniGoParser.LBRACKET)
            self.state = 364
            self.index_expr()
            self.state = 365
            self.match(MiniGoParser.RBRACKET)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 366
                self.array_access_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_index_or_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_index_or_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = MiniGoParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.logical_index_or_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_index_or_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_index_and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_index_and_exprContext,0)


        def logical_index_or_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_index_or_exprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logical_index_or_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_index_or_expr" ):
                return visitor.visitLogical_index_or_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_index_or_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Logical_index_or_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_logical_index_or_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.logical_index_and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_index_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_index_or_expr)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self.match(MiniGoParser.OR)
                    self.state = 376
                    self.logical_index_and_expr(0) 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_index_and_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_index_exprContext,0)


        def logical_index_and_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_index_and_exprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logical_index_and_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_index_and_expr" ):
                return visitor.visitLogical_index_and_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_index_and_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Logical_index_and_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_logical_index_and_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.relational_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_index_and_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_index_and_expr)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    self.match(MiniGoParser.AND)
                    self.state = 387
                    self.relational_index_expr(0) 
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Additive_index_exprContext,0)


        def relational_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_index_exprContext,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relational_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_index_expr" ):
                return visitor.visitRelational_index_expr(self)
            else:
                return visitor.visitChildren(self)



    def relational_index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Relational_index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_relational_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.additive_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Relational_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_index_expr)
                    self.state = 396
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 397
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 398
                    self.additive_index_expr(0) 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Additive_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Multiplicative_index_exprContext,0)


        def additive_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Additive_index_exprContext,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_additive_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_index_expr" ):
                return visitor.visitAdditive_index_expr(self)
            else:
                return visitor.visitChildren(self)



    def additive_index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Additive_index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_additive_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.multiplicative_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Additive_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_index_expr)
                    self.state = 407
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 408
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 409
                    self.multiplicative_index_expr(0) 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplicative_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Signed_index_exprContext,0)


        def multiplicative_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Multiplicative_index_exprContext,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplicative_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_index_expr" ):
                return visitor.visitMultiplicative_index_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplicative_index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Multiplicative_index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_multiplicative_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.signed_index_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Multiplicative_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_index_expr)
                    self.state = 418
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 419
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 420
                    self.signed_index_expr() 
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Signed_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signed_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Signed_tailContext,0)


        def primary_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_index_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_signed_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigned_index_expr" ):
                return visitor.visitSigned_index_expr(self)
            else:
                return visitor.visitChildren(self)




    def signed_index_expr(self):

        localctx = MiniGoParser.Signed_index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_signed_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.signed_tail()
            self.state = 427
            self.primary_index_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def secondary_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Secondary_index_exprContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def int_number(self):
            return self.getTypedRuleContext(MiniGoParser.Int_numberContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Index_exprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def struct_field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_accessContext,0)


        def struct_field_access_no_func(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_no_funcContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primary_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_index_expr" ):
                return visitor.visitPrimary_index_expr(self)
            else:
                return visitor.visitChildren(self)




    def primary_index_expr(self):

        localctx = MiniGoParser.Primary_index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_primary_index_expr)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.secondary_index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.int_number()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 432
                self.match(MiniGoParser.LPAREN)
                self.state = 433
                self.index_expr()
                self.state = 434
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 436
                self.array_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 437
                self.struct_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 438
                self.struct_field_access()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 439
                self.struct_field_access_no_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Secondary_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_secondary_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecondary_index_expr" ):
                return visitor.visitSecondary_index_expr(self)
            else:
                return visitor.visitChildren(self)




    def secondary_index_expr(self):

        localctx = MiniGoParser.Secondary_index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_secondary_index_expr)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 444
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Signed_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def signed_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Signed_tailContext,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_signed_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigned_tail" ):
                return visitor.visitSigned_tail(self)
            else:
                return visitor.visitChildren(self)




    def signed_tail(self):

        localctx = MiniGoParser.Signed_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_signed_tail)
        try:
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(MiniGoParser.SUB)
                self.state = 449
                self.signed_tail()
                pass
            elif token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 450
                self.match(MiniGoParser.NOT)
                self.state = 451
                self.signed_tail()
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal_tail3(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_tail3Context,0)


        def arr_init_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_init_listContext,0)


        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def compositeType(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.array_literal_tail3()
            self.state = 457
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 455
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 456
                self.compositeType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 459
            self.arr_init_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_tail3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Index_exprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def array_literal_tail3(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_tail3Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal_tail3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_tail3" ):
                return visitor.visitArray_literal_tail3(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_tail3(self):

        localctx = MiniGoParser.Array_literal_tail3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_array_literal_tail3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.match(MiniGoParser.LBRACKET)
            self.state = 462
            self.index_expr()
            self.state = 463
            self.match(MiniGoParser.RBRACKET)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 464
                self.array_literal_tail3()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def struct_literal_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literal_tailContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(MiniGoParser.ID)
            self.state = 468
            self.match(MiniGoParser.LBRACE)
            self.state = 469
            self.struct_literal_tail()
            self.state = 470
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literal_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_init(self):
            return self.getTypedRuleContext(MiniGoParser.Field_initContext,0)


        def struct_literal_tail2(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literal_tail2Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal_tail" ):
                return visitor.visitStruct_literal_tail(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal_tail(self):

        localctx = MiniGoParser.Struct_literal_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_struct_literal_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 472
                self.field_init()
                self.state = 473
                self.struct_literal_tail2()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literal_tail2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def field_init(self):
            return self.getTypedRuleContext(MiniGoParser.Field_initContext,0)


        def struct_literal_tail2(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literal_tail2Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal_tail2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal_tail2" ):
                return visitor.visitStruct_literal_tail2(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal_tail2(self):

        localctx = MiniGoParser.Struct_literal_tail2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_struct_literal_tail2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 477
                self.match(MiniGoParser.COMMA)
                self.state = 478
                self.field_init()
                self.state = 479
                self.struct_literal_tail2()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_init" ):
                return visitor.visitField_init(self)
            else:
                return visitor.visitChildren(self)




    def field_init(self):

        localctx = MiniGoParser.Field_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(MiniGoParser.ID)
            self.state = 484
            self.match(MiniGoParser.COLON)
            self.state = 485
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_field_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field_access_head(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_headContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field_access" ):
                return visitor.visitStruct_field_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_field_access(self):

        localctx = MiniGoParser.Struct_field_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_field_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.struct_field_access_head(0)
            self.state = 488
            self.match(MiniGoParser.DOT)
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 489
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 490
                self.function_call()
                pass

            elif la_ == 3:
                self.state = 491
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_field_access_headContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_field_access_head(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_headContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field_access_head

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field_access_head" ):
                return visitor.visitStruct_field_access_head(self)
            else:
                return visitor.visitChildren(self)



    def struct_field_access_head(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Struct_field_access_headContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_struct_field_access_head, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 495
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 496
                self.function_call()
                pass

            elif la_ == 3:
                self.state = 497
                self.array_access()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 509
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_field_access_headContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_field_access_head)
                    self.state = 500
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 501
                    self.match(MiniGoParser.DOT)
                    self.state = 505
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 502
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 503
                        self.function_call()
                        pass

                    elif la_ == 3:
                        self.state = 504
                        self.array_access()
                        pass

             
                self.state = 511
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Struct_field_access_no_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field_access_no_func_head(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_no_func_headContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field_access_no_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field_access_no_func" ):
                return visitor.visitStruct_field_access_no_func(self)
            else:
                return visitor.visitChildren(self)




    def struct_field_access_no_func(self):

        localctx = MiniGoParser.Struct_field_access_no_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_struct_field_access_no_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.struct_field_access_no_func_head(0)
            self.state = 513
            self.match(MiniGoParser.DOT)
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 514
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 515
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_field_access_no_func_headContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_field_access_no_func_head(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_no_func_headContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field_access_no_func_head

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field_access_no_func_head" ):
                return visitor.visitStruct_field_access_no_func_head(self)
            else:
                return visitor.visitChildren(self)



    def struct_field_access_no_func_head(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Struct_field_access_no_func_headContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_struct_field_access_no_func_head, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 519
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 520
                self.array_access()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 531
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_field_access_no_func_headContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_field_access_no_func_head)
                    self.state = 523
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 524
                    self.match(MiniGoParser.DOT)
                    self.state = 527
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        self.state = 525
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 526
                        self.array_access()
                        pass

             
                self.state = 533
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Stmt_in_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_accessContext,0)


        def struct_field_access_no_func(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_no_funcContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def array_decl_with_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_decl_with_initContext,0)


        def var_decl_no_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decl_no_initContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_stmtContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_in_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_in_block" ):
                return visitor.visitStmt_in_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_in_block(self):

        localctx = MiniGoParser.Stmt_in_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmt_in_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 534
                self.array_access()
                pass

            elif la_ == 2:
                self.state = 535
                self.struct_field_access()
                pass

            elif la_ == 3:
                self.state = 536
                self.struct_field_access_no_func()
                pass

            elif la_ == 4:
                self.state = 537
                self.const_decl()
                pass

            elif la_ == 5:
                self.state = 538
                self.var_decl()
                pass

            elif la_ == 6:
                self.state = 539
                self.array_decl()
                pass

            elif la_ == 7:
                self.state = 540
                self.array_decl_with_init()
                pass

            elif la_ == 8:
                self.state = 541
                self.var_decl_no_init()
                pass

            elif la_ == 9:
                self.state = 542
                self.break_stmt()
                pass

            elif la_ == 10:
                self.state = 543
                self.continue_stmt()
                pass

            elif la_ == 11:
                self.state = 544
                self.if_stmt()
                pass

            elif la_ == 12:
                self.state = 545
                self.for_stmt()
                pass

            elif la_ == 13:
                self.state = 546
                self.assignment_stmt()
                pass

            elif la_ == 14:
                self.state = 547
                self.function_call()
                pass

            elif la_ == 15:
                self.state = 548
                self.return_stmt()
                pass


            self.state = 551
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_in_block(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_in_blockContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)



    def stmt_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Stmt_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_stmt_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.stmt_in_block()
            self._ctx.stop = self._input.LT(-1)
            self.state = 562
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 560
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Stmt_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                        self.state = 556
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 557
                        self.stmt_in_block()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Stmt_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                        self.state = 558
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 559
                        self.match(MiniGoParser.NEWLINE)
                        pass

             
                self.state = 564
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assignment_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt" ):
                return visitor.visitAssignment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt(self):

        localctx = MiniGoParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.lhs()
            self.state = 566
            self.assignment_operator()
            self.state = 567
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmt_scalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignment_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_stmt_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_stmt_scalar" ):
                return visitor.visitAssignment_stmt_scalar(self)
            else:
                return visitor.visitChildren(self)




    def assignment_stmt_scalar(self):

        localctx = MiniGoParser.Assignment_stmt_scalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_assignment_stmt_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.ID)
            self.state = 570
            self.assignment_operator()
            self.state = 571
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_operator" ):
                return visitor.visitAssignment_operator(self)
            else:
                return visitor.visitChildren(self)




    def assignment_operator(self):

        localctx = MiniGoParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SHORT_ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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


    class Assignment_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_expr" ):
                return visitor.visitAssignment_expr(self)
            else:
                return visitor.visitChildren(self)




    def assignment_expr(self):

        localctx = MiniGoParser.Assignment_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_assignment_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.lhs()
            self.state = 576
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ASSIGN or _la==MiniGoParser.SHORT_ASSIGN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 577
                self.expr()
                pass

            elif la_ == 2:
                self.state = 578
                self.struct_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_field_access_no_func(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_no_funcContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_lhs)
        try:
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 583
                self.struct_field_access_no_func()
                pass


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
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def if_stmt_tail(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(MiniGoParser.IF)
            self.state = 587
            self.match(MiniGoParser.LPAREN)
            self.state = 588
            self.expr()
            self.state = 589
            self.match(MiniGoParser.RPAREN)
            self.state = 590
            self.block()
            self.state = 591
            self.if_stmt_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmt_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def if_stmt_tail(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmt_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt_tail" ):
                return visitor.visitIf_stmt_tail(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt_tail(self):

        localctx = MiniGoParser.If_stmt_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_if_stmt_tail)
        try:
            self.state = 604
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                self.match(MiniGoParser.ELSE)
                self.state = 594
                self.match(MiniGoParser.IF)
                self.state = 595
                self.match(MiniGoParser.LPAREN)
                self.state = 596
                self.expr()
                self.state = 597
                self.match(MiniGoParser.RPAREN)
                self.state = 598
                self.block()
                self.state = 599
                self.if_stmt_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
                self.match(MiniGoParser.ELSE)
                self.state = 602
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


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
            return self.getToken(MiniGoParser.FOR, 0)

        def for_init(self):
            return self.getTypedRuleContext(MiniGoParser.For_initContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def for_update(self):
            return self.getTypedRuleContext(MiniGoParser.For_updateContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def atom(self):
            return self.getTypedRuleContext(MiniGoParser.AtomContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_for_stmt)
        try:
            self.state = 630
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.match(MiniGoParser.FOR)
                self.state = 607
                self.for_init()
                self.state = 608
                self.match(MiniGoParser.SEMICOLON)
                self.state = 609
                self.expr()
                self.state = 610
                self.match(MiniGoParser.SEMICOLON)
                self.state = 611
                self.for_update()
                self.state = 612
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 614
                self.match(MiniGoParser.FOR)
                self.state = 615
                self.match(MiniGoParser.ID)
                self.state = 616
                self.match(MiniGoParser.COMMA)
                self.state = 617
                self.match(MiniGoParser.ID)
                self.state = 618
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 619
                self.match(MiniGoParser.RANGE)
                self.state = 622
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                if la_ == 1:
                    self.state = 620
                    self.atom()
                    pass

                elif la_ == 2:
                    self.state = 621
                    self.array_access()
                    pass


                self.state = 624
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 626
                self.match(MiniGoParser.FOR)
                self.state = 627
                self.expr()
                self.state = 628
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def assignment_stmt_scalar(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_stmt_scalarContext,0)


        def array_decl_with_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_decl_with_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init" ):
                return visitor.visitFor_init(self)
            else:
                return visitor.visitChildren(self)




    def for_init(self):

        localctx = MiniGoParser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_for_init)
        try:
            self.state = 635
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 632
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 633
                self.assignment_stmt_scalar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 634
                self.array_decl_with_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_updateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt_scalar(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_stmt_scalarContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_update" ):
                return visitor.visitFor_update(self)
            else:
                return visitor.visitChildren(self)




    def for_update(self):

        localctx = MiniGoParser.For_updateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_for_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.assignment_stmt_scalar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = MiniGoParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.expr()
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
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(MiniGoParser.RETURN)
            self.state = 643
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 642
                self.expr()


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
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 645
            self.match(MiniGoParser.CONTINUE)
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
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def compositeType(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(MiniGoParser.VAR)
            self.state = 650
            self.match(MiniGoParser.ID)
            self.state = 653
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 651
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 652
                self.compositeType()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                pass
            else:
                pass
            self.state = 655
            self.match(MiniGoParser.ASSIGN)
            self.state = 656
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_no_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def compositeType(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_no_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_no_init" ):
                return visitor.visitVar_decl_no_init(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_no_init(self):

        localctx = MiniGoParser.Var_decl_no_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_var_decl_no_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.match(MiniGoParser.VAR)
            self.state = 659
            self.match(MiniGoParser.ID)
            self.state = 662
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 660
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 661
                self.compositeType()
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


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_decl" ):
                return visitor.visitConst_decl(self)
            else:
                return visitor.visitChildren(self)




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 664
            self.match(MiniGoParser.CONST)
            self.state = 665
            self.match(MiniGoParser.ID)
            self.state = 666
            self.match(MiniGoParser.ASSIGN)
            self.state = 667
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def compositeType(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MiniGoParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_types)
        try:
            self.state = 672
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 669
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 670
                self.compositeType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 671
                self.arrayType()
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


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitiveType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = MiniGoParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def compositeType(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.dimensions()
            self.state = 679
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 677
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 678
                self.compositeType()
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


    class CompositeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compositeType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositeType" ):
                return visitor.visitCompositeType(self)
            else:
                return visitor.visitChildren(self)




    def compositeType(self):

        localctx = MiniGoParser.CompositeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_compositeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_decl_with_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def array_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl_with_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl_with_init" ):
                return visitor.visitArray_decl_with_init(self)
            else:
                return visitor.visitChildren(self)




    def array_decl_with_init(self):

        localctx = MiniGoParser.Array_decl_with_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_array_decl_with_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
            self.match(MiniGoParser.VAR)
            self.state = 684
            self.match(MiniGoParser.ID)
            self.state = 685
            self.arrayType()
            self.state = 686
            self.match(MiniGoParser.ASSIGN)
            self.state = 687
            self.array_init()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            self.match(MiniGoParser.VAR)
            self.state = 690
            self.match(MiniGoParser.ID)
            self.state = 691
            self.arrayType()
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

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def int_number(self):
            return self.getTypedRuleContext(MiniGoParser.Int_numberContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MiniGoParser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 693
            self.match(MiniGoParser.LBRACKET)
            self.state = 696
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT]:
                self.state = 694
                self.int_number()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 695
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 698
            self.match(MiniGoParser.RBRACKET)
            self.state = 700
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 699
                self.dimensions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init" ):
                return visitor.visitArray_init(self)
            else:
                return visitor.visitChildren(self)




    def array_init(self):

        localctx = MiniGoParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_array_init)
        try:
            self.state = 704
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 702
                self.array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 703
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def field_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_decl_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_decl" ):
                return visitor.visitStruct_decl(self)
            else:
                return visitor.visitChildren(self)




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(MiniGoParser.TYPE)
            self.state = 707
            self.match(MiniGoParser.ID)
            self.state = 708
            self.match(MiniGoParser.STRUCT)
            self.state = 709
            self.match(MiniGoParser.LBRACE)
            self.state = 711
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 710
                self.newlines(0)


            self.state = 713
            self.field_decl_list()
            self.state = 714
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Field_declContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def field_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_decl_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_decl_list" ):
                return visitor.visitField_decl_list(self)
            else:
                return visitor.visitChildren(self)




    def field_decl_list(self):

        localctx = MiniGoParser.Field_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_field_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 716
                self.field_decl()
                self.state = 717
                self.eos()
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 719
                self.match(MiniGoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 723
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE or _la==MiniGoParser.ID:
                self.state = 722
                self.field_decl_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_decl" ):
                return visitor.visitField_decl(self)
            else:
                return visitor.visitChildren(self)




    def field_decl(self):

        localctx = MiniGoParser.Field_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 725
            self.match(MiniGoParser.ID)
            self.state = 726
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def method_in_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_in_declContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_decl" ):
                return visitor.visitInterface_decl(self)
            else:
                return visitor.visitChildren(self)




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 728
            self.match(MiniGoParser.TYPE)
            self.state = 729
            self.match(MiniGoParser.ID)
            self.state = 730
            self.match(MiniGoParser.INTERFACE)
            self.state = 731
            self.match(MiniGoParser.LBRACE)
            self.state = 733
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 732
                self.newlines(0)


            self.state = 735
            self.method_in_decl()
            self.state = 736
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_in_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def method_in_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_in_declContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def param_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Param_declContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_in_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_in_decl" ):
                return visitor.visitMethod_in_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_in_decl(self):

        localctx = MiniGoParser.Method_in_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_method_in_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 749
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 738
                self.match(MiniGoParser.ID)
                self.state = 739
                self.match(MiniGoParser.LPAREN)
                self.state = 741
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 740
                    self.param_decl()


                self.state = 743
                self.match(MiniGoParser.RPAREN)
                self.state = 745
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LBRACKET))) != 0):
                    self.state = 744
                    self.types()


                self.state = 747
                self.eos()
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 748
                self.match(MiniGoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 752
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE or _la==MiniGoParser.ID:
                self.state = 751
                self.method_in_decl()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def param_decl_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Param_decl_tailContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Param_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = MiniGoParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_param_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 754
            self.match(MiniGoParser.ID)
            self.state = 755
            self.param_decl_tail()
            self.state = 756
            self.types()
            self.state = 760
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 758
                self.match(MiniGoParser.COMMA)
                self.state = 759
                self.param_decl()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_decl_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def param_decl_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Param_decl_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_decl_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl_tail" ):
                return visitor.visitParam_decl_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_decl_tail(self):

        localctx = MiniGoParser.Param_decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_param_decl_tail)
        try:
            self.state = 766
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 762
                self.match(MiniGoParser.COMMA)
                self.state = 763
                self.match(MiniGoParser.ID)
                self.state = 764
                self.param_decl_tail()
                pass
            elif token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.ID, MiniGoParser.LBRACKET]:
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


    class Param_call_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param_call_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_call_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_call_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_call_list" ):
                return visitor.visitParam_call_list(self)
            else:
                return visitor.visitChildren(self)




    def param_call_list(self):

        localctx = MiniGoParser.Param_call_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_param_call_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 768
            self.expr()
            self.state = 771
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 769
                self.match(MiniGoParser.COMMA)
                self.state = 770
                self.param_call_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def param_call_list(self):
            return self.getTypedRuleContext(MiniGoParser.Param_call_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 773
            self.match(MiniGoParser.ID)
            self.state = 774
            self.match(MiniGoParser.LPAREN)
            self.state = 776
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.HEX_LIT) | (1 << MiniGoParser.OCT_LIT) | (1 << MiniGoParser.BIN_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 775
                self.param_call_list()


            self.state = 778
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def param_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Param_declContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 780
            self.match(MiniGoParser.FUNC)
            self.state = 781
            self.match(MiniGoParser.ID)
            self.state = 782
            self.match(MiniGoParser.LPAREN)
            self.state = 784
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 783
                self.param_decl()


            self.state = 786
            self.match(MiniGoParser.RPAREN)
            self.state = 788
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LBRACKET))) != 0):
                self.state = 787
                self.types()


            self.state = 790
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def compositeType(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeTypeContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def param_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Param_declContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = MiniGoParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 792
            self.match(MiniGoParser.FUNC)
            self.state = 793
            self.match(MiniGoParser.LPAREN)
            self.state = 794
            self.match(MiniGoParser.ID)
            self.state = 795
            self.compositeType()
            self.state = 796
            self.match(MiniGoParser.RPAREN)
            self.state = 797
            self.match(MiniGoParser.ID)
            self.state = 798
            self.match(MiniGoParser.LPAREN)
            self.state = 800
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 799
                self.param_decl()


            self.state = 802
            self.match(MiniGoParser.RPAREN)
            self.state = 804
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.LBRACKET))) != 0):
                self.state = 803
                self.types()


            self.state = 806
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 808
            self.match(MiniGoParser.LBRACE)
            self.state = 810
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 809
                self.match(MiniGoParser.NEWLINE)


            self.state = 812
            self.stmt_list(0)
            self.state = 813
            self.match(MiniGoParser.RBRACE)
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
        self._predicates[2] = self.decl_or_stmt_sempred
        self._predicates[4] = self.newlines_sempred
        self._predicates[7] = self.logical_or_expr_sempred
        self._predicates[8] = self.logical_and_expr_sempred
        self._predicates[9] = self.relational_expr_sempred
        self._predicates[10] = self.additive_expr_sempred
        self._predicates[11] = self.multiplicative_expr_sempred
        self._predicates[13] = self.field_access_sempred
        self._predicates[14] = self.atom_arr_access_sempred
        self._predicates[26] = self.logical_index_or_expr_sempred
        self._predicates[27] = self.logical_index_and_expr_sempred
        self._predicates[28] = self.relational_index_expr_sempred
        self._predicates[29] = self.additive_index_expr_sempred
        self._predicates[30] = self.multiplicative_index_expr_sempred
        self._predicates[42] = self.struct_field_access_head_sempred
        self._predicates[44] = self.struct_field_access_no_func_head_sempred
        self._predicates[46] = self.stmt_list_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def decl_or_stmt_sempred(self, localctx:Decl_or_stmtContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def newlines_sempred(self, localctx:NewlinesContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def logical_or_expr_sempred(self, localctx:Logical_or_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def logical_and_expr_sempred(self, localctx:Logical_and_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def relational_expr_sempred(self, localctx:Relational_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def additive_expr_sempred(self, localctx:Additive_exprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def multiplicative_expr_sempred(self, localctx:Multiplicative_exprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def field_access_sempred(self, localctx:Field_accessContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def atom_arr_access_sempred(self, localctx:Atom_arr_accessContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def logical_index_or_expr_sempred(self, localctx:Logical_index_or_exprContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def logical_index_and_expr_sempred(self, localctx:Logical_index_and_exprContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def relational_index_expr_sempred(self, localctx:Relational_index_exprContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def additive_index_expr_sempred(self, localctx:Additive_index_exprContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

    def multiplicative_index_expr_sempred(self, localctx:Multiplicative_index_exprContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         

    def struct_field_access_head_sempred(self, localctx:Struct_field_access_headContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 4)
         

    def struct_field_access_no_func_head_sempred(self, localctx:Struct_field_access_no_func_headContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 3)
         

    def stmt_list_sempred(self, localctx:Stmt_listContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 1)
         




