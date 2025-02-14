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
        buf.write("\u036e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\5\3\u00af\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u00b8\n\4\f\4\16\4\u00bb\13\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u00c5\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\7\6\u00ce\n\6\f\6\16\6\u00d1\13\6\3\7\3\7\5\7\u00d5")
        buf.write("\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00df\n\t\f\t")
        buf.write("\16\t\u00e2\13\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00ea\n\n")
        buf.write("\f\n\16\n\u00ed\13\n\3\13\3\13\3\13\3\13\3\13\3\13\7\13")
        buf.write("\u00f5\n\13\f\13\16\13\u00f8\13\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\7\f\u0100\n\f\f\f\16\f\u0103\13\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\7\r\u010b\n\r\f\r\16\r\u010e\13\r\3\16\3\16\3")
        buf.write("\16\5\16\u0113\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u011d\n\17\7\17\u011f\n\17\f\17\16\17\u0122")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u012c")
        buf.write("\n\20\f\20\16\20\u012f\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u013d\n\21\3")
        buf.write("\22\3\22\3\22\3\22\3\22\5\22\u0144\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u014e\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\25\5\25\u0158\n\25\3\25\3\25")
        buf.write("\3\25\5\25\u015d\n\25\3\26\3\26\5\26\u0161\n\26\3\27\3")
        buf.write("\27\3\30\3\30\5\30\u0167\n\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u0170\n\32\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\7\34\u017a\n\34\f\34\16\34\u017d\13\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\7\35\u0185\n\35\f\35\16\35")
        buf.write("\u0188\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0190")
        buf.write("\n\36\f\36\16\36\u0193\13\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u019b\n\37\f\37\16\37\u019e\13\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \7 \u01a6\n \f \16 \u01a9\13 \3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u01b9\n!\3\"\3\"\3\"\5")
        buf.write("\"\u01be\n\"\3#\3#\3#\3#\3#\5#\u01c5\n#\3$\3$\3$\5$\u01ca")
        buf.write("\n$\3$\3$\3%\3%\3%\3%\5%\u01d2\n%\3&\3&\3&\3&\3&\3\'\3")
        buf.write("\'\3\'\5\'\u01dc\n\'\3(\3(\3(\3(\5(\u01e2\n(\3)\3)\3)")
        buf.write("\3)\3*\3*\3*\3*\3*\5*\u01ed\n*\3+\3+\3+\3+\5+\u01f3\n")
        buf.write("+\3+\3+\3+\3+\3+\5+\u01fa\n+\7+\u01fc\n+\f+\16+\u01ff")
        buf.write("\13+\3,\3,\3,\3,\5,\u0205\n,\3-\3-\3-\5-\u020a\n-\3-\3")
        buf.write("-\3-\3-\5-\u0210\n-\7-\u0212\n-\f-\16-\u0215\13-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0225\n.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3/\7/\u0230\n/\f/\16/\u0233\13/\3")
        buf.write("\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u0243\n\63\3\64\3\64\3\64\5\64\u0248")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\5\65\u024f\n\65\3\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u025a\n\66")
        buf.write("\3\66\3\66\3\66\5\66\u025f\n\66\3\66\3\66\5\66\u0263\n")
        buf.write("\66\3\66\5\66\u0266\n\66\5\66\u0268\n\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u027f\n\67\3")
        buf.write("8\38\58\u0283\n8\39\39\3:\3:\3;\3;\5;\u028b\n;\3<\3<\3")
        buf.write("=\3=\3>\3>\3>\5>\u0294\n>\3>\3>\3>\3?\3?\3?\3?\3@\3@\3")
        buf.write("@\3@\3@\3A\3A\3A\5A\u02a5\nA\3B\3B\3C\3C\3C\3D\3D\3E\3")
        buf.write("E\3E\3E\3E\5E\u02b3\nE\3E\3E\5E\u02b7\nE\3F\3F\3F\3F\5")
        buf.write("F\u02bd\nF\3G\3G\5G\u02c1\nG\3H\3H\3H\3H\3H\5H\u02c8\n")
        buf.write("H\3H\3H\3H\3I\3I\3I\5I\u02d0\nI\3I\3I\3I\5I\u02d5\nI\3")
        buf.write("I\5I\u02d8\nI\3J\3J\3J\3K\3K\3K\3K\3K\5K\u02e2\nK\3K\3")
        buf.write("K\3K\3L\3L\3L\5L\u02ea\nL\3L\3L\5L\u02ee\nL\3L\3L\5L\u02f2")
        buf.write("\nL\3L\5L\u02f5\nL\3M\3M\3M\3M\3M\3M\5M\u02fd\nM\3N\3")
        buf.write("N\3N\5N\u0302\nN\3O\3O\3O\5O\u0307\nO\3P\3P\3P\5P\u030c")
        buf.write("\nP\3P\3P\5P\u0310\nP\3Q\3Q\3Q\3Q\5Q\u0316\nQ\3Q\3Q\5")
        buf.write("Q\u031a\nQ\3Q\3Q\3R\3R\3R\3R\3R\3R\3R\3R\5R\u0326\nR\3")
        buf.write("R\3R\5R\u032a\nR\3R\3R\3S\3S\5S\u0330\nS\3S\3S\3S\3T\3")
        buf.write("T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3")
        buf.write("T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3")
        buf.write("T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\5")
        buf.write("T\u036c\nT\3T\2\23\6\n\20\22\24\26\30\34\36\668:<>TX\\")
        buf.write("U\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write("\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6")
        buf.write("\2\n\3\2+\60\3\2&\'\3\2(*\3\2EH\3\2\61\62\3\2\65:\3\2")
        buf.write("\64\65\3\2\13\16\2\u03ac\2\u00a8\3\2\2\2\4\u00ae\3\2\2")
        buf.write("\2\6\u00b0\3\2\2\2\b\u00c4\3\2\2\2\n\u00c8\3\2\2\2\f\u00d4")
        buf.write("\3\2\2\2\16\u00d6\3\2\2\2\20\u00d8\3\2\2\2\22\u00e3\3")
        buf.write("\2\2\2\24\u00ee\3\2\2\2\26\u00f9\3\2\2\2\30\u0104\3\2")
        buf.write("\2\2\32\u010f\3\2\2\2\34\u0114\3\2\2\2\36\u0123\3\2\2")
        buf.write("\2 \u013c\3\2\2\2\"\u0143\3\2\2\2$\u014d\3\2\2\2&\u014f")
        buf.write("\3\2\2\2(\u015c\3\2\2\2*\u0160\3\2\2\2,\u0162\3\2\2\2")
        buf.write(".\u0166\3\2\2\2\60\u0168\3\2\2\2\62\u016b\3\2\2\2\64\u0171")
        buf.write("\3\2\2\2\66\u0173\3\2\2\28\u017e\3\2\2\2:\u0189\3\2\2")
        buf.write("\2<\u0194\3\2\2\2>\u019f\3\2\2\2@\u01b8\3\2\2\2B\u01bd")
        buf.write("\3\2\2\2D\u01c4\3\2\2\2F\u01c6\3\2\2\2H\u01cd\3\2\2\2")
        buf.write("J\u01d3\3\2\2\2L\u01db\3\2\2\2N\u01e1\3\2\2\2P\u01e3\3")
        buf.write("\2\2\2R\u01e7\3\2\2\2T\u01f2\3\2\2\2V\u0200\3\2\2\2X\u0209")
        buf.write("\3\2\2\2Z\u0224\3\2\2\2\\\u0228\3\2\2\2^\u0234\3\2\2\2")
        buf.write("`\u0238\3\2\2\2b\u023c\3\2\2\2d\u023e\3\2\2\2f\u0247\3")
        buf.write("\2\2\2h\u0249\3\2\2\2j\u0267\3\2\2\2l\u027e\3\2\2\2n\u0282")
        buf.write("\3\2\2\2p\u0284\3\2\2\2r\u0286\3\2\2\2t\u0288\3\2\2\2")
        buf.write("v\u028c\3\2\2\2x\u028e\3\2\2\2z\u0290\3\2\2\2|\u0298\3")
        buf.write("\2\2\2~\u029c\3\2\2\2\u0080\u02a4\3\2\2\2\u0082\u02a6")
        buf.write("\3\2\2\2\u0084\u02a8\3\2\2\2\u0086\u02ab\3\2\2\2\u0088")
        buf.write("\u02ad\3\2\2\2\u008a\u02b8\3\2\2\2\u008c\u02c0\3\2\2\2")
        buf.write("\u008e\u02c2\3\2\2\2\u0090\u02d4\3\2\2\2\u0092\u02d9\3")
        buf.write("\2\2\2\u0094\u02dc\3\2\2\2\u0096\u02f1\3\2\2\2\u0098\u02f6")
        buf.write("\3\2\2\2\u009a\u0301\3\2\2\2\u009c\u0303\3\2\2\2\u009e")
        buf.write("\u030f\3\2\2\2\u00a0\u0311\3\2\2\2\u00a2\u031d\3\2\2\2")
        buf.write("\u00a4\u032d\3\2\2\2\u00a6\u036b\3\2\2\2\u00a8\u00a9\5")
        buf.write("\4\3\2\u00a9\u00aa\7\2\2\3\u00aa\3\3\2\2\2\u00ab\u00ac")
        buf.write("\7$\2\2\u00ac\u00af\5\4\3\2\u00ad\u00af\5\6\4\2\u00ae")
        buf.write("\u00ab\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\5\3\2\2\2\u00b0")
        buf.write("\u00b1\b\4\1\2\u00b1\u00b2\5\b\5\2\u00b2\u00b9\3\2\2\2")
        buf.write("\u00b3\u00b4\f\4\2\2\u00b4\u00b8\7$\2\2\u00b5\u00b6\f")
        buf.write("\3\2\2\u00b6\u00b8\5\b\5\2\u00b7\u00b3\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\7\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc")
        buf.write("\u00c5\5\u008eH\2\u00bd\u00c5\5\u0094K\2\u00be\u00c5\5")
        buf.write("~@\2\u00bf\u00c5\5z>\2\u00c0\u00c5\5\u0088E\2\u00c1\u00c5")
        buf.write("\5|?\2\u00c2\u00c5\5\u00a0Q\2\u00c3\u00c5\5\u00a2R\2\u00c4")
        buf.write("\u00bc\3\2\2\2\u00c4\u00bd\3\2\2\2\u00c4\u00be\3\2\2\2")
        buf.write("\u00c4\u00bf\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c4\u00c1\3")
        buf.write("\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\u00c7\5\f\7\2\u00c7\t\3\2\2\2\u00c8\u00c9")
        buf.write("\b\6\1\2\u00c9\u00ca\7$\2\2\u00ca\u00cf\3\2\2\2\u00cb")
        buf.write("\u00cc\f\3\2\2\u00cc\u00ce\7$\2\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3")
        buf.write("\2\2\2\u00d0\13\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d5")
        buf.write("\7=\2\2\u00d3\u00d5\5\n\6\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\r\3\2\2\2\u00d6\u00d7\5\20\t\2\u00d7")
        buf.write("\17\3\2\2\2\u00d8\u00d9\b\t\1\2\u00d9\u00da\5\22\n\2\u00da")
        buf.write("\u00e0\3\2\2\2\u00db\u00dc\f\4\2\2\u00dc\u00dd\7\62\2")
        buf.write("\2\u00dd\u00df\5\22\n\2\u00de\u00db\3\2\2\2\u00df\u00e2")
        buf.write("\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("\21\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\b\n\1\2\u00e4")
        buf.write("\u00e5\5\24\13\2\u00e5\u00eb\3\2\2\2\u00e6\u00e7\f\4\2")
        buf.write("\2\u00e7\u00e8\7\61\2\2\u00e8\u00ea\5\24\13\2\u00e9\u00e6")
        buf.write("\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\23\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee")
        buf.write("\u00ef\b\13\1\2\u00ef\u00f0\5\26\f\2\u00f0\u00f6\3\2\2")
        buf.write("\2\u00f1\u00f2\f\4\2\2\u00f2\u00f3\t\2\2\2\u00f3\u00f5")
        buf.write("\5\26\f\2\u00f4\u00f1\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\25\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f9\u00fa\b\f\1\2\u00fa\u00fb\5\30\r")
        buf.write("\2\u00fb\u0101\3\2\2\2\u00fc\u00fd\f\4\2\2\u00fd\u00fe")
        buf.write("\t\3\2\2\u00fe\u0100\5\30\r\2\u00ff\u00fc\3\2\2\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\27\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\b\r")
        buf.write("\1\2\u0105\u0106\5\32\16\2\u0106\u010c\3\2\2\2\u0107\u0108")
        buf.write("\f\4\2\2\u0108\u0109\t\4\2\2\u0109\u010b\5\32\16\2\u010a")
        buf.write("\u0107\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010d\3\2\2\2\u010d\31\3\2\2\2\u010e\u010c\3\2")
        buf.write("\2\2\u010f\u0112\5D#\2\u0110\u0113\5\34\17\2\u0111\u0113")
        buf.write("\5\36\20\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113")
        buf.write("\33\3\2\2\2\u0114\u0115\b\17\1\2\u0115\u0116\5\36\20\2")
        buf.write("\u0116\u0120\3\2\2\2\u0117\u0118\f\4\2\2\u0118\u011c\7")
        buf.write(";\2\2\u0119\u011d\7%\2\2\u011a\u011d\5\u009eP\2\u011b")
        buf.write("\u011d\5\60\31\2\u011c\u0119\3\2\2\2\u011c\u011a\3\2\2")
        buf.write("\2\u011c\u011b\3\2\2\2\u011d\u011f\3\2\2\2\u011e\u0117")
        buf.write("\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\35\3\2\2\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u0124\b\20\1\2\u0124\u0125\5 \21\2\u0125\u012d\3\2\2")
        buf.write("\2\u0126\u0127\f\4\2\2\u0127\u0128\7C\2\2\u0128\u0129")
        buf.write("\5\64\33\2\u0129\u012a\7D\2\2\u012a\u012c\3\2\2\2\u012b")
        buf.write("\u0126\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\37\3\2\2\2\u012f\u012d\3\2")
        buf.write("\2\2\u0130\u013d\5\"\22\2\u0131\u0132\7?\2\2\u0132\u0133")
        buf.write("\5\16\b\2\u0133\u0134\7@\2\2\u0134\u013d\3\2\2\2\u0135")
        buf.write("\u013d\7%\2\2\u0136\u013d\5\u009eP\2\u0137\u013d\5F$\2")
        buf.write("\u0138\u013d\5J&\2\u0139\u013d\5R*\2\u013a\u013d\5V,\2")
        buf.write("\u013b\u013d\5\60\31\2\u013c\u0130\3\2\2\2\u013c\u0131")
        buf.write("\3\2\2\2\u013c\u0135\3\2\2\2\u013c\u0136\3\2\2\2\u013c")
        buf.write("\u0137\3\2\2\2\u013c\u0138\3\2\2\2\u013c\u0139\3\2\2\2")
        buf.write("\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013d!\3\2\2")
        buf.write("\2\u013e\u0144\5.\30\2\u013f\u0144\7\25\2\2\u0140\u0144")
        buf.write("\7\26\2\2\u0141\u0144\7\24\2\2\u0142\u0144\7K\2\2\u0143")
        buf.write("\u013e\3\2\2\2\u0143\u013f\3\2\2\2\u0143\u0140\3\2\2\2")
        buf.write("\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144#\3\2\2")
        buf.write("\2\u0145\u014e\5,\27\2\u0146\u014e\7I\2\2\u0147\u014e")
        buf.write("\7K\2\2\u0148\u014e\7\25\2\2\u0149\u014e\7\26\2\2\u014a")
        buf.write("\u014e\7\24\2\2\u014b\u014e\5J&\2\u014c\u014e\7%\2\2\u014d")
        buf.write("\u0145\3\2\2\2\u014d\u0146\3\2\2\2\u014d\u0147\3\2\2\2")
        buf.write("\u014d\u0148\3\2\2\2\u014d\u0149\3\2\2\2\u014d\u014a\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2\u014e%")
        buf.write("\3\2\2\2\u014f\u0150\7A\2\2\u0150\u0151\5(\25\2\u0151")
        buf.write("\u0152\7B\2\2\u0152\'\3\2\2\2\u0153\u015d\5$\23\2\u0154")
        buf.write("\u015d\5&\24\2\u0155\u0158\5$\23\2\u0156\u0158\5&\24\2")
        buf.write("\u0157\u0155\3\2\2\2\u0157\u0156\3\2\2\2\u0158\u0159\3")
        buf.write("\2\2\2\u0159\u015a\7<\2\2\u015a\u015b\5(\25\2\u015b\u015d")
        buf.write("\3\2\2\2\u015c\u0153\3\2\2\2\u015c\u0154\3\2\2\2\u015c")
        buf.write("\u0157\3\2\2\2\u015d)\3\2\2\2\u015e\u0161\5F$\2\u015f")
        buf.write("\u0161\5J&\2\u0160\u015e\3\2\2\2\u0160\u015f\3\2\2\2\u0161")
        buf.write("+\3\2\2\2\u0162\u0163\t\5\2\2\u0163-\3\2\2\2\u0164\u0167")
        buf.write("\5,\27\2\u0165\u0167\7I\2\2\u0166\u0164\3\2\2\2\u0166")
        buf.write("\u0165\3\2\2\2\u0167/\3\2\2\2\u0168\u0169\5B\"\2\u0169")
        buf.write("\u016a\5\62\32\2\u016a\61\3\2\2\2\u016b\u016c\7C\2\2\u016c")
        buf.write("\u016d\5\64\33\2\u016d\u016f\7D\2\2\u016e\u0170\5\62\32")
        buf.write("\2\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2\2\u0170\63\3")
        buf.write("\2\2\2\u0171\u0172\5\66\34\2\u0172\65\3\2\2\2\u0173\u0174")
        buf.write("\b\34\1\2\u0174\u0175\58\35\2\u0175\u017b\3\2\2\2\u0176")
        buf.write("\u0177\f\4\2\2\u0177\u0178\7\62\2\2\u0178\u017a\58\35")
        buf.write("\2\u0179\u0176\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\67\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u017f\b\35\1\2\u017f\u0180\5:\36\2\u0180")
        buf.write("\u0186\3\2\2\2\u0181\u0182\f\4\2\2\u0182\u0183\t\6\2\2")
        buf.write("\u0183\u0185\5:\36\2\u0184\u0181\3\2\2\2\u0185\u0188\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u01879")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\b\36\1\2\u018a")
        buf.write("\u018b\5<\37\2\u018b\u0191\3\2\2\2\u018c\u018d\f\4\2\2")
        buf.write("\u018d\u018e\t\2\2\2\u018e\u0190\5<\37\2\u018f\u018c\3")
        buf.write("\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192")
        buf.write("\3\2\2\2\u0192;\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195")
        buf.write("\b\37\1\2\u0195\u0196\5> \2\u0196\u019c\3\2\2\2\u0197")
        buf.write("\u0198\f\4\2\2\u0198\u0199\t\3\2\2\u0199\u019b\5> \2\u019a")
        buf.write("\u0197\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019c\u019d\3\2\2\2\u019d=\3\2\2\2\u019e\u019c\3\2\2")
        buf.write("\2\u019f\u01a0\b \1\2\u01a0\u01a1\5@!\2\u01a1\u01a7\3")
        buf.write("\2\2\2\u01a2\u01a3\f\4\2\2\u01a3\u01a4\t\4\2\2\u01a4\u01a6")
        buf.write("\5@!\2\u01a5\u01a2\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8?\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01aa\u01b9\5B\"\2\u01ab\u01b9\5\60\31\2\u01ac")
        buf.write("\u01b9\5,\27\2\u01ad\u01ae\5D#\2\u01ae\u01af\5,\27\2\u01af")
        buf.write("\u01b9\3\2\2\2\u01b0\u01b1\7?\2\2\u01b1\u01b2\5\64\33")
        buf.write("\2\u01b2\u01b3\7@\2\2\u01b3\u01b9\3\2\2\2\u01b4\u01b9")
        buf.write("\5F$\2\u01b5\u01b9\5J&\2\u01b6\u01b9\5R*\2\u01b7\u01b9")
        buf.write("\5V,\2\u01b8\u01aa\3\2\2\2\u01b8\u01ab\3\2\2\2\u01b8\u01ac")
        buf.write("\3\2\2\2\u01b8\u01ad\3\2\2\2\u01b8\u01b0\3\2\2\2\u01b8")
        buf.write("\u01b4\3\2\2\2\u01b8\u01b5\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b7\3\2\2\2\u01b9A\3\2\2\2\u01ba\u01be\7%\2\2")
        buf.write("\u01bb\u01be\7K\2\2\u01bc\u01be\5\u009eP\2\u01bd\u01ba")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("C\3\2\2\2\u01bf\u01c5\3\2\2\2\u01c0\u01c1\7\'\2\2\u01c1")
        buf.write("\u01c5\5D#\2\u01c2\u01c3\7\63\2\2\u01c3\u01c5\5D#\2\u01c4")
        buf.write("\u01bf\3\2\2\2\u01c4\u01c0\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c5E\3\2\2\2\u01c6\u01c9\5H%\2\u01c7\u01ca\5\u0082")
        buf.write("B\2\u01c8\u01ca\5\u0086D\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\5&\24\2\u01cc")
        buf.write("G\3\2\2\2\u01cd\u01ce\7C\2\2\u01ce\u01cf\5\64\33\2\u01cf")
        buf.write("\u01d1\7D\2\2\u01d0\u01d2\5H%\2\u01d1\u01d0\3\2\2\2\u01d1")
        buf.write("\u01d2\3\2\2\2\u01d2I\3\2\2\2\u01d3\u01d4\7%\2\2\u01d4")
        buf.write("\u01d5\7A\2\2\u01d5\u01d6\5L\'\2\u01d6\u01d7\7B\2\2\u01d7")
        buf.write("K\3\2\2\2\u01d8\u01d9\5P)\2\u01d9\u01da\5N(\2\u01da\u01dc")
        buf.write("\3\2\2\2\u01db\u01d8\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc")
        buf.write("M\3\2\2\2\u01dd\u01de\7<\2\2\u01de\u01df\5P)\2\u01df\u01e0")
        buf.write("\5N(\2\u01e0\u01e2\3\2\2\2\u01e1\u01dd\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2O\3\2\2\2\u01e3\u01e4\7%\2\2\u01e4\u01e5")
        buf.write("\7>\2\2\u01e5\u01e6\5\16\b\2\u01e6Q\3\2\2\2\u01e7\u01e8")
        buf.write("\5T+\2\u01e8\u01ec\7;\2\2\u01e9\u01ed\7%\2\2\u01ea\u01ed")
        buf.write("\5\u009eP\2\u01eb\u01ed\5\60\31\2\u01ec\u01e9\3\2\2\2")
        buf.write("\u01ec\u01ea\3\2\2\2\u01ec\u01eb\3\2\2\2\u01edS\3\2\2")
        buf.write("\2\u01ee\u01ef\b+\1\2\u01ef\u01f3\7%\2\2\u01f0\u01f3\5")
        buf.write("\u009eP\2\u01f1\u01f3\5\60\31\2\u01f2\u01ee\3\2\2\2\u01f2")
        buf.write("\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01fd\3\2\2\2")
        buf.write("\u01f4\u01f5\f\6\2\2\u01f5\u01f9\7;\2\2\u01f6\u01fa\7")
        buf.write("%\2\2\u01f7\u01fa\5\u009eP\2\u01f8\u01fa\5\60\31\2\u01f9")
        buf.write("\u01f6\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01f8\3\2\2\2")
        buf.write("\u01fa\u01fc\3\2\2\2\u01fb\u01f4\3\2\2\2\u01fc\u01ff\3")
        buf.write("\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01feU")
        buf.write("\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0201\5X-\2\u0201\u0204")
        buf.write("\7;\2\2\u0202\u0205\7%\2\2\u0203\u0205\5\60\31\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0203\3\2\2\2\u0205W\3\2\2\2\u0206")
        buf.write("\u0207\b-\1\2\u0207\u020a\7%\2\2\u0208\u020a\5\60\31\2")
        buf.write("\u0209\u0206\3\2\2\2\u0209\u0208\3\2\2\2\u020a\u0213\3")
        buf.write("\2\2\2\u020b\u020c\f\5\2\2\u020c\u020f\7;\2\2\u020d\u0210")
        buf.write("\7%\2\2\u020e\u0210\5\60\31\2\u020f\u020d\3\2\2\2\u020f")
        buf.write("\u020e\3\2\2\2\u0210\u0212\3\2\2\2\u0211\u020b\3\2\2\2")
        buf.write("\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3")
        buf.write("\2\2\2\u0214Y\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0225")
        buf.write("\5\60\31\2\u0217\u0225\5R*\2\u0218\u0225\5V,\2\u0219\u0225")
        buf.write("\5~@\2\u021a\u0225\5z>\2\u021b\u0225\5\u0088E\2\u021c")
        buf.write("\u0225\5|?\2\u021d\u0225\5x=\2\u021e\u0225\5v<\2\u021f")
        buf.write("\u0225\5h\65\2\u0220\u0225\5l\67\2\u0221\u0225\5^\60\2")
        buf.write("\u0222\u0225\5\u009eP\2\u0223\u0225\5t;\2\u0224\u0216")
        buf.write("\3\2\2\2\u0224\u0217\3\2\2\2\u0224\u0218\3\2\2\2\u0224")
        buf.write("\u0219\3\2\2\2\u0224\u021a\3\2\2\2\u0224\u021b\3\2\2\2")
        buf.write("\u0224\u021c\3\2\2\2\u0224\u021d\3\2\2\2\u0224\u021e\3")
        buf.write("\2\2\2\u0224\u021f\3\2\2\2\u0224\u0220\3\2\2\2\u0224\u0221")
        buf.write("\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0223\3\2\2\2\u0225")
        buf.write("\u0226\3\2\2\2\u0226\u0227\5\f\7\2\u0227[\3\2\2\2\u0228")
        buf.write("\u0229\b/\1\2\u0229\u022a\5Z.\2\u022a\u0231\3\2\2\2\u022b")
        buf.write("\u022c\f\4\2\2\u022c\u0230\5Z.\2\u022d\u022e\f\3\2\2\u022e")
        buf.write("\u0230\7$\2\2\u022f\u022b\3\2\2\2\u022f\u022d\3\2\2\2")
        buf.write("\u0230\u0233\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3")
        buf.write("\2\2\2\u0232]\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0235")
        buf.write("\5f\64\2\u0235\u0236\5b\62\2\u0236\u0237\5\16\b\2\u0237")
        buf.write("_\3\2\2\2\u0238\u0239\7%\2\2\u0239\u023a\5b\62\2\u023a")
        buf.write("\u023b\5\16\b\2\u023ba\3\2\2\2\u023c\u023d\t\7\2\2\u023d")
        buf.write("c\3\2\2\2\u023e\u023f\5f\64\2\u023f\u0242\t\b\2\2\u0240")
        buf.write("\u0243\5\16\b\2\u0241\u0243\5J&\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0241\3\2\2\2\u0243e\3\2\2\2\u0244\u0248\7%\2\2")
        buf.write("\u0245\u0248\5\60\31\2\u0246\u0248\5V,\2\u0247\u0244\3")
        buf.write("\2\2\2\u0247\u0245\3\2\2\2\u0247\u0246\3\2\2\2\u0248g")
        buf.write("\3\2\2\2\u0249\u024a\7\3\2\2\u024a\u024b\7?\2\2\u024b")
        buf.write("\u024c\5\16\b\2\u024c\u024e\7@\2\2\u024d\u024f\5\n\6\2")
        buf.write("\u024e\u024d\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\3")
        buf.write("\2\2\2\u0250\u0251\5\u00a4S\2\u0251\u0252\5j\66\2\u0252")
        buf.write("i\3\2\2\2\u0253\u0254\7\4\2\2\u0254\u0255\7\3\2\2\u0255")
        buf.write("\u0256\7?\2\2\u0256\u0257\5\16\b\2\u0257\u0259\7@\2\2")
        buf.write("\u0258\u025a\5\n\6\2\u0259\u0258\3\2\2\2\u0259\u025a\3")
        buf.write("\2\2\2\u025a\u025b\3\2\2\2\u025b\u025c\5\u00a4S\2\u025c")
        buf.write("\u025d\5j\66\2\u025d\u025f\3\2\2\2\u025e\u0253\3\2\2\2")
        buf.write("\u025e\u025f\3\2\2\2\u025f\u0268\3\2\2\2\u0260\u0262\7")
        buf.write("\4\2\2\u0261\u0263\5\n\6\2\u0262\u0261\3\2\2\2\u0262\u0263")
        buf.write("\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0266\5\u00a4S\2\u0265")
        buf.write("\u0260\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0268\3\2\2\2")
        buf.write("\u0267\u025e\3\2\2\2\u0267\u0265\3\2\2\2\u0268k\3\2\2")
        buf.write("\2\u0269\u026a\7\5\2\2\u026a\u026b\5n8\2\u026b\u026c\7")
        buf.write("=\2\2\u026c\u026d\5\16\b\2\u026d\u026e\7=\2\2\u026e\u026f")
        buf.write("\5p9\2\u026f\u0270\5\u00a4S\2\u0270\u027f\3\2\2\2\u0271")
        buf.write("\u0272\7\5\2\2\u0272\u0273\7%\2\2\u0273\u0274\7<\2\2\u0274")
        buf.write("\u0275\7%\2\2\u0275\u0276\7\65\2\2\u0276\u0277\7\23\2")
        buf.write("\2\u0277\u0278\5 \21\2\u0278\u0279\5\u00a4S\2\u0279\u027f")
        buf.write("\3\2\2\2\u027a\u027b\7\5\2\2\u027b\u027c\5\16\b\2\u027c")
        buf.write("\u027d\5\u00a4S\2\u027d\u027f\3\2\2\2\u027e\u0269\3\2")
        buf.write("\2\2\u027e\u0271\3\2\2\2\u027e\u027a\3\2\2\2\u027fm\3")
        buf.write("\2\2\2\u0280\u0283\5z>\2\u0281\u0283\5`\61\2\u0282\u0280")
        buf.write("\3\2\2\2\u0282\u0281\3\2\2\2\u0283o\3\2\2\2\u0284\u0285")
        buf.write("\5`\61\2\u0285q\3\2\2\2\u0286\u0287\5\16\b\2\u0287s\3")
        buf.write("\2\2\2\u0288\u028a\7\6\2\2\u0289\u028b\5\16\b\2\u028a")
        buf.write("\u0289\3\2\2\2\u028a\u028b\3\2\2\2\u028bu\3\2\2\2\u028c")
        buf.write("\u028d\7\21\2\2\u028dw\3\2\2\2\u028e\u028f\7\22\2\2\u028f")
        buf.write("y\3\2\2\2\u0290\u0291\7\20\2\2\u0291\u0293\7%\2\2\u0292")
        buf.write("\u0294\5\u0080A\2\u0293\u0292\3\2\2\2\u0293\u0294\3\2")
        buf.write("\2\2\u0294\u0295\3\2\2\2\u0295\u0296\7\64\2\2\u0296\u0297")
        buf.write("\5\16\b\2\u0297{\3\2\2\2\u0298\u0299\7\20\2\2\u0299\u029a")
        buf.write("\7%\2\2\u029a\u029b\5\u0080A\2\u029b}\3\2\2\2\u029c\u029d")
        buf.write("\7\17\2\2\u029d\u029e\7%\2\2\u029e\u029f\7\64\2\2\u029f")
        buf.write("\u02a0\5\16\b\2\u02a0\177\3\2\2\2\u02a1\u02a5\5\u0082")
        buf.write("B\2\u02a2\u02a5\5\u0086D\2\u02a3\u02a5\5\u0084C\2\u02a4")
        buf.write("\u02a1\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4\u02a3\3\2\2\2")
        buf.write("\u02a5\u0081\3\2\2\2\u02a6\u02a7\t\t\2\2\u02a7\u0083\3")
        buf.write("\2\2\2\u02a8\u02a9\5\62\32\2\u02a9\u02aa\5\u0080A\2\u02aa")
        buf.write("\u0085\3\2\2\2\u02ab\u02ac\7%\2\2\u02ac\u0087\3\2\2\2")
        buf.write("\u02ad\u02ae\7\20\2\2\u02ae\u02af\7%\2\2\u02af\u02b2\5")
        buf.write("\u008aF\2\u02b0\u02b3\5\u0082B\2\u02b1\u02b3\5\u0086D")
        buf.write("\2\u02b2\u02b0\3\2\2\2\u02b2\u02b1\3\2\2\2\u02b3\u02b6")
        buf.write("\3\2\2\2\u02b4\u02b5\7\64\2\2\u02b5\u02b7\5\u008cG\2\u02b6")
        buf.write("\u02b4\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b7\u0089\3\2\2\2")
        buf.write("\u02b8\u02b9\7C\2\2\u02b9\u02ba\7E\2\2\u02ba\u02bc\7D")
        buf.write("\2\2\u02bb\u02bd\5\u008aF\2\u02bc\u02bb\3\2\2\2\u02bc")
        buf.write("\u02bd\3\2\2\2\u02bd\u008b\3\2\2\2\u02be\u02c1\5&\24\2")
        buf.write("\u02bf\u02c1\5\16\b\2\u02c0\u02be\3\2\2\2\u02c0\u02bf")
        buf.write("\3\2\2\2\u02c1\u008d\3\2\2\2\u02c2\u02c3\7\b\2\2\u02c3")
        buf.write("\u02c4\7%\2\2\u02c4\u02c5\7\t\2\2\u02c5\u02c7\7A\2\2\u02c6")
        buf.write("\u02c8\5\n\6\2\u02c7\u02c6\3\2\2\2\u02c7\u02c8\3\2\2\2")
        buf.write("\u02c8\u02c9\3\2\2\2\u02c9\u02ca\5\u0090I\2\u02ca\u02cb")
        buf.write("\7B\2\2\u02cb\u008f\3\2\2\2\u02cc\u02d0\5\u0092J\2\u02cd")
        buf.write("\u02d0\5\u008eH\2\u02ce\u02d0\5\u0094K\2\u02cf\u02cc\3")
        buf.write("\2\2\2\u02cf\u02cd\3\2\2\2\u02cf\u02ce\3\2\2\2\u02d0\u02d1")
        buf.write("\3\2\2\2\u02d1\u02d2\5\f\7\2\u02d2\u02d5\3\2\2\2\u02d3")
        buf.write("\u02d5\7$\2\2\u02d4\u02cf\3\2\2\2\u02d4\u02d3\3\2\2\2")
        buf.write("\u02d5\u02d7\3\2\2\2\u02d6\u02d8\5\u0090I\2\u02d7\u02d6")
        buf.write("\3\2\2\2\u02d7\u02d8\3\2\2\2\u02d8\u0091\3\2\2\2\u02d9")
        buf.write("\u02da\7%\2\2\u02da\u02db\5\u0080A\2\u02db\u0093\3\2\2")
        buf.write("\2\u02dc\u02dd\7\b\2\2\u02dd\u02de\7%\2\2\u02de\u02df")
        buf.write("\7\n\2\2\u02df\u02e1\7A\2\2\u02e0\u02e2\5\n\6\2\u02e1")
        buf.write("\u02e0\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2\u02e3\3\2\2\2")
        buf.write("\u02e3\u02e4\5\u0096L\2\u02e4\u02e5\7B\2\2\u02e5\u0095")
        buf.write("\3\2\2\2\u02e6\u02e7\7%\2\2\u02e7\u02e9\7?\2\2\u02e8\u02ea")
        buf.write("\5\u0098M\2\u02e9\u02e8\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea")
        buf.write("\u02eb\3\2\2\2\u02eb\u02ed\7@\2\2\u02ec\u02ee\5\u0080")
        buf.write("A\2\u02ed\u02ec\3\2\2\2\u02ed\u02ee\3\2\2\2\u02ee\u02ef")
        buf.write("\3\2\2\2\u02ef\u02f2\5\f\7\2\u02f0\u02f2\7$\2\2\u02f1")
        buf.write("\u02e6\3\2\2\2\u02f1\u02f0\3\2\2\2\u02f2\u02f4\3\2\2\2")
        buf.write("\u02f3\u02f5\5\u0096L\2\u02f4\u02f3\3\2\2\2\u02f4\u02f5")
        buf.write("\3\2\2\2\u02f5\u0097\3\2\2\2\u02f6\u02f7\7%\2\2\u02f7")
        buf.write("\u02f8\5\u009aN\2\u02f8\u02f9\5\u0080A\2\u02f9\u02fc\3")
        buf.write("\2\2\2\u02fa\u02fb\7<\2\2\u02fb\u02fd\5\u0098M\2\u02fc")
        buf.write("\u02fa\3\2\2\2\u02fc\u02fd\3\2\2\2\u02fd\u0099\3\2\2\2")
        buf.write("\u02fe\u02ff\7<\2\2\u02ff\u0300\7%\2\2\u0300\u0302\5\u009a")
        buf.write("N\2\u0301\u02fe\3\2\2\2\u0301\u0302\3\2\2\2\u0302\u009b")
        buf.write("\3\2\2\2\u0303\u0306\5\16\b\2\u0304\u0305\7<\2\2\u0305")
        buf.write("\u0307\5\u009cO\2\u0306\u0304\3\2\2\2\u0306\u0307\3\2")
        buf.write("\2\2\u0307\u009d\3\2\2\2\u0308\u0309\7%\2\2\u0309\u030b")
        buf.write("\7?\2\2\u030a\u030c\5\u009cO\2\u030b\u030a\3\2\2\2\u030b")
        buf.write("\u030c\3\2\2\2\u030c\u030d\3\2\2\2\u030d\u0310\7@\2\2")
        buf.write("\u030e\u0310\5\u00a6T\2\u030f\u0308\3\2\2\2\u030f\u030e")
        buf.write("\3\2\2\2\u0310\u009f\3\2\2\2\u0311\u0312\7\7\2\2\u0312")
        buf.write("\u0313\7%\2\2\u0313\u0315\7?\2\2\u0314\u0316\5\u0098M")
        buf.write("\2\u0315\u0314\3\2\2\2\u0315\u0316\3\2\2\2\u0316\u0317")
        buf.write("\3\2\2\2\u0317\u0319\7@\2\2\u0318\u031a\5\u0080A\2\u0319")
        buf.write("\u0318\3\2\2\2\u0319\u031a\3\2\2\2\u031a\u031b\3\2\2\2")
        buf.write("\u031b\u031c\5\u00a4S\2\u031c\u00a1\3\2\2\2\u031d\u031e")
        buf.write("\7\7\2\2\u031e\u031f\7?\2\2\u031f\u0320\7%\2\2\u0320\u0321")
        buf.write("\5\u0086D\2\u0321\u0322\7@\2\2\u0322\u0323\7%\2\2\u0323")
        buf.write("\u0325\7?\2\2\u0324\u0326\5\u0098M\2\u0325\u0324\3\2\2")
        buf.write("\2\u0325\u0326\3\2\2\2\u0326\u0327\3\2\2\2\u0327\u0329")
        buf.write("\7@\2\2\u0328\u032a\5\u0080A\2\u0329\u0328\3\2\2\2\u0329")
        buf.write("\u032a\3\2\2\2\u032a\u032b\3\2\2\2\u032b\u032c\5\u00a4")
        buf.write("S\2\u032c\u00a3\3\2\2\2\u032d\u032f\7A\2\2\u032e\u0330")
        buf.write("\7$\2\2\u032f\u032e\3\2\2\2\u032f\u0330\3\2\2\2\u0330")
        buf.write("\u0331\3\2\2\2\u0331\u0332\5\\/\2\u0332\u0333\7B\2\2\u0333")
        buf.write("\u00a5\3\2\2\2\u0334\u0335\7\27\2\2\u0335\u0336\7?\2\2")
        buf.write("\u0336\u036c\7@\2\2\u0337\u0338\7\30\2\2\u0338\u0339\7")
        buf.write("?\2\2\u0339\u033a\5\16\b\2\u033a\u033b\7@\2\2\u033b\u036c")
        buf.write("\3\2\2\2\u033c\u033d\7\31\2\2\u033d\u033e\7?\2\2\u033e")
        buf.write("\u033f\5\16\b\2\u033f\u0340\7@\2\2\u0340\u036c\3\2\2\2")
        buf.write("\u0341\u0342\7\32\2\2\u0342\u0343\7?\2\2\u0343\u036c\7")
        buf.write("@\2\2\u0344\u0345\7\33\2\2\u0345\u0346\7?\2\2\u0346\u0347")
        buf.write("\5\16\b\2\u0347\u0348\7@\2\2\u0348\u036c\3\2\2\2\u0349")
        buf.write("\u034a\7\34\2\2\u034a\u034b\7?\2\2\u034b\u034c\5\16\b")
        buf.write("\2\u034c\u034d\7@\2\2\u034d\u036c\3\2\2\2\u034e\u034f")
        buf.write("\7\35\2\2\u034f\u0350\7?\2\2\u0350\u036c\7@\2\2\u0351")
        buf.write("\u0352\7\36\2\2\u0352\u0353\7?\2\2\u0353\u0354\5\16\b")
        buf.write("\2\u0354\u0355\7@\2\2\u0355\u036c\3\2\2\2\u0356\u0357")
        buf.write("\7\37\2\2\u0357\u0358\7?\2\2\u0358\u0359\5\16\b\2\u0359")
        buf.write("\u035a\7@\2\2\u035a\u036c\3\2\2\2\u035b\u035c\7 \2\2\u035c")
        buf.write("\u035d\7?\2\2\u035d\u036c\7@\2\2\u035e\u035f\7!\2\2\u035f")
        buf.write("\u0360\7?\2\2\u0360\u0361\5\16\b\2\u0361\u0362\7@\2\2")
        buf.write("\u0362\u036c\3\2\2\2\u0363\u0364\7\"\2\2\u0364\u0365\7")
        buf.write("?\2\2\u0365\u0366\5\16\b\2\u0366\u0367\7@\2\2\u0367\u036c")
        buf.write("\3\2\2\2\u0368\u0369\7#\2\2\u0369\u036a\7?\2\2\u036a\u036c")
        buf.write("\7@\2\2\u036b\u0334\3\2\2\2\u036b\u0337\3\2\2\2\u036b")
        buf.write("\u033c\3\2\2\2\u036b\u0341\3\2\2\2\u036b\u0344\3\2\2\2")
        buf.write("\u036b\u0349\3\2\2\2\u036b\u034e\3\2\2\2\u036b\u0351\3")
        buf.write("\2\2\2\u036b\u0356\3\2\2\2\u036b\u035b\3\2\2\2\u036b\u035e")
        buf.write("\3\2\2\2\u036b\u0363\3\2\2\2\u036b\u0368\3\2\2\2\u036c")
        buf.write("\u00a7\3\2\2\2U\u00ae\u00b7\u00b9\u00c4\u00cf\u00d4\u00e0")
        buf.write("\u00eb\u00f6\u0101\u010c\u0112\u011c\u0120\u012d\u013c")
        buf.write("\u0143\u014d\u0157\u015c\u0160\u0166\u016f\u017b\u0186")
        buf.write("\u0191\u019c\u01a7\u01b8\u01bd\u01c4\u01c9\u01d1\u01db")
        buf.write("\u01e1\u01ec\u01f2\u01f9\u01fd\u0204\u0209\u020f\u0213")
        buf.write("\u0224\u022f\u0231\u0242\u0247\u024e\u0259\u025e\u0262")
        buf.write("\u0265\u0267\u027e\u0282\u028a\u0293\u02a4\u02b2\u02b6")
        buf.write("\u02bc\u02c0\u02c7\u02cf\u02d4\u02d7\u02e1\u02e9\u02ed")
        buf.write("\u02f1\u02f4\u02fc\u0301\u0306\u030b\u030f\u0315\u0319")
        buf.write("\u0325\u0329\u032f\u036b")
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
    RULE_primary_index_expr = 31
    RULE_secondary_index_expr = 32
    RULE_signed_tail = 33
    RULE_array_literal = 34
    RULE_array_literal_tail3 = 35
    RULE_struct_literal = 36
    RULE_struct_literal_tail = 37
    RULE_struct_literal_tail2 = 38
    RULE_field_init = 39
    RULE_struct_field_access = 40
    RULE_struct_field_access_head = 41
    RULE_struct_field_access_no_func = 42
    RULE_struct_field_access_no_func_head = 43
    RULE_stmt_in_block = 44
    RULE_stmt_list = 45
    RULE_assignment_stmt = 46
    RULE_assignment_stmt_scalar = 47
    RULE_assignment_operator = 48
    RULE_assignment_expr = 49
    RULE_lhs = 50
    RULE_if_stmt = 51
    RULE_if_stmt_tail = 52
    RULE_for_stmt = 53
    RULE_for_init = 54
    RULE_for_update = 55
    RULE_for_condition = 56
    RULE_return_stmt = 57
    RULE_continue_stmt = 58
    RULE_break_stmt = 59
    RULE_var_decl = 60
    RULE_var_decl_no_init = 61
    RULE_const_decl = 62
    RULE_types = 63
    RULE_primitiveType = 64
    RULE_arrayType = 65
    RULE_compositeType = 66
    RULE_array_decl = 67
    RULE_dimensions = 68
    RULE_array_init = 69
    RULE_struct_decl = 70
    RULE_field_decl_list = 71
    RULE_field_decl = 72
    RULE_interface_decl = 73
    RULE_method_in_decl = 74
    RULE_param_decl = 75
    RULE_param_decl_tail = 76
    RULE_param_call_list = 77
    RULE_function_call = 78
    RULE_func_decl = 79
    RULE_method_decl = 80
    RULE_block = 81
    RULE_built_in_function_call = 82

    ruleNames =  [ "program", "program_list", "decl_or_stmt", "decl", "newlines", 
                   "eos", "expr", "logical_or_expr", "logical_and_expr", 
                   "relational_expr", "additive_expr", "multiplicative_expr", 
                   "primary_expr", "field_access", "atom_arr_access", "atom", 
                   "atom_value", "arr_allow_lit", "arr_init_list", "arr_init_list_body", 
                   "literal", "int_number", "number", "array_access", "array_access_tail", 
                   "index_expr", "logical_index_or_expr", "logical_index_and_expr", 
                   "relational_index_expr", "additive_index_expr", "multiplicative_index_expr", 
                   "primary_index_expr", "secondary_index_expr", "signed_tail", 
                   "array_literal", "array_literal_tail3", "struct_literal", 
                   "struct_literal_tail", "struct_literal_tail2", "field_init", 
                   "struct_field_access", "struct_field_access_head", "struct_field_access_no_func", 
                   "struct_field_access_no_func_head", "stmt_in_block", 
                   "stmt_list", "assignment_stmt", "assignment_stmt_scalar", 
                   "assignment_operator", "assignment_expr", "lhs", "if_stmt", 
                   "if_stmt_tail", "for_stmt", "for_init", "for_update", 
                   "for_condition", "return_stmt", "continue_stmt", "break_stmt", 
                   "var_decl", "var_decl_no_init", "const_decl", "types", 
                   "primitiveType", "arrayType", "compositeType", "array_decl", 
                   "dimensions", "array_init", "struct_decl", "field_decl_list", 
                   "field_decl", "interface_decl", "method_in_decl", "param_decl", 
                   "param_decl_tail", "param_call_list", "function_call", 
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
            self.state = 166
            self.program_list()
            self.state = 167
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
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(MiniGoParser.NEWLINE)
                self.state = 170
                self.program_list()
                pass
            elif token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
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
            self.state = 175
            self.decl()
            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 181
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 177
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 178
                        self.match(MiniGoParser.NEWLINE)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 179
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 180
                        self.decl()
                        pass

             
                self.state = 185
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 186
                self.struct_decl()
                pass

            elif la_ == 2:
                self.state = 187
                self.interface_decl()
                pass

            elif la_ == 3:
                self.state = 188
                self.const_decl()
                pass

            elif la_ == 4:
                self.state = 189
                self.var_decl()
                pass

            elif la_ == 5:
                self.state = 190
                self.array_decl()
                pass

            elif la_ == 6:
                self.state = 191
                self.var_decl_no_init()
                pass

            elif la_ == 7:
                self.state = 192
                self.func_decl()
                pass

            elif la_ == 8:
                self.state = 193
                self.method_decl()
                pass


            self.state = 196
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
            self.state = 199
            self.match(MiniGoParser.NEWLINE)
            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.NewlinesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_newlines)
                    self.state = 201
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 202
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 207
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
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(MiniGoParser.SEMICOLON)
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
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
            self.state = 212
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
            self.state = 215
            self.logical_and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_or_expr)
                    self.state = 217
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 218
                    self.match(MiniGoParser.OR)
                    self.state = 219
                    self.logical_and_expr(0) 
                self.state = 224
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
            self.state = 226
            self.relational_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_and_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_and_expr)
                    self.state = 228
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 229
                    self.match(MiniGoParser.AND)
                    self.state = 230
                    self.relational_expr(0) 
                self.state = 235
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
            self.state = 237
            self.additive_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Relational_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr)
                    self.state = 239
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 240
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 241
                    self.additive_expr(0) 
                self.state = 246
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
            self.state = 248
            self.multiplicative_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Additive_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expr)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 252
                    self.multiplicative_expr(0) 
                self.state = 257
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
            self.state = 259
            self.primary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Multiplicative_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expr)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.primary_expr() 
                self.state = 268
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
            self.state = 269
            self.signed_tail()
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 270
                self.field_access(0)
                pass

            elif la_ == 2:
                self.state = 271
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
            self.state = 275
            self.atom_arr_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Field_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_field_access)
                    self.state = 277
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 278
                    self.match(MiniGoParser.DOT)
                    self.state = 282
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        self.state = 279
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 280
                        self.function_call()
                        pass

                    elif la_ == 3:
                        self.state = 281
                        self.array_access()
                        pass

             
                self.state = 288
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
            self.state = 290
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Atom_arr_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_atom_arr_access)
                    self.state = 292
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 293
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 294
                    self.index_expr()
                    self.state = 295
                    self.match(MiniGoParser.RBRACKET) 
                self.state = 301
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
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.atom_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(MiniGoParser.LPAREN)
                self.state = 304
                self.expr()
                self.state = 305
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 307
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 308
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 309
                self.array_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 310
                self.struct_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 311
                self.struct_field_access()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 312
                self.struct_field_access_no_func()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 313
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
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.number()
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 319
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 320
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
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.int_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 327
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 328
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 329
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 330
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
            self.state = 333
            self.match(MiniGoParser.LBRACE)
            self.state = 334
            self.arr_init_list_body()
            self.state = 335
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
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.arr_allow_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.arr_init_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                    self.state = 339
                    self.arr_allow_lit()
                    pass
                elif token in [MiniGoParser.LBRACE]:
                    self.state = 340
                    self.arr_init_list()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 343
                self.match(MiniGoParser.COMMA)
                self.state = 344
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
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
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
            self.state = 352
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
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.int_number()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
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
            self.state = 358
            self.secondary_index_expr()
            self.state = 359
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
            self.state = 361
            self.match(MiniGoParser.LBRACKET)
            self.state = 362
            self.index_expr()
            self.state = 363
            self.match(MiniGoParser.RBRACKET)
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 364
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
            self.state = 367
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
            self.state = 370
            self.logical_index_and_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_index_or_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_index_or_expr)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    self.match(MiniGoParser.OR)
                    self.state = 374
                    self.logical_index_and_expr(0) 
                self.state = 379
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
            self.state = 381
            self.relational_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_index_and_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_index_and_expr)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.AND or _la==MiniGoParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 385
                    self.relational_index_expr(0) 
                self.state = 390
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
            self.state = 392
            self.additive_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Relational_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_index_expr)
                    self.state = 394
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 395
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 396
                    self.additive_index_expr(0) 
                self.state = 401
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
            self.state = 403
            self.multiplicative_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Additive_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_index_expr)
                    self.state = 405
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 406
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 407
                    self.multiplicative_index_expr(0) 
                self.state = 412
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

        def primary_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Primary_index_exprContext,0)


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
            self.state = 414
            self.primary_index_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Multiplicative_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_index_expr)
                    self.state = 416
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 417
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 418
                    self.primary_index_expr() 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def signed_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Signed_tailContext,0)


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
        self.enterRule(localctx, 62, self.RULE_primary_index_expr)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.secondary_index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self.int_number()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.signed_tail()
                self.state = 428
                self.int_number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 430
                self.match(MiniGoParser.LPAREN)
                self.state = 431
                self.index_expr()
                self.state = 432
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 434
                self.array_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 435
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 436
                self.struct_field_access()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 437
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
        self.enterRule(localctx, 64, self.RULE_secondary_index_expr)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 442
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
        self.enterRule(localctx, 66, self.RULE_signed_tail)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.GET_INT, MiniGoParser.PUT_INT, MiniGoParser.PUT_INT_LN, MiniGoParser.GET_FLOAT, MiniGoParser.PUT_FLOAT, MiniGoParser.PUT_FLOAT_LN, MiniGoParser.GET_BOOL, MiniGoParser.PUT_BOOL, MiniGoParser.PUT_BOOL_LN, MiniGoParser.GET_STRING, MiniGoParser.PUT_STRING, MiniGoParser.PUT_STRING_LN, MiniGoParser.PUT_LN, MiniGoParser.ID, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [MiniGoParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.match(MiniGoParser.SUB)
                self.state = 447
                self.signed_tail()
                pass
            elif token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 448
                self.match(MiniGoParser.NOT)
                self.state = 449
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
        self.enterRule(localctx, 68, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.array_literal_tail3()
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 453
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 454
                self.compositeType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 457
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
        self.enterRule(localctx, 70, self.RULE_array_literal_tail3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(MiniGoParser.LBRACKET)
            self.state = 460
            self.index_expr()
            self.state = 461
            self.match(MiniGoParser.RBRACKET)
            self.state = 463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 462
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
        self.enterRule(localctx, 72, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(MiniGoParser.ID)
            self.state = 466
            self.match(MiniGoParser.LBRACE)
            self.state = 467
            self.struct_literal_tail()
            self.state = 468
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
        self.enterRule(localctx, 74, self.RULE_struct_literal_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 470
                self.field_init()
                self.state = 471
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
        self.enterRule(localctx, 76, self.RULE_struct_literal_tail2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 475
                self.match(MiniGoParser.COMMA)
                self.state = 476
                self.field_init()
                self.state = 477
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
        self.enterRule(localctx, 78, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(MiniGoParser.ID)
            self.state = 482
            self.match(MiniGoParser.COLON)
            self.state = 483
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
        self.enterRule(localctx, 80, self.RULE_struct_field_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.struct_field_access_head(0)
            self.state = 486
            self.match(MiniGoParser.DOT)
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 487
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 488
                self.function_call()
                pass

            elif la_ == 3:
                self.state = 489
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_struct_field_access_head, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 493
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 494
                self.function_call()
                pass

            elif la_ == 3:
                self.state = 495
                self.array_access()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 507
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_field_access_headContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_field_access_head)
                    self.state = 498
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 499
                    self.match(MiniGoParser.DOT)
                    self.state = 503
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 500
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 501
                        self.function_call()
                        pass

                    elif la_ == 3:
                        self.state = 502
                        self.array_access()
                        pass

             
                self.state = 509
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
        self.enterRule(localctx, 84, self.RULE_struct_field_access_no_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.struct_field_access_no_func_head(0)
            self.state = 511
            self.match(MiniGoParser.DOT)
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 512
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 513
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_struct_field_access_no_func_head, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 517
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 518
                self.array_access()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 529
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_field_access_no_func_headContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_field_access_no_func_head)
                    self.state = 521
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 522
                    self.match(MiniGoParser.DOT)
                    self.state = 525
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                    if la_ == 1:
                        self.state = 523
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 524
                        self.array_access()
                        pass

             
                self.state = 531
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
        self.enterRule(localctx, 88, self.RULE_stmt_in_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 532
                self.array_access()
                pass

            elif la_ == 2:
                self.state = 533
                self.struct_field_access()
                pass

            elif la_ == 3:
                self.state = 534
                self.struct_field_access_no_func()
                pass

            elif la_ == 4:
                self.state = 535
                self.const_decl()
                pass

            elif la_ == 5:
                self.state = 536
                self.var_decl()
                pass

            elif la_ == 6:
                self.state = 537
                self.array_decl()
                pass

            elif la_ == 7:
                self.state = 538
                self.var_decl_no_init()
                pass

            elif la_ == 8:
                self.state = 539
                self.break_stmt()
                pass

            elif la_ == 9:
                self.state = 540
                self.continue_stmt()
                pass

            elif la_ == 10:
                self.state = 541
                self.if_stmt()
                pass

            elif la_ == 11:
                self.state = 542
                self.for_stmt()
                pass

            elif la_ == 12:
                self.state = 543
                self.assignment_stmt()
                pass

            elif la_ == 13:
                self.state = 544
                self.function_call()
                pass

            elif la_ == 14:
                self.state = 545
                self.return_stmt()
                pass


            self.state = 548
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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_stmt_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.stmt_in_block()
            self._ctx.stop = self._input.LT(-1)
            self.state = 559
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 557
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Stmt_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                        self.state = 553
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 554
                        self.stmt_in_block()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Stmt_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                        self.state = 555
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 556
                        self.match(MiniGoParser.NEWLINE)
                        pass

             
                self.state = 561
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
        self.enterRule(localctx, 92, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.lhs()
            self.state = 563
            self.assignment_operator()
            self.state = 564
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
        self.enterRule(localctx, 94, self.RULE_assignment_stmt_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(MiniGoParser.ID)
            self.state = 567
            self.assignment_operator()
            self.state = 568
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
        self.enterRule(localctx, 96, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
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
        self.enterRule(localctx, 98, self.RULE_assignment_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.lhs()
            self.state = 573
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ASSIGN or _la==MiniGoParser.SHORT_ASSIGN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 574
                self.expr()
                pass

            elif la_ == 2:
                self.state = 575
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
        self.enterRule(localctx, 100, self.RULE_lhs)
        try:
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 580
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
        self.enterRule(localctx, 102, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(MiniGoParser.IF)
            self.state = 584
            self.match(MiniGoParser.LPAREN)
            self.state = 585
            self.expr()
            self.state = 586
            self.match(MiniGoParser.RPAREN)
            self.state = 588
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 587
                self.newlines(0)


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
        self.enterRule(localctx, 104, self.RULE_if_stmt_tail)
        self._la = 0 # Token type
        try:
            self.state = 613
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 604
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ELSE:
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
                    self.state = 599
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.NEWLINE:
                        self.state = 598
                        self.newlines(0)


                    self.state = 601
                    self.block()
                    self.state = 602
                    self.if_stmt_tail()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ELSE:
                    self.state = 606
                    self.match(MiniGoParser.ELSE)
                    self.state = 608
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.NEWLINE:
                        self.state = 607
                        self.newlines(0)


                    self.state = 610
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
        self.enterRule(localctx, 106, self.RULE_for_stmt)
        try:
            self.state = 636
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 615
                self.match(MiniGoParser.FOR)
                self.state = 616
                self.for_init()
                self.state = 617
                self.match(MiniGoParser.SEMICOLON)
                self.state = 618
                self.expr()
                self.state = 619
                self.match(MiniGoParser.SEMICOLON)
                self.state = 620
                self.for_update()
                self.state = 621
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 623
                self.match(MiniGoParser.FOR)
                self.state = 624
                self.match(MiniGoParser.ID)
                self.state = 625
                self.match(MiniGoParser.COMMA)
                self.state = 626
                self.match(MiniGoParser.ID)
                self.state = 627
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 628
                self.match(MiniGoParser.RANGE)
                self.state = 629
                self.atom()
                self.state = 630
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 632
                self.match(MiniGoParser.FOR)
                self.state = 633
                self.expr()
                self.state = 634
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init" ):
                return visitor.visitFor_init(self)
            else:
                return visitor.visitChildren(self)




    def for_init(self):

        localctx = MiniGoParser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_for_init)
        try:
            self.state = 640
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 638
                self.var_decl()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 639
                self.assignment_stmt_scalar()
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
        self.enterRule(localctx, 110, self.RULE_for_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
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
        self.enterRule(localctx, 112, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
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
        self.enterRule(localctx, 114, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.match(MiniGoParser.RETURN)
            self.state = 648
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & ((1 << (MiniGoParser.NIL - 18)) | (1 << (MiniGoParser.TRUE - 18)) | (1 << (MiniGoParser.FALSE - 18)) | (1 << (MiniGoParser.GET_INT - 18)) | (1 << (MiniGoParser.PUT_INT - 18)) | (1 << (MiniGoParser.PUT_INT_LN - 18)) | (1 << (MiniGoParser.GET_FLOAT - 18)) | (1 << (MiniGoParser.PUT_FLOAT - 18)) | (1 << (MiniGoParser.PUT_FLOAT_LN - 18)) | (1 << (MiniGoParser.GET_BOOL - 18)) | (1 << (MiniGoParser.PUT_BOOL - 18)) | (1 << (MiniGoParser.PUT_BOOL_LN - 18)) | (1 << (MiniGoParser.GET_STRING - 18)) | (1 << (MiniGoParser.PUT_STRING - 18)) | (1 << (MiniGoParser.PUT_STRING_LN - 18)) | (1 << (MiniGoParser.PUT_LN - 18)) | (1 << (MiniGoParser.ID - 18)) | (1 << (MiniGoParser.SUB - 18)) | (1 << (MiniGoParser.NOT - 18)) | (1 << (MiniGoParser.LPAREN - 18)) | (1 << (MiniGoParser.LBRACKET - 18)) | (1 << (MiniGoParser.INT_LIT - 18)) | (1 << (MiniGoParser.HEX_LIT - 18)) | (1 << (MiniGoParser.OCT_LIT - 18)) | (1 << (MiniGoParser.BIN_LIT - 18)) | (1 << (MiniGoParser.FLOAT_LIT - 18)) | (1 << (MiniGoParser.STRING_LIT - 18)))) != 0):
                self.state = 647
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
        self.enterRule(localctx, 116, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
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
        self.enterRule(localctx, 118, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
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


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(MiniGoParser.VAR)
            self.state = 655
            self.match(MiniGoParser.ID)
            self.state = 657
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                self.state = 656
                self.types()


            self.state = 659
            self.match(MiniGoParser.ASSIGN)
            self.state = 660
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

        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl_no_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_no_init" ):
                return visitor.visitVar_decl_no_init(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_no_init(self):

        localctx = MiniGoParser.Var_decl_no_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_var_decl_no_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 662
            self.match(MiniGoParser.VAR)
            self.state = 663
            self.match(MiniGoParser.ID)
            self.state = 664
            self.types()
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
        self.enterRule(localctx, 124, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.match(MiniGoParser.CONST)
            self.state = 667
            self.match(MiniGoParser.ID)
            self.state = 668
            self.match(MiniGoParser.ASSIGN)
            self.state = 669
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
        self.enterRule(localctx, 126, self.RULE_types)
        try:
            self.state = 674
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 671
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 672
                self.compositeType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 3)
                self.state = 673
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
        self.enterRule(localctx, 128, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
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
        self.enterRule(localctx, 130, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
            self.array_access_tail()
            self.state = 679
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
        self.enterRule(localctx, 132, self.RULE_compositeType)
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


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def array_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_array_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
            self.match(MiniGoParser.VAR)
            self.state = 684
            self.match(MiniGoParser.ID)
            self.state = 685
            self.dimensions()
            self.state = 688
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 686
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 687
                self.compositeType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 692
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 690
                self.match(MiniGoParser.ASSIGN)
                self.state = 691
                self.array_init()


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

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

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
        self.enterRule(localctx, 136, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 694
            self.match(MiniGoParser.LBRACKET)
            self.state = 695
            self.match(MiniGoParser.INT_LIT)
            self.state = 696
            self.match(MiniGoParser.RBRACKET)
            self.state = 698
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 697
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

        def arr_init_list(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_init_listContext,0)


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
        self.enterRule(localctx, 138, self.RULE_array_init)
        try:
            self.state = 702
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 700
                self.arr_init_list()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.GET_INT, MiniGoParser.PUT_INT, MiniGoParser.PUT_INT_LN, MiniGoParser.GET_FLOAT, MiniGoParser.PUT_FLOAT, MiniGoParser.PUT_FLOAT_LN, MiniGoParser.GET_BOOL, MiniGoParser.PUT_BOOL, MiniGoParser.PUT_BOOL_LN, MiniGoParser.GET_STRING, MiniGoParser.PUT_STRING, MiniGoParser.PUT_STRING_LN, MiniGoParser.PUT_LN, MiniGoParser.ID, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 701
                self.expr()
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
        self.enterRule(localctx, 140, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 704
            self.match(MiniGoParser.TYPE)
            self.state = 705
            self.match(MiniGoParser.ID)
            self.state = 706
            self.match(MiniGoParser.STRUCT)
            self.state = 707
            self.match(MiniGoParser.LBRACE)
            self.state = 709
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 708
                self.newlines(0)


            self.state = 711
            self.field_decl_list()
            self.state = 712
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
        self.enterRule(localctx, 142, self.RULE_field_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TYPE, MiniGoParser.ID]:
                self.state = 717
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 714
                    self.field_decl()
                    pass

                elif la_ == 2:
                    self.state = 715
                    self.struct_decl()
                    pass

                elif la_ == 3:
                    self.state = 716
                    self.interface_decl()
                    pass


                self.state = 719
                self.eos()
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 721
                self.match(MiniGoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 725
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TYPE) | (1 << MiniGoParser.NEWLINE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 724
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
        self.enterRule(localctx, 144, self.RULE_field_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            self.match(MiniGoParser.ID)
            self.state = 728
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
        self.enterRule(localctx, 146, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 730
            self.match(MiniGoParser.TYPE)
            self.state = 731
            self.match(MiniGoParser.ID)
            self.state = 732
            self.match(MiniGoParser.INTERFACE)
            self.state = 733
            self.match(MiniGoParser.LBRACE)
            self.state = 735
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 734
                self.newlines(0)


            self.state = 737
            self.method_in_decl()
            self.state = 738
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
        self.enterRule(localctx, 148, self.RULE_method_in_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 740
                self.match(MiniGoParser.ID)
                self.state = 741
                self.match(MiniGoParser.LPAREN)
                self.state = 743
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 742
                    self.param_decl()


                self.state = 745
                self.match(MiniGoParser.RPAREN)
                self.state = 747
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                    self.state = 746
                    self.types()


                self.state = 749
                self.eos()
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 750
                self.match(MiniGoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 754
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE or _la==MiniGoParser.ID:
                self.state = 753
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
        self.enterRule(localctx, 150, self.RULE_param_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 756
            self.match(MiniGoParser.ID)
            self.state = 757
            self.param_decl_tail()
            self.state = 758
            self.types()
            self.state = 762
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 760
                self.match(MiniGoParser.COMMA)
                self.state = 761
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
        self.enterRule(localctx, 152, self.RULE_param_decl_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 767
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 764
                self.match(MiniGoParser.COMMA)
                self.state = 765
                self.match(MiniGoParser.ID)
                self.state = 766
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
        self.enterRule(localctx, 154, self.RULE_param_call_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 769
            self.expr()
            self.state = 772
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 770
                self.match(MiniGoParser.COMMA)
                self.state = 771
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
        self.enterRule(localctx, 156, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.state = 781
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 774
                self.match(MiniGoParser.ID)
                self.state = 775
                self.match(MiniGoParser.LPAREN)
                self.state = 777
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & ((1 << (MiniGoParser.NIL - 18)) | (1 << (MiniGoParser.TRUE - 18)) | (1 << (MiniGoParser.FALSE - 18)) | (1 << (MiniGoParser.GET_INT - 18)) | (1 << (MiniGoParser.PUT_INT - 18)) | (1 << (MiniGoParser.PUT_INT_LN - 18)) | (1 << (MiniGoParser.GET_FLOAT - 18)) | (1 << (MiniGoParser.PUT_FLOAT - 18)) | (1 << (MiniGoParser.PUT_FLOAT_LN - 18)) | (1 << (MiniGoParser.GET_BOOL - 18)) | (1 << (MiniGoParser.PUT_BOOL - 18)) | (1 << (MiniGoParser.PUT_BOOL_LN - 18)) | (1 << (MiniGoParser.GET_STRING - 18)) | (1 << (MiniGoParser.PUT_STRING - 18)) | (1 << (MiniGoParser.PUT_STRING_LN - 18)) | (1 << (MiniGoParser.PUT_LN - 18)) | (1 << (MiniGoParser.ID - 18)) | (1 << (MiniGoParser.SUB - 18)) | (1 << (MiniGoParser.NOT - 18)) | (1 << (MiniGoParser.LPAREN - 18)) | (1 << (MiniGoParser.LBRACKET - 18)) | (1 << (MiniGoParser.INT_LIT - 18)) | (1 << (MiniGoParser.HEX_LIT - 18)) | (1 << (MiniGoParser.OCT_LIT - 18)) | (1 << (MiniGoParser.BIN_LIT - 18)) | (1 << (MiniGoParser.FLOAT_LIT - 18)) | (1 << (MiniGoParser.STRING_LIT - 18)))) != 0):
                    self.state = 776
                    self.param_call_list()


                self.state = 779
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_INT, MiniGoParser.PUT_INT, MiniGoParser.PUT_INT_LN, MiniGoParser.GET_FLOAT, MiniGoParser.PUT_FLOAT, MiniGoParser.PUT_FLOAT_LN, MiniGoParser.GET_BOOL, MiniGoParser.PUT_BOOL, MiniGoParser.PUT_BOOL_LN, MiniGoParser.GET_STRING, MiniGoParser.PUT_STRING, MiniGoParser.PUT_STRING_LN, MiniGoParser.PUT_LN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 780
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
        self.enterRule(localctx, 158, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 783
            self.match(MiniGoParser.FUNC)
            self.state = 784
            self.match(MiniGoParser.ID)
            self.state = 785
            self.match(MiniGoParser.LPAREN)
            self.state = 787
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 786
                self.param_decl()


            self.state = 789
            self.match(MiniGoParser.RPAREN)
            self.state = 791
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                self.state = 790
                self.types()


            self.state = 793
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
        self.enterRule(localctx, 160, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 795
            self.match(MiniGoParser.FUNC)
            self.state = 796
            self.match(MiniGoParser.LPAREN)
            self.state = 797
            self.match(MiniGoParser.ID)
            self.state = 798
            self.compositeType()
            self.state = 799
            self.match(MiniGoParser.RPAREN)
            self.state = 800
            self.match(MiniGoParser.ID)
            self.state = 801
            self.match(MiniGoParser.LPAREN)
            self.state = 803
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 802
                self.param_decl()


            self.state = 805
            self.match(MiniGoParser.RPAREN)
            self.state = 807
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                self.state = 806
                self.types()


            self.state = 809
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
        self.enterRule(localctx, 162, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 811
            self.match(MiniGoParser.LBRACE)
            self.state = 813
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 812
                self.match(MiniGoParser.NEWLINE)


            self.state = 815
            self.stmt_list(0)
            self.state = 816
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
        self.enterRule(localctx, 164, self.RULE_built_in_function_call)
        try:
            self.state = 873
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.GET_INT]:
                localctx = MiniGoParser.GetIntCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 818
                self.match(MiniGoParser.GET_INT)
                self.state = 819
                self.match(MiniGoParser.LPAREN)
                self.state = 820
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_INT]:
                localctx = MiniGoParser.PutIntCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 821
                self.match(MiniGoParser.PUT_INT)
                self.state = 822
                self.match(MiniGoParser.LPAREN)
                self.state = 823
                self.expr()
                self.state = 824
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_INT_LN]:
                localctx = MiniGoParser.PutIntLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 826
                self.match(MiniGoParser.PUT_INT_LN)
                self.state = 827
                self.match(MiniGoParser.LPAREN)
                self.state = 828
                self.expr()
                self.state = 829
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_FLOAT]:
                localctx = MiniGoParser.GetFloatCallContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 831
                self.match(MiniGoParser.GET_FLOAT)
                self.state = 832
                self.match(MiniGoParser.LPAREN)
                self.state = 833
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_FLOAT]:
                localctx = MiniGoParser.PutFloatCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 834
                self.match(MiniGoParser.PUT_FLOAT)
                self.state = 835
                self.match(MiniGoParser.LPAREN)
                self.state = 836
                self.expr()
                self.state = 837
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_FLOAT_LN]:
                localctx = MiniGoParser.PutFloatLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 839
                self.match(MiniGoParser.PUT_FLOAT_LN)
                self.state = 840
                self.match(MiniGoParser.LPAREN)
                self.state = 841
                self.expr()
                self.state = 842
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_BOOL]:
                localctx = MiniGoParser.GetBoolCallContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 844
                self.match(MiniGoParser.GET_BOOL)
                self.state = 845
                self.match(MiniGoParser.LPAREN)
                self.state = 846
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_BOOL]:
                localctx = MiniGoParser.PutBoolCallContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 847
                self.match(MiniGoParser.PUT_BOOL)
                self.state = 848
                self.match(MiniGoParser.LPAREN)
                self.state = 849
                self.expr()
                self.state = 850
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_BOOL_LN]:
                localctx = MiniGoParser.PutBoolLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 852
                self.match(MiniGoParser.PUT_BOOL_LN)
                self.state = 853
                self.match(MiniGoParser.LPAREN)
                self.state = 854
                self.expr()
                self.state = 855
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_STRING]:
                localctx = MiniGoParser.GetStringCallContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 857
                self.match(MiniGoParser.GET_STRING)
                self.state = 858
                self.match(MiniGoParser.LPAREN)
                self.state = 859
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_STRING]:
                localctx = MiniGoParser.PutStringCallContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 860
                self.match(MiniGoParser.PUT_STRING)
                self.state = 861
                self.match(MiniGoParser.LPAREN)
                self.state = 862
                self.expr()
                self.state = 863
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_STRING_LN]:
                localctx = MiniGoParser.PutStringLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 865
                self.match(MiniGoParser.PUT_STRING_LN)
                self.state = 866
                self.match(MiniGoParser.LPAREN)
                self.state = 867
                self.expr()
                self.state = 868
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_LN]:
                localctx = MiniGoParser.PutLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 870
                self.match(MiniGoParser.PUT_LN)
                self.state = 871
                self.match(MiniGoParser.LPAREN)
                self.state = 872
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
        self._predicates[41] = self.struct_field_access_head_sempred
        self._predicates[43] = self.struct_field_access_no_func_head_sempred
        self._predicates[45] = self.stmt_list_sempred
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
         




