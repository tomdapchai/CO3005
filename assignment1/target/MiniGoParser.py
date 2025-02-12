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
        buf.write("\u039d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\5\3\u00ad\n\3\3\4\3\4\3\4\3\4\5\4\u00b3\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\7\4\u00bb\n\4\f\4\16\4\u00be\13")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00c9\n\5\3")
        buf.write("\5\3\5\5\5\u00cd\n\5\3\6\3\6\3\6\3\6\3\6\7\6\u00d4\n\6")
        buf.write("\f\6\16\6\u00d7\13\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\7\t\u00e3\n\t\f\t\16\t\u00e6\13\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\7\n\u00ee\n\n\f\n\16\n\u00f1\13\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\7\13\u00f9\n\13\f\13\16\13\u00fc")
        buf.write("\13\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0104\n\f\f\f\16\f")
        buf.write("\u0107\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u010f\n\r\f\r")
        buf.write("\16\r\u0112\13\r\3\16\3\16\3\16\5\16\u0117\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0121\n\17\7\17")
        buf.write("\u0123\n\17\f\17\16\17\u0126\13\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u0130\n\20\f\20\16\20\u0133")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u013d")
        buf.write("\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0146\n")
        buf.write("\21\3\21\3\21\5\21\u014a\n\21\3\21\5\21\u014d\n\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u0154\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u015e\n\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u0166\n\24\3\24\3\24\3\24\5\24\u016b")
        buf.write("\n\24\3\25\3\25\5\25\u016f\n\25\3\26\3\26\3\27\3\27\5")
        buf.write("\27\u0175\n\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u017e\n\31\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\7")
        buf.write("\33\u0188\n\33\f\33\16\33\u018b\13\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\7\34\u0193\n\34\f\34\16\34\u0196\13\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\7\35\u019e\n\35\f\35\16\35")
        buf.write("\u01a1\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u01a9")
        buf.write("\n\36\f\36\16\36\u01ac\13\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u01b4\n\37\f\37\16\37\u01b7\13\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u01c5\n \3!\3!\3!\5!\u01ca")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u01d3\n\"\f\"\16\"")
        buf.write("\u01d6\13\"\3#\3#\3#\5#\u01db\n#\3#\3#\3#\3#\3$\3$\5$")
        buf.write("\u01e3\n$\3$\3$\5$\u01e7\n$\3%\3%\3%\3%\5%\u01ed\n%\3")
        buf.write("&\3&\3&\3&\3&\3\'\3\'\3\'\5\'\u01f7\n\'\3(\3(\3(\3(\5")
        buf.write("(\u01fd\n(\3)\3)\3)\3)\3*\3*\3*\3*\5*\u0207\n*\3*\3*\3")
        buf.write("*\3*\3*\5*\u020e\n*\7*\u0210\n*\f*\16*\u0213\13*\3+\3")
        buf.write("+\3+\5+\u0218\n+\3+\3+\3+\3+\5+\u021e\n+\7+\u0220\n+\f")
        buf.write("+\16+\u0223\13+\3,\3,\3,\3,\3,\3,\3,\5,\u022c\n,\3,\3")
        buf.write(",\3-\3-\3-\3-\3-\5-\u0235\n-\3-\3-\5-\u0239\n-\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\7.\u0242\n.\f.\16.\u0245\13.\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\61\3\61\5\61\u0251\n\61\3\62\3")
        buf.write("\62\3\62\5\62\u0256\n\62\3\63\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u025d\n\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\5\64\u0268\n\64\3\64\3\64\3\64\5\64\u026d\n\64\3\64")
        buf.write("\3\64\5\64\u0271\n\64\3\64\5\64\u0274\n\64\5\64\u0276")
        buf.write("\n\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u027f\n")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\5\65\u028b\n\65\3\65\3\65\3\65\3\65\3\65\5\65\u0292\n")
        buf.write("\65\3\65\3\65\5\65\u0296\n\65\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u029c\n\66\3\67\3\67\5\67\u02a0\n\67\38\38\39\39\59\u02a6")
        buf.write("\n9\3:\3:\3;\3;\3<\3<\3<\5<\u02af\n<\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\3>\3>\3>\3>\3>\5>\u02bd\n>\3>\3>\3>\3?\3?\3?\3?\3")
        buf.write("?\3@\3@\3@\3@\5@\u02cb\n@\3A\3A\3B\3B\3B\3C\3C\3D\3D\3")
        buf.write("D\3D\3D\5D\u02d9\nD\3D\3D\5D\u02dd\nD\3E\3E\3E\3E\5E\u02e3")
        buf.write("\nE\3F\3F\3F\3F\3F\5F\u02ea\nF\3G\3G\5G\u02ee\nG\3G\3")
        buf.write("G\5G\u02f2\nG\5G\u02f4\nG\3H\3H\3H\3H\3H\5H\u02fb\nH\3")
        buf.write("H\3H\3H\3I\3I\3I\3I\5I\u0304\nI\3I\3I\3I\5I\u0309\nI\3")
        buf.write("I\5I\u030c\nI\3J\3J\3J\3K\3K\3K\3K\3K\5K\u0316\nK\3K\3")
        buf.write("K\3K\3L\3L\3L\5L\u031e\nL\3L\3L\5L\u0322\nL\3L\3L\5L\u0326")
        buf.write("\nL\3L\5L\u0329\nL\3M\3M\3M\3M\3M\3M\5M\u0331\nM\3N\3")
        buf.write("N\3N\5N\u0336\nN\3O\3O\3O\5O\u033b\nO\3O\3O\5O\u033f\n")
        buf.write("O\3P\3P\3P\3P\5P\u0345\nP\3P\3P\5P\u0349\nP\3P\3P\3Q\3")
        buf.write("Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u0355\nQ\3Q\3Q\5Q\u0359\nQ\3Q\3")
        buf.write("Q\3R\3R\5R\u035f\nR\3R\3R\3R\3S\3S\3S\3S\3S\3S\3S\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\5S\u039b\nS\3S\2\24\6")
        buf.write("\n\20\22\24\26\30\34\36\64\668:<BRTZT\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write("\u009c\u009e\u00a0\u00a2\u00a4\2\f\4\2$$==\3\2\61\62\3")
        buf.write("\2+,\3\2-\60\3\2&\'\3\2(*\3\2EH\4\2\64\64\66:\3\2\64\65")
        buf.write("\3\2\13\16\2\u03e6\2\u00a6\3\2\2\2\4\u00ac\3\2\2\2\6\u00b2")
        buf.write("\3\2\2\2\b\u00c8\3\2\2\2\n\u00ce\3\2\2\2\f\u00d8\3\2\2")
        buf.write("\2\16\u00da\3\2\2\2\20\u00dc\3\2\2\2\22\u00e7\3\2\2\2")
        buf.write("\24\u00f2\3\2\2\2\26\u00fd\3\2\2\2\30\u0108\3\2\2\2\32")
        buf.write("\u0113\3\2\2\2\34\u0118\3\2\2\2\36\u0127\3\2\2\2 \u014c")
        buf.write("\3\2\2\2\"\u0153\3\2\2\2$\u015d\3\2\2\2&\u016a\3\2\2\2")
        buf.write("(\u016e\3\2\2\2*\u0170\3\2\2\2,\u0174\3\2\2\2.\u0176\3")
        buf.write("\2\2\2\60\u0179\3\2\2\2\62\u017f\3\2\2\2\64\u0181\3\2")
        buf.write("\2\2\66\u018c\3\2\2\28\u0197\3\2\2\2:\u01a2\3\2\2\2<\u01ad")
        buf.write("\3\2\2\2>\u01c4\3\2\2\2@\u01c9\3\2\2\2B\u01cb\3\2\2\2")
        buf.write("D\u01d7\3\2\2\2F\u01e2\3\2\2\2H\u01e8\3\2\2\2J\u01ee\3")
        buf.write("\2\2\2L\u01f6\3\2\2\2N\u01fc\3\2\2\2P\u01fe\3\2\2\2R\u0206")
        buf.write("\3\2\2\2T\u0217\3\2\2\2V\u022b\3\2\2\2X\u0238\3\2\2\2")
        buf.write("Z\u023a\3\2\2\2\\\u0246\3\2\2\2^\u024a\3\2\2\2`\u024c")
        buf.write("\3\2\2\2b\u0255\3\2\2\2d\u0257\3\2\2\2f\u0275\3\2\2\2")
        buf.write("h\u0295\3\2\2\2j\u029b\3\2\2\2l\u029f\3\2\2\2n\u02a1\3")
        buf.write("\2\2\2p\u02a3\3\2\2\2r\u02a7\3\2\2\2t\u02a9\3\2\2\2v\u02ab")
        buf.write("\3\2\2\2x\u02b3\3\2\2\2z\u02bc\3\2\2\2|\u02c1\3\2\2\2")
        buf.write("~\u02ca\3\2\2\2\u0080\u02cc\3\2\2\2\u0082\u02ce\3\2\2")
        buf.write("\2\u0084\u02d1\3\2\2\2\u0086\u02d3\3\2\2\2\u0088\u02de")
        buf.write("\3\2\2\2\u008a\u02e9\3\2\2\2\u008c\u02f3\3\2\2\2\u008e")
        buf.write("\u02f5\3\2\2\2\u0090\u0308\3\2\2\2\u0092\u030d\3\2\2\2")
        buf.write("\u0094\u0310\3\2\2\2\u0096\u0325\3\2\2\2\u0098\u032a\3")
        buf.write("\2\2\2\u009a\u0335\3\2\2\2\u009c\u033e\3\2\2\2\u009e\u0340")
        buf.write("\3\2\2\2\u00a0\u034c\3\2\2\2\u00a2\u035c\3\2\2\2\u00a4")
        buf.write("\u039a\3\2\2\2\u00a6\u00a7\5\4\3\2\u00a7\u00a8\7\2\2\3")
        buf.write("\u00a8\3\3\2\2\2\u00a9\u00aa\7$\2\2\u00aa\u00ad\5\4\3")
        buf.write("\2\u00ab\u00ad\5\6\4\2\u00ac\u00a9\3\2\2\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ad\5\3\2\2\2\u00ae\u00af\b\4\1\2\u00af\u00b3")
        buf.write("\5\b\5\2\u00b0\u00b3\5V,\2\u00b1\u00b3\5\16\b\2\u00b2")
        buf.write("\u00ae\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b3\u00bc\3\2\2\2\u00b4\u00b5\f\6\2\2\u00b5\u00bb\7")
        buf.write("$\2\2\u00b6\u00b7\f\5\2\2\u00b7\u00bb\5\b\5\2\u00b8\u00b9")
        buf.write("\f\4\2\2\u00b9\u00bb\5V,\2\u00ba\u00b4\3\2\2\2\u00ba\u00b6")
        buf.write("\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\7\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00bf\u00c9\5\u008eH\2\u00c0\u00c9\5\u0094")
        buf.write("K\2\u00c1\u00c9\5|?\2\u00c2\u00c9\5v<\2\u00c3\u00c9\5")
        buf.write("\u0086D\2\u00c4\u00c9\5x=\2\u00c5\u00c9\5z>\2\u00c6\u00c9")
        buf.write("\5\u009eP\2\u00c7\u00c9\5\u00a0Q\2\u00c8\u00bf\3\2\2\2")
        buf.write("\u00c8\u00c0\3\2\2\2\u00c8\u00c1\3\2\2\2\u00c8\u00c2\3")
        buf.write("\2\2\2\u00c8\u00c3\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c8\u00c5")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9")
        buf.write("\u00cc\3\2\2\2\u00ca\u00cd\7=\2\2\u00cb\u00cd\5\n\6\2")
        buf.write("\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\t\3\2\2")
        buf.write("\2\u00ce\u00cf\b\6\1\2\u00cf\u00d0\7$\2\2\u00d0\u00d5")
        buf.write("\3\2\2\2\u00d1\u00d2\f\3\2\2\u00d2\u00d4\7$\2\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2")
        buf.write("\u00d5\u00d6\3\2\2\2\u00d6\13\3\2\2\2\u00d7\u00d5\3\2")
        buf.write("\2\2\u00d8\u00d9\t\2\2\2\u00d9\r\3\2\2\2\u00da\u00db\5")
        buf.write("\20\t\2\u00db\17\3\2\2\2\u00dc\u00dd\b\t\1\2\u00dd\u00de")
        buf.write("\5\22\n\2\u00de\u00e4\3\2\2\2\u00df\u00e0\f\4\2\2\u00e0")
        buf.write("\u00e1\t\3\2\2\u00e1\u00e3\5\22\n\2\u00e2\u00df\3\2\2")
        buf.write("\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\21\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8")
        buf.write("\b\n\1\2\u00e8\u00e9\5\24\13\2\u00e9\u00ef\3\2\2\2\u00ea")
        buf.write("\u00eb\f\4\2\2\u00eb\u00ec\t\4\2\2\u00ec\u00ee\5\24\13")
        buf.write("\2\u00ed\u00ea\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed")
        buf.write("\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\23\3\2\2\2\u00f1\u00ef")
        buf.write("\3\2\2\2\u00f2\u00f3\b\13\1\2\u00f3\u00f4\5\26\f\2\u00f4")
        buf.write("\u00fa\3\2\2\2\u00f5\u00f6\f\4\2\2\u00f6\u00f7\t\5\2\2")
        buf.write("\u00f7\u00f9\5\26\f\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc")
        buf.write("\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\25\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\b\f\1\2\u00fe")
        buf.write("\u00ff\5\30\r\2\u00ff\u0105\3\2\2\2\u0100\u0101\f\4\2")
        buf.write("\2\u0101\u0102\t\6\2\2\u0102\u0104\5\30\r\2\u0103\u0100")
        buf.write("\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105")
        buf.write("\u0106\3\2\2\2\u0106\27\3\2\2\2\u0107\u0105\3\2\2\2\u0108")
        buf.write("\u0109\b\r\1\2\u0109\u010a\5\32\16\2\u010a\u0110\3\2\2")
        buf.write("\2\u010b\u010c\f\4\2\2\u010c\u010d\t\7\2\2\u010d\u010f")
        buf.write("\5\32\16\2\u010e\u010b\3\2\2\2\u010f\u0112\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\31\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0113\u0116\5B\"\2\u0114\u0117\5\34\17")
        buf.write("\2\u0115\u0117\5\36\20\2\u0116\u0114\3\2\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117\33\3\2\2\2\u0118\u0119\b\17\1\2\u0119\u011a")
        buf.write("\5\36\20\2\u011a\u0124\3\2\2\2\u011b\u011c\f\4\2\2\u011c")
        buf.write("\u0120\7;\2\2\u011d\u0121\7%\2\2\u011e\u0121\5\u009cO")
        buf.write("\2\u011f\u0121\5.\30\2\u0120\u011d\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0123\3\2\2\2\u0122")
        buf.write("\u011b\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2")
        buf.write("\u0124\u0125\3\2\2\2\u0125\35\3\2\2\2\u0126\u0124\3\2")
        buf.write("\2\2\u0127\u0128\b\20\1\2\u0128\u0129\5 \21\2\u0129\u0131")
        buf.write("\3\2\2\2\u012a\u012b\f\4\2\2\u012b\u012c\7C\2\2\u012c")
        buf.write("\u012d\5\62\32\2\u012d\u012e\7D\2\2\u012e\u0130\3\2\2")
        buf.write("\2\u012f\u012a\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\37\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0134\u014d\5\"\22\2\u0135\u0136\7?\2\2\u0136")
        buf.write("\u0137\5\16\b\2\u0137\u0138\7@\2\2\u0138\u014d\3\2\2\2")
        buf.write("\u0139\u014d\7%\2\2\u013a\u013c\5\u009cO\2\u013b\u013d")
        buf.write("\5\f\7\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u014d\3\2\2\2\u013e\u014d\5D#\2\u013f\u014d\5J&\2\u0140")
        buf.write("\u0141\5\\/\2\u0141\u0142\5\f\7\2\u0142\u014d\3\2\2\2")
        buf.write("\u0143\u0145\5R*\2\u0144\u0146\5\f\7\2\u0145\u0144\3\2")
        buf.write("\2\2\u0145\u0146\3\2\2\2\u0146\u014d\3\2\2\2\u0147\u0149")
        buf.write("\5T+\2\u0148\u014a\5\f\7\2\u0149\u0148\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u014d\5.\30\2\u014c")
        buf.write("\u0134\3\2\2\2\u014c\u0135\3\2\2\2\u014c\u0139\3\2\2\2")
        buf.write("\u014c\u013a\3\2\2\2\u014c\u013e\3\2\2\2\u014c\u013f\3")
        buf.write("\2\2\2\u014c\u0140\3\2\2\2\u014c\u0143\3\2\2\2\u014c\u0147")
        buf.write("\3\2\2\2\u014c\u014b\3\2\2\2\u014d!\3\2\2\2\u014e\u0154")
        buf.write("\5,\27\2\u014f\u0154\7\25\2\2\u0150\u0154\7\26\2\2\u0151")
        buf.write("\u0154\7\24\2\2\u0152\u0154\7K\2\2\u0153\u014e\3\2\2\2")
        buf.write("\u0153\u014f\3\2\2\2\u0153\u0150\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0153\u0152\3\2\2\2\u0154#\3\2\2\2\u0155\u0156")
        buf.write("\7?\2\2\u0156\u0157\5&\24\2\u0157\u0158\7@\2\2\u0158\u015e")
        buf.write("\3\2\2\2\u0159\u015a\7A\2\2\u015a\u015b\5&\24\2\u015b")
        buf.write("\u015c\7B\2\2\u015c\u015e\3\2\2\2\u015d\u0155\3\2\2\2")
        buf.write("\u015d\u0159\3\2\2\2\u015e%\3\2\2\2\u015f\u016b\5\16\b")
        buf.write("\2\u0160\u016b\5J&\2\u0161\u016b\5$\23\2\u0162\u0166\5")
        buf.write("\16\b\2\u0163\u0166\5J&\2\u0164\u0166\5$\23\2\u0165\u0162")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("\u0167\3\2\2\2\u0167\u0168\7<\2\2\u0168\u0169\5&\24\2")
        buf.write("\u0169\u016b\3\2\2\2\u016a\u015f\3\2\2\2\u016a\u0160\3")
        buf.write("\2\2\2\u016a\u0161\3\2\2\2\u016a\u0165\3\2\2\2\u016b\'")
        buf.write("\3\2\2\2\u016c\u016f\5D#\2\u016d\u016f\5J&\2\u016e\u016c")
        buf.write("\3\2\2\2\u016e\u016d\3\2\2\2\u016f)\3\2\2\2\u0170\u0171")
        buf.write("\t\b\2\2\u0171+\3\2\2\2\u0172\u0175\5*\26\2\u0173\u0175")
        buf.write("\7I\2\2\u0174\u0172\3\2\2\2\u0174\u0173\3\2\2\2\u0175")
        buf.write("-\3\2\2\2\u0176\u0177\5@!\2\u0177\u0178\5\60\31\2\u0178")
        buf.write("/\3\2\2\2\u0179\u017a\7C\2\2\u017a\u017b\5\62\32\2\u017b")
        buf.write("\u017d\7D\2\2\u017c\u017e\5\60\31\2\u017d\u017c\3\2\2")
        buf.write("\2\u017d\u017e\3\2\2\2\u017e\61\3\2\2\2\u017f\u0180\5")
        buf.write("\64\33\2\u0180\63\3\2\2\2\u0181\u0182\b\33\1\2\u0182\u0183")
        buf.write("\5\66\34\2\u0183\u0189\3\2\2\2\u0184\u0185\f\4\2\2\u0185")
        buf.write("\u0186\t\3\2\2\u0186\u0188\5\66\34\2\u0187\u0184\3\2\2")
        buf.write("\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018a\65\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018d")
        buf.write("\b\34\1\2\u018d\u018e\58\35\2\u018e\u0194\3\2\2\2\u018f")
        buf.write("\u0190\f\4\2\2\u0190\u0191\t\4\2\2\u0191\u0193\58\35\2")
        buf.write("\u0192\u018f\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3")
        buf.write("\2\2\2\u0194\u0195\3\2\2\2\u0195\67\3\2\2\2\u0196\u0194")
        buf.write("\3\2\2\2\u0197\u0198\b\35\1\2\u0198\u0199\5:\36\2\u0199")
        buf.write("\u019f\3\2\2\2\u019a\u019b\f\4\2\2\u019b\u019c\t\5\2\2")
        buf.write("\u019c\u019e\5:\36\2\u019d\u019a\3\2\2\2\u019e\u01a1\3")
        buf.write("\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a09")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a3\b\36\1\2\u01a3")
        buf.write("\u01a4\5<\37\2\u01a4\u01aa\3\2\2\2\u01a5\u01a6\f\4\2\2")
        buf.write("\u01a6\u01a7\t\6\2\2\u01a7\u01a9\5<\37\2\u01a8\u01a5\3")
        buf.write("\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01ab;\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae")
        buf.write("\b\37\1\2\u01ae\u01af\5> \2\u01af\u01b5\3\2\2\2\u01b0")
        buf.write("\u01b1\f\4\2\2\u01b1\u01b2\t\7\2\2\u01b2\u01b4\5> \2\u01b3")
        buf.write("\u01b0\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6=\3\2\2\2\u01b7\u01b5\3\2\2")
        buf.write("\2\u01b8\u01c5\5@!\2\u01b9\u01c5\5.\30\2\u01ba\u01c5\5")
        buf.write("*\26\2\u01bb\u01bc\5B\"\2\u01bc\u01bd\5*\26\2\u01bd\u01c5")
        buf.write("\3\2\2\2\u01be\u01bf\7?\2\2\u01bf\u01c0\5\62\32\2\u01c0")
        buf.write("\u01c1\7@\2\2\u01c1\u01c5\3\2\2\2\u01c2\u01c5\5D#\2\u01c3")
        buf.write("\u01c5\5J&\2\u01c4\u01b8\3\2\2\2\u01c4\u01b9\3\2\2\2\u01c4")
        buf.write("\u01ba\3\2\2\2\u01c4\u01bb\3\2\2\2\u01c4\u01be\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5?\3\2\2")
        buf.write("\2\u01c6\u01ca\7%\2\2\u01c7\u01ca\7K\2\2\u01c8\u01ca\5")
        buf.write("\u009cO\2\u01c9\u01c6\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01caA\3\2\2\2\u01cb\u01d4\b\"\1\2\u01cc")
        buf.write("\u01cd\f\5\2\2\u01cd\u01d3\7&\2\2\u01ce\u01cf\f\4\2\2")
        buf.write("\u01cf\u01d3\7\'\2\2\u01d0\u01d1\f\3\2\2\u01d1\u01d3\7")
        buf.write("\63\2\2\u01d2\u01cc\3\2\2\2\u01d2\u01ce\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d4\u01d5\3\2\2\2\u01d5C\3\2\2\2\u01d6\u01d4\3\2\2")
        buf.write("\2\u01d7\u01da\5H%\2\u01d8\u01db\5\u0080A\2\u01d9\u01db")
        buf.write("\5\u0084C\2\u01da\u01d8\3\2\2\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01dd\7A\2\2\u01dd\u01de\5F$\2\u01de")
        buf.write("\u01df\7B\2\2\u01dfE\3\2\2\2\u01e0\u01e3\5\16\b\2\u01e1")
        buf.write("\u01e3\5$\23\2\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e6\3\2\2\2\u01e4\u01e5\7<\2\2\u01e5\u01e7\5")
        buf.write("F$\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7G\3")
        buf.write("\2\2\2\u01e8\u01e9\7C\2\2\u01e9\u01ea\5\62\32\2\u01ea")
        buf.write("\u01ec\7D\2\2\u01eb\u01ed\5H%\2\u01ec\u01eb\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01edI\3\2\2\2\u01ee\u01ef\7%\2\2\u01ef")
        buf.write("\u01f0\7A\2\2\u01f0\u01f1\5L\'\2\u01f1\u01f2\7B\2\2\u01f2")
        buf.write("K\3\2\2\2\u01f3\u01f4\5P)\2\u01f4\u01f5\5N(\2\u01f5\u01f7")
        buf.write("\3\2\2\2\u01f6\u01f3\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("M\3\2\2\2\u01f8\u01f9\7<\2\2\u01f9\u01fa\5P)\2\u01fa\u01fb")
        buf.write("\5N(\2\u01fb\u01fd\3\2\2\2\u01fc\u01f8\3\2\2\2\u01fc\u01fd")
        buf.write("\3\2\2\2\u01fdO\3\2\2\2\u01fe\u01ff\7%\2\2\u01ff\u0200")
        buf.write("\7>\2\2\u0200\u0201\5\16\b\2\u0201Q\3\2\2\2\u0202\u0203")
        buf.write("\b*\1\2\u0203\u0207\7%\2\2\u0204\u0207\5\u009cO\2\u0205")
        buf.write("\u0207\5.\30\2\u0206\u0202\3\2\2\2\u0206\u0204\3\2\2\2")
        buf.write("\u0206\u0205\3\2\2\2\u0207\u0211\3\2\2\2\u0208\u0209\f")
        buf.write("\6\2\2\u0209\u020d\7;\2\2\u020a\u020e\7%\2\2\u020b\u020e")
        buf.write("\5\u009cO\2\u020c\u020e\5.\30\2\u020d\u020a\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020d\u020c\3\2\2\2\u020e\u0210\3\2\2\2")
        buf.write("\u020f\u0208\3\2\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3")
        buf.write("\2\2\2\u0211\u0212\3\2\2\2\u0212S\3\2\2\2\u0213\u0211")
        buf.write("\3\2\2\2\u0214\u0215\b+\1\2\u0215\u0218\7%\2\2\u0216\u0218")
        buf.write("\5.\30\2\u0217\u0214\3\2\2\2\u0217\u0216\3\2\2\2\u0218")
        buf.write("\u0221\3\2\2\2\u0219\u021a\f\5\2\2\u021a\u021d\7;\2\2")
        buf.write("\u021b\u021e\7%\2\2\u021c\u021e\5.\30\2\u021d\u021b\3")
        buf.write("\2\2\2\u021d\u021c\3\2\2\2\u021e\u0220\3\2\2\2\u021f\u0219")
        buf.write("\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222U\3\2\2\2\u0223\u0221\3\2\2\2\u0224")
        buf.write("\u022c\5\u009cO\2\u0225\u022c\5.\30\2\u0226\u022c\5R*")
        buf.write("\2\u0227\u022c\5T+\2\u0228\u022c\5d\63\2\u0229\u022c\5")
        buf.write("h\65\2\u022a\u022c\5\\/\2\u022b\u0224\3\2\2\2\u022b\u0225")
        buf.write("\3\2\2\2\u022b\u0226\3\2\2\2\u022b\u0227\3\2\2\2\u022b")
        buf.write("\u0228\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022a\3\2\2\2")
        buf.write("\u022c\u022d\3\2\2\2\u022d\u022e\5\f\7\2\u022eW\3\2\2")
        buf.write("\2\u022f\u0239\5\b\5\2\u0230\u0239\5V,\2\u0231\u0235\5")
        buf.write("t;\2\u0232\u0235\5r:\2\u0233\u0235\5p9\2\u0234\u0231\3")
        buf.write("\2\2\2\u0234\u0232\3\2\2\2\u0234\u0233\3\2\2\2\u0235\u0236")
        buf.write("\3\2\2\2\u0236\u0237\5\f\7\2\u0237\u0239\3\2\2\2\u0238")
        buf.write("\u022f\3\2\2\2\u0238\u0230\3\2\2\2\u0238\u0234\3\2\2\2")
        buf.write("\u0239Y\3\2\2\2\u023a\u023b\b.\1\2\u023b\u023c\5X-\2\u023c")
        buf.write("\u0243\3\2\2\2\u023d\u023e\f\4\2\2\u023e\u0242\5X-\2\u023f")
        buf.write("\u0240\f\3\2\2\u0240\u0242\7$\2\2\u0241\u023d\3\2\2\2")
        buf.write("\u0241\u023f\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3")
        buf.write("\2\2\2\u0243\u0244\3\2\2\2\u0244[\3\2\2\2\u0245\u0243")
        buf.write("\3\2\2\2\u0246\u0247\5b\62\2\u0247\u0248\5^\60\2\u0248")
        buf.write("\u0249\5\16\b\2\u0249]\3\2\2\2\u024a\u024b\t\t\2\2\u024b")
        buf.write("_\3\2\2\2\u024c\u024d\5b\62\2\u024d\u0250\t\n\2\2\u024e")
        buf.write("\u0251\5\16\b\2\u024f\u0251\5J&\2\u0250\u024e\3\2\2\2")
        buf.write("\u0250\u024f\3\2\2\2\u0251a\3\2\2\2\u0252\u0256\7%\2\2")
        buf.write("\u0253\u0256\5.\30\2\u0254\u0256\5T+\2\u0255\u0252\3\2")
        buf.write("\2\2\u0255\u0253\3\2\2\2\u0255\u0254\3\2\2\2\u0256c\3")
        buf.write("\2\2\2\u0257\u0258\7\3\2\2\u0258\u0259\7?\2\2\u0259\u025a")
        buf.write("\5\16\b\2\u025a\u025c\7@\2\2\u025b\u025d\5\n\6\2\u025c")
        buf.write("\u025b\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e\3\2\2\2")
        buf.write("\u025e\u025f\5\u00a2R\2\u025f\u0260\5f\64\2\u0260e\3\2")
        buf.write("\2\2\u0261\u0262\7\4\2\2\u0262\u0263\7\3\2\2\u0263\u0264")
        buf.write("\7?\2\2\u0264\u0265\5\16\b\2\u0265\u0267\7@\2\2\u0266")
        buf.write("\u0268\5\n\6\2\u0267\u0266\3\2\2\2\u0267\u0268\3\2\2\2")
        buf.write("\u0268\u0269\3\2\2\2\u0269\u026a\5\u00a2R\2\u026a\u026b")
        buf.write("\5f\64\2\u026b\u026d\3\2\2\2\u026c\u0261\3\2\2\2\u026c")
        buf.write("\u026d\3\2\2\2\u026d\u0276\3\2\2\2\u026e\u0270\7\4\2\2")
        buf.write("\u026f\u0271\5\n\6\2\u0270\u026f\3\2\2\2\u0270\u0271\3")
        buf.write("\2\2\2\u0271\u0272\3\2\2\2\u0272\u0274\5\u00a2R\2\u0273")
        buf.write("\u026e\3\2\2\2\u0273\u0274\3\2\2\2\u0274\u0276\3\2\2\2")
        buf.write("\u0275\u026c\3\2\2\2\u0275\u0273\3\2\2\2\u0276g\3\2\2")
        buf.write("\2\u0277\u0278\7\5\2\2\u0278\u0279\5j\66\2\u0279\u027a")
        buf.write("\7=\2\2\u027a\u027b\5\16\b\2\u027b\u027c\7=\2\2\u027c")
        buf.write("\u027e\5l\67\2\u027d\u027f\5\n\6\2\u027e\u027d\3\2\2\2")
        buf.write("\u027e\u027f\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0281\5")
        buf.write("\u00a2R\2\u0281\u0296\3\2\2\2\u0282\u0283\7\5\2\2\u0283")
        buf.write("\u0284\7%\2\2\u0284\u0285\7<\2\2\u0285\u0286\7%\2\2\u0286")
        buf.write("\u0287\7\65\2\2\u0287\u0288\7\23\2\2\u0288\u028a\5 \21")
        buf.write("\2\u0289\u028b\5\n\6\2\u028a\u0289\3\2\2\2\u028a\u028b")
        buf.write("\3\2\2\2\u028b\u028c\3\2\2\2\u028c\u028d\5\u00a2R\2\u028d")
        buf.write("\u0296\3\2\2\2\u028e\u028f\7\5\2\2\u028f\u0291\5\16\b")
        buf.write("\2\u0290\u0292\5\n\6\2\u0291\u0290\3\2\2\2\u0291\u0292")
        buf.write("\3\2\2\2\u0292\u0293\3\2\2\2\u0293\u0294\5\u00a2R\2\u0294")
        buf.write("\u0296\3\2\2\2\u0295\u0277\3\2\2\2\u0295\u0282\3\2\2\2")
        buf.write("\u0295\u028e\3\2\2\2\u0296i\3\2\2\2\u0297\u029c\5z>\2")
        buf.write("\u0298\u029c\5v<\2\u0299\u029c\5\u0086D\2\u029a\u029c")
        buf.write("\5\u009eP\2\u029b\u0297\3\2\2\2\u029b\u0298\3\2\2\2\u029b")
        buf.write("\u0299\3\2\2\2\u029b\u029a\3\2\2\2\u029ck\3\2\2\2\u029d")
        buf.write("\u02a0\5\\/\2\u029e\u02a0\5z>\2\u029f\u029d\3\2\2\2\u029f")
        buf.write("\u029e\3\2\2\2\u02a0m\3\2\2\2\u02a1\u02a2\5\16\b\2\u02a2")
        buf.write("o\3\2\2\2\u02a3\u02a5\7\6\2\2\u02a4\u02a6\5\16\b\2\u02a5")
        buf.write("\u02a4\3\2\2\2\u02a5\u02a6\3\2\2\2\u02a6q\3\2\2\2\u02a7")
        buf.write("\u02a8\7\21\2\2\u02a8s\3\2\2\2\u02a9\u02aa\7\22\2\2\u02aa")
        buf.write("u\3\2\2\2\u02ab\u02ac\7\20\2\2\u02ac\u02ae\7%\2\2\u02ad")
        buf.write("\u02af\5~@\2\u02ae\u02ad\3\2\2\2\u02ae\u02af\3\2\2\2\u02af")
        buf.write("\u02b0\3\2\2\2\u02b0\u02b1\7\64\2\2\u02b1\u02b2\5\16\b")
        buf.write("\2\u02b2w\3\2\2\2\u02b3\u02b4\7\20\2\2\u02b4\u02b5\7%")
        buf.write("\2\2\u02b5\u02b6\5~@\2\u02b6y\3\2\2\2\u02b7\u02bd\5b\62")
        buf.write("\2\u02b8\u02b9\7%\2\2\u02b9\u02ba\5\u0088E\2\u02ba\u02bb")
        buf.write("\5~@\2\u02bb\u02bd\3\2\2\2\u02bc\u02b7\3\2\2\2\u02bc\u02b8")
        buf.write("\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02bf\7\65\2\2\u02bf")
        buf.write("\u02c0\5\16\b\2\u02c0{\3\2\2\2\u02c1\u02c2\7\17\2\2\u02c2")
        buf.write("\u02c3\7%\2\2\u02c3\u02c4\7\64\2\2\u02c4\u02c5\5\16\b")
        buf.write("\2\u02c5}\3\2\2\2\u02c6\u02cb\5\u0080A\2\u02c7\u02cb\5")
        buf.write("\u0084C\2\u02c8\u02cb\5\u0084C\2\u02c9\u02cb\5\u0082B")
        buf.write("\2\u02ca\u02c6\3\2\2\2\u02ca\u02c7\3\2\2\2\u02ca\u02c8")
        buf.write("\3\2\2\2\u02ca\u02c9\3\2\2\2\u02cb\177\3\2\2\2\u02cc\u02cd")
        buf.write("\t\13\2\2\u02cd\u0081\3\2\2\2\u02ce\u02cf\5\60\31\2\u02cf")
        buf.write("\u02d0\5~@\2\u02d0\u0083\3\2\2\2\u02d1\u02d2\7%\2\2\u02d2")
        buf.write("\u0085\3\2\2\2\u02d3\u02d4\7\20\2\2\u02d4\u02d5\7%\2\2")
        buf.write("\u02d5\u02d8\5\u0088E\2\u02d6\u02d9\5\u0080A\2\u02d7\u02d9")
        buf.write("\5\u0084C\2\u02d8\u02d6\3\2\2\2\u02d8\u02d7\3\2\2\2\u02d9")
        buf.write("\u02dc\3\2\2\2\u02da\u02db\7\64\2\2\u02db\u02dd\5\u008a")
        buf.write("F\2\u02dc\u02da\3\2\2\2\u02dc\u02dd\3\2\2\2\u02dd\u0087")
        buf.write("\3\2\2\2\u02de\u02df\7C\2\2\u02df\u02e0\7E\2\2\u02e0\u02e2")
        buf.write("\7D\2\2\u02e1\u02e3\5\u0088E\2\u02e2\u02e1\3\2\2\2\u02e2")
        buf.write("\u02e3\3\2\2\2\u02e3\u0089\3\2\2\2\u02e4\u02e5\7A\2\2")
        buf.write("\u02e5\u02e6\5\u008cG\2\u02e6\u02e7\7B\2\2\u02e7\u02ea")
        buf.write("\3\2\2\2\u02e8\u02ea\5\16\b\2\u02e9\u02e4\3\2\2\2\u02e9")
        buf.write("\u02e8\3\2\2\2\u02ea\u008b\3\2\2\2\u02eb\u02ee\5\16\b")
        buf.write("\2\u02ec\u02ee\5$\23\2\u02ed\u02eb\3\2\2\2\u02ed\u02ec")
        buf.write("\3\2\2\2\u02ee\u02f1\3\2\2\2\u02ef\u02f0\7<\2\2\u02f0")
        buf.write("\u02f2\5\u008cG\2\u02f1\u02ef\3\2\2\2\u02f1\u02f2\3\2")
        buf.write("\2\2\u02f2\u02f4\3\2\2\2\u02f3\u02ed\3\2\2\2\u02f3\u02f4")
        buf.write("\3\2\2\2\u02f4\u008d\3\2\2\2\u02f5\u02f6\7\b\2\2\u02f6")
        buf.write("\u02f7\7%\2\2\u02f7\u02f8\7\t\2\2\u02f8\u02fa\7A\2\2\u02f9")
        buf.write("\u02fb\5\n\6\2\u02fa\u02f9\3\2\2\2\u02fa\u02fb\3\2\2\2")
        buf.write("\u02fb\u02fc\3\2\2\2\u02fc\u02fd\5\u0090I\2\u02fd\u02fe")
        buf.write("\7B\2\2\u02fe\u008f\3\2\2\2\u02ff\u0304\5\u0092J\2\u0300")
        buf.write("\u0304\5\u008eH\2\u0301\u0304\5\u0094K\2\u0302\u0304\5")
        buf.write("\u00a0Q\2\u0303\u02ff\3\2\2\2\u0303\u0300\3\2\2\2\u0303")
        buf.write("\u0301\3\2\2\2\u0303\u0302\3\2\2\2\u0304\u0305\3\2\2\2")
        buf.write("\u0305\u0306\5\f\7\2\u0306\u0309\3\2\2\2\u0307\u0309\7")
        buf.write("$\2\2\u0308\u0303\3\2\2\2\u0308\u0307\3\2\2\2\u0309\u030b")
        buf.write("\3\2\2\2\u030a\u030c\5\u0090I\2\u030b\u030a\3\2\2\2\u030b")
        buf.write("\u030c\3\2\2\2\u030c\u0091\3\2\2\2\u030d\u030e\7%\2\2")
        buf.write("\u030e\u030f\5~@\2\u030f\u0093\3\2\2\2\u0310\u0311\7\b")
        buf.write("\2\2\u0311\u0312\7%\2\2\u0312\u0313\7\n\2\2\u0313\u0315")
        buf.write("\7A\2\2\u0314\u0316\5\n\6\2\u0315\u0314\3\2\2\2\u0315")
        buf.write("\u0316\3\2\2\2\u0316\u0317\3\2\2\2\u0317\u0318\5\u0096")
        buf.write("L\2\u0318\u0319\7B\2\2\u0319\u0095\3\2\2\2\u031a\u031b")
        buf.write("\7%\2\2\u031b\u031d\7?\2\2\u031c\u031e\5\u0098M\2\u031d")
        buf.write("\u031c\3\2\2\2\u031d\u031e\3\2\2\2\u031e\u031f\3\2\2\2")
        buf.write("\u031f\u0321\7@\2\2\u0320\u0322\5~@\2\u0321\u0320\3\2")
        buf.write("\2\2\u0321\u0322\3\2\2\2\u0322\u0323\3\2\2\2\u0323\u0326")
        buf.write("\5\f\7\2\u0324\u0326\7$\2\2\u0325\u031a\3\2\2\2\u0325")
        buf.write("\u0324\3\2\2\2\u0326\u0328\3\2\2\2\u0327\u0329\5\u0096")
        buf.write("L\2\u0328\u0327\3\2\2\2\u0328\u0329\3\2\2\2\u0329\u0097")
        buf.write("\3\2\2\2\u032a\u032b\7%\2\2\u032b\u032c\5\u009aN\2\u032c")
        buf.write("\u032d\5~@\2\u032d\u0330\3\2\2\2\u032e\u032f\7<\2\2\u032f")
        buf.write("\u0331\5\u0098M\2\u0330\u032e\3\2\2\2\u0330\u0331\3\2")
        buf.write("\2\2\u0331\u0099\3\2\2\2\u0332\u0333\7<\2\2\u0333\u0334")
        buf.write("\7%\2\2\u0334\u0336\5\u009aN\2\u0335\u0332\3\2\2\2\u0335")
        buf.write("\u0336\3\2\2\2\u0336\u009b\3\2\2\2\u0337\u0338\7%\2\2")
        buf.write("\u0338\u033a\7?\2\2\u0339\u033b\5&\24\2\u033a\u0339\3")
        buf.write("\2\2\2\u033a\u033b\3\2\2\2\u033b\u033c\3\2\2\2\u033c\u033f")
        buf.write("\7@\2\2\u033d\u033f\5\u00a4S\2\u033e\u0337\3\2\2\2\u033e")
        buf.write("\u033d\3\2\2\2\u033f\u009d\3\2\2\2\u0340\u0341\7\7\2\2")
        buf.write("\u0341\u0342\7%\2\2\u0342\u0344\7?\2\2\u0343\u0345\5\u0098")
        buf.write("M\2\u0344\u0343\3\2\2\2\u0344\u0345\3\2\2\2\u0345\u0346")
        buf.write("\3\2\2\2\u0346\u0348\7@\2\2\u0347\u0349\5~@\2\u0348\u0347")
        buf.write("\3\2\2\2\u0348\u0349\3\2\2\2\u0349\u034a\3\2\2\2\u034a")
        buf.write("\u034b\5\u00a2R\2\u034b\u009f\3\2\2\2\u034c\u034d\7\7")
        buf.write("\2\2\u034d\u034e\7?\2\2\u034e\u034f\7%\2\2\u034f\u0350")
        buf.write("\5\u0084C\2\u0350\u0351\7@\2\2\u0351\u0352\7%\2\2\u0352")
        buf.write("\u0354\7?\2\2\u0353\u0355\5\u0098M\2\u0354\u0353\3\2\2")
        buf.write("\2\u0354\u0355\3\2\2\2\u0355\u0356\3\2\2\2\u0356\u0358")
        buf.write("\7@\2\2\u0357\u0359\5~@\2\u0358\u0357\3\2\2\2\u0358\u0359")
        buf.write("\3\2\2\2\u0359\u035a\3\2\2\2\u035a\u035b\5\u00a2R\2\u035b")
        buf.write("\u00a1\3\2\2\2\u035c\u035e\7A\2\2\u035d\u035f\7$\2\2\u035e")
        buf.write("\u035d\3\2\2\2\u035e\u035f\3\2\2\2\u035f\u0360\3\2\2\2")
        buf.write("\u0360\u0361\5Z.\2\u0361\u0362\7B\2\2\u0362\u00a3\3\2")
        buf.write("\2\2\u0363\u0364\7\27\2\2\u0364\u0365\7?\2\2\u0365\u039b")
        buf.write("\7@\2\2\u0366\u0367\7\30\2\2\u0367\u0368\7?\2\2\u0368")
        buf.write("\u0369\5\16\b\2\u0369\u036a\7@\2\2\u036a\u039b\3\2\2\2")
        buf.write("\u036b\u036c\7\31\2\2\u036c\u036d\7?\2\2\u036d\u036e\5")
        buf.write("\16\b\2\u036e\u036f\7@\2\2\u036f\u039b\3\2\2\2\u0370\u0371")
        buf.write("\7\32\2\2\u0371\u0372\7?\2\2\u0372\u039b\7@\2\2\u0373")
        buf.write("\u0374\7\33\2\2\u0374\u0375\7?\2\2\u0375\u0376\5\16\b")
        buf.write("\2\u0376\u0377\7@\2\2\u0377\u039b\3\2\2\2\u0378\u0379")
        buf.write("\7\34\2\2\u0379\u037a\7?\2\2\u037a\u037b\5\16\b\2\u037b")
        buf.write("\u037c\7@\2\2\u037c\u039b\3\2\2\2\u037d\u037e\7\35\2\2")
        buf.write("\u037e\u037f\7?\2\2\u037f\u039b\7@\2\2\u0380\u0381\7\36")
        buf.write("\2\2\u0381\u0382\7?\2\2\u0382\u0383\5\16\b\2\u0383\u0384")
        buf.write("\7@\2\2\u0384\u039b\3\2\2\2\u0385\u0386\7\37\2\2\u0386")
        buf.write("\u0387\7?\2\2\u0387\u0388\5\16\b\2\u0388\u0389\7@\2\2")
        buf.write("\u0389\u039b\3\2\2\2\u038a\u038b\7 \2\2\u038b\u038c\7")
        buf.write("?\2\2\u038c\u039b\7@\2\2\u038d\u038e\7!\2\2\u038e\u038f")
        buf.write("\7?\2\2\u038f\u0390\5\16\b\2\u0390\u0391\7@\2\2\u0391")
        buf.write("\u039b\3\2\2\2\u0392\u0393\7\"\2\2\u0393\u0394\7?\2\2")
        buf.write("\u0394\u0395\5\16\b\2\u0395\u0396\7@\2\2\u0396\u039b\3")
        buf.write("\2\2\2\u0397\u0398\7#\2\2\u0398\u0399\7?\2\2\u0399\u039b")
        buf.write("\7@\2\2\u039a\u0363\3\2\2\2\u039a\u0366\3\2\2\2\u039a")
        buf.write("\u036b\3\2\2\2\u039a\u0370\3\2\2\2\u039a\u0373\3\2\2\2")
        buf.write("\u039a\u0378\3\2\2\2\u039a\u037d\3\2\2\2\u039a\u0380\3")
        buf.write("\2\2\2\u039a\u0385\3\2\2\2\u039a\u038a\3\2\2\2\u039a\u038d")
        buf.write("\3\2\2\2\u039a\u0392\3\2\2\2\u039a\u0397\3\2\2\2\u039b")
        buf.write("\u00a5\3\2\2\2c\u00ac\u00b2\u00ba\u00bc\u00c8\u00cc\u00d5")
        buf.write("\u00e4\u00ef\u00fa\u0105\u0110\u0116\u0120\u0124\u0131")
        buf.write("\u013c\u0145\u0149\u014c\u0153\u015d\u0165\u016a\u016e")
        buf.write("\u0174\u017d\u0189\u0194\u019f\u01aa\u01b5\u01c4\u01c9")
        buf.write("\u01d2\u01d4\u01da\u01e2\u01e6\u01ec\u01f6\u01fc\u0206")
        buf.write("\u020d\u0211\u0217\u021d\u0221\u022b\u0234\u0238\u0241")
        buf.write("\u0243\u0250\u0255\u025c\u0267\u026c\u0270\u0273\u0275")
        buf.write("\u027e\u028a\u0291\u0295\u029b\u029f\u02a5\u02ae\u02bc")
        buf.write("\u02ca\u02d8\u02dc\u02e2\u02e9\u02ed\u02f1\u02f3\u02fa")
        buf.write("\u0303\u0308\u030b\u0315\u031d\u0321\u0325\u0328\u0330")
        buf.write("\u0335\u033a\u033e\u0344\u0348\u0354\u0358\u035e\u039a")
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
    RULE_logical_expr = 7
    RULE_equality_expr = 8
    RULE_relational_expr = 9
    RULE_additive_expr = 10
    RULE_multiplicative_expr = 11
    RULE_primary_expr = 12
    RULE_field_access = 13
    RULE_atom_arr_access = 14
    RULE_atom = 15
    RULE_atom_value = 16
    RULE_atom_list = 17
    RULE_expr_list = 18
    RULE_literal = 19
    RULE_int_number = 20
    RULE_number = 21
    RULE_array_access = 22
    RULE_array_access_tail = 23
    RULE_index_expr = 24
    RULE_logical_index_expr = 25
    RULE_equality_index_expr = 26
    RULE_relational_index_expr = 27
    RULE_additive_index_expr = 28
    RULE_multiplicative_index_expr = 29
    RULE_primary_index_expr = 30
    RULE_secondary_index_expr = 31
    RULE_signed_tail = 32
    RULE_array_literal = 33
    RULE_array_literal_tail = 34
    RULE_array_literal_tail3 = 35
    RULE_struct_literal = 36
    RULE_struct_literal_tail = 37
    RULE_struct_literal_tail2 = 38
    RULE_field_init = 39
    RULE_struct_field_access = 40
    RULE_struct_field_access_no_func = 41
    RULE_stmt_primary = 42
    RULE_stmt_in_block = 43
    RULE_stmt_list = 44
    RULE_assignment_stmt = 45
    RULE_assignment_operator = 46
    RULE_assignment_expr = 47
    RULE_lhs = 48
    RULE_if_stmt = 49
    RULE_if_stmt_tail = 50
    RULE_for_stmt = 51
    RULE_for_init = 52
    RULE_for_update = 53
    RULE_for_condition = 54
    RULE_return_stmt = 55
    RULE_continue_stmt = 56
    RULE_break_stmt = 57
    RULE_var_decl = 58
    RULE_var_decl_no_init = 59
    RULE_short_decl = 60
    RULE_const_decl = 61
    RULE_types = 62
    RULE_primitiveType = 63
    RULE_arrayType = 64
    RULE_compositeType = 65
    RULE_array_decl = 66
    RULE_dimensions = 67
    RULE_array_init = 68
    RULE_array_init_tail = 69
    RULE_struct_decl = 70
    RULE_field_decl_list = 71
    RULE_field_decl = 72
    RULE_interface_decl = 73
    RULE_method_in_decl = 74
    RULE_param_decl = 75
    RULE_param_decl_tail = 76
    RULE_function_call = 77
    RULE_func_decl = 78
    RULE_method_decl = 79
    RULE_block = 80
    RULE_built_in_function_call = 81

    ruleNames =  [ "program", "program_list", "decl_or_stmt", "decl", "newlines", 
                   "eos", "expr", "logical_expr", "equality_expr", "relational_expr", 
                   "additive_expr", "multiplicative_expr", "primary_expr", 
                   "field_access", "atom_arr_access", "atom", "atom_value", 
                   "atom_list", "expr_list", "literal", "int_number", "number", 
                   "array_access", "array_access_tail", "index_expr", "logical_index_expr", 
                   "equality_index_expr", "relational_index_expr", "additive_index_expr", 
                   "multiplicative_index_expr", "primary_index_expr", "secondary_index_expr", 
                   "signed_tail", "array_literal", "array_literal_tail", 
                   "array_literal_tail3", "struct_literal", "struct_literal_tail", 
                   "struct_literal_tail2", "field_init", "struct_field_access", 
                   "struct_field_access_no_func", "stmt_primary", "stmt_in_block", 
                   "stmt_list", "assignment_stmt", "assignment_operator", 
                   "assignment_expr", "lhs", "if_stmt", "if_stmt_tail", 
                   "for_stmt", "for_init", "for_update", "for_condition", 
                   "return_stmt", "continue_stmt", "break_stmt", "var_decl", 
                   "var_decl_no_init", "short_decl", "const_decl", "types", 
                   "primitiveType", "arrayType", "compositeType", "array_decl", 
                   "dimensions", "array_init", "array_init_tail", "struct_decl", 
                   "field_decl_list", "field_decl", "interface_decl", "method_in_decl", 
                   "param_decl", "param_decl_tail", "function_call", "func_decl", 
                   "method_decl", "block", "built_in_function_call" ]

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
            self.state = 164
            self.program_list()
            self.state = 165
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
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(MiniGoParser.NEWLINE)
                self.state = 168
                self.program_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.decl_or_stmt(0)
                pass


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


        def stmt_primary(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_primaryContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 173
                self.decl()
                pass

            elif la_ == 2:
                self.state = 174
                self.stmt_primary()
                pass

            elif la_ == 3:
                self.state = 175
                self.expr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 184
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 178
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 179
                        self.match(MiniGoParser.NEWLINE)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 180
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 181
                        self.decl()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Decl_or_stmtContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_decl_or_stmt)
                        self.state = 182
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 183
                        self.stmt_primary()
                        pass

             
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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


        def short_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Short_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 189
                self.struct_decl()
                pass

            elif la_ == 2:
                self.state = 190
                self.interface_decl()
                pass

            elif la_ == 3:
                self.state = 191
                self.const_decl()
                pass

            elif la_ == 4:
                self.state = 192
                self.var_decl()
                pass

            elif la_ == 5:
                self.state = 193
                self.array_decl()
                pass

            elif la_ == 6:
                self.state = 194
                self.var_decl_no_init()
                pass

            elif la_ == 7:
                self.state = 195
                self.short_decl()
                pass

            elif la_ == 8:
                self.state = 196
                self.func_decl()
                pass

            elif la_ == 9:
                self.state = 197
                self.method_decl()
                pass


            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEMICOLON]:
                self.state = 200
                self.match(MiniGoParser.SEMICOLON)
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 201
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
            self.state = 205
            self.match(MiniGoParser.NEWLINE)
            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.NewlinesContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_newlines)
                    self.state = 207
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 208
                    self.match(MiniGoParser.NEWLINE) 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.NEWLINE or _la==MiniGoParser.SEMICOLON):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_exprContext,0)


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
            self.state = 216
            self.logical_expr(0)
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

        def equality_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Equality_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_exprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.equality_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.AND or _la==MiniGoParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 223
                    self.equality_expr(0) 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Equality_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_exprContext,0)


        def equality_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Equality_exprContext,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_equality_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_expr" ):
                return visitor.visitEquality_expr(self)
            else:
                return visitor.visitChildren(self)



    def equality_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Equality_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_equality_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.relational_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Equality_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_expr)
                    self.state = 232
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 233
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.EQ or _la==MiniGoParser.NEQ):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 234
                    self.relational_expr(0) 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 241
            self.additive_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Relational_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expr)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.additive_expr(0) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            self.state = 252
            self.multiplicative_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Additive_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expr)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.multiplicative_expr(0) 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            self.state = 263
            self.primary_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Multiplicative_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expr)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 267
                    self.primary_expr() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
            self.state = 273
            self.signed_tail(0)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 274
                self.field_access(0)
                pass

            elif la_ == 2:
                self.state = 275
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
            self.state = 279
            self.atom_arr_access(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Field_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_field_access)
                    self.state = 281
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 282
                    self.match(MiniGoParser.DOT)
                    self.state = 286
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 283
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 284
                        self.function_call()
                        pass

                    elif la_ == 3:
                        self.state = 285
                        self.array_access()
                        pass

             
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
            self.state = 294
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Atom_arr_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_atom_arr_access)
                    self.state = 296
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 297
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 298
                    self.index_expr()
                    self.state = 299
                    self.match(MiniGoParser.RBRACKET) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_stmtContext,0)


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
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.atom_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(MiniGoParser.LPAREN)
                self.state = 308
                self.expr()
                self.state = 309
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.function_call()
                self.state = 314
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 313
                    self.eos()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.array_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 317
                self.struct_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 318
                self.assignment_stmt()
                self.state = 319
                self.eos()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 321
                self.struct_field_access(0)
                self.state = 323
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 322
                    self.eos()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 325
                self.struct_field_access_no_func(0)
                self.state = 327
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 326
                    self.eos()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 329
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
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT, MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.number()
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 335
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 336
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


    class Atom_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_atom_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom_list" ):
                return visitor.visitAtom_list(self)
            else:
                return visitor.visitChildren(self)




    def atom_list(self):

        localctx = MiniGoParser.Atom_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_atom_list)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(MiniGoParser.LPAREN)
                self.state = 340
                self.expr_list()
                self.state = 341
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(MiniGoParser.LBRACE)
                self.state = 344
                self.expr_list()
                self.state = 345
                self.match(MiniGoParser.RBRACE)
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


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def atom_list(self):
            return self.getTypedRuleContext(MiniGoParser.Atom_listContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = MiniGoParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr_list)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.struct_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 351
                self.atom_list()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 352
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 353
                    self.struct_literal()
                    pass

                elif la_ == 3:
                    self.state = 354
                    self.atom_list()
                    pass


                self.state = 357
                self.match(MiniGoParser.COMMA)
                self.state = 358
                self.expr_list()
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
        self.enterRule(localctx, 38, self.RULE_literal)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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
        self.enterRule(localctx, 40, self.RULE_int_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
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
        self.enterRule(localctx, 42, self.RULE_number)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT, MiniGoParser.HEX_LIT, MiniGoParser.OCT_LIT, MiniGoParser.BIN_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.int_number()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
        self.enterRule(localctx, 44, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.secondary_index_expr()
            self.state = 373
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
        self.enterRule(localctx, 46, self.RULE_array_access_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(MiniGoParser.LBRACKET)
            self.state = 376
            self.index_expr()
            self.state = 377
            self.match(MiniGoParser.RBRACKET)
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 378
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

        def logical_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_index_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = MiniGoParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_index_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.logical_index_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Equality_index_exprContext,0)


        def logical_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Logical_index_exprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logical_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_index_expr" ):
                return visitor.visitLogical_index_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Logical_index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_logical_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.equality_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Logical_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_index_expr)
                    self.state = 386
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 387
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.AND or _la==MiniGoParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 388
                    self.equality_index_expr(0) 
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Equality_index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Relational_index_exprContext,0)


        def equality_index_expr(self):
            return self.getTypedRuleContext(MiniGoParser.Equality_index_exprContext,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_equality_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_index_expr" ):
                return visitor.visitEquality_index_expr(self)
            else:
                return visitor.visitChildren(self)



    def equality_index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Equality_index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_equality_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.relational_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 402
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Equality_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_index_expr)
                    self.state = 397
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 398
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.EQ or _la==MiniGoParser.NEQ):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 399
                    self.relational_index_expr(0) 
                self.state = 404
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_relational_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.additive_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Relational_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_index_expr)
                    self.state = 408
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 409
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 410
                    self.additive_index_expr(0) 
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_additive_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.multiplicative_index_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Additive_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_index_expr)
                    self.state = 419
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 420
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 421
                    self.multiplicative_index_expr(0) 
                self.state = 426
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_multiplicative_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.primary_index_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 435
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Multiplicative_index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_index_expr)
                    self.state = 430
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 431
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 432
                    self.primary_index_expr() 
                self.state = 437
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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


        def getRuleIndex(self):
            return MiniGoParser.RULE_primary_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_index_expr" ):
                return visitor.visitPrimary_index_expr(self)
            else:
                return visitor.visitChildren(self)




    def primary_index_expr(self):

        localctx = MiniGoParser.Primary_index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_primary_index_expr)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                self.secondary_index_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 440
                self.int_number()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 441
                self.signed_tail(0)
                self.state = 442
                self.int_number()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 444
                self.match(MiniGoParser.LPAREN)
                self.state = 445
                self.index_expr()
                self.state = 446
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 448
                self.array_literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 449
                self.struct_literal()
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
        self.enterRule(localctx, 62, self.RULE_secondary_index_expr)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
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

        def signed_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Signed_tailContext,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_signed_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSigned_tail" ):
                return visitor.visitSigned_tail(self)
            else:
                return visitor.visitChildren(self)



    def signed_tail(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Signed_tailContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_signed_tail, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 464
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Signed_tailContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_signed_tail)
                        self.state = 458
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 459
                        self.match(MiniGoParser.ADD)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Signed_tailContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_signed_tail)
                        self.state = 460
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 461
                        self.match(MiniGoParser.SUB)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Signed_tailContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_signed_tail)
                        self.state = 462
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 463
                        self.match(MiniGoParser.NOT)
                        pass

             
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal_tail3(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_tail3Context,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_literal_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_tailContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 66, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.array_literal_tail3()
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 470
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 471
                self.compositeType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 474
            self.match(MiniGoParser.LBRACE)
            self.state = 475
            self.array_literal_tail()
            self.state = 476
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literal_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def atom_list(self):
            return self.getTypedRuleContext(MiniGoParser.Atom_listContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_literal_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literal_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_tail" ):
                return visitor.visitArray_literal_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_tail(self):

        localctx = MiniGoParser.Array_literal_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_literal_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 478
                self.expr()
                pass

            elif la_ == 2:
                self.state = 479
                self.atom_list()
                pass


            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 482
                self.match(MiniGoParser.COMMA)
                self.state = 483
                self.array_literal_tail()


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
            self.state = 486
            self.match(MiniGoParser.LBRACKET)
            self.state = 487
            self.index_expr()
            self.state = 488
            self.match(MiniGoParser.RBRACKET)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 489
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
            self.state = 492
            self.match(MiniGoParser.ID)
            self.state = 493
            self.match(MiniGoParser.LBRACE)
            self.state = 494
            self.struct_literal_tail()
            self.state = 495
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
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 497
                self.field_init()
                self.state = 498
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
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 502
                self.match(MiniGoParser.COMMA)
                self.state = 503
                self.field_init()
                self.state = 504
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
            self.state = 508
            self.match(MiniGoParser.ID)
            self.state = 509
            self.match(MiniGoParser.COLON)
            self.state = 510
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_accessContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field_access" ):
                return visitor.visitStruct_field_access(self)
            else:
                return visitor.visitChildren(self)



    def struct_field_access(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Struct_field_accessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_struct_field_access, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 513
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 514
                self.function_call()
                pass

            elif la_ == 3:
                self.state = 515
                self.array_access()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 527
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_field_accessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_field_access)
                    self.state = 518
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 519
                    self.match(MiniGoParser.DOT)
                    self.state = 523
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        self.state = 520
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 521
                        self.function_call()
                        pass

                    elif la_ == 3:
                        self.state = 522
                        self.array_access()
                        pass

             
                self.state = 529
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_field_access_no_func(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_no_funcContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field_access_no_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field_access_no_func" ):
                return visitor.visitStruct_field_access_no_func(self)
            else:
                return visitor.visitChildren(self)



    def struct_field_access_no_func(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Struct_field_access_no_funcContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_struct_field_access_no_func, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 531
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 532
                self.array_access()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 543
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_field_access_no_funcContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_field_access_no_func)
                    self.state = 535
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 536
                    self.match(MiniGoParser.DOT)
                    self.state = 539
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        self.state = 537
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 538
                        self.array_access()
                        pass

             
                self.state = 545
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Stmt_primaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_field_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_accessContext,0)


        def struct_field_access_no_func(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_access_no_funcContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def assignment_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_primary" ):
                return visitor.visitStmt_primary(self)
            else:
                return visitor.visitChildren(self)




    def stmt_primary(self):

        localctx = MiniGoParser.Stmt_primaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_stmt_primary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 546
                self.function_call()
                pass

            elif la_ == 2:
                self.state = 547
                self.array_access()
                pass

            elif la_ == 3:
                self.state = 548
                self.struct_field_access(0)
                pass

            elif la_ == 4:
                self.state = 549
                self.struct_field_access_no_func(0)
                pass

            elif la_ == 5:
                self.state = 550
                self.if_stmt()
                pass

            elif la_ == 6:
                self.state = 551
                self.for_stmt()
                pass

            elif la_ == 7:
                self.state = 552
                self.assignment_stmt()
                pass


            self.state = 555
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_in_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def stmt_primary(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_primaryContext,0)


        def eos(self):
            return self.getTypedRuleContext(MiniGoParser.EosContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


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
        self.enterRule(localctx, 86, self.RULE_stmt_in_block)
        try:
            self.state = 566
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                self.stmt_primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 562
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.BREAK]:
                    self.state = 559
                    self.break_stmt()
                    pass
                elif token in [MiniGoParser.CONTINUE]:
                    self.state = 560
                    self.continue_stmt()
                    pass
                elif token in [MiniGoParser.RETURN]:
                    self.state = 561
                    self.return_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 564
                self.eos()
                pass


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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_stmt_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.stmt_in_block()
            self._ctx.stop = self._input.LT(-1)
            self.state = 577
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 575
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Stmt_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                        self.state = 571
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 572
                        self.stmt_in_block()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Stmt_listContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_stmt_list)
                        self.state = 573
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 574
                        self.match(MiniGoParser.NEWLINE)
                        pass

             
                self.state = 579
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        self.enterRule(localctx, 90, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.lhs()
            self.state = 581
            self.assignment_operator()
            self.state = 582
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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

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
        self.enterRule(localctx, 92, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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
        self.enterRule(localctx, 94, self.RULE_assignment_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.lhs()
            self.state = 587
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ASSIGN or _la==MiniGoParser.SHORT_ASSIGN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 588
                self.expr()
                pass

            elif la_ == 2:
                self.state = 589
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
        self.enterRule(localctx, 96, self.RULE_lhs)
        try:
            self.state = 595
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 592
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.array_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 594
                self.struct_field_access_no_func(0)
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
        self.enterRule(localctx, 98, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(MiniGoParser.IF)
            self.state = 598
            self.match(MiniGoParser.LPAREN)
            self.state = 599
            self.expr()
            self.state = 600
            self.match(MiniGoParser.RPAREN)
            self.state = 602
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 601
                self.newlines(0)


            self.state = 604
            self.block()
            self.state = 605
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
        self.enterRule(localctx, 100, self.RULE_if_stmt_tail)
        self._la = 0 # Token type
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ELSE:
                    self.state = 607
                    self.match(MiniGoParser.ELSE)
                    self.state = 608
                    self.match(MiniGoParser.IF)
                    self.state = 609
                    self.match(MiniGoParser.LPAREN)
                    self.state = 610
                    self.expr()
                    self.state = 611
                    self.match(MiniGoParser.RPAREN)
                    self.state = 613
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.NEWLINE:
                        self.state = 612
                        self.newlines(0)


                    self.state = 615
                    self.block()
                    self.state = 616
                    self.if_stmt_tail()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ELSE:
                    self.state = 620
                    self.match(MiniGoParser.ELSE)
                    self.state = 622
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.NEWLINE:
                        self.state = 621
                        self.newlines(0)


                    self.state = 624
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


        def newlines(self):
            return self.getTypedRuleContext(MiniGoParser.NewlinesContext,0)


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
        self.enterRule(localctx, 102, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.state = 659
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.match(MiniGoParser.FOR)
                self.state = 630
                self.for_init()
                self.state = 631
                self.match(MiniGoParser.SEMICOLON)
                self.state = 632
                self.expr()
                self.state = 633
                self.match(MiniGoParser.SEMICOLON)
                self.state = 634
                self.for_update()
                self.state = 636
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NEWLINE:
                    self.state = 635
                    self.newlines(0)


                self.state = 638
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 640
                self.match(MiniGoParser.FOR)
                self.state = 641
                self.match(MiniGoParser.ID)
                self.state = 642
                self.match(MiniGoParser.COMMA)
                self.state = 643
                self.match(MiniGoParser.ID)
                self.state = 644
                self.match(MiniGoParser.SHORT_ASSIGN)
                self.state = 645
                self.match(MiniGoParser.RANGE)
                self.state = 646
                self.atom()
                self.state = 648
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NEWLINE:
                    self.state = 647
                    self.newlines(0)


                self.state = 650
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 652
                self.match(MiniGoParser.FOR)
                self.state = 653
                self.expr()
                self.state = 655
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.NEWLINE:
                    self.state = 654
                    self.newlines(0)


                self.state = 657
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

        def short_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Short_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init" ):
                return visitor.visitFor_init(self)
            else:
                return visitor.visitChildren(self)




    def for_init(self):

        localctx = MiniGoParser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_for_init)
        try:
            self.state = 665
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 661
                self.short_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 662
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 663
                self.array_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 664
                self.func_decl()
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

        def assignment_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assignment_stmtContext,0)


        def short_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Short_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_update" ):
                return visitor.visitFor_update(self)
            else:
                return visitor.visitChildren(self)




    def for_update(self):

        localctx = MiniGoParser.For_updateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_for_update)
        try:
            self.state = 669
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.assignment_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 668
                self.short_decl()
                pass


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
        self.enterRule(localctx, 108, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
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
        self.enterRule(localctx, 110, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            self.match(MiniGoParser.RETURN)
            self.state = 675
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 674
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
        self.enterRule(localctx, 112, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
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
        self.enterRule(localctx, 114, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
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
        self.enterRule(localctx, 116, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.match(MiniGoParser.VAR)
            self.state = 682
            self.match(MiniGoParser.ID)
            self.state = 684
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                self.state = 683
                self.types()


            self.state = 686
            self.match(MiniGoParser.ASSIGN)
            self.state = 687
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
        self.enterRule(localctx, 118, self.RULE_var_decl_no_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            self.match(MiniGoParser.VAR)
            self.state = 690
            self.match(MiniGoParser.ID)
            self.state = 691
            self.types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORT_ASSIGN(self):
            return self.getToken(MiniGoParser.SHORT_ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MiniGoParser.DimensionsContext,0)


        def types(self):
            return self.getTypedRuleContext(MiniGoParser.TypesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_short_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShort_decl" ):
                return visitor.visitShort_decl(self)
            else:
                return visitor.visitChildren(self)




    def short_decl(self):

        localctx = MiniGoParser.Short_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_short_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.state = 693
                self.lhs()
                pass

            elif la_ == 2:
                self.state = 694
                self.match(MiniGoParser.ID)
                self.state = 695
                self.dimensions()
                self.state = 696
                self.types()
                pass


            self.state = 700
            self.match(MiniGoParser.SHORT_ASSIGN)
            self.state = 701
            self.expr()
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
        self.enterRule(localctx, 122, self.RULE_const_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 703
            self.match(MiniGoParser.CONST)
            self.state = 704
            self.match(MiniGoParser.ID)
            self.state = 705
            self.match(MiniGoParser.ASSIGN)
            self.state = 706
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
        self.enterRule(localctx, 124, self.RULE_types)
        try:
            self.state = 712
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 708
                self.primitiveType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 709
                self.compositeType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 710
                self.compositeType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 711
                self.arrayType()
                pass


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
        self.enterRule(localctx, 126, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
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
        self.enterRule(localctx, 128, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.array_access_tail()
            self.state = 717
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
        self.enterRule(localctx, 130, self.RULE_compositeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
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
        self.enterRule(localctx, 132, self.RULE_array_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self.match(MiniGoParser.VAR)
            self.state = 722
            self.match(MiniGoParser.ID)
            self.state = 723
            self.dimensions()
            self.state = 726
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 724
                self.primitiveType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 725
                self.compositeType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 730
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 728
                self.match(MiniGoParser.ASSIGN)
                self.state = 729
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
        self.enterRule(localctx, 134, self.RULE_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self.match(MiniGoParser.LBRACKET)
            self.state = 733
            self.match(MiniGoParser.INT_LIT)
            self.state = 734
            self.match(MiniGoParser.RBRACKET)
            self.state = 736
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                self.state = 735
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_init_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_init_tailContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 136, self.RULE_array_init)
        try:
            self.state = 743
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 738
                self.match(MiniGoParser.LBRACE)
                self.state = 739
                self.array_init_tail()
                self.state = 740
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 742
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_init_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def atom_list(self):
            return self.getTypedRuleContext(MiniGoParser.Atom_listContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_init_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Array_init_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_init_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init_tail" ):
                return visitor.visitArray_init_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_init_tail(self):

        localctx = MiniGoParser.Array_init_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_array_init_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 753
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.state = 747
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
                if la_ == 1:
                    self.state = 745
                    self.expr()
                    pass

                elif la_ == 2:
                    self.state = 746
                    self.atom_list()
                    pass


                self.state = 751
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
                    self.state = 749
                    self.match(MiniGoParser.COMMA)
                    self.state = 750
                    self.array_init_tail()




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
            self.state = 755
            self.match(MiniGoParser.TYPE)
            self.state = 756
            self.match(MiniGoParser.ID)
            self.state = 757
            self.match(MiniGoParser.STRUCT)
            self.state = 758
            self.match(MiniGoParser.LBRACE)
            self.state = 760
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 759
                self.newlines(0)


            self.state = 762
            self.field_decl_list()
            self.state = 763
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


        def method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declContext,0)


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
            self.state = 774
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.ID]:
                self.state = 769
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                if la_ == 1:
                    self.state = 765
                    self.field_decl()
                    pass

                elif la_ == 2:
                    self.state = 766
                    self.struct_decl()
                    pass

                elif la_ == 3:
                    self.state = 767
                    self.interface_decl()
                    pass

                elif la_ == 4:
                    self.state = 768
                    self.method_decl()
                    pass


                self.state = 771
                self.eos()
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 773
                self.match(MiniGoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 777
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.NEWLINE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 776
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
            self.state = 779
            self.match(MiniGoParser.ID)
            self.state = 780
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
            self.state = 782
            self.match(MiniGoParser.TYPE)
            self.state = 783
            self.match(MiniGoParser.ID)
            self.state = 784
            self.match(MiniGoParser.INTERFACE)
            self.state = 785
            self.match(MiniGoParser.LBRACE)
            self.state = 787
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.state = 786
                self.newlines(0)


            self.state = 789
            self.method_in_decl()
            self.state = 790
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
            self.state = 803
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 792
                self.match(MiniGoParser.ID)
                self.state = 793
                self.match(MiniGoParser.LPAREN)
                self.state = 795
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ID:
                    self.state = 794
                    self.param_decl()


                self.state = 797
                self.match(MiniGoParser.RPAREN)
                self.state = 799
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                    self.state = 798
                    self.types()


                self.state = 801
                self.eos()
                pass
            elif token in [MiniGoParser.NEWLINE]:
                self.state = 802
                self.match(MiniGoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 806
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE or _la==MiniGoParser.ID:
                self.state = 805
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
            self.state = 808
            self.match(MiniGoParser.ID)
            self.state = 809
            self.param_decl_tail()
            self.state = 810
            self.types()
            self.state = 814
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 812
                self.match(MiniGoParser.COMMA)
                self.state = 813
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
            self.state = 819
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.COMMA:
                self.state = 816
                self.match(MiniGoParser.COMMA)
                self.state = 817
                self.match(MiniGoParser.ID)
                self.state = 818
                self.param_decl_tail()


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

        def expr_list(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_listContext,0)


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
        self.enterRule(localctx, 154, self.RULE_function_call)
        try:
            self.state = 828
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 821
                self.match(MiniGoParser.ID)
                self.state = 822
                self.match(MiniGoParser.LPAREN)
                self.state = 824
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
                if la_ == 1:
                    self.state = 823
                    self.expr_list()


                self.state = 826
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_INT, MiniGoParser.PUT_INT, MiniGoParser.PUT_INT_LN, MiniGoParser.GET_FLOAT, MiniGoParser.PUT_FLOAT, MiniGoParser.PUT_FLOAT_LN, MiniGoParser.GET_BOOL, MiniGoParser.PUT_BOOL, MiniGoParser.PUT_BOOL_LN, MiniGoParser.GET_STRING, MiniGoParser.PUT_STRING, MiniGoParser.PUT_STRING_LN, MiniGoParser.PUT_LN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 827
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
        self.enterRule(localctx, 156, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 830
            self.match(MiniGoParser.FUNC)
            self.state = 831
            self.match(MiniGoParser.ID)
            self.state = 832
            self.match(MiniGoParser.LPAREN)
            self.state = 834
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 833
                self.param_decl()


            self.state = 836
            self.match(MiniGoParser.RPAREN)
            self.state = 838
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                self.state = 837
                self.types()


            self.state = 840
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
        self.enterRule(localctx, 158, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 842
            self.match(MiniGoParser.FUNC)
            self.state = 843
            self.match(MiniGoParser.LPAREN)
            self.state = 844
            self.match(MiniGoParser.ID)
            self.state = 845
            self.compositeType()
            self.state = 846
            self.match(MiniGoParser.RPAREN)
            self.state = 847
            self.match(MiniGoParser.ID)
            self.state = 848
            self.match(MiniGoParser.LPAREN)
            self.state = 850
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 849
                self.param_decl()


            self.state = 852
            self.match(MiniGoParser.RPAREN)
            self.state = 854
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 9)) & ~0x3f) == 0 and ((1 << (_la - 9)) & ((1 << (MiniGoParser.STRING - 9)) | (1 << (MiniGoParser.INT - 9)) | (1 << (MiniGoParser.FLOAT - 9)) | (1 << (MiniGoParser.BOOLEAN - 9)) | (1 << (MiniGoParser.ID - 9)) | (1 << (MiniGoParser.LBRACKET - 9)))) != 0):
                self.state = 853
                self.types()


            self.state = 856
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
        self.enterRule(localctx, 160, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 858
            self.match(MiniGoParser.LBRACE)
            self.state = 860
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.NEWLINE:
                self.state = 859
                self.match(MiniGoParser.NEWLINE)


            self.state = 862
            self.stmt_list(0)
            self.state = 863
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
        self.enterRule(localctx, 162, self.RULE_built_in_function_call)
        try:
            self.state = 920
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.GET_INT]:
                localctx = MiniGoParser.GetIntCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 865
                self.match(MiniGoParser.GET_INT)
                self.state = 866
                self.match(MiniGoParser.LPAREN)
                self.state = 867
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_INT]:
                localctx = MiniGoParser.PutIntCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 868
                self.match(MiniGoParser.PUT_INT)
                self.state = 869
                self.match(MiniGoParser.LPAREN)
                self.state = 870
                self.expr()
                self.state = 871
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_INT_LN]:
                localctx = MiniGoParser.PutIntLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 873
                self.match(MiniGoParser.PUT_INT_LN)
                self.state = 874
                self.match(MiniGoParser.LPAREN)
                self.state = 875
                self.expr()
                self.state = 876
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_FLOAT]:
                localctx = MiniGoParser.GetFloatCallContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 878
                self.match(MiniGoParser.GET_FLOAT)
                self.state = 879
                self.match(MiniGoParser.LPAREN)
                self.state = 880
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_FLOAT]:
                localctx = MiniGoParser.PutFloatCallContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 881
                self.match(MiniGoParser.PUT_FLOAT)
                self.state = 882
                self.match(MiniGoParser.LPAREN)
                self.state = 883
                self.expr()
                self.state = 884
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_FLOAT_LN]:
                localctx = MiniGoParser.PutFloatLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 886
                self.match(MiniGoParser.PUT_FLOAT_LN)
                self.state = 887
                self.match(MiniGoParser.LPAREN)
                self.state = 888
                self.expr()
                self.state = 889
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_BOOL]:
                localctx = MiniGoParser.GetBoolCallContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 891
                self.match(MiniGoParser.GET_BOOL)
                self.state = 892
                self.match(MiniGoParser.LPAREN)
                self.state = 893
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_BOOL]:
                localctx = MiniGoParser.PutBoolCallContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 894
                self.match(MiniGoParser.PUT_BOOL)
                self.state = 895
                self.match(MiniGoParser.LPAREN)
                self.state = 896
                self.expr()
                self.state = 897
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_BOOL_LN]:
                localctx = MiniGoParser.PutBoolLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 899
                self.match(MiniGoParser.PUT_BOOL_LN)
                self.state = 900
                self.match(MiniGoParser.LPAREN)
                self.state = 901
                self.expr()
                self.state = 902
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.GET_STRING]:
                localctx = MiniGoParser.GetStringCallContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 904
                self.match(MiniGoParser.GET_STRING)
                self.state = 905
                self.match(MiniGoParser.LPAREN)
                self.state = 906
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_STRING]:
                localctx = MiniGoParser.PutStringCallContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 907
                self.match(MiniGoParser.PUT_STRING)
                self.state = 908
                self.match(MiniGoParser.LPAREN)
                self.state = 909
                self.expr()
                self.state = 910
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_STRING_LN]:
                localctx = MiniGoParser.PutStringLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 912
                self.match(MiniGoParser.PUT_STRING_LN)
                self.state = 913
                self.match(MiniGoParser.LPAREN)
                self.state = 914
                self.expr()
                self.state = 915
                self.match(MiniGoParser.RPAREN)
                pass
            elif token in [MiniGoParser.PUT_LN]:
                localctx = MiniGoParser.PutLnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 917
                self.match(MiniGoParser.PUT_LN)
                self.state = 918
                self.match(MiniGoParser.LPAREN)
                self.state = 919
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
        self._predicates[7] = self.logical_expr_sempred
        self._predicates[8] = self.equality_expr_sempred
        self._predicates[9] = self.relational_expr_sempred
        self._predicates[10] = self.additive_expr_sempred
        self._predicates[11] = self.multiplicative_expr_sempred
        self._predicates[13] = self.field_access_sempred
        self._predicates[14] = self.atom_arr_access_sempred
        self._predicates[25] = self.logical_index_expr_sempred
        self._predicates[26] = self.equality_index_expr_sempred
        self._predicates[27] = self.relational_index_expr_sempred
        self._predicates[28] = self.additive_index_expr_sempred
        self._predicates[29] = self.multiplicative_index_expr_sempred
        self._predicates[32] = self.signed_tail_sempred
        self._predicates[40] = self.struct_field_access_sempred
        self._predicates[41] = self.struct_field_access_no_func_sempred
        self._predicates[44] = self.stmt_list_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def decl_or_stmt_sempred(self, localctx:Decl_or_stmtContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def newlines_sempred(self, localctx:NewlinesContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def equality_expr_sempred(self, localctx:Equality_exprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def relational_expr_sempred(self, localctx:Relational_exprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def additive_expr_sempred(self, localctx:Additive_exprContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def multiplicative_expr_sempred(self, localctx:Multiplicative_exprContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def field_access_sempred(self, localctx:Field_accessContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def atom_arr_access_sempred(self, localctx:Atom_arr_accessContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def logical_index_expr_sempred(self, localctx:Logical_index_exprContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def equality_index_expr_sempred(self, localctx:Equality_index_exprContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def relational_index_expr_sempred(self, localctx:Relational_index_exprContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

    def additive_index_expr_sempred(self, localctx:Additive_index_exprContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         

    def multiplicative_index_expr_sempred(self, localctx:Multiplicative_index_exprContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         

    def signed_tail_sempred(self, localctx:Signed_tailContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 1)
         

    def struct_field_access_sempred(self, localctx:Struct_field_accessContext, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 4)
         

    def struct_field_access_no_func_sempred(self, localctx:Struct_field_access_no_funcContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 3)
         

    def stmt_list_sempred(self, localctx:Stmt_listContext, predIndex:int):
            if predIndex == 21:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 1)
         




