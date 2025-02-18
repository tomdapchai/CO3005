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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3P")
        buf.write("\u0381\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\3\2\3\2\3\2\3\3\3\3\3\3\5\3\u00b3\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\7\4\u00bc\n\4\f\4\16\4\u00bf\13\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00ca\n\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\7\6\u00d3\n\6\f\6\16\6\u00d6\13\6\3")
        buf.write("\7\3\7\5\7\u00da\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\t\u00e4\n\t\f\t\16\t\u00e7\13\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\7\n\u00ef\n\n\f\n\16\n\u00f2\13\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\7\13\u00fa\n\13\f\13\16\13\u00fd\13\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\7\f\u0105\n\f\f\f\16\f\u0108\13")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0110\n\r\f\r\16\r\u0113")
        buf.write("\13\r\3\16\3\16\3\16\5\16\u0118\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u0122\n\17\7\17\u0124\n\17")
        buf.write("\f\17\16\17\u0127\13\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u0131\n\20\f\20\16\20\u0134\13\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u0142\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u0149\n")
        buf.write("\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0153")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u015d")
        buf.write("\n\25\3\25\3\25\3\25\5\25\u0162\n\25\3\26\3\26\5\26\u0166")
        buf.write("\n\26\3\27\3\27\3\30\3\30\5\30\u016c\n\30\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\5\32\u0175\n\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\7\34\u017f\n\34\f\34\16\34\u0182")
        buf.write("\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u018a\n\35\f")
        buf.write("\35\16\35\u018d\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7")
        buf.write("\36\u0195\n\36\f\36\16\36\u0198\13\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\7\37\u01a0\n\37\f\37\16\37\u01a3\13\37\3")
        buf.write(" \3 \3 \3 \3 \3 \7 \u01ab\n \f \16 \u01ae\13 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01be")
        buf.write("\n\"\3#\3#\3#\5#\u01c3\n#\3$\3$\3$\3$\3$\5$\u01ca\n$\3")
        buf.write("%\3%\3%\5%\u01cf\n%\3%\3%\3&\3&\3&\3&\5&\u01d7\n&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u01e1\n(\3)\3)\3)\3)\5)\u01e7")
        buf.write("\n)\3*\3*\3*\3*\3+\3+\3+\3+\3+\5+\u01f2\n+\3,\3,\3,\3")
        buf.write(",\5,\u01f8\n,\3,\3,\3,\3,\3,\5,\u01ff\n,\7,\u0201\n,\f")
        buf.write(",\16,\u0204\13,\3-\3-\3-\3-\5-\u020a\n-\3.\3.\3.\5.\u020f")
        buf.write("\n.\3.\3.\3.\3.\5.\u0215\n.\7.\u0217\n.\f.\16.\u021a\13")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u022b")
        buf.write("\n/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u0236")
        buf.write("\n\60\f\60\16\60\u0239\13\60\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\5\64\u0249")
        buf.write("\n\64\3\65\3\65\3\65\5\65\u024e\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\5\66\u0255\n\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\5\67\u0260\n\67\3\67\3\67\3\67\5\67\u0265")
        buf.write("\n\67\3\67\3\67\5\67\u0269\n\67\3\67\5\67\u026c\n\67\5")
        buf.write("\67\u026e\n\67\38\38\38\38\38\38\38\38\38\38\38\38\38")
        buf.write("\38\38\38\38\38\38\38\38\58\u0285\n8\39\39\39\59\u028a")
        buf.write("\n9\3:\3:\3;\3;\3<\3<\5<\u0292\n<\3=\3=\3>\3>\3?\3?\3")
        buf.write("?\3?\5?\u029c\n?\3?\3?\3?\3@\3@\3@\3@\5@\u02a5\n@\3A\3")
        buf.write("A\3A\3A\3A\3B\3B\3B\5B\u02af\nB\3C\3C\3D\3D\3D\3E\3E\3")
        buf.write("F\3F\3F\3F\3F\5F\u02bd\nF\3F\3F\3F\3G\3G\3G\3G\3G\5G\u02c7")
        buf.write("\nG\3H\3H\3H\5H\u02cc\nH\3H\3H\5H\u02d0\nH\3I\3I\5I\u02d4")
        buf.write("\nI\3J\3J\3J\3J\3J\5J\u02db\nJ\3J\3J\3J\3K\3K\3K\5K\u02e3")
        buf.write("\nK\3K\3K\3K\5K\u02e8\nK\3K\5K\u02eb\nK\3L\3L\3L\3M\3")
        buf.write("M\3M\3M\3M\5M\u02f5\nM\3M\3M\3M\3N\3N\3N\5N\u02fd\nN\3")
        buf.write("N\3N\5N\u0301\nN\3N\3N\5N\u0305\nN\3N\5N\u0308\nN\3O\3")
        buf.write("O\3O\3O\3O\3O\5O\u0310\nO\3P\3P\3P\5P\u0315\nP\3Q\3Q\3")
        buf.write("Q\5Q\u031a\nQ\3R\3R\3R\5R\u031f\nR\3R\3R\5R\u0323\nR\3")
        buf.write("S\3S\3S\3S\5S\u0329\nS\3S\3S\5S\u032d\nS\3S\3S\3T\3T\3")
        buf.write("T\3T\3T\3T\3T\3T\5T\u0339\nT\3T\3T\5T\u033d\nT\3T\3T\3")
        buf.write("U\3U\5U\u0343\nU\3U\3U\3U\3V\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u037f\nV\3V\2\23\6\n\20")
        buf.write("\22\24\26\30\34\36\668:<>VZ^W\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c")
        buf.write("\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\2\n\3\2+\60")
        buf.write("\3\2&\'\3\2(*\3\2EH\3\2\61\62\3\2\65:\3\2\64\65\3\2\13")
        buf.write("\16\2\u03c2\2\u00ac\3\2\2\2\4\u00b2\3\2\2\2\6\u00b4\3")
        buf.write("\2\2\2\b\u00c9\3\2\2\2\n\u00cd\3\2\2\2\f\u00d9\3\2\2\2")
        buf.write("\16\u00db\3\2\2\2\20\u00dd\3\2\2\2\22\u00e8\3\2\2\2\24")
        buf.write("\u00f3\3\2\2\2\26\u00fe\3\2\2\2\30\u0109\3\2\2\2\32\u0114")
        buf.write("\3\2\2\2\34\u0119\3\2\2\2\36\u0128\3\2\2\2 \u0141\3\2")
        buf.write("\2\2\"\u0148\3\2\2\2$\u0152\3\2\2\2&\u0154\3\2\2\2(\u0161")
        buf.write("\3\2\2\2*\u0165\3\2\2\2,\u0167\3\2\2\2.\u016b\3\2\2\2")
        buf.write("\60\u016d\3\2\2\2\62\u0170\3\2\2\2\64\u0176\3\2\2\2\66")
        buf.write("\u0178\3\2\2\28\u0183\3\2\2\2:\u018e\3\2\2\2<\u0199\3")
        buf.write("\2\2\2>\u01a4\3\2\2\2@\u01af\3\2\2\2B\u01bd\3\2\2\2D\u01c2")
        buf.write("\3\2\2\2F\u01c9\3\2\2\2H\u01cb\3\2\2\2J\u01d2\3\2\2\2")
        buf.write("L\u01d8\3\2\2\2N\u01e0\3\2\2\2P\u01e6\3\2\2\2R\u01e8\3")
        buf.write("\2\2\2T\u01ec\3\2\2\2V\u01f7\3\2\2\2X\u0205\3\2\2\2Z\u020e")
        buf.write("\3\2\2\2\\\u022a\3\2\2\2^\u022e\3\2\2\2`\u023a\3\2\2\2")
        buf.write("b\u023e\3\2\2\2d\u0242\3\2\2\2f\u0244\3\2\2\2h\u024d\3")
        buf.write("\2\2\2j\u024f\3\2\2\2l\u026d\3\2\2\2n\u0284\3\2\2\2p\u0289")
        buf.write("\3\2\2\2r\u028b\3\2\2\2t\u028d\3\2\2\2v\u028f\3\2\2\2")
        buf.write("x\u0293\3\2\2\2z\u0295\3\2\2\2|\u0297\3\2\2\2~\u02a0\3")
        buf.write("\2\2\2\u0080\u02a6\3\2\2\2\u0082\u02ae\3\2\2\2\u0084\u02b0")
        buf.write("\3\2\2\2\u0086\u02b2\3\2\2\2\u0088\u02b5\3\2\2\2\u008a")
        buf.write("\u02b7\3\2\2\2\u008c\u02c1\3\2\2\2\u008e\u02c8\3\2\2\2")
        buf.write("\u0090\u02d3\3\2\2\2\u0092\u02d5\3\2\2\2\u0094\u02e7\3")
        buf.write("\2\2\2\u0096\u02ec\3\2\2\2\u0098\u02ef\3\2\2\2\u009a\u0304")
        buf.write("\3\2\2\2\u009c\u0309\3\2\2\2\u009e\u0314\3\2\2\2\u00a0")
        buf.write("\u0316\3\2\2\2\u00a2\u0322\3\2\2\2\u00a4\u0324\3\2\2\2")
        buf.write("\u00a6\u0330\3\2\2\2\u00a8\u0340\3\2\2\2\u00aa\u037e\3")
        buf.write("\2\2\2\u00ac\u00ad\5\4\3\2\u00ad\u00ae\7\2\2\3\u00ae\3")
        buf.write("\3\2\2\2\u00af\u00b0\7$\2\2\u00b0\u00b3\5\4\3\2\u00b1")
        buf.write("\u00b3\5\6\4\2\u00b2\u00af\3\2\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\5\3\2\2\2\u00b4\u00b5\b\4\1\2\u00b5\u00b6\5\b\5")
        buf.write("\2\u00b6\u00bd\3\2\2\2\u00b7\u00b8\f\4\2\2\u00b8\u00bc")
        buf.write("\7$\2\2\u00b9\u00ba\f\3\2\2\u00ba\u00bc\5\b\5\2\u00bb")
        buf.write("\u00b7\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bf\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\7\3\2\2")
        buf.write("\2\u00bf\u00bd\3\2\2\2\u00c0\u00ca\5\u0092J\2\u00c1\u00ca")
        buf.write("\5\u0098M\2\u00c2\u00ca\5\u0080A\2\u00c3\u00ca\5|?\2\u00c4")
        buf.write("\u00ca\5\u008cG\2\u00c5\u00ca\5\u008aF\2\u00c6\u00ca\5")
        buf.write("~@\2\u00c7\u00ca\5\u00a4S\2\u00c8\u00ca\5\u00a6T\2\u00c9")
        buf.write("\u00c0\3\2\2\2\u00c9\u00c1\3\2\2\2\u00c9\u00c2\3\2\2\2")
        buf.write("\u00c9\u00c3\3\2\2\2\u00c9\u00c4\3\2\2\2\u00c9\u00c5\3")
        buf.write("\2\2\2\u00c9\u00c6\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8")
        buf.write("\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\5\f\7\2\u00cc")
        buf.write("\t\3\2\2\2\u00cd\u00ce\b\6\1\2\u00ce\u00cf\7$\2\2\u00cf")
        buf.write("\u00d4\3\2\2\2\u00d0\u00d1\f\3\2\2\u00d1\u00d3\7$\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\13\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d7\u00da\7=\2\2\u00d8\u00da\5\n\6\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da\r\3\2\2\2\u00db")
        buf.write("\u00dc\5\20\t\2\u00dc\17\3\2\2\2\u00dd\u00de\b\t\1\2\u00de")
        buf.write("\u00df\5\22\n\2\u00df\u00e5\3\2\2\2\u00e0\u00e1\f\4\2")
        buf.write("\2\u00e1\u00e2\7\62\2\2\u00e2\u00e4\5\22\n\2\u00e3\u00e0")
        buf.write("\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e6\3\2\2\2\u00e6\21\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8")
        buf.write("\u00e9\b\n\1\2\u00e9\u00ea\5\24\13\2\u00ea\u00f0\3\2\2")
        buf.write("\2\u00eb\u00ec\f\4\2\2\u00ec\u00ed\7\61\2\2\u00ed\u00ef")
        buf.write("\5\24\13\2\u00ee\u00eb\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\23\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f3\u00f4\b\13\1\2\u00f4\u00f5\5\26\f")
        buf.write("\2\u00f5\u00fb\3\2\2\2\u00f6\u00f7\f\4\2\2\u00f7\u00f8")
        buf.write("\t\2\2\2\u00f8\u00fa\5\26\f\2\u00f9\u00f6\3\2\2\2\u00fa")
        buf.write("\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\25\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\b\f")
        buf.write("\1\2\u00ff\u0100\5\30\r\2\u0100\u0106\3\2\2\2\u0101\u0102")
        buf.write("\f\4\2\2\u0102\u0103\t\3\2\2\u0103\u0105\5\30\r\2\u0104")
        buf.write("\u0101\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107\27\3\2\2\2\u0108\u0106\3\2")
        buf.write("\2\2\u0109\u010a\b\r\1\2\u010a\u010b\5\32\16\2\u010b\u0111")
        buf.write("\3\2\2\2\u010c\u010d\f\4\2\2\u010d\u010e\t\4\2\2\u010e")
        buf.write("\u0110\5\32\16\2\u010f\u010c\3\2\2\2\u0110\u0113\3\2\2")
        buf.write("\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\31\3")
        buf.write("\2\2\2\u0113\u0111\3\2\2\2\u0114\u0117\5F$\2\u0115\u0118")
        buf.write("\5\34\17\2\u0116\u0118\5\36\20\2\u0117\u0115\3\2\2\2\u0117")
        buf.write("\u0116\3\2\2\2\u0118\33\3\2\2\2\u0119\u011a\b\17\1\2\u011a")
        buf.write("\u011b\5\36\20\2\u011b\u0125\3\2\2\2\u011c\u011d\f\4\2")
        buf.write("\2\u011d\u0121\7;\2\2\u011e\u0122\7%\2\2\u011f\u0122\5")
        buf.write("\u00a2R\2\u0120\u0122\5\60\31\2\u0121\u011e\3\2\2\2\u0121")
        buf.write("\u011f\3\2\2\2\u0121\u0120\3\2\2\2\u0122\u0124\3\2\2\2")
        buf.write("\u0123\u011c\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126\35\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0128\u0129\b\20\1\2\u0129\u012a\5 \21\2\u012a")
        buf.write("\u0132\3\2\2\2\u012b\u012c\f\4\2\2\u012c\u012d\7C\2\2")
        buf.write("\u012d\u012e\5\64\33\2\u012e\u012f\7D\2\2\u012f\u0131")
        buf.write("\3\2\2\2\u0130\u012b\3\2\2\2\u0131\u0134\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\37\3\2\2\2\u0134")
        buf.write("\u0132\3\2\2\2\u0135\u0142\5\"\22\2\u0136\u0137\7?\2\2")
        buf.write("\u0137\u0138\5\16\b\2\u0138\u0139\7@\2\2\u0139\u0142\3")
        buf.write("\2\2\2\u013a\u0142\7%\2\2\u013b\u0142\5\u00a2R\2\u013c")
        buf.write("\u0142\5H%\2\u013d\u0142\5L\'\2\u013e\u0142\5T+\2\u013f")
        buf.write("\u0142\5X-\2\u0140\u0142\5\60\31\2\u0141\u0135\3\2\2\2")
        buf.write("\u0141\u0136\3\2\2\2\u0141\u013a\3\2\2\2\u0141\u013b\3")
        buf.write("\2\2\2\u0141\u013c\3\2\2\2\u0141\u013d\3\2\2\2\u0141\u013e")
        buf.write("\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("!\3\2\2\2\u0143\u0149\5.\30\2\u0144\u0149\7\25\2\2\u0145")
        buf.write("\u0149\7\26\2\2\u0146\u0149\7\24\2\2\u0147\u0149\7K\2")
        buf.write("\2\u0148\u0143\3\2\2\2\u0148\u0144\3\2\2\2\u0148\u0145")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write("#\3\2\2\2\u014a\u0153\5,\27\2\u014b\u0153\7I\2\2\u014c")
        buf.write("\u0153\7K\2\2\u014d\u0153\7\25\2\2\u014e\u0153\7\26\2")
        buf.write("\2\u014f\u0153\7\24\2\2\u0150\u0153\5L\'\2\u0151\u0153")
        buf.write("\7%\2\2\u0152\u014a\3\2\2\2\u0152\u014b\3\2\2\2\u0152")
        buf.write("\u014c\3\2\2\2\u0152\u014d\3\2\2\2\u0152\u014e\3\2\2\2")
        buf.write("\u0152\u014f\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0151\3")
        buf.write("\2\2\2\u0153%\3\2\2\2\u0154\u0155\7A\2\2\u0155\u0156\5")
        buf.write("(\25\2\u0156\u0157\7B\2\2\u0157\'\3\2\2\2\u0158\u0162")
        buf.write("\5$\23\2\u0159\u0162\5&\24\2\u015a\u015d\5$\23\2\u015b")
        buf.write("\u015d\5&\24\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2")
        buf.write("\u015d\u015e\3\2\2\2\u015e\u015f\7<\2\2\u015f\u0160\5")
        buf.write("(\25\2\u0160\u0162\3\2\2\2\u0161\u0158\3\2\2\2\u0161\u0159")
        buf.write("\3\2\2\2\u0161\u015c\3\2\2\2\u0162)\3\2\2\2\u0163\u0166")
        buf.write("\5H%\2\u0164\u0166\5L\'\2\u0165\u0163\3\2\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166+\3\2\2\2\u0167\u0168\t\5\2\2\u0168-\3\2")
        buf.write("\2\2\u0169\u016c\5,\27\2\u016a\u016c\7I\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016a\3\2\2\2\u016c/\3\2\2\2\u016d\u016e")
        buf.write("\5D#\2\u016e\u016f\5\62\32\2\u016f\61\3\2\2\2\u0170\u0171")
        buf.write("\7C\2\2\u0171\u0172\5\64\33\2\u0172\u0174\7D\2\2\u0173")
        buf.write("\u0175\5\62\32\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2")
        buf.write("\2\u0175\63\3\2\2\2\u0176\u0177\5\66\34\2\u0177\65\3\2")
        buf.write("\2\2\u0178\u0179\b\34\1\2\u0179\u017a\58\35\2\u017a\u0180")
        buf.write("\3\2\2\2\u017b\u017c\f\4\2\2\u017c\u017d\7\62\2\2\u017d")
        buf.write("\u017f\58\35\2\u017e\u017b\3\2\2\2\u017f\u0182\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\67\3\2")
        buf.write("\2\2\u0182\u0180\3\2\2\2\u0183\u0184\b\35\1\2\u0184\u0185")
        buf.write("\5:\36\2\u0185\u018b\3\2\2\2\u0186\u0187\f\4\2\2\u0187")
        buf.write("\u0188\t\6\2\2\u0188\u018a\5:\36\2\u0189\u0186\3\2\2\2")
        buf.write("\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3")
        buf.write("\2\2\2\u018c9\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f")
        buf.write("\b\36\1\2\u018f\u0190\5<\37\2\u0190\u0196\3\2\2\2\u0191")
        buf.write("\u0192\f\4\2\2\u0192\u0193\t\2\2\2\u0193\u0195\5<\37\2")
        buf.write("\u0194\u0191\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3")
        buf.write("\2\2\2\u0196\u0197\3\2\2\2\u0197;\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0199\u019a\b\37\1\2\u019a\u019b\5> \2\u019b")
        buf.write("\u01a1\3\2\2\2\u019c\u019d\f\4\2\2\u019d\u019e\t\3\2\2")
        buf.write("\u019e\u01a0\5> \2\u019f\u019c\3\2\2\2\u01a0\u01a3\3\2")
        buf.write("\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2=\3")
        buf.write("\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\b \1\2\u01a5\u01a6")
        buf.write("\5@!\2\u01a6\u01ac\3\2\2\2\u01a7\u01a8\f\4\2\2\u01a8\u01a9")
        buf.write("\t\4\2\2\u01a9\u01ab\5B\"\2\u01aa\u01a7\3\2\2\2\u01ab")
        buf.write("\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad?\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b0\5F$\2")
        buf.write("\u01b0\u01b1\5B\"\2\u01b1A\3\2\2\2\u01b2\u01be\5D#\2\u01b3")
        buf.write("\u01be\5\60\31\2\u01b4\u01be\5,\27\2\u01b5\u01b6\7?\2")
        buf.write("\2\u01b6\u01b7\5\64\33\2\u01b7\u01b8\7@\2\2\u01b8\u01be")
        buf.write("\3\2\2\2\u01b9\u01be\5H%\2\u01ba\u01be\5L\'\2\u01bb\u01be")
        buf.write("\5T+\2\u01bc\u01be\5X-\2\u01bd\u01b2\3\2\2\2\u01bd\u01b3")
        buf.write("\3\2\2\2\u01bd\u01b4\3\2\2\2\u01bd\u01b5\3\2\2\2\u01bd")
        buf.write("\u01b9\3\2\2\2\u01bd\u01ba\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01bd\u01bc\3\2\2\2\u01beC\3\2\2\2\u01bf\u01c3\7%\2\2")
        buf.write("\u01c0\u01c3\7K\2\2\u01c1\u01c3\5\u00a2R\2\u01c2\u01bf")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("E\3\2\2\2\u01c4\u01ca\3\2\2\2\u01c5\u01c6\7\'\2\2\u01c6")
        buf.write("\u01ca\5F$\2\u01c7\u01c8\7\63\2\2\u01c8\u01ca\5F$\2\u01c9")
        buf.write("\u01c4\3\2\2\2\u01c9\u01c5\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01caG\3\2\2\2\u01cb\u01ce\5J&\2\u01cc\u01cf\5\u0084")
        buf.write("C\2\u01cd\u01cf\5\u0088E\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\5&\24\2\u01d1")
        buf.write("I\3\2\2\2\u01d2\u01d3\7C\2\2\u01d3\u01d4\5\64\33\2\u01d4")
        buf.write("\u01d6\7D\2\2\u01d5\u01d7\5J&\2\u01d6\u01d5\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7K\3\2\2\2\u01d8\u01d9\7%\2\2\u01d9")
        buf.write("\u01da\7A\2\2\u01da\u01db\5N(\2\u01db\u01dc\7B\2\2\u01dc")
        buf.write("M\3\2\2\2\u01dd\u01de\5R*\2\u01de\u01df\5P)\2\u01df\u01e1")
        buf.write("\3\2\2\2\u01e0\u01dd\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1")
        buf.write("O\3\2\2\2\u01e2\u01e3\7<\2\2\u01e3\u01e4\5R*\2\u01e4\u01e5")
        buf.write("\5P)\2\u01e5\u01e7\3\2\2\2\u01e6\u01e2\3\2\2\2\u01e6\u01e7")
        buf.write("\3\2\2\2\u01e7Q\3\2\2\2\u01e8\u01e9\7%\2\2\u01e9\u01ea")
        buf.write("\7>\2\2\u01ea\u01eb\5\16\b\2\u01ebS\3\2\2\2\u01ec\u01ed")
        buf.write("\5V,\2\u01ed\u01f1\7;\2\2\u01ee\u01f2\7%\2\2\u01ef\u01f2")
        buf.write("\5\u00a2R\2\u01f0\u01f2\5\60\31\2\u01f1\u01ee\3\2\2\2")
        buf.write("\u01f1\u01ef\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2U\3\2\2")
        buf.write("\2\u01f3\u01f4\b,\1\2\u01f4\u01f8\7%\2\2\u01f5\u01f8\5")
        buf.write("\u00a2R\2\u01f6\u01f8\5\60\31\2\u01f7\u01f3\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8\u0202\3\2\2\2")
        buf.write("\u01f9\u01fa\f\6\2\2\u01fa\u01fe\7;\2\2\u01fb\u01ff\7")
        buf.write("%\2\2\u01fc\u01ff\5\u00a2R\2\u01fd\u01ff\5\60\31\2\u01fe")
        buf.write("\u01fb\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01fd\3\2\2\2")
        buf.write("\u01ff\u0201\3\2\2\2\u0200\u01f9\3\2\2\2\u0201\u0204\3")
        buf.write("\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203W")
        buf.write("\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0206\5Z.\2\u0206\u0209")
        buf.write("\7;\2\2\u0207\u020a\7%\2\2\u0208\u020a\5\60\31\2\u0209")
        buf.write("\u0207\3\2\2\2\u0209\u0208\3\2\2\2\u020aY\3\2\2\2\u020b")
        buf.write("\u020c\b.\1\2\u020c\u020f\7%\2\2\u020d\u020f\5\60\31\2")
        buf.write("\u020e\u020b\3\2\2\2\u020e\u020d\3\2\2\2\u020f\u0218\3")
        buf.write("\2\2\2\u0210\u0211\f\5\2\2\u0211\u0214\7;\2\2\u0212\u0215")
        buf.write("\7%\2\2\u0213\u0215\5\60\31\2\u0214\u0212\3\2\2\2\u0214")
        buf.write("\u0213\3\2\2\2\u0215\u0217\3\2\2\2\u0216\u0210\3\2\2\2")
        buf.write("\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3")
        buf.write("\2\2\2\u0219[\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u022b")
        buf.write("\5\60\31\2\u021c\u022b\5T+\2\u021d\u022b\5X-\2\u021e\u022b")
        buf.write("\5\u0080A\2\u021f\u022b\5|?\2\u0220\u022b\5\u008cG\2\u0221")
        buf.write("\u022b\5\u008aF\2\u0222\u022b\5~@\2\u0223\u022b\5z>\2")
        buf.write("\u0224\u022b\5x=\2\u0225\u022b\5j\66\2\u0226\u022b\5n")
        buf.write("8\2\u0227\u022b\5`\61\2\u0228\u022b\5\u00a2R\2\u0229\u022b")
        buf.write("\5v<\2\u022a\u021b\3\2\2\2\u022a\u021c\3\2\2\2\u022a\u021d")
        buf.write("\3\2\2\2\u022a\u021e\3\2\2\2\u022a\u021f\3\2\2\2\u022a")
        buf.write("\u0220\3\2\2\2\u022a\u0221\3\2\2\2\u022a\u0222\3\2\2\2")
        buf.write("\u022a\u0223\3\2\2\2\u022a\u0224\3\2\2\2\u022a\u0225\3")
        buf.write("\2\2\2\u022a\u0226\3\2\2\2\u022a\u0227\3\2\2\2\u022a\u0228")
        buf.write("\3\2\2\2\u022a\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c")
        buf.write("\u022d\5\f\7\2\u022d]\3\2\2\2\u022e\u022f\b\60\1\2\u022f")
        buf.write("\u0230\5\\/\2\u0230\u0237\3\2\2\2\u0231\u0232\f\4\2\2")
        buf.write("\u0232\u0236\5\\/\2\u0233\u0234\f\3\2\2\u0234\u0236\7")
        buf.write("$\2\2\u0235\u0231\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0239")
        buf.write("\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238")
        buf.write("_\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b\5h\65\2\u023b")
        buf.write("\u023c\5d\63\2\u023c\u023d\5\16\b\2\u023da\3\2\2\2\u023e")
        buf.write("\u023f\7%\2\2\u023f\u0240\5d\63\2\u0240\u0241\5\16\b\2")
        buf.write("\u0241c\3\2\2\2\u0242\u0243\t\7\2\2\u0243e\3\2\2\2\u0244")
        buf.write("\u0245\5h\65\2\u0245\u0248\t\b\2\2\u0246\u0249\5\16\b")
        buf.write("\2\u0247\u0249\5L\'\2\u0248\u0246\3\2\2\2\u0248\u0247")
        buf.write("\3\2\2\2\u0249g\3\2\2\2\u024a\u024e\7%\2\2\u024b\u024e")
        buf.write("\5\60\31\2\u024c\u024e\5X-\2\u024d\u024a\3\2\2\2\u024d")
        buf.write("\u024b\3\2\2\2\u024d\u024c\3\2\2\2\u024ei\3\2\2\2\u024f")
        buf.write("\u0250\7\3\2\2\u0250\u0251\7?\2\2\u0251\u0252\5\16\b\2")
        buf.write("\u0252\u0254\7@\2\2\u0253\u0255\5\n\6\2\u0254\u0253\3")
        buf.write("\2\2\2\u0254\u0255\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0257")
        buf.write("\5\u00a8U\2\u0257\u0258\5l\67\2\u0258k\3\2\2\2\u0259\u025a")
        buf.write("\7\4\2\2\u025a\u025b\7\3\2\2\u025b\u025c\7?\2\2\u025c")
        buf.write("\u025d\5\16\b\2\u025d\u025f\7@\2\2\u025e\u0260\5\n\6\2")
        buf.write("\u025f\u025e\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0261\3")
        buf.write("\2\2\2\u0261\u0262\5\u00a8U\2\u0262\u0263\5l\67\2\u0263")
        buf.write("\u0265\3\2\2\2\u0264\u0259\3\2\2\2\u0264\u0265\3\2\2\2")
        buf.write("\u0265\u026e\3\2\2\2\u0266\u0268\7\4\2\2\u0267\u0269\5")
        buf.write("\n\6\2\u0268\u0267\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026a")
        buf.write("\3\2\2\2\u026a\u026c\5\u00a8U\2\u026b\u0266\3\2\2\2\u026b")
        buf.write("\u026c\3\2\2\2\u026c\u026e\3\2\2\2\u026d\u0264\3\2\2\2")
        buf.write("\u026d\u026b\3\2\2\2\u026em\3\2\2\2\u026f\u0270\7\5\2")
        buf.write("\2\u0270\u0271\5p9\2\u0271\u0272\7=\2\2\u0272\u0273\5")
        buf.write("\16\b\2\u0273\u0274\7=\2\2\u0274\u0275\5r:\2\u0275\u0276")
        buf.write("\5\u00a8U\2\u0276\u0285\3\2\2\2\u0277\u0278\7\5\2\2\u0278")
        buf.write("\u0279\7%\2\2\u0279\u027a\7<\2\2\u027a\u027b\7%\2\2\u027b")
        buf.write("\u027c\7\65\2\2\u027c\u027d\7\23\2\2\u027d\u027e\5 \21")
        buf.write("\2\u027e\u027f\5\u00a8U\2\u027f\u0285\3\2\2\2\u0280\u0281")
        buf.write("\7\5\2\2\u0281\u0282\5\16\b\2\u0282\u0283\5\u00a8U\2\u0283")
        buf.write("\u0285\3\2\2\2\u0284\u026f\3\2\2\2\u0284\u0277\3\2\2\2")
        buf.write("\u0284\u0280\3\2\2\2\u0285o\3\2\2\2\u0286\u028a\5|?\2")
        buf.write("\u0287\u028a\5b\62\2\u0288\u028a\5\u008aF\2\u0289\u0286")
        buf.write("\3\2\2\2\u0289\u0287\3\2\2\2\u0289\u0288\3\2\2\2\u028a")
        buf.write("q\3\2\2\2\u028b\u028c\5b\62\2\u028cs\3\2\2\2\u028d\u028e")
        buf.write("\5\16\b\2\u028eu\3\2\2\2\u028f\u0291\7\6\2\2\u0290\u0292")
        buf.write("\5\16\b\2\u0291\u0290\3\2\2\2\u0291\u0292\3\2\2\2\u0292")
        buf.write("w\3\2\2\2\u0293\u0294\7\21\2\2\u0294y\3\2\2\2\u0295\u0296")
        buf.write("\7\22\2\2\u0296{\3\2\2\2\u0297\u0298\7\20\2\2\u0298\u029b")
        buf.write("\7%\2\2\u0299\u029c\5\u0084C\2\u029a\u029c\5\u0088E\2")
        buf.write("\u029b\u0299\3\2\2\2\u029b\u029a\3\2\2\2\u029b\u029c\3")
        buf.write("\2\2\2\u029c\u029d\3\2\2\2\u029d\u029e\7\64\2\2\u029e")
        buf.write("\u029f\5\16\b\2\u029f}\3\2\2\2\u02a0\u02a1\7\20\2\2\u02a1")
        buf.write("\u02a4\7%\2\2\u02a2\u02a5\5\u0084C\2\u02a3\u02a5\5\u0088")
        buf.write("E\2\u02a4\u02a2\3\2\2\2\u02a4\u02a3\3\2\2\2\u02a5\177")
        buf.write("\3\2\2\2\u02a6\u02a7\7\17\2\2\u02a7\u02a8\7%\2\2\u02a8")
        buf.write("\u02a9\7\64\2\2\u02a9\u02aa\5\16\b\2\u02aa\u0081\3\2\2")
        buf.write("\2\u02ab\u02af\5\u0084C\2\u02ac\u02af\5\u0088E\2\u02ad")
        buf.write("\u02af\5\u0086D\2\u02ae\u02ab\3\2\2\2\u02ae\u02ac\3\2")
        buf.write("\2\2\u02ae\u02ad\3\2\2\2\u02af\u0083\3\2\2\2\u02b0\u02b1")
        buf.write("\t\t\2\2\u02b1\u0085\3\2\2\2\u02b2\u02b3\5\62\32\2\u02b3")
        buf.write("\u02b4\5\u0082B\2\u02b4\u0087\3\2\2\2\u02b5\u02b6\7%\2")
        buf.write("\2\u02b6\u0089\3\2\2\2\u02b7\u02b8\7\20\2\2\u02b8\u02b9")
        buf.write("\7%\2\2\u02b9\u02bc\5\u008eH\2\u02ba\u02bd\5\u0084C\2")
        buf.write("\u02bb\u02bd\5\u0088E\2\u02bc\u02ba\3\2\2\2\u02bc\u02bb")
        buf.write("\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02bf\7\64\2\2\u02bf")
        buf.write("\u02c0\5\u0090I\2\u02c0\u008b\3\2\2\2\u02c1\u02c2\7\20")
        buf.write("\2\2\u02c2\u02c3\7%\2\2\u02c3\u02c6\5\u008eH\2\u02c4\u02c7")
        buf.write("\5\u0084C\2\u02c5\u02c7\5\u0088E\2\u02c6\u02c4\3\2\2\2")
        buf.write("\u02c6\u02c5\3\2\2\2\u02c7\u008d\3\2\2\2\u02c8\u02cb\7")
        buf.write("C\2\2\u02c9\u02cc\5,\27\2\u02ca\u02cc\7%\2\2\u02cb\u02c9")
        buf.write("\3\2\2\2\u02cb\u02ca\3\2\2\2\u02cc\u02cd\3\2\2\2\u02cd")
        buf.write("\u02cf\7D\2\2\u02ce\u02d0\5\u008eH\2\u02cf\u02ce\3\2\2")
        buf.write("\2\u02cf\u02d0\3\2\2\2\u02d0\u008f\3\2\2\2\u02d1\u02d4")
        buf.write("\5H%\2\u02d2\u02d4\5\16\b\2\u02d3\u02d1\3\2\2\2\u02d3")
        buf.write("\u02d2\3\2\2\2\u02d4\u0091\3\2\2\2\u02d5\u02d6\7\b\2\2")
        buf.write("\u02d6\u02d7\7%\2\2\u02d7\u02d8\7\t\2\2\u02d8\u02da\7")
        buf.write("A\2\2\u02d9\u02db\5\n\6\2\u02da\u02d9\3\2\2\2\u02da\u02db")
        buf.write("\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc\u02dd\5\u0094K\2\u02dd")
        buf.write("\u02de\7B\2\2\u02de\u0093\3\2\2\2\u02df\u02e3\5\u0096")
        buf.write("L\2\u02e0\u02e3\5\u0092J\2\u02e1\u02e3\5\u0098M\2\u02e2")
        buf.write("\u02df\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e2\u02e1\3\2\2\2")
        buf.write("\u02e3\u02e4\3\2\2\2\u02e4\u02e5\5\f\7\2\u02e5\u02e8\3")
        buf.write("\2\2\2\u02e6\u02e8\7$\2\2\u02e7\u02e2\3\2\2\2\u02e7\u02e6")
        buf.write("\3\2\2\2\u02e8\u02ea\3\2\2\2\u02e9\u02eb\5\u0094K\2\u02ea")
        buf.write("\u02e9\3\2\2\2\u02ea\u02eb\3\2\2\2\u02eb\u0095\3\2\2\2")
        buf.write("\u02ec\u02ed\7%\2\2\u02ed\u02ee\5\u0082B\2\u02ee\u0097")
        buf.write("\3\2\2\2\u02ef\u02f0\7\b\2\2\u02f0\u02f1\7%\2\2\u02f1")
        buf.write("\u02f2\7\n\2\2\u02f2\u02f4\7A\2\2\u02f3\u02f5\5\n\6\2")
        buf.write("\u02f4\u02f3\3\2\2\2\u02f4\u02f5\3\2\2\2\u02f5\u02f6\3")
        buf.write("\2\2\2\u02f6\u02f7\5\u009aN\2\u02f7\u02f8\7B\2\2\u02f8")
        buf.write("\u0099\3\2\2\2\u02f9\u02fa\7%\2\2\u02fa\u02fc\7?\2\2\u02fb")
        buf.write("\u02fd\5\u009cO\2\u02fc\u02fb\3\2\2\2\u02fc\u02fd\3\2")
        buf.write("\2\2\u02fd\u02fe\3\2\2\2\u02fe\u0300\7@\2\2\u02ff\u0301")
        buf.write("\5\u0082B\2\u0300\u02ff\3\2\2\2\u0300\u0301\3\2\2\2\u0301")
        buf.write("\u0302\3\2\2\2\u0302\u0305\5\f\7\2\u0303\u0305\7$\2\2")
        buf.write("\u0304\u02f9\3\2\2\2\u0304\u0303\3\2\2\2\u0305\u0307\3")
        buf.write("\2\2\2\u0306\u0308\5\u009aN\2\u0307\u0306\3\2\2\2\u0307")
        buf.write("\u0308\3\2\2\2\u0308\u009b\3\2\2\2\u0309\u030a\7%\2\2")
        buf.write("\u030a\u030b\5\u009eP\2\u030b\u030c\5\u0082B\2\u030c\u030f")
        buf.write("\3\2\2\2\u030d\u030e\7<\2\2\u030e\u0310\5\u009cO\2\u030f")
        buf.write("\u030d\3\2\2\2\u030f\u0310\3\2\2\2\u0310\u009d\3\2\2\2")
        buf.write("\u0311\u0312\7<\2\2\u0312\u0313\7%\2\2\u0313\u0315\5\u009e")
        buf.write("P\2\u0314\u0311\3\2\2\2\u0314\u0315\3\2\2\2\u0315\u009f")
        buf.write("\3\2\2\2\u0316\u0319\5\16\b\2\u0317\u0318\7<\2\2\u0318")
        buf.write("\u031a\5\u00a0Q\2\u0319\u0317\3\2\2\2\u0319\u031a\3\2")
        buf.write("\2\2\u031a\u00a1\3\2\2\2\u031b\u031c\7%\2\2\u031c\u031e")
        buf.write("\7?\2\2\u031d\u031f\5\u00a0Q\2\u031e\u031d\3\2\2\2\u031e")
        buf.write("\u031f\3\2\2\2\u031f\u0320\3\2\2\2\u0320\u0323\7@\2\2")
        buf.write("\u0321\u0323\5\u00aaV\2\u0322\u031b\3\2\2\2\u0322\u0321")
        buf.write("\3\2\2\2\u0323\u00a3\3\2\2\2\u0324\u0325\7\7\2\2\u0325")
        buf.write("\u0326\7%\2\2\u0326\u0328\7?\2\2\u0327\u0329\5\u009cO")
        buf.write("\2\u0328\u0327\3\2\2\2\u0328\u0329\3\2\2\2\u0329\u032a")
        buf.write("\3\2\2\2\u032a\u032c\7@\2\2\u032b\u032d\5\u0082B\2\u032c")
        buf.write("\u032b\3\2\2\2\u032c\u032d\3\2\2\2\u032d\u032e\3\2\2\2")
        buf.write("\u032e\u032f\5\u00a8U\2\u032f\u00a5\3\2\2\2\u0330\u0331")
        buf.write("\7\7\2\2\u0331\u0332\7?\2\2\u0332\u0333\7%\2\2\u0333\u0334")
        buf.write("\5\u0088E\2\u0334\u0335\7@\2\2\u0335\u0336\7%\2\2\u0336")
        buf.write("\u0338\7?\2\2\u0337\u0339\5\u009cO\2\u0338\u0337\3\2\2")
        buf.write("\2\u0338\u0339\3\2\2\2\u0339\u033a\3\2\2\2\u033a\u033c")
        buf.write("\7@\2\2\u033b\u033d\5\u0082B\2\u033c\u033b\3\2\2\2\u033c")
        buf.write("\u033d\3\2\2\2\u033d\u033e\3\2\2\2\u033e\u033f\5\u00a8")
        buf.write("U\2\u033f\u00a7\3\2\2\2\u0340\u0342\7A\2\2\u0341\u0343")
        buf.write("\7$\2\2\u0342\u0341\3\2\2\2\u0342\u0343\3\2\2\2\u0343")
        buf.write("\u0344\3\2\2\2\u0344\u0345\5^\60\2\u0345\u0346\7B\2\2")
        buf.write("\u0346\u00a9\3\2\2\2\u0347\u0348\7\27\2\2\u0348\u0349")
        buf.write("\7?\2\2\u0349\u037f\7@\2\2\u034a\u034b\7\30\2\2\u034b")
        buf.write("\u034c\7?\2\2\u034c\u034d\5\16\b\2\u034d\u034e\7@\2\2")
        buf.write("\u034e\u037f\3\2\2\2\u034f\u0350\7\31\2\2\u0350\u0351")
        buf.write("\7?\2\2\u0351\u0352\5\16\b\2\u0352\u0353\7@\2\2\u0353")
        buf.write("\u037f\3\2\2\2\u0354\u0355\7\32\2\2\u0355\u0356\7?\2\2")
        buf.write("\u0356\u037f\7@\2\2\u0357\u0358\7\33\2\2\u0358\u0359\7")
        buf.write("?\2\2\u0359\u035a\5\16\b\2\u035a\u035b\7@\2\2\u035b\u037f")
        buf.write("\3\2\2\2\u035c\u035d\7\34\2\2\u035d\u035e\7?\2\2\u035e")
        buf.write("\u035f\5\16\b\2\u035f\u0360\7@\2\2\u0360\u037f\3\2\2\2")
        buf.write("\u0361\u0362\7\35\2\2\u0362\u0363\7?\2\2\u0363\u037f\7")
        buf.write("@\2\2\u0364\u0365\7\36\2\2\u0365\u0366\7?\2\2\u0366\u0367")
        buf.write("\5\16\b\2\u0367\u0368\7@\2\2\u0368\u037f\3\2\2\2\u0369")
        buf.write("\u036a\7\37\2\2\u036a\u036b\7?\2\2\u036b\u036c\5\16\b")
        buf.write("\2\u036c\u036d\7@\2\2\u036d\u037f\3\2\2\2\u036e\u036f")
        buf.write("\7 \2\2\u036f\u0370\7?\2\2\u0370\u037f\7@\2\2\u0371\u0372")
        buf.write("\7!\2\2\u0372\u0373\7?\2\2\u0373\u0374\5\16\b\2\u0374")
        buf.write("\u0375\7@\2\2\u0375\u037f\3\2\2\2\u0376\u0377\7\"\2\2")
        buf.write("\u0377\u0378\7?\2\2\u0378\u0379\5\16\b\2\u0379\u037a\7")
        buf.write("@\2\2\u037a\u037f\3\2\2\2\u037b\u037c\7#\2\2\u037c\u037d")
        buf.write("\7?\2\2\u037d\u037f\7@\2\2\u037e\u0347\3\2\2\2\u037e\u034a")
        buf.write("\3\2\2\2\u037e\u034f\3\2\2\2\u037e\u0354\3\2\2\2\u037e")
        buf.write("\u0357\3\2\2\2\u037e\u035c\3\2\2\2\u037e\u0361\3\2\2\2")
        buf.write("\u037e\u0364\3\2\2\2\u037e\u0369\3\2\2\2\u037e\u036e\3")
        buf.write("\2\2\2\u037e\u0371\3\2\2\2\u037e\u0376\3\2\2\2\u037e\u037b")
        buf.write("\3\2\2\2\u037f\u00ab\3\2\2\2W\u00b2\u00bb\u00bd\u00c9")
        buf.write("\u00d4\u00d9\u00e5\u00f0\u00fb\u0106\u0111\u0117\u0121")
        buf.write("\u0125\u0132\u0141\u0148\u0152\u015c\u0161\u0165\u016b")
        buf.write("\u0174\u0180\u018b\u0196\u01a1\u01ac\u01bd\u01c2\u01c9")
        buf.write("\u01ce\u01d6\u01e0\u01e6\u01f1\u01f7\u01fe\u0202\u0209")
        buf.write("\u020e\u0214\u0218\u022a\u0235\u0237\u0248\u024d\u0254")
        buf.write("\u025f\u0264\u0268\u026b\u026d\u0284\u0289\u0291\u029b")
        buf.write("\u02a4\u02ae\u02bc\u02c6\u02cb\u02cf\u02d3\u02da\u02e2")
        buf.write("\u02e7\u02ea\u02f4\u02fc\u0300\u0304\u0307\u030f\u0314")
        buf.write("\u0319\u031e\u0322\u0328\u032c\u0338\u033c\u0342\u037e")
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
                     "'false'", "'getInt'", "'putInt'", "'putIntLn'", "'getFloat'", 
                     "'putFloat'", "'putFloatLn'", "'getBool'", "'putBool'", 
                     "'putBoolLn'", "'getString'", "'putString'", "'putStringLn'", 
                     "'putLn'", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", "','", 
                     "';'", "':'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "GET_INT", "PUT_INT", "PUT_INT_LN", 
                      "GET_FLOAT", "PUT_FLOAT", "PUT_FLOAT_LN", "GET_BOOL", 
                      "PUT_BOOL", "PUT_BOOL_LN", "GET_STRING", "PUT_STRING", 
                      "PUT_STRING_LN", "PUT_LN", "NEWLINE", "ID", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LE", 
                      "GT", "GE", "AND", "OR", "NOT", "ASSIGN", "SHORT_ASSIGN", 
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
    RULE_built_in_function_call = 84

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
                   "func_decl", "method_decl", "block", "built_in_function_call" ]

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
    GET_INT=21
    PUT_INT=22
    PUT_INT_LN=23
    GET_FLOAT=24
    PUT_FLOAT=25
    PUT_FLOAT_LN=26
    GET_BOOL=27
    PUT_BOOL=28
    PUT_BOOL_LN=29
    GET_STRING=30
    PUT_STRING=31
    PUT_STRING_LN=32
    PUT_LN=33
    NEWLINE=34
    ID=35
    ADD=36
    SUB=37
    MUL=38
    DIV=39
    MOD=40
    EQ=41
    NEQ=42
    LT=43
    LE=44
    GT=45
    GE=46
    AND=47
    OR=48
    NOT=49
    ASSIGN=50
    SHORT_ASSIGN=51
    ADD_ASSIGN=52
    SUB_ASSIGN=53
    MUL_ASSIGN=54
    DIV_ASSIGN=55
    MOD_ASSIGN=56
    DOT=57
    COMMA=58
    SEMICOLON=59
    COLON=60
    LPAREN=61
    RPAREN=62
    LBRACE=63
    RBRACE=64
    LBRACKET=65
    RBRACKET=66
    INT_LIT=67
    HEX_LIT=68
    OCT_LIT=69
    BIN_LIT=70
    FLOAT_LIT=71
    WS=72
    STRING_LIT=73
    LINE_COMMENT=74
    BLOCK_COMMENT=75
    ERROR_CHAR=76
    ILLEGAL_ESCAPE=77
    UNCLOSE_STRING=78

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
            self.state = 170
            self.program_list()
            self.state = 171
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
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(MiniGoParser.NEWLINE)
                self.state = 174
                self.program_list()
                pass
            elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
            self.state = 179
            self.decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 185
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 181
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 182
                        self.match(MiniGoParser.NEWLINE)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 183
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 184
                        self.decl()
                        pass

             
                self.state = 189
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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 190
                self.struct_decl()
                pass

            elif la_ == 2:
                self.state = 191
                self.interface_decl()
                pass

            elif la_ == 3:
                self.state = 192
                self.const_decl()
                pass

            elif la_ == 4:
                self.state = 193
                self.var_decl()
                pass

            elif la_ == 5:
                self.state = 194
                self.array_decl()
                pass

            elif la_ == 6:
                self.state = 195
                self.array_decl_with_init()
                pass

            elif la_ == 7:
                self.state = 196
                self.var_decl_no_init()
                pass

            elif la_ == 8:
                self.state = 197
                self.func_decl()
                pass

            elif la_ == 9:
                self.state = 198
                self.method_decl()
                pass


            self.state = 201
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
            self.state = 204
            self.match(MiniGoParser.NEWLINE)
            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.NewlinesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_newlines)
                    self.state = 206
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 207
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 212
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
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(MiniGoParser.SEMICOLON)
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
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
            self.state = 217
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
            self.state = 220
            self.logical_and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_or_expr)
                    self.state = 222
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 223
                    self.match(MiniGoParser.OR)
                    self.state = 224
                    self.logical_and_expr(0) 
                self.state = 229
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
            self.state = 231
            self.relational_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_and_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_and_expr)
                    self.state = 233
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 234
                    self.match(MiniGoParser.AND)
                    self.state = 235
                    self.relational_expr(0) 
                self.state = 240
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
            self.state = 242
            self.additive_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Relational_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 246
                    self.additive_expr(0) 
                self.state = 251
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
            self.state = 253
            self.multiplicative_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Additive_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expr)
                    self.state = 255
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 256
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 257
                    self.multiplicative_expr(0) 
                self.state = 262
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
            self.state = 264
            self.primary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Multiplicative_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expr)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 268
                    self.primary_expr() 
                self.state = 273
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
            self.state = 274
            self.signed_tail()
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 275
                self.field_access(0)
                pass

            elif la_ == 2:
                self.state = 276
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
            self.state = 280
            self.atom_arr_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Field_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_field_access)
                    self.state = 282
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 283
                    self.match(MiniGoParser.DOT)
                    self.state = 287
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        self.state = 284
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 285
                        self.function_call()
                        pass

                    elif la_ == 3:
                        self.state = 286
                        self.array_access()
                        pass

             
                self.state = 293
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
            self.state = 295
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Atom_arr_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_atom_arr_access)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 299
                    self.index_expr()
                    self.state = 300
                    self.match(MiniGoParser.RBRACKET) 
                self.state = 306
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


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


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
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.atom_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(MiniGoParser.LPAREN)
                self.state = 309
                self.expr()
                self.state = 310
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.array_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 315
                self.struct_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 316
                self.struct_field_access()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 317
                self.struct_field_access_no_func()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 318
                self.array_access()
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
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.number()
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 323
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 324
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 325
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
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.int_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 331
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 332
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 333
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 334
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 335
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
            self.state = 338
            self.match(MiniGoParser.LBRACE)
            self.state = 339
            self.arr_init_list_body()
            self.state = 340
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
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.arr_allow_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.arr_init_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                    self.state = 344
                    self.arr_allow_lit()
                    pass
                elif token in [MiniGoParser.LBRACE]:
                    self.state = 345
                    self.arr_init_list()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 348
                self.match(MiniGoParser.COMMA)
                self.state = 349
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
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
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
            self.state = 357
            _la = self._input.LA(1)
            if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (MiniGoParser.INT_LIT - 67)) | (1 << (MiniGoParser.HEX_LIT - 67)) | (1 << (MiniGoParser.OCT_LIT - 67)) | (1 << (MiniGoParser.BIN_LIT - 67)))) != 0)):
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
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.int_number()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
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
            self.state = 363
            self.secondary_index_expr()
            self.state = 364
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
            self.state = 366
            self.match(MiniGoParser.LBRACKET)
            self.state = 367
            self.index_expr()
            self.state = 368
            self.match(MiniGoParser.RBRACKET)
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 369
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
            self.state = 372
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
            self.state = 375
            self.logical_index_and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 382
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_index_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_index_or_expr)
                    self.state = 377
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 378
                    self.match(MiniGoParser.OR)
                    self.state = 379
                    self.logical_index_and_expr(0) 
                self.state = 384
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

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.relational_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_index_and_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_index_and_expr)
                    self.state = 388
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 389
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.AND or _la==MiniGoParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 390
                    self.relational_index_expr(0) 
                self.state = 395
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
            self.state = 397
            self.additive_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Relational_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_index_expr)
                    self.state = 399
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 400
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 401
                    self.additive_index_expr(0) 
                self.state = 406
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
            self.state = 408
            self.multiplicative_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Additive_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_index_expr)
                    self.state = 410
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 411
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 412
                    self.multiplicative_index_expr(0) 
                self.state = 417
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


        def primary_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_index_exprContext,0)


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
            self.state = 419
            self.signed_index_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 426
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Multiplicative_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_index_expr)
                    self.state = 421
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 422
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 423
                    self.primary_index_expr() 
                self.state = 428
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
            self.state = 429
            self.signed_tail()
            self.state = 430
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
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.secondary_index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 434
                self.int_number()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 435
                self.match(MiniGoParser.LPAREN)
                self.state = 436
                self.index_expr()
                self.state = 437
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.array_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 440
                self.struct_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 441
                self.struct_field_access()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 442
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
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 447
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
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.GET_INT, MiniGoParser.PUT_INT, MiniGoParser.PUT_INT_LN, MiniGoParser.GET_FLOAT, MiniGoParser.PUT_FLOAT, MiniGoParser.PUT_FLOAT_LN, MiniGoParser.GET_BOOL, MiniGoParser.PUT_BOOL, MiniGoParser.PUT_BOOL_LN, MiniGoParser.GET_STRING, MiniGoParser.PUT_STRING, MiniGoParser.PUT_STRING_LN, MiniGoParser.PUT_LN, MiniGoParser.ID, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(MiniGoParser.SUB)
                self.state = 452
                self.signed_tail()
                pass
            elif token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 453
                self.match(MiniGoParser.NOT)
                self.state = 454
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
            self.state = 457
            self.array_literal_tail3()
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 458
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 459
                self.compositeType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 462
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
            self.state = 464
            self.match(MiniGoParser.LBRACKET)
            self.state = 465
            self.index_expr()
            self.state = 466
            self.match(MiniGoParser.RBRACKET)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 467
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
            self.state = 470
            self.match(MiniGoParser.ID)
            self.state = 471
            self.match(MiniGoParser.LBRACE)
            self.state = 472
            self.struct_literal_tail()
            self.state = 473
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
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 475
                self.field_init()
                self.state = 476
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
            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 480
                self.match(MiniGoParser.COMMA)
                self.state = 481
                self.field_init()
                self.state = 482
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
            self.state = 486
            self.match(MiniGoParser.ID)
            self.state = 487
            self.match(MiniGoParser.COLON)
            self.state = 488
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
            self.state = 490
            self.struct_field_access_head(0)
            self.state = 491
            self.match(MiniGoParser.DOT)
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 492
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 493
                self.function_call()
                pass

            elif la_ == 3:
                self.state = 494
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
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 498
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 499
                self.function_call()
                pass

            elif la_ == 3:
                self.state = 500
                self.array_access()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 512
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_field_access_headContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_field_access_head)
                    self.state = 503
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 504
                    self.match(MiniGoParser.DOT)
                    self.state = 508
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 505
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 506
                        self.function_call()
                        pass

                    elif la_ == 3:
                        self.state = 507
                        self.array_access()
                        pass

             
                self.state = 514
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
            self.state = 515
            self.struct_field_access_no_func_head(0)
            self.state = 516
            self.match(MiniGoParser.DOT)
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 517
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 518
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
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 522
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 523
                self.array_access()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_field_access_no_func_headContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_field_access_no_func_head)
                    self.state = 526
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 527
                    self.match(MiniGoParser.DOT)
                    self.state = 530
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        self.state = 528
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 529
                        self.array_access()
                        pass

             
                self.state = 536
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
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 537
                self.array_access()
                pass

            elif la_ == 2:
                self.state = 538
                self.struct_field_access()
                pass

            elif la_ == 3:
                self.state = 539
                self.struct_field_access_no_func()
                pass

            elif la_ == 4:
                self.state = 540
                self.const_decl()
                pass

            elif la_ == 5:
                self.state = 541
                self.var_decl()
                pass

            elif la_ == 6:
                self.state = 542
                self.array_decl()
                pass

            elif la_ == 7:
                self.state = 543
                self.array_decl_with_init()
                pass

            elif la_ == 8:
                self.state = 544
                self.var_decl_no_init()
                pass

            elif la_ == 9:
                self.state = 545
                self.break_stmt()
                pass

            elif la_ == 10:
                self.state = 546
                self.continue_stmt()
                pass

            elif la_ == 11:
                self.state = 547
                self.if_stmt()
                pass

            elif la_ == 12:
                self.state = 548
                self.for_stmt()
                pass

            elif la_ == 13:
                self.state = 549
                self.assignment_stmt()
                pass

            elif la_ == 14:
                self.state = 550
                self.function_call()
                pass

            elif la_ == 15:
                self.state = 551
                self.return_stmt()
                pass


            self.state = 554
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
            self.state = 557
            self.stmt_in_block()
            self._ctx.stop = self._input.LT(-1)
            self.state = 565
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 563
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Stmt_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                        self.state = 559
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 560
                        self.stmt_in_block()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Stmt_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                        self.state = 561
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 562
                        self.match(MiniGoParser.NEWLINE)
                        pass

             
                self.state = 567
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
            self.state = 568
            self.lhs()
            self.state = 569
            self.assignment_operator()
            self.state = 570
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
            self.state = 572
            self.match(MiniGoParser.ID)
            self.state = 573
            self.assignment_operator()
            self.state = 574
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
            self.state = 576
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
            self.state = 578
            self.lhs()
            self.state = 579
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ASSIGN or _la==MiniGoParser.SHORT_ASSIGN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 582
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 580
                self.expr()
                pass

            elif la_ == 2:
                self.state = 581
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
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 584
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 585
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 586
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


        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.match(MiniGoParser.IF)
            self.state = 590
            self.match(MiniGoParser.LPAREN)
            self.state = 591
            self.expr()
            self.state = 592
            self.match(MiniGoParser.RPAREN)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 593
                self.newlines(0)


            self.state = 596
            self.block()
            self.state = 597
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


        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 619
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 610
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ELSE:
                    self.state = 599
                    self.match(MiniGoParser.ELSE)
                    self.state = 600
                    self.match(MiniGoParser.IF)
                    self.state = 601
                    self.match(MiniGoParser.LPAREN)
                    self.state = 602
                    self.expr()
                    self.state = 603
                    self.match(MiniGoParser.RPAREN)
                    self.state = 605
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.NEWLINE:
                        self.state = 604
                        self.newlines(0)


                    self.state = 607
                    self.block()
                    self.state = 608
                    self.if_stmt_tail()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ELSE:
                    self.state = 612
                    self.match(MiniGoParser.ELSE)
                    self.state = 614
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.NEWLINE:
                        self.state = 613
                        self.newlines(0)


                    self.state = 616
                    self.block()


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
            self.state = 642
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 621
                self.match(MiniGoParser.FOR)
                self.state = 622
                self.for_init()
                self.state = 623
                self.match(MiniGoParser.SEMICOLON)
                self.state = 624
                self.expr()
                self.state = 625
                self.match(MiniGoParser.SEMICOLON)
                self.state = 626
                self.for_update()
                self.state = 627
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 629
                self.match(MiniGoParser.FOR)
                self.state = 630
                self.match(MiniGoParser.ID)
                self.state = 631
                self.match(MiniGoParser.COMMA)
                self.state = 632
                self.match(MiniGoParser.ID)
                self.state = 633
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 634
                self.match(MiniGoParser.RANGE)
                self.state = 635
                self.atom()
                self.state = 636
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 638
                self.match(MiniGoParser.FOR)
                self.state = 639
                self.expr()
                self.state = 640
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
            self.state = 647
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 644
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 645
                self.assignment_stmt_scalar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 646
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
            self.state = 649
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
            self.state = 651
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
            self.state = 653
            self.match(MiniGoParser.RETURN)
            self.state = 655
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & ((1 << (MiniGoParser.NIL - 18)) | (1 << (MiniGoParser.TRUE - 18)) | (1 << (MiniGoParser.FALSE - 18)) | (1 << (MiniGoParser.GET_INT - 18)) | (1 << (MiniGoParser.PUT_INT - 18)) | (1 << (MiniGoParser.PUT_INT_LN - 18)) | (1 << (MiniGoParser.GET_FLOAT - 18)) | (1 << (MiniGoParser.PUT_FLOAT - 18)) | (1 << (MiniGoParser.PUT_FLOAT_LN - 18)) | (1 << (MiniGoParser.GET_BOOL - 18)) | (1 << (MiniGoParser.PUT_BOOL - 18)) | (1 << (MiniGoParser.PUT_BOOL_LN - 18)) | (1 << (MiniGoParser.GET_STRING - 18)) | (1 << (MiniGoParser.PUT_STRING - 18)) | (1 << (MiniGoParser.PUT_STRING_LN - 18)) | (1 << (MiniGoParser.PUT_LN - 18)) | (1 << (MiniGoParser.ID - 18)) | (1 << (MiniGoParser.SUB - 18)) | (1 << (MiniGoParser.NOT - 18)) | (1 << (MiniGoParser.LPAREN - 18)) | (1 << (MiniGoParser.LBRACKET - 18)) | (1 << (MiniGoParser.INT_LIT - 18)) | (1 << (MiniGoParser.HEX_LIT - 18)) | (1 << (MiniGoParser.OCT_LIT - 18)) | (1 << (MiniGoParser.BIN_LIT - 18)) | (1 << (MiniGoParser.FLOAT_LIT - 18)) | (1 << (MiniGoParser.STRING_LIT - 18)))) != 0):
                self.state = 654
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
            self.state = 657
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
            self.state = 659
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
            self.state = 661
            self.match(MiniGoParser.VAR)
            self.state = 662
            self.match(MiniGoParser.ID)
            self.state = 665
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 663
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 664
                self.compositeType()
                pass
            elif token in [MiniGoParser.ASSIGN]:
                pass
            else:
                pass
            self.state = 667
            self.match(MiniGoParser.ASSIGN)
            self.state = 668
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
            self.state = 670
            self.match(MiniGoParser.VAR)
            self.state = 671
            self.match(MiniGoParser.ID)
            self.state = 674
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 672
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 673
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
            self.state = 676
            self.match(MiniGoParser.CONST)
            self.state = 677
            self.match(MiniGoParser.ID)
            self.state = 678
            self.match(MiniGoParser.ASSIGN)
            self.state = 679
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
            self.state = 684
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 681
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 682
                self.compositeType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 683
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
            self.state = 686
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

        def array_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_access_tailContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


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
            self.state = 688
            self.array_access_tail()
            self.state = 689
            self.types()
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
            self.state = 691
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

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def array_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_initContext,0)


        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def compositeType(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeTypeContext,0)


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
            self.state = 693
            self.match(MiniGoParser.VAR)
            self.state = 694
            self.match(MiniGoParser.ID)
            self.state = 695
            self.dimensions()
            self.state = 698
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 696
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 697
                self.compositeType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 700
            self.match(MiniGoParser.ASSIGN)
            self.state = 701
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

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def compositeType(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeTypeContext,0)


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
            self.state = 703
            self.match(MiniGoParser.VAR)
            self.state = 704
            self.match(MiniGoParser.ID)
            self.state = 705
            self.dimensions()
            self.state = 708
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 706
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 707
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
            self.state = 710
            self.match(MiniGoParser.LBRACKET)
            self.state = 713
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT]:
                self.state = 711
                self.int_number()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 712
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 715
            self.match(MiniGoParser.RBRACKET)
            self.state = 717
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 716
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
            self.state = 721
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 719
                self.array_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 720
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
            self.state = 723
            self.match(MiniGoParser.TYPE)
            self.state = 724
            self.match(MiniGoParser.ID)
            self.state = 725
            self.match(MiniGoParser.STRUCT)
            self.state = 726
            self.match(MiniGoParser.LBRACE)
            self.state = 728
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 727
                self.newlines(0)


            self.state = 730
            self.field_decl_list()
            self.state = 731
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

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def field_decl_list(self):
            return self.getTypedRuleContext(MiniGoParser.Field_decl_listContext,0)


        def field_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Field_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


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
            self.state = 741
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TYPE, MiniGoParser.ID]:
                self.state = 736
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 733
                    self.field_decl()
                    pass

                elif la_ == 2:
                    self.state = 734
                    self.struct_decl()
                    pass

                elif la_ == 3:
                    self.state = 735
                    self.interface_decl()
                    pass


                self.state = 738
                self.eos()
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 740
                self.match(MiniGoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 744
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TYPE) | (1 << MiniGoParser.NEWLINE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 743
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
            self.state = 746
            self.match(MiniGoParser.ID)
            self.state = 747
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
            self.state = 749
            self.match(MiniGoParser.TYPE)
            self.state = 750
            self.match(MiniGoParser.ID)
            self.state = 751
            self.match(MiniGoParser.INTERFACE)
            self.state = 752
            self.match(MiniGoParser.LBRACE)
            self.state = 754
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 753
                self.newlines(0)


            self.state = 756
            self.method_in_decl()
            self.state = 757
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
            self.state = 770
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 759
                self.match(MiniGoParser.ID)
                self.state = 760
                self.match(MiniGoParser.LPAREN)
                self.state = 762
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 761
                    self.param_decl()


                self.state = 764
                self.match(MiniGoParser.RPAREN)
                self.state = 766
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                    self.state = 765
                    self.types()


                self.state = 768
                self.eos()
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 769
                self.match(MiniGoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 773
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE or _la==MiniGoParser.ID:
                self.state = 772
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
            self.state = 775
            self.match(MiniGoParser.ID)
            self.state = 776
            self.param_decl_tail()
            self.state = 777
            self.types()
            self.state = 781
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 779
                self.match(MiniGoParser.COMMA)
                self.state = 780
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 786
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 783
                self.match(MiniGoParser.COMMA)
                self.state = 784
                self.match(MiniGoParser.ID)
                self.state = 785
                self.param_decl_tail()


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
            self.state = 788
            self.expr()
            self.state = 791
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 789
                self.match(MiniGoParser.COMMA)
                self.state = 790
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


        def built_in_function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Built_in_function_callContext,0)


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
            self.state = 800
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 793
                self.match(MiniGoParser.ID)
                self.state = 794
                self.match(MiniGoParser.LPAREN)
                self.state = 796
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & ((1 << (MiniGoParser.NIL - 18)) | (1 << (MiniGoParser.TRUE - 18)) | (1 << (MiniGoParser.FALSE - 18)) | (1 << (MiniGoParser.GET_INT - 18)) | (1 << (MiniGoParser.PUT_INT - 18)) | (1 << (MiniGoParser.PUT_INT_LN - 18)) | (1 << (MiniGoParser.GET_FLOAT - 18)) | (1 << (MiniGoParser.PUT_FLOAT - 18)) | (1 << (MiniGoParser.PUT_FLOAT_LN - 18)) | (1 << (MiniGoParser.GET_BOOL - 18)) | (1 << (MiniGoParser.PUT_BOOL - 18)) | (1 << (MiniGoParser.PUT_BOOL_LN - 18)) | (1 << (MiniGoParser.GET_STRING - 18)) | (1 << (MiniGoParser.PUT_STRING - 18)) | (1 << (MiniGoParser.PUT_STRING_LN - 18)) | (1 << (MiniGoParser.PUT_LN - 18)) | (1 << (MiniGoParser.ID - 18)) | (1 << (MiniGoParser.SUB - 18)) | (1 << (MiniGoParser.NOT - 18)) | (1 << (MiniGoParser.LPAREN - 18)) | (1 << (MiniGoParser.LBRACKET - 18)) | (1 << (MiniGoParser.INT_LIT - 18)) | (1 << (MiniGoParser.HEX_LIT - 18)) | (1 << (MiniGoParser.OCT_LIT - 18)) | (1 << (MiniGoParser.BIN_LIT - 18)) | (1 << (MiniGoParser.FLOAT_LIT - 18)) | (1 << (MiniGoParser.STRING_LIT - 18)))) != 0):
                    self.state = 795
                    self.param_call_list()


                self.state = 798
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_INT, MiniGoParser.PUT_INT, MiniGoParser.PUT_INT_LN, MiniGoParser.GET_FLOAT, MiniGoParser.PUT_FLOAT, MiniGoParser.PUT_FLOAT_LN, MiniGoParser.GET_BOOL, MiniGoParser.PUT_BOOL, MiniGoParser.PUT_BOOL_LN, MiniGoParser.GET_STRING, MiniGoParser.PUT_STRING, MiniGoParser.PUT_STRING_LN, MiniGoParser.PUT_LN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 799
                self.built_in_function_call()
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
            self.state = 802
            self.match(MiniGoParser.FUNC)
            self.state = 803
            self.match(MiniGoParser.ID)
            self.state = 804
            self.match(MiniGoParser.LPAREN)
            self.state = 806
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 805
                self.param_decl()


            self.state = 808
            self.match(MiniGoParser.RPAREN)
            self.state = 810
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                self.state = 809
                self.types()


            self.state = 812
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
            self.state = 814
            self.match(MiniGoParser.FUNC)
            self.state = 815
            self.match(MiniGoParser.LPAREN)
            self.state = 816
            self.match(MiniGoParser.ID)
            self.state = 817
            self.compositeType()
            self.state = 818
            self.match(MiniGoParser.RPAREN)
            self.state = 819
            self.match(MiniGoParser.ID)
            self.state = 820
            self.match(MiniGoParser.LPAREN)
            self.state = 822
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 821
                self.param_decl()


            self.state = 824
            self.match(MiniGoParser.RPAREN)
            self.state = 826
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                self.state = 825
                self.types()


            self.state = 828
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
            self.state = 830
            self.match(MiniGoParser.LBRACE)
            self.state = 832
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 831
                self.match(MiniGoParser.NEWLINE)


            self.state = 834
            self.stmt_list(0)
            self.state = 835
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Built_in_function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_built_in_function_call

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PutIntLnCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_INT_LN(self):
            return self.getToken(MiniGoParser.PUT_INT_LN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutIntLnCall" ):
                return visitor.visitPutIntLnCall(self)
            else:
                return visitor.visitChildren(self)


    class PutFloatCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_FLOAT(self):
            return self.getToken(MiniGoParser.PUT_FLOAT, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutFloatCall" ):
                return visitor.visitPutFloatCall(self)
            else:
                return visitor.visitChildren(self)


    class PutFloatLnCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_FLOAT_LN(self):
            return self.getToken(MiniGoParser.PUT_FLOAT_LN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutFloatLnCall" ):
                return visitor.visitPutFloatLnCall(self)
            else:
                return visitor.visitChildren(self)


    class PutStringLnCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_STRING_LN(self):
            return self.getToken(MiniGoParser.PUT_STRING_LN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutStringLnCall" ):
                return visitor.visitPutStringLnCall(self)
            else:
                return visitor.visitChildren(self)


    class PutBoolCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_BOOL(self):
            return self.getToken(MiniGoParser.PUT_BOOL, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutBoolCall" ):
                return visitor.visitPutBoolCall(self)
            else:
                return visitor.visitChildren(self)


    class GetStringCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GET_STRING(self):
            return self.getToken(MiniGoParser.GET_STRING, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetStringCall" ):
                return visitor.visitGetStringCall(self)
            else:
                return visitor.visitChildren(self)


    class GetIntCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GET_INT(self):
            return self.getToken(MiniGoParser.GET_INT, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetIntCall" ):
                return visitor.visitGetIntCall(self)
            else:
                return visitor.visitChildren(self)


    class PutLnCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_LN(self):
            return self.getToken(MiniGoParser.PUT_LN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutLnCall" ):
                return visitor.visitPutLnCall(self)
            else:
                return visitor.visitChildren(self)


    class PutStringCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_STRING(self):
            return self.getToken(MiniGoParser.PUT_STRING, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutStringCall" ):
                return visitor.visitPutStringCall(self)
            else:
                return visitor.visitChildren(self)


    class GetBoolCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GET_BOOL(self):
            return self.getToken(MiniGoParser.GET_BOOL, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetBoolCall" ):
                return visitor.visitGetBoolCall(self)
            else:
                return visitor.visitChildren(self)


    class PutBoolLnCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_BOOL_LN(self):
            return self.getToken(MiniGoParser.PUT_BOOL_LN, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutBoolLnCall" ):
                return visitor.visitPutBoolLnCall(self)
            else:
                return visitor.visitChildren(self)


    class GetFloatCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GET_FLOAT(self):
            return self.getToken(MiniGoParser.GET_FLOAT, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetFloatCall" ):
                return visitor.visitGetFloatCall(self)
            else:
                return visitor.visitChildren(self)


    class PutIntCallContext(Built_in_function_callContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Built_in_function_callContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUT_INT(self):
            return self.getToken(MiniGoParser.PUT_INT, 0)
        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPutIntCall" ):
                return visitor.visitPutIntCall(self)
            else:
                return visitor.visitChildren(self)



    def built_in_function_call(self):

        localctx = MiniGoParser.Built_in_function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_built_in_function_call)
        try:
            self.state = 892
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.GET_INT]:
                localctx = MiniGoParser.GetIntCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 837
                self.match(MiniGoParser.GET_INT)
                self.state = 838
                self.match(MiniGoParser.LPAREN)
                self.state = 839
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_INT]:
                localctx = MiniGoParser.PutIntCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 840
                self.match(MiniGoParser.PUT_INT)
                self.state = 841
                self.match(MiniGoParser.LPAREN)
                self.state = 842
                self.expr()
                self.state = 843
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_INT_LN]:
                localctx = MiniGoParser.PutIntLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 845
                self.match(MiniGoParser.PUT_INT_LN)
                self.state = 846
                self.match(MiniGoParser.LPAREN)
                self.state = 847
                self.expr()
                self.state = 848
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_FLOAT]:
                localctx = MiniGoParser.GetFloatCallContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 850
                self.match(MiniGoParser.GET_FLOAT)
                self.state = 851
                self.match(MiniGoParser.LPAREN)
                self.state = 852
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_FLOAT]:
                localctx = MiniGoParser.PutFloatCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 853
                self.match(MiniGoParser.PUT_FLOAT)
                self.state = 854
                self.match(MiniGoParser.LPAREN)
                self.state = 855
                self.expr()
                self.state = 856
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_FLOAT_LN]:
                localctx = MiniGoParser.PutFloatLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 858
                self.match(MiniGoParser.PUT_FLOAT_LN)
                self.state = 859
                self.match(MiniGoParser.LPAREN)
                self.state = 860
                self.expr()
                self.state = 861
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_BOOL]:
                localctx = MiniGoParser.GetBoolCallContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 863
                self.match(MiniGoParser.GET_BOOL)
                self.state = 864
                self.match(MiniGoParser.LPAREN)
                self.state = 865
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_BOOL]:
                localctx = MiniGoParser.PutBoolCallContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 866
                self.match(MiniGoParser.PUT_BOOL)
                self.state = 867
                self.match(MiniGoParser.LPAREN)
                self.state = 868
                self.expr()
                self.state = 869
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_BOOL_LN]:
                localctx = MiniGoParser.PutBoolLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 871
                self.match(MiniGoParser.PUT_BOOL_LN)
                self.state = 872
                self.match(MiniGoParser.LPAREN)
                self.state = 873
                self.expr()
                self.state = 874
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_STRING]:
                localctx = MiniGoParser.GetStringCallContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 876
                self.match(MiniGoParser.GET_STRING)
                self.state = 877
                self.match(MiniGoParser.LPAREN)
                self.state = 878
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_STRING]:
                localctx = MiniGoParser.PutStringCallContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 879
                self.match(MiniGoParser.PUT_STRING)
                self.state = 880
                self.match(MiniGoParser.LPAREN)
                self.state = 881
                self.expr()
                self.state = 882
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_STRING_LN]:
                localctx = MiniGoParser.PutStringLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 884
                self.match(MiniGoParser.PUT_STRING_LN)
                self.state = 885
                self.match(MiniGoParser.LPAREN)
                self.state = 886
                self.expr()
                self.state = 887
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_LN]:
                localctx = MiniGoParser.PutLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 889
                self.match(MiniGoParser.PUT_LN)
                self.state = 890
                self.match(MiniGoParser.LPAREN)
                self.state = 891
                self.match(MiniGoParser.RPAREN)
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
         




