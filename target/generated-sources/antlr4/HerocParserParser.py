# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .HerocParserListener import HerocParserListener
else:
    from HerocParserListener import HerocParserListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3E")
        buf.write("\u025d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\5\2`\n\2\3\2\3\2\3\3\3\3\3\3\5\3g\n\3\3\3\3\3")
        buf.write("\3\3\3\3\7\3m\n\3\f\3\16\3p\13\3\3\4\3\4\5\4t\n\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5~\n\5\f\5\16\5\u0081\13")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\5\6\u0088\n\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\5\7\u0094\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\b\u009c\n\b\f\b\16\b\u009f\13\b\3\t\5\t\u00a2")
        buf.write("\n\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00af\n\13\3\13\3\13\3\13\5\13\u00b4\n\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00bf\n\13")
        buf.write("\3\13\7\13\u00c2\n\13\f\13\16\13\u00c5\13\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u00cc\n\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00d4")
        buf.write("\n\r\f\r\16\r\u00d7\13\r\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00e1\n\17\f\17\16\17\u00e4\13\17\3\20")
        buf.write("\3\20\5\20\u00e8\n\20\3\20\3\20\3\21\3\21\5\21\u00ee\n")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u00f4\n\21\3\21\7\21\u00f7")
        buf.write("\n\21\f\21\16\21\u00fa\13\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\7\22\u0102\n\22\f\22\16\22\u0105\13\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u010c\n\23\3\24\3\24\3\25\3\25\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u011a\n\27")
        buf.write("\f\27\16\27\u011d\13\27\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0124\n\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u012c\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0134\n\32\f\32")
        buf.write("\16\32\u0137\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33")
        buf.write("\u013f\n\33\f\33\16\33\u0142\13\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\7\34\u014a\n\34\f\34\16\34\u014d\13\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\7\35\u0155\n\35\f\35\16\35\u0158")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0160\n\36\f")
        buf.write("\36\16\36\u0163\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\7\37\u016e\n\37\f\37\16\37\u0171\13\37\3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \7 \u0182\n")
        buf.write(" \f \16 \u0185\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\7!\u0190")
        buf.write("\n!\f!\16!\u0193\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\7\"\u019e\n\"\f\"\16\"\u01a1\13\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\7#\u01af\n#\f#\16#\u01b2\13#\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01c2\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01cf\n%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\5%\u01d9\n%\3%\3%\3%\3%\3%\7%\u01e0\n%\f%\16")
        buf.write("%\u01e3\13%\3&\3&\3&\3&\3&\3&\7&\u01eb\n&\f&\16&\u01ee")
        buf.write("\13&\3\'\3\'\3\'\6\'\u01f3\n\'\r\'\16\'\u01f4\3\'\3\'")
        buf.write("\3\'\3\'\5\'\u01fb\n\'\3(\3(\3(\3(\3(\5(\u0202\n(\3)\3")
        buf.write(")\5)\u0206\n)\3)\3)\3*\3*\3*\3*\3*\7*\u020f\n*\f*\16*")
        buf.write("\u0212\13*\3+\3+\5+\u0216\n+\3,\5,\u0219\n,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\5-\u0224\n-\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0237\n.\3.\3.\5.\u023b\n")
        buf.write(".\3.\3.\5.\u023f\n.\3.\3.\3.\3.\3.\3.\5.\u0247\n.\3.\3")
        buf.write(".\5.\u024b\n.\3.\3.\3.\5.\u0250\n.\3/\3/\3/\3/\3/\3/\5")
        buf.write("/\u0258\n/\3/\5/\u025b\n/\3/\2\30\4\b\16\24\30\34 \",")
        buf.write("\62\64\668:<>@BDHJR\60\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\\2\4\b")
        buf.write("\2\6\6\25\25\30\30\32\32\35\35\63\63\r\2\24\24\27\27\31")
        buf.write("\31\34\34\37\37!!%%\'\',,//\61\61\u0282\2_\3\2\2\2\4f")
        buf.write("\3\2\2\2\6q\3\2\2\2\bw\3\2\2\2\n\u0087\3\2\2\2\f\u0093")
        buf.write("\3\2\2\2\16\u0095\3\2\2\2\20\u00a1\3\2\2\2\22\u00a5\3")
        buf.write("\2\2\2\24\u00ae\3\2\2\2\26\u00cb\3\2\2\2\30\u00cd\3\2")
        buf.write("\2\2\32\u00d8\3\2\2\2\34\u00da\3\2\2\2\36\u00e5\3\2\2")
        buf.write("\2 \u00eb\3\2\2\2\"\u00fb\3\2\2\2$\u010b\3\2\2\2&\u010d")
        buf.write("\3\2\2\2(\u010f\3\2\2\2*\u0111\3\2\2\2,\u0113\3\2\2\2")
        buf.write(".\u0123\3\2\2\2\60\u0125\3\2\2\2\62\u012d\3\2\2\2\64\u0138")
        buf.write("\3\2\2\2\66\u0143\3\2\2\28\u014e\3\2\2\2:\u0159\3\2\2")
        buf.write("\2<\u0164\3\2\2\2>\u0172\3\2\2\2@\u0186\3\2\2\2B\u0194")
        buf.write("\3\2\2\2D\u01a2\3\2\2\2F\u01c1\3\2\2\2H\u01ce\3\2\2\2")
        buf.write("J\u01e4\3\2\2\2L\u01fa\3\2\2\2N\u0201\3\2\2\2P\u0203\3")
        buf.write("\2\2\2R\u0209\3\2\2\2T\u0215\3\2\2\2V\u0218\3\2\2\2X\u021c")
        buf.write("\3\2\2\2Z\u024f\3\2\2\2\\\u025a\3\2\2\2^`\5\4\3\2_^\3")
        buf.write("\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\2\2\3b\3\3\2\2\2cd\b\3")
        buf.write("\1\2dg\5\6\4\2eg\5\36\20\2fc\3\2\2\2fe\3\2\2\2gn\3\2\2")
        buf.write("\2hi\f\4\2\2im\5\6\4\2jk\f\3\2\2km\5\36\20\2lh\3\2\2\2")
        buf.write("lj\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2o\5\3\2\2\2pn")
        buf.write("\3\2\2\2qs\7\r\2\2rt\5\b\5\2sr\3\2\2\2st\3\2\2\2tu\3\2")
        buf.write("\2\2uv\7:\2\2v\7\3\2\2\2wx\b\5\1\2xy\5\n\6\2y\177\3\2")
        buf.write("\2\2z{\f\3\2\2{|\7;\2\2|~\5\n\6\2}z\3\2\2\2~\u0081\3\2")
        buf.write("\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\t\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0082\u0088\5\20\t\2\u0083\u0084\5\20\t\2")
        buf.write("\u0084\u0085\7\'\2\2\u0085\u0086\5\f\7\2\u0086\u0088\3")
        buf.write("\2\2\2\u0087\u0082\3\2\2\2\u0087\u0083\3\2\2\2\u0088\13")
        buf.write("\3\2\2\2\u0089\u0094\5.\30\2\u008a\u008b\78\2\2\u008b")
        buf.write("\u008c\5\16\b\2\u008c\u008d\79\2\2\u008d\u0094\3\2\2\2")
        buf.write("\u008e\u008f\78\2\2\u008f\u0090\5\16\b\2\u0090\u0091\7")
        buf.write(";\2\2\u0091\u0092\79\2\2\u0092\u0094\3\2\2\2\u0093\u0089")
        buf.write("\3\2\2\2\u0093\u008a\3\2\2\2\u0093\u008e\3\2\2\2\u0094")
        buf.write("\r\3\2\2\2\u0095\u0096\b\b\1\2\u0096\u0097\5\f\7\2\u0097")
        buf.write("\u009d\3\2\2\2\u0098\u0099\f\3\2\2\u0099\u009a\7;\2\2")
        buf.write("\u009a\u009c\5\f\7\2\u009b\u0098\3\2\2\2\u009c\u009f\3")
        buf.write("\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\17")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2\5\22\n\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\5\24\13\2\u00a4\21\3\2\2\2\u00a5\u00a6\7")
        buf.write("\30\2\2\u00a6\u00a7\5\22\n\2\u00a7\23\3\2\2\2\u00a8\u00a9")
        buf.write("\b\13\1\2\u00a9\u00af\7<\2\2\u00aa\u00ab\7\3\2\2\u00ab")
        buf.write("\u00ac\5\20\t\2\u00ac\u00ad\7\65\2\2\u00ad\u00af\3\2\2")
        buf.write("\2\u00ae\u00a8\3\2\2\2\u00ae\u00aa\3\2\2\2\u00af\u00c3")
        buf.write("\3\2\2\2\u00b0\u00b1\f\5\2\2\u00b1\u00b3\7\66\2\2\u00b2")
        buf.write("\u00b4\5.\30\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\u00c2\7\67\2\2\u00b6\u00b7")
        buf.write("\f\4\2\2\u00b7\u00b8\7\3\2\2\u00b8\u00b9\5\26\f\2\u00b9")
        buf.write("\u00ba\7\65\2\2\u00ba\u00c2\3\2\2\2\u00bb\u00bc\f\3\2")
        buf.write("\2\u00bc\u00be\7\3\2\2\u00bd\u00bf\5\34\17\2\u00be\u00bd")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write("\u00c2\7\65\2\2\u00c1\u00b0\3\2\2\2\u00c1\u00b6\3\2\2")
        buf.write("\2\u00c1\u00bb\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\25\3\2\2\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c6\u00cc\5\30\r\2\u00c7\u00c8\5\30\r\2\u00c8")
        buf.write("\u00c9\7;\2\2\u00c9\u00ca\7\5\2\2\u00ca\u00cc\3\2\2\2")
        buf.write("\u00cb\u00c6\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cc\27\3\2")
        buf.write("\2\2\u00cd\u00ce\b\r\1\2\u00ce\u00cf\5\32\16\2\u00cf\u00d5")
        buf.write("\3\2\2\2\u00d0\u00d1\f\3\2\2\u00d1\u00d2\7;\2\2\u00d2")
        buf.write("\u00d4\5\32\16\2\u00d3\u00d0\3\2\2\2\u00d4\u00d7\3\2\2")
        buf.write("\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\31\3")
        buf.write("\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\5\20\t\2\u00d9")
        buf.write("\33\3\2\2\2\u00da\u00db\b\17\1\2\u00db\u00dc\7<\2\2\u00dc")
        buf.write("\u00e2\3\2\2\2\u00dd\u00de\f\3\2\2\u00de\u00df\7;\2\2")
        buf.write("\u00df\u00e1\7<\2\2\u00e0\u00dd\3\2\2\2\u00e1\u00e4\3")
        buf.write("\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\35")
        buf.write("\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00e7\5\20\t\2\u00e6")
        buf.write("\u00e8\5 \21\2\u00e7\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\u00ea\5P)\2\u00ea\37\3\2\2")
        buf.write("\2\u00eb\u00ed\b\21\1\2\u00ec\u00ee\5\"\22\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\u00f0\7:\2\2\u00f0\u00f8\3\2\2\2\u00f1\u00f3\f\3\2\2")
        buf.write("\u00f2\u00f4\5\"\22\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\7:\2\2\u00f6")
        buf.write("\u00f1\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9!\3\2\2\2\u00fa\u00f8\3\2\2")
        buf.write("\2\u00fb\u00fc\b\22\1\2\u00fc\u00fd\5$\23\2\u00fd\u0103")
        buf.write("\3\2\2\2\u00fe\u00ff\f\3\2\2\u00ff\u0100\7;\2\2\u0100")
        buf.write("\u0102\5$\23\2\u0101\u00fe\3\2\2\2\u0102\u0105\3\2\2\2")
        buf.write("\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104#\3\2\2")
        buf.write("\2\u0105\u0103\3\2\2\2\u0106\u010c\5\20\t\2\u0107\u0108")
        buf.write("\5\20\t\2\u0108\u0109\7\'\2\2\u0109\u010a\5\f\7\2\u010a")
        buf.write("\u010c\3\2\2\2\u010b\u0106\3\2\2\2\u010b\u0107\3\2\2\2")
        buf.write("\u010c%\3\2\2\2\u010d\u010e\t\2\2\2\u010e\'\3\2\2\2\u010f")
        buf.write("\u0110\t\3\2\2\u0110)\3\2\2\2\u0111\u0112\5\60\31\2\u0112")
        buf.write("+\3\2\2\2\u0113\u0114\b\27\1\2\u0114\u0115\5.\30\2\u0115")
        buf.write("\u011b\3\2\2\2\u0116\u0117\f\3\2\2\u0117\u0118\7;\2\2")
        buf.write("\u0118\u011a\5.\30\2\u0119\u0116\3\2\2\2\u011a\u011d\3")
        buf.write("\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c-")
        buf.write("\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u0124\5\60\31\2\u011f")
        buf.write("\u0120\5F$\2\u0120\u0121\5(\25\2\u0121\u0122\5.\30\2\u0122")
        buf.write("\u0124\3\2\2\2\u0123\u011e\3\2\2\2\u0123\u011f\3\2\2\2")
        buf.write("\u0124/\3\2\2\2\u0125\u012b\5\62\32\2\u0126\u0127\7-\2")
        buf.write("\2\u0127\u0128\5,\27\2\u0128\u0129\7\"\2\2\u0129\u012a")
        buf.write("\5\60\31\2\u012a\u012c\3\2\2\2\u012b\u0126\3\2\2\2\u012b")
        buf.write("\u012c\3\2\2\2\u012c\61\3\2\2\2\u012d\u012e\b\32\1\2\u012e")
        buf.write("\u012f\5\64\33\2\u012f\u0135\3\2\2\2\u0130\u0131\f\3\2")
        buf.write("\2\u0131\u0132\7\62\2\2\u0132\u0134\5\64\33\2\u0133\u0130")
        buf.write("\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\63\3\2\2\2\u0137\u0135\3\2\2\2\u0138")
        buf.write("\u0139\b\33\1\2\u0139\u013a\5\66\34\2\u013a\u0140\3\2")
        buf.write("\2\2\u013b\u013c\f\3\2\2\u013c\u013d\7\26\2\2\u013d\u013f")
        buf.write("\5\66\34\2\u013e\u013b\3\2\2\2\u013f\u0142\3\2\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\65\3\2\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0143\u0144\b\34\1\2\u0144\u0145\58\35")
        buf.write("\2\u0145\u014b\3\2\2\2\u0146\u0147\f\3\2\2\u0147\u0148")
        buf.write("\7\60\2\2\u0148\u014a\58\35\2\u0149\u0146\3\2\2\2\u014a")
        buf.write("\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2")
        buf.write("\u014c\67\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\b\35")
        buf.write("\1\2\u014f\u0150\5:\36\2\u0150\u0156\3\2\2\2\u0151\u0152")
        buf.write("\f\3\2\2\u0152\u0153\7.\2\2\u0153\u0155\5:\36\2\u0154")
        buf.write("\u0151\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154\3\2\2\2")
        buf.write("\u0156\u0157\3\2\2\2\u01579\3\2\2\2\u0158\u0156\3\2\2")
        buf.write("\2\u0159\u015a\b\36\1\2\u015a\u015b\5<\37\2\u015b\u0161")
        buf.write("\3\2\2\2\u015c\u015d\f\3\2\2\u015d\u015e\7\25\2\2\u015e")
        buf.write("\u0160\5<\37\2\u015f\u015c\3\2\2\2\u0160\u0163\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162;\3\2\2")
        buf.write("\2\u0163\u0161\3\2\2\2\u0164\u0165\b\37\1\2\u0165\u0166")
        buf.write("\5> \2\u0166\u016f\3\2\2\2\u0167\u0168\f\4\2\2\u0168\u0169")
        buf.write("\7(\2\2\u0169\u016e\5> \2\u016a\u016b\f\3\2\2\u016b\u016c")
        buf.write("\7\22\2\2\u016c\u016e\5> \2\u016d\u0167\3\2\2\2\u016d")
        buf.write("\u016a\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2")
        buf.write("\u016f\u0170\3\2\2\2\u0170=\3\2\2\2\u0171\u016f\3\2\2")
        buf.write("\2\u0172\u0173\b \1\2\u0173\u0174\5@!\2\u0174\u0183\3")
        buf.write("\2\2\2\u0175\u0176\f\6\2\2\u0176\u0177\7#\2\2\u0177\u0182")
        buf.write("\5@!\2\u0178\u0179\f\5\2\2\u0179\u017a\7)\2\2\u017a\u0182")
        buf.write("\5@!\2\u017b\u017c\f\4\2\2\u017c\u017d\7&\2\2\u017d\u0182")
        buf.write("\5@!\2\u017e\u017f\f\3\2\2\u017f\u0180\7*\2\2\u0180\u0182")
        buf.write("\5@!\2\u0181\u0175\3\2\2\2\u0181\u0178\3\2\2\2\u0181\u017b")
        buf.write("\3\2\2\2\u0181\u017e\3\2\2\2\u0182\u0185\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184?\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0186\u0187\b!\1\2\u0187\u0188\5B\"\2\u0188")
        buf.write("\u0191\3\2\2\2\u0189\u018a\f\4\2\2\u018a\u018b\7$\2\2")
        buf.write("\u018b\u0190\5B\"\2\u018c\u018d\f\3\2\2\u018d\u018e\7")
        buf.write("+\2\2\u018e\u0190\5B\"\2\u018f\u0189\3\2\2\2\u018f\u018c")
        buf.write("\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192A\3\2\2\2\u0193\u0191\3\2\2\2\u0194")
        buf.write("\u0195\b\"\1\2\u0195\u0196\5D#\2\u0196\u019f\3\2\2\2\u0197")
        buf.write("\u0198\f\4\2\2\u0198\u0199\7\32\2\2\u0199\u019e\5D#\2")
        buf.write("\u019a\u019b\f\3\2\2\u019b\u019c\7\35\2\2\u019c\u019e")
        buf.write("\5D#\2\u019d\u0197\3\2\2\2\u019d\u019a\3\2\2\2\u019e\u01a1")
        buf.write("\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("C\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a3\b#\1\2\u01a3")
        buf.write("\u01a4\5F$\2\u01a4\u01b0\3\2\2\2\u01a5\u01a6\f\5\2\2\u01a6")
        buf.write("\u01a7\7\30\2\2\u01a7\u01af\5F$\2\u01a8\u01a9\f\4\2\2")
        buf.write("\u01a9\u01aa\7 \2\2\u01aa\u01af\5F$\2\u01ab\u01ac\f\3")
        buf.write("\2\2\u01ac\u01ad\7\23\2\2\u01ad\u01af\5F$\2\u01ae\u01a5")
        buf.write("\3\2\2\2\u01ae\u01a8\3\2\2\2\u01ae\u01ab\3\2\2\2\u01af")
        buf.write("\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2")
        buf.write("\u01b1E\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01c2\5H%\2")
        buf.write("\u01b4\u01b5\7\33\2\2\u01b5\u01c2\5F$\2\u01b6\u01b7\7")
        buf.write("\36\2\2\u01b7\u01c2\5F$\2\u01b8\u01b9\5&\24\2\u01b9\u01ba")
        buf.write("\5F$\2\u01ba\u01c2\3\2\2\2\u01bb\u01bc\7\17\2\2\u01bc")
        buf.write("\u01bd\7\3\2\2\u01bd\u01be\7\r\2\2\u01be\u01c2\7\65\2")
        buf.write("\2\u01bf\u01c0\7\26\2\2\u01c0\u01c2\7<\2\2\u01c1\u01b3")
        buf.write("\3\2\2\2\u01c1\u01b4\3\2\2\2\u01c1\u01b6\3\2\2\2\u01c1")
        buf.write("\u01b8\3\2\2\2\u01c1\u01bb\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c2G\3\2\2\2\u01c3\u01c4\b%\1\2\u01c4\u01cf\5L\'\2")
        buf.write("\u01c5\u01c6\78\2\2\u01c6\u01c7\5\16\b\2\u01c7\u01c8\7")
        buf.write("9\2\2\u01c8\u01cf\3\2\2\2\u01c9\u01ca\78\2\2\u01ca\u01cb")
        buf.write("\5\16\b\2\u01cb\u01cc\7;\2\2\u01cc\u01cd\79\2\2\u01cd")
        buf.write("\u01cf\3\2\2\2\u01ce\u01c3\3\2\2\2\u01ce\u01c5\3\2\2\2")
        buf.write("\u01ce\u01c9\3\2\2\2\u01cf\u01e1\3\2\2\2\u01d0\u01d1\f")
        buf.write("\b\2\2\u01d1\u01d2\7\66\2\2\u01d2\u01d3\5,\27\2\u01d3")
        buf.write("\u01d4\7\67\2\2\u01d4\u01e0\3\2\2\2\u01d5\u01d6\f\7\2")
        buf.write("\2\u01d6\u01d8\7\3\2\2\u01d7\u01d9\5J&\2\u01d8\u01d7\3")
        buf.write("\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01e0")
        buf.write("\7\65\2\2\u01db\u01dc\f\6\2\2\u01dc\u01e0\7\33\2\2\u01dd")
        buf.write("\u01de\f\5\2\2\u01de\u01e0\7\36\2\2\u01df\u01d0\3\2\2")
        buf.write("\2\u01df\u01d5\3\2\2\2\u01df\u01db\3\2\2\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1")
        buf.write("\u01e2\3\2\2\2\u01e2I\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4")
        buf.write("\u01e5\b&\1\2\u01e5\u01e6\5.\30\2\u01e6\u01ec\3\2\2\2")
        buf.write("\u01e7\u01e8\f\3\2\2\u01e8\u01e9\7;\2\2\u01e9\u01eb\5")
        buf.write(".\30\2\u01ea\u01e7\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea")
        buf.write("\3\2\2\2\u01ec\u01ed\3\2\2\2\u01edK\3\2\2\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ef\u01fb\7<\2\2\u01f0\u01fb\7=\2\2\u01f1\u01f3")
        buf.write("\7B\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01fb\3\2\2\2")
        buf.write("\u01f6\u01f7\7\3\2\2\u01f7\u01f8\5,\27\2\u01f8\u01f9\7")
        buf.write("\65\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01ef\3\2\2\2\u01fa")
        buf.write("\u01f0\3\2\2\2\u01fa\u01f2\3\2\2\2\u01fa\u01f6\3\2\2\2")
        buf.write("\u01fbM\3\2\2\2\u01fc\u0202\5P)\2\u01fd\u0202\5V,\2\u01fe")
        buf.write("\u0202\5X-\2\u01ff\u0202\5Z.\2\u0200\u0202\5\\/\2\u0201")
        buf.write("\u01fc\3\2\2\2\u0201\u01fd\3\2\2\2\u0201\u01fe\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0201\u0200\3\2\2\2\u0202O\3\2\2")
        buf.write("\2\u0203\u0205\78\2\2\u0204\u0206\5R*\2\u0205\u0204\3")
        buf.write("\2\2\2\u0205\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208")
        buf.write("\79\2\2\u0208Q\3\2\2\2\u0209\u020a\b*\1\2\u020a\u020b")
        buf.write("\5T+\2\u020b\u0210\3\2\2\2\u020c\u020d\f\3\2\2\u020d\u020f")
        buf.write("\5T+\2\u020e\u020c\3\2\2\2\u020f\u0212\3\2\2\2\u0210\u020e")
        buf.write("\3\2\2\2\u0210\u0211\3\2\2\2\u0211S\3\2\2\2\u0212\u0210")
        buf.write("\3\2\2\2\u0213\u0216\5\6\4\2\u0214\u0216\5N(\2\u0215\u0213")
        buf.write("\3\2\2\2\u0215\u0214\3\2\2\2\u0216U\3\2\2\2\u0217\u0219")
        buf.write("\5,\27\2\u0218\u0217\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u021a\3\2\2\2\u021a\u021b\7:\2\2\u021bW\3\2\2\2\u021c")
        buf.write("\u021d\7\f\2\2\u021d\u021e\7\3\2\2\u021e\u021f\5,\27\2")
        buf.write("\u021f\u0220\7\65\2\2\u0220\u0223\5N(\2\u0221\u0222\7")
        buf.write("\n\2\2\u0222\u0224\5N(\2\u0223\u0221\3\2\2\2\u0223\u0224")
        buf.write("\3\2\2\2\u0224Y\3\2\2\2\u0225\u0226\7\20\2\2\u0226\u0227")
        buf.write("\7\3\2\2\u0227\u0228\5,\27\2\u0228\u0229\7\65\2\2\u0229")
        buf.write("\u022a\5N(\2\u022a\u0250\3\2\2\2\u022b\u022c\7\t\2\2\u022c")
        buf.write("\u022d\5N(\2\u022d\u022e\7\20\2\2\u022e\u022f\7\3\2\2")
        buf.write("\u022f\u0230\5,\27\2\u0230\u0231\7\65\2\2\u0231\u0232")
        buf.write("\7:\2\2\u0232\u0250\3\2\2\2\u0233\u0234\7\13\2\2\u0234")
        buf.write("\u0236\7\3\2\2\u0235\u0237\5,\27\2\u0236\u0235\3\2\2\2")
        buf.write("\u0236\u0237\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u023a\7")
        buf.write(":\2\2\u0239\u023b\5,\27\2\u023a\u0239\3\2\2\2\u023a\u023b")
        buf.write("\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023e\7:\2\2\u023d")
        buf.write("\u023f\5,\27\2\u023e\u023d\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0240\3\2\2\2\u0240\u0241\7\65\2\2\u0241\u0250")
        buf.write("\5N(\2\u0242\u0243\7\13\2\2\u0243\u0244\7\3\2\2\u0244")
        buf.write("\u0246\5\6\4\2\u0245\u0247\5,\27\2\u0246\u0245\3\2\2\2")
        buf.write("\u0246\u0247\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024a\7")
        buf.write(":\2\2\u0249\u024b\5,\27\2\u024a\u0249\3\2\2\2\u024a\u024b")
        buf.write("\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024d\7\65\2\2\u024d")
        buf.write("\u024e\5N(\2\u024e\u0250\3\2\2\2\u024f\u0225\3\2\2\2\u024f")
        buf.write("\u022b\3\2\2\2\u024f\u0233\3\2\2\2\u024f\u0242\3\2\2\2")
        buf.write("\u0250[\3\2\2\2\u0251\u0252\7\b\2\2\u0252\u025b\7:\2\2")
        buf.write("\u0253\u0254\7\4\2\2\u0254\u025b\7:\2\2\u0255\u0257\7")
        buf.write("\16\2\2\u0256\u0258\5,\27\2\u0257\u0256\3\2\2\2\u0257")
        buf.write("\u0258\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025b\7:\2\2")
        buf.write("\u025a\u0251\3\2\2\2\u025a\u0253\3\2\2\2\u025a\u0255\3")
        buf.write("\2\2\2\u025b]\3\2\2\2B_flns\177\u0087\u0093\u009d\u00a1")
        buf.write("\u00ae\u00b3\u00be\u00c1\u00c3\u00cb\u00d5\u00e2\u00e7")
        buf.write("\u00ed\u00f3\u00f8\u0103\u010b\u011b\u0123\u012b\u0135")
        buf.write("\u0140\u014b\u0156\u0161\u016d\u016f\u0181\u0183\u018f")
        buf.write("\u0191\u019d\u019f\u01ae\u01b0\u01c1\u01ce\u01d8\u01df")
        buf.write("\u01e1\u01ec\u01f4\u01fa\u0201\u0205\u0210\u0215\u0218")
        buf.write("\u0223\u0236\u023a\u023e\u0246\u024a\u024f\u0257\u025a")
        return buf.getvalue()
		

class HerocParserParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__3=1
    T__2=2
    T__1=3
    T__0=4
    BREAK=5
    CONTINUE=6
    DO=7
    ELSE=8
    FOR=9
    IF=10
    LONG=11
    RETURN=12
    SIZEOF=13
    WHILE=14
    NOT=15
    NOT_EQUAL=16
    MOD=17
    MOD_ASIGN=18
    AND=19
    AND_AND=20
    AND_ASSIGN=21
    STAR=22
    STAR_ASSIGN=23
    PLUS=24
    PLUS_PLUS=25
    PLUS_ASSIGN=26
    MINUS=27
    MINUS_MINUS=28
    MINUS_ASSIGN=29
    DIV=30
    DIV_ASSIGN=31
    COLON=32
    LESS=33
    LEFT_SHIFT=34
    LEFT_SHIFT_ASSIGN=35
    LESS_EQUAL=36
    ASSIGN=37
    EQUAL=38
    GREATER=39
    GREATER_EQUAL=40
    RIGHT_SHIFT=41
    RIGHT_SHIFT_ASSIGN=42
    QUESTION=43
    CARET=44
    XOR_ASSIGN=45
    OR=46
    OR_ASSIGN=47
    OR_OR=48
    TILDE=49
    LEFT_PAREN=50
    RIGHT_PAREN=51
    LEFT_BRACKET=52
    RIGHT_BRACKET=53
    LEFT_BRACE=54
    RIGHT_BRACE=55
    SEMI=56
    COMMA=57
    IDENTIFIER=58
    CONSTANT=59
    INT_CONSTANT=60
    OCTAL_CONSTANT=61
    HEX_CONSTANT=62
    CHAR_CONSTANT=63
    STRING=64
    WHITESPACE=65
    NEWLINE=66
    COMMENT=67

    tokenNames = [ "<INVALID>", "'('", "'break'", "'...'", "'!'", "BREAK", 
                   "'continue'", "'do'", "'else'", "'for'", "'if'", "'long'", 
                   "'return'", "'sizeof'", "'while'", "NOT", "'!='", "'%'", 
                   "'%='", "'&'", "'&&'", "'&='", "'*'", "'*='", "'+'", 
                   "'++'", "'+='", "'-'", "'--'", "'-='", "'/'", "'/='", 
                   "':'", "'<'", "'<<'", "'<<='", "'<='", "'='", "'=='", 
                   "'>'", "'>='", "'>>'", "'>>='", "'?'", "'^'", "'^='", 
                   "'|'", "'|='", "'||'", "'~'", "LEFT_PAREN", "')'", "'['", 
                   "']'", "'{'", "'}'", "';'", "','", "IDENTIFIER", "CONSTANT", 
                   "INT_CONSTANT", "OCTAL_CONSTANT", "HEX_CONSTANT", "CHAR_CONSTANT", 
                   "STRING", "WHITESPACE", "NEWLINE", "COMMENT" ]

    RULE_program = 0
    RULE_source = 1
    RULE_variableDeclaration = 2
    RULE_initVariableDeclarationList = 3
    RULE_initDeclaratorVariable = 4
    RULE_initializer = 5
    RULE_initializerList = 6
    RULE_declarator = 7
    RULE_pointer = 8
    RULE_directDeclarator = 9
    RULE_parameterTypeList = 10
    RULE_parameterList = 11
    RULE_parameterDeclaration = 12
    RULE_identifierList = 13
    RULE_functionDefinition = 14
    RULE_declarationList = 15
    RULE_initDeclaratorList = 16
    RULE_initDeclarator = 17
    RULE_unaryOperator = 18
    RULE_assignmentOperator = 19
    RULE_constantExpression = 20
    RULE_expression = 21
    RULE_assignmentExpression = 22
    RULE_conditionalExpression = 23
    RULE_logicalOrExpression = 24
    RULE_logicalAndExpression = 25
    RULE_bitwiseOrExpression = 26
    RULE_bitwiseXOrExpression = 27
    RULE_andExpression = 28
    RULE_equalityExpression = 29
    RULE_relationalExpression = 30
    RULE_shiftExpression = 31
    RULE_additiveExpression = 32
    RULE_multiplicativeExpression = 33
    RULE_unaryExpression = 34
    RULE_postfixExpression = 35
    RULE_argumentExpressionList = 36
    RULE_primaryExpression = 37
    RULE_statement = 38
    RULE_compoundStatement = 39
    RULE_blockItemList = 40
    RULE_blockItem = 41
    RULE_expressionStatement = 42
    RULE_selectionStatement = 43
    RULE_iterationStatement = 44
    RULE_jumpStatement = 45

    ruleNames =  [ "program", "source", "variableDeclaration", "initVariableDeclarationList", 
                   "initDeclaratorVariable", "initializer", "initializerList", 
                   "declarator", "pointer", "directDeclarator", "parameterTypeList", 
                   "parameterList", "parameterDeclaration", "identifierList", 
                   "functionDefinition", "declarationList", "initDeclaratorList", 
                   "initDeclarator", "unaryOperator", "assignmentOperator", 
                   "constantExpression", "expression", "assignmentExpression", 
                   "conditionalExpression", "logicalOrExpression", "logicalAndExpression", 
                   "bitwiseOrExpression", "bitwiseXOrExpression", "andExpression", 
                   "equalityExpression", "relationalExpression", "shiftExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "postfixExpression", "argumentExpressionList", "primaryExpression", 
                   "statement", "compoundStatement", "blockItemList", "blockItem", 
                   "expressionStatement", "selectionStatement", "iterationStatement", 
                   "jumpStatement" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def source(self):
            return self.getTypedRuleContext(HerocParserParser.SourceContext,0)


        def EOF(self):
            return self.getToken(HerocParserParser.EOF, 0)

        def getRuleIndex(self):
            return HerocParserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitProgram(self)




    def program(self):

        localctx = HerocParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.LONG) | (1 << self.STAR) | (1 << self.IDENTIFIER))) != 0):
                self.state = 92 
                self.source(0)


            self.state = 95
            self.match(self.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def source(self):
            return self.getTypedRuleContext(HerocParserParser.SourceContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(HerocParserParser.VariableDeclarationContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(HerocParserParser.FunctionDefinitionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_source

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitSource(self)



    def source(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.SourceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_source, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            token = self._input.LA(1)
            if token in [self.LONG]:
                self.state = 98 
                self.variableDeclaration()

            elif token in [self.T__3, self.STAR, self.IDENTIFIER]:
                self.state = 99 
                self.functionDefinition()

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 106
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.SourceContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_source)
                        self.state = 102
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 103 
                        self.variableDeclaration()
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.SourceContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_source)
                        self.state = 104
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 105 
                        self.functionDefinition()
                        pass

             
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LONG(self):
            return self.getToken(HerocParserParser.LONG, 0)

        def initVariableDeclarationList(self):
            return self.getTypedRuleContext(HerocParserParser.InitVariableDeclarationListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = HerocParserParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(self.LONG)
            self.state = 113
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.STAR) | (1 << self.IDENTIFIER))) != 0):
                self.state = 112 
                self.initVariableDeclarationList(0)


            self.state = 115
            self.match(self.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitVariableDeclarationListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initDeclaratorVariable(self):
            return self.getTypedRuleContext(HerocParserParser.InitDeclaratorVariableContext,0)


        def initVariableDeclarationList(self):
            return self.getTypedRuleContext(HerocParserParser.InitVariableDeclarationListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_initVariableDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterInitVariableDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitInitVariableDeclarationList(self)



    def initVariableDeclarationList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.InitVariableDeclarationListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_initVariableDeclarationList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118 
            self.initDeclaratorVariable()
            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitVariableDeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initVariableDeclarationList)
                    self.state = 120
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 121
                    self.match(self.COMMA)
                    self.state = 122 
                    self.initDeclaratorVariable() 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class InitDeclaratorVariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(HerocParserParser.DeclaratorContext,0)


        def initializer(self):
            return self.getTypedRuleContext(HerocParserParser.InitializerContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_initDeclaratorVariable

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterInitDeclaratorVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitInitDeclaratorVariable(self)




    def initDeclaratorVariable(self):

        localctx = HerocParserParser.InitDeclaratorVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_initDeclaratorVariable)
        try:
            self.state = 133
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128 
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129 
                self.declarator()
                self.state = 130
                self.match(self.ASSIGN)
                self.state = 131 
                self.initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AssignmentExpressionContext,0)


        def initializerList(self):
            return self.getTypedRuleContext(HerocParserParser.InitializerListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_initializer

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitInitializer(self)




    def initializer(self):

        localctx = HerocParserParser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_initializer)
        try:
            self.state = 145
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135 
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(self.LEFT_BRACE)
                self.state = 137 
                self.initializerList(0)
                self.state = 138
                self.match(self.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.match(self.LEFT_BRACE)
                self.state = 141 
                self.initializerList(0)
                self.state = 142
                self.match(self.COMMA)
                self.state = 143
                self.match(self.RIGHT_BRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializerList(self):
            return self.getTypedRuleContext(HerocParserParser.InitializerListContext,0)


        def initializer(self):
            return self.getTypedRuleContext(HerocParserParser.InitializerContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_initializerList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterInitializerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitInitializerList(self)



    def initializerList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.InitializerListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_initializerList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148 
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 150
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 151
                    self.match(self.COMMA)
                    self.state = 152 
                    self.initializer() 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directDeclarator(self):
            return self.getTypedRuleContext(HerocParserParser.DirectDeclaratorContext,0)


        def pointer(self):
            return self.getTypedRuleContext(HerocParserParser.PointerContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_declarator

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitDeclarator(self)




    def declarator(self):

        localctx = HerocParserParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if _la==HerocParserParser.STAR:
                self.state = 158 
                self.pointer()


            self.state = 161 
            self.directDeclarator(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PointerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pointer(self):
            return self.getTypedRuleContext(HerocParserParser.PointerContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_pointer

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitPointer(self)




    def pointer(self):

        localctx = HerocParserParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(self.STAR)
            self.state = 164 
            self.pointer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directDeclarator(self):
            return self.getTypedRuleContext(HerocParserParser.DirectDeclaratorContext,0)


        def declarator(self):
            return self.getTypedRuleContext(HerocParserParser.DeclaratorContext,0)


        def identifierList(self):
            return self.getTypedRuleContext(HerocParserParser.IdentifierListContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AssignmentExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def parameterTypeList(self):
            return self.getTypedRuleContext(HerocParserParser.ParameterTypeListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_directDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterDirectDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitDirectDeclarator(self)



    def directDeclarator(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.DirectDeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_directDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.state = 167
                self.match(self.IDENTIFIER)

            elif token in [self.T__3]:
                self.state = 168
                self.match(self.T__3)
                self.state = 169 
                self.declarator()
                self.state = 170
                self.match(self.RIGHT_PAREN)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 191
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 174
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 175
                        self.match(self.LEFT_BRACKET)
                        self.state = 177
                        _la = self._input.LA(1)
                        if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                            self.state = 176 
                            self.assignmentExpression()


                        self.state = 179
                        self.match(self.RIGHT_BRACKET)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 180
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 181
                        self.match(self.T__3)
                        self.state = 182 
                        self.parameterTypeList()
                        self.state = 183
                        self.match(self.RIGHT_PAREN)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 185
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 186
                        self.match(self.T__3)
                        self.state = 188
                        _la = self._input.LA(1)
                        if _la==HerocParserParser.IDENTIFIER:
                            self.state = 187 
                            self.identifierList(0)


                        self.state = 190
                        self.match(self.RIGHT_PAREN)
                        pass

             
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParameterTypeListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterList(self):
            return self.getTypedRuleContext(HerocParserParser.ParameterListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_parameterTypeList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterParameterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitParameterTypeList(self)




    def parameterTypeList(self):

        localctx = HerocParserParser.ParameterTypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameterTypeList)
        try:
            self.state = 201
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196 
                self.parameterList(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197 
                self.parameterList(0)
                self.state = 198
                self.match(self.COMMA)
                self.state = 199
                self.match(self.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameterDeclaration(self):
            return self.getTypedRuleContext(HerocParserParser.ParameterDeclarationContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(HerocParserParser.ParameterListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitParameterList(self)



    def parameterList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.ParameterListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_parameterList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204 
            self.parameterDeclaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ParameterListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterList)
                    self.state = 206
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 207
                    self.match(self.COMMA)
                    self.state = 208 
                    self.parameterDeclaration() 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParameterDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(HerocParserParser.DeclaratorContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_parameterDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterParameterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitParameterDeclaration(self)




    def parameterDeclaration(self):

        localctx = HerocParserParser.ParameterDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameterDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214 
            self.declarator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(HerocParserParser.IdentifierListContext,0)


        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return HerocParserParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitIdentifierList(self)



    def identifierList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.IdentifierListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_identifierList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(self.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.IdentifierListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_identifierList)
                    self.state = 219
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 220
                    self.match(self.COMMA)
                    self.state = 221
                    self.match(self.IDENTIFIER) 
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FunctionDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(HerocParserParser.DeclaratorContext,0)


        def declarationList(self):
            return self.getTypedRuleContext(HerocParserParser.DeclarationListContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(HerocParserParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = HerocParserParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227 
            self.declarator()
            self.state = 229
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.STAR) | (1 << self.SEMI) | (1 << self.IDENTIFIER))) != 0):
                self.state = 228 
                self.declarationList(0)


            self.state = 231 
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationList(self):
            return self.getTypedRuleContext(HerocParserParser.DeclarationListContext,0)


        def initDeclaratorList(self):
            return self.getTypedRuleContext(HerocParserParser.InitDeclaratorListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_declarationList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitDeclarationList(self)



    def declarationList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.DeclarationListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_declarationList, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.STAR) | (1 << self.IDENTIFIER))) != 0):
                self.state = 234 
                self.initDeclaratorList(0)


            self.state = 237
            self.match(self.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.DeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationList)
                    self.state = 239
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 241
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.STAR) | (1 << self.IDENTIFIER))) != 0):
                        self.state = 240 
                        self.initDeclaratorList(0)


                    self.state = 243
                    self.match(self.SEMI) 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class InitDeclaratorListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initDeclarator(self):
            return self.getTypedRuleContext(HerocParserParser.InitDeclaratorContext,0)


        def initDeclaratorList(self):
            return self.getTypedRuleContext(HerocParserParser.InitDeclaratorListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_initDeclaratorList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterInitDeclaratorList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitInitDeclaratorList(self)



    def initDeclaratorList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.InitDeclaratorListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_initDeclaratorList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250 
            self.initDeclarator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitDeclaratorListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initDeclaratorList)
                    self.state = 252
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 253
                    self.match(self.COMMA)
                    self.state = 254 
                    self.initDeclarator() 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class InitDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(HerocParserParser.DeclaratorContext,0)


        def initializer(self):
            return self.getTypedRuleContext(HerocParserParser.InitializerContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_initDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterInitDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitInitDeclarator(self)




    def initDeclarator(self):

        localctx = HerocParserParser.InitDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_initDeclarator)
        try:
            self.state = 265
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260 
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261 
                self.declarator()
                self.state = 262
                self.match(self.ASSIGN)
                self.state = 263 
                self.initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HerocParserParser.RULE_unaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitUnaryOperator(self)




    def unaryOperator(self):

        localctx = HerocParserParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__0) | (1 << self.AND) | (1 << self.STAR) | (1 << self.PLUS) | (1 << self.MINUS) | (1 << self.TILDE))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HerocParserParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitAssignmentOperator(self)




    def assignmentOperator(self):

        localctx = HerocParserParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.MOD_ASIGN) | (1 << self.AND_ASSIGN) | (1 << self.STAR_ASSIGN) | (1 << self.PLUS_ASSIGN) | (1 << self.MINUS_ASSIGN) | (1 << self.DIV_ASSIGN) | (1 << self.LEFT_SHIFT_ASSIGN) | (1 << self.ASSIGN) | (1 << self.RIGHT_SHIFT_ASSIGN) | (1 << self.XOR_ASSIGN) | (1 << self.OR_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(HerocParserParser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_constantExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitConstantExpression(self)




    def constantExpression(self):

        localctx = HerocParserParser.ConstantExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271 
            self.conditionalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AssignmentExpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274 
            self.assignmentExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 276
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 277
                    self.match(self.COMMA)
                    self.state = 278 
                    self.assignmentExpression() 
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AssignmentExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(HerocParserParser.ConditionalExpressionContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(HerocParserParser.UnaryExpressionContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AssignmentExpressionContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(HerocParserParser.AssignmentOperatorContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_assignmentExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitAssignmentExpression(self)




    def assignmentExpression(self):

        localctx = HerocParserParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignmentExpression)
        try:
            self.state = 289
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284 
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285 
                self.unaryExpression()
                self.state = 286 
                self.assignmentOperator()
                self.state = 287 
                self.assignmentExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionalExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(HerocParserParser.ConditionalExpressionContext,0)


        def logicalOrExpression(self):
            return self.getTypedRuleContext(HerocParserParser.LogicalOrExpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_conditionalExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterConditionalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitConditionalExpression(self)




    def conditionalExpression(self):

        localctx = HerocParserParser.ConditionalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_conditionalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291 
            self.logicalOrExpression(0)
            self.state = 297
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 292
                self.match(self.QUESTION)
                self.state = 293 
                self.expression(0)
                self.state = 294
                self.match(self.COLON)
                self.state = 295 
                self.conditionalExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LogicalOrExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(HerocParserParser.LogicalOrExpressionContext,0)


        def logicalAndExpression(self):
            return self.getTypedRuleContext(HerocParserParser.LogicalAndExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitLogicalOrExpression(self)



    def logicalOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.LogicalOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_logicalOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300 
            self.logicalAndExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                    self.state = 302
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 303
                    self.match(self.OR_OR)
                    self.state = 304 
                    self.logicalAndExpression(0) 
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class LogicalAndExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseOrExpression(self):
            return self.getTypedRuleContext(HerocParserParser.BitwiseOrExpressionContext,0)


        def logicalAndExpression(self):
            return self.getTypedRuleContext(HerocParserParser.LogicalAndExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitLogicalAndExpression(self)



    def logicalAndExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.LogicalAndExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_logicalAndExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311 
            self.bitwiseOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.LogicalAndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalAndExpression)
                    self.state = 313
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 314
                    self.match(self.AND_AND)
                    self.state = 315 
                    self.bitwiseOrExpression(0) 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BitwiseOrExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseXOrExpression(self):
            return self.getTypedRuleContext(HerocParserParser.BitwiseXOrExpressionContext,0)


        def bitwiseOrExpression(self):
            return self.getTypedRuleContext(HerocParserParser.BitwiseOrExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_bitwiseOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterBitwiseOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitBitwiseOrExpression(self)



    def bitwiseOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.BitwiseOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_bitwiseOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322 
            self.bitwiseXOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BitwiseOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseOrExpression)
                    self.state = 324
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 325
                    self.match(self.OR)
                    self.state = 326 
                    self.bitwiseXOrExpression(0) 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BitwiseXOrExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AndExpressionContext,0)


        def bitwiseXOrExpression(self):
            return self.getTypedRuleContext(HerocParserParser.BitwiseXOrExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_bitwiseXOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterBitwiseXOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitBitwiseXOrExpression(self)



    def bitwiseXOrExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.BitwiseXOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_bitwiseXOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333 
            self.andExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BitwiseXOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseXOrExpression)
                    self.state = 335
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 336
                    self.match(self.CARET)
                    self.state = 337 
                    self.andExpression(0) 
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AndExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AndExpressionContext,0)


        def equalityExpression(self):
            return self.getTypedRuleContext(HerocParserParser.EqualityExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_andExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitAndExpression(self)



    def andExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.AndExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_andExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344 
            self.equalityExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.AndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpression)
                    self.state = 346
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 347
                    self.match(self.AND)
                    self.state = 348 
                    self.equalityExpression(0) 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class EqualityExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self):
            return self.getTypedRuleContext(HerocParserParser.RelationalExpressionContext,0)


        def equalityExpression(self):
            return self.getTypedRuleContext(HerocParserParser.EqualityExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitEqualityExpression(self)



    def equalityExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.EqualityExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_equalityExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355 
            self.relationalExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 363
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 357
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 358
                        self.match(self.EQUAL)
                        self.state = 359 
                        self.relationalExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 360
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 361
                        self.match(self.NOT_EQUAL)
                        self.state = 362 
                        self.relationalExpression(0)
                        pass

             
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class RelationalExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self):
            return self.getTypedRuleContext(HerocParserParser.RelationalExpressionContext,0)


        def shiftExpression(self):
            return self.getTypedRuleContext(HerocParserParser.ShiftExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitRelationalExpression(self)



    def relationalExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.RelationalExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_relationalExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369 
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 383
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 371
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 372
                        self.match(self.LESS)
                        self.state = 373 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 374
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 375
                        self.match(self.GREATER)
                        self.state = 376 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 377
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 378
                        self.match(self.LESS_EQUAL)
                        self.state = 379 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 4:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 380
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 381
                        self.match(self.GREATER_EQUAL)
                        self.state = 382 
                        self.shiftExpression(0)
                        pass

             
                self.state = 387
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ShiftExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AdditiveExpressionContext,0)


        def shiftExpression(self):
            return self.getTypedRuleContext(HerocParserParser.ShiftExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_shiftExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitShiftExpression(self)



    def shiftExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.ShiftExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_shiftExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389 
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 397
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 391
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 392
                        self.match(self.LEFT_SHIFT)
                        self.state = 393 
                        self.additiveExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 394
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 395
                        self.match(self.RIGHT_SHIFT)
                        self.state = 396 
                        self.additiveExpression(0)
                        pass

             
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AdditiveExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self):
            return self.getTypedRuleContext(HerocParserParser.MultiplicativeExpressionContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitAdditiveExpression(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403 
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 411
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 405
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 406
                        self.match(self.PLUS)
                        self.state = 407 
                        self.multiplicativeExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 408
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 409
                        self.match(self.MINUS)
                        self.state = 410 
                        self.multiplicativeExpression(0)
                        pass

             
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MultiplicativeExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(HerocParserParser.UnaryExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(HerocParserParser.MultiplicativeExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitMultiplicativeExpression(self)



    def multiplicativeExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.MultiplicativeExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_multiplicativeExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417 
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 428
                    la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 419
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 420
                        self.match(self.STAR)
                        self.state = 421 
                        self.unaryExpression()
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 422
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 423
                        self.match(self.DIV)
                        self.state = 424 
                        self.unaryExpression()
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 425
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 426
                        self.match(self.MOD)
                        self.state = 427 
                        self.unaryExpression()
                        pass

             
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class UnaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(HerocParserParser.PostfixExpressionContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(HerocParserParser.UnaryExpressionContext,0)


        def LONG(self):
            return self.getToken(HerocParserParser.LONG, 0)

        def unaryOperator(self):
            return self.getTypedRuleContext(HerocParserParser.UnaryOperatorContext,0)


        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return HerocParserParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitUnaryExpression(self)




    def unaryExpression(self):

        localctx = HerocParserParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_unaryExpression)
        try:
            self.state = 447
            token = self._input.LA(1)
            if token in [self.T__3, self.LEFT_BRACE, self.IDENTIFIER, self.CONSTANT, self.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 433 
                self.postfixExpression(0)

            elif token in [self.PLUS_PLUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(self.PLUS_PLUS)
                self.state = 435 
                self.unaryExpression()

            elif token in [self.MINUS_MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.match(self.MINUS_MINUS)
                self.state = 437 
                self.unaryExpression()

            elif token in [self.T__0, self.AND, self.STAR, self.PLUS, self.MINUS, self.TILDE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 438 
                self.unaryOperator()
                self.state = 439 
                self.unaryExpression()

            elif token in [self.SIZEOF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 441
                self.match(self.SIZEOF)
                self.state = 442
                self.match(self.T__3)
                self.state = 443
                self.match(self.LONG)
                self.state = 444
                self.match(self.RIGHT_PAREN)

            elif token in [self.AND_AND]:
                self.enterOuterAlt(localctx, 6)
                self.state = 445
                self.match(self.AND_AND)
                self.state = 446
                self.match(self.IDENTIFIER)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PostfixExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpression(self):
            return self.getTypedRuleContext(HerocParserParser.PostfixExpressionContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(HerocParserParser.PrimaryExpressionContext,0)


        def initializerList(self):
            return self.getTypedRuleContext(HerocParserParser.InitializerListContext,0)


        def expression(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionContext,0)


        def argumentExpressionList(self):
            return self.getTypedRuleContext(HerocParserParser.ArgumentExpressionListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_postfixExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterPostfixExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitPostfixExpression(self)



    def postfixExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.PostfixExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_postfixExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 450 
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.state = 451
                self.match(self.LEFT_BRACE)
                self.state = 452 
                self.initializerList(0)
                self.state = 453
                self.match(self.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.state = 455
                self.match(self.LEFT_BRACE)
                self.state = 456 
                self.initializerList(0)
                self.state = 457
                self.match(self.COMMA)
                self.state = 458
                self.match(self.RIGHT_BRACE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 479
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 477
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 462
                        if not self.precpred(self._ctx, 6):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 463
                        self.match(self.LEFT_BRACKET)
                        self.state = 464 
                        self.expression(0)
                        self.state = 465
                        self.match(self.RIGHT_BRACKET)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 467
                        if not self.precpred(self._ctx, 5):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 468
                        self.match(self.T__3)
                        self.state = 470
                        _la = self._input.LA(1)
                        if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                            self.state = 469 
                            self.argumentExpressionList(0)


                        self.state = 472
                        self.match(self.RIGHT_PAREN)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 473
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 474
                        self.match(self.PLUS_PLUS)
                        pass

                    elif la_ == 4:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 475
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 476
                        self.match(self.MINUS_MINUS)
                        pass

             
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgumentExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(HerocParserParser.AssignmentExpressionContext,0)


        def argumentExpressionList(self):
            return self.getTypedRuleContext(HerocParserParser.ArgumentExpressionListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_argumentExpressionList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterArgumentExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitArgumentExpressionList(self)



    def argumentExpressionList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.ArgumentExpressionListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_argumentExpressionList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483 
            self.assignmentExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ArgumentExpressionListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argumentExpressionList)
                    self.state = 485
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 486
                    self.match(self.COMMA)
                    self.state = 487 
                    self.assignmentExpression() 
                self.state = 492
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class PrimaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(HerocParserParser.STRING)
            else:
                return self.getToken(HerocParserParser.STRING, i)

        def CONSTANT(self):
            return self.getToken(HerocParserParser.CONSTANT, 0)

        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitPrimaryExpression(self)




    def primaryExpression(self):

        localctx = HerocParserParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_primaryExpression)
        try:
            self.state = 504
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.match(self.IDENTIFIER)

            elif token in [self.CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.match(self.CONSTANT)

            elif token in [self.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 496 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 495
                        self.match(self.STRING)

                    else:
                        raise NoViableAltException(self)
                    self.state = 498 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,48,self._ctx)


            elif token in [self.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 500
                self.match(self.T__3)
                self.state = 501 
                self.expression(0)
                self.state = 502
                self.match(self.RIGHT_PAREN)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStatement(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionStatementContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(HerocParserParser.JumpStatementContext,0)


        def selectionStatement(self):
            return self.getTypedRuleContext(HerocParserParser.SelectionStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(HerocParserParser.IterationStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(HerocParserParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitStatement(self)




    def statement(self):

        localctx = HerocParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_statement)
        try:
            self.state = 511
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506 
                self.compoundStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507 
                self.expressionStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 508 
                self.selectionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 509 
                self.iterationStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 510 
                self.jumpStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompoundStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockItemList(self):
            return self.getTypedRuleContext(HerocParserParser.BlockItemListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitCompoundStatement(self)




    def compoundStatement(self):

        localctx = HerocParserParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(self.LEFT_BRACE)
            self.state = 515
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__2 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.CONTINUE - 1)) | (1 << (self.DO - 1)) | (1 << (self.FOR - 1)) | (1 << (self.IF - 1)) | (1 << (self.LONG - 1)) | (1 << (self.RETURN - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.WHILE - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.SEMI - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                self.state = 514 
                self.blockItemList(0)


            self.state = 517
            self.match(self.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockItemListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockItem(self):
            return self.getTypedRuleContext(HerocParserParser.BlockItemContext,0)


        def blockItemList(self):
            return self.getTypedRuleContext(HerocParserParser.BlockItemListContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_blockItemList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterBlockItemList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitBlockItemList(self)



    def blockItemList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HerocParserParser.BlockItemListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_blockItemList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520 
            self.blockItem()
            self._ctx.stop = self._input.LT(-1)
            self.state = 526
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BlockItemListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_blockItemList)
                    self.state = 522
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 523 
                    self.blockItem() 
                self.state = 528
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BlockItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(HerocParserParser.VariableDeclarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(HerocParserParser.StatementContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_blockItem

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterBlockItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitBlockItem(self)




    def blockItem(self):

        localctx = HerocParserParser.BlockItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_blockItem)
        try:
            self.state = 531
            token = self._input.LA(1)
            if token in [self.LONG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 529 
                self.variableDeclaration()

            elif token in [self.T__3, self.T__2, self.T__0, self.CONTINUE, self.DO, self.FOR, self.IF, self.RETURN, self.SIZEOF, self.WHILE, self.AND, self.AND_AND, self.STAR, self.PLUS, self.PLUS_PLUS, self.MINUS, self.MINUS_MINUS, self.TILDE, self.LEFT_BRACE, self.SEMI, self.IDENTIFIER, self.CONSTANT, self.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 530 
                self.statement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = HerocParserParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                self.state = 533 
                self.expression(0)


            self.state = 536
            self.match(self.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelectionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HerocParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(HerocParserParser.StatementContext,i)


        def expression(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_selectionStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterSelectionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitSelectionStatement(self)




    def selectionStatement(self):

        localctx = HerocParserParser.SelectionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_selectionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.match(self.IF)
            self.state = 539
            self.match(self.T__3)
            self.state = 540 
            self.expression(0)
            self.state = 541
            self.match(self.RIGHT_PAREN)
            self.state = 542 
            self.statement()
            self.state = 545
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 543
                self.match(self.ELSE)
                self.state = 544 
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(HerocParserParser.VariableDeclarationContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HerocParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(HerocParserParser.ExpressionContext,i)


        def statement(self):
            return self.getTypedRuleContext(HerocParserParser.StatementContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_iterationStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterIterationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitIterationStatement(self)




    def iterationStatement(self):

        localctx = HerocParserParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 589
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.match(self.WHILE)
                self.state = 548
                self.match(self.T__3)
                self.state = 549 
                self.expression(0)
                self.state = 550
                self.match(self.RIGHT_PAREN)
                self.state = 551 
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.match(self.DO)
                self.state = 554 
                self.statement()
                self.state = 555
                self.match(self.WHILE)
                self.state = 556
                self.match(self.T__3)
                self.state = 557 
                self.expression(0)
                self.state = 558
                self.match(self.RIGHT_PAREN)
                self.state = 559
                self.match(self.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 561
                self.match(self.FOR)
                self.state = 562
                self.match(self.T__3)
                self.state = 564
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 563 
                    self.expression(0)


                self.state = 566
                self.match(self.SEMI)
                self.state = 568
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 567 
                    self.expression(0)


                self.state = 570
                self.match(self.SEMI)
                self.state = 572
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 571 
                    self.expression(0)


                self.state = 574
                self.match(self.RIGHT_PAREN)
                self.state = 575 
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 576
                self.match(self.FOR)
                self.state = 577
                self.match(self.T__3)
                self.state = 578 
                self.variableDeclaration()
                self.state = 580
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 579 
                    self.expression(0)


                self.state = 582
                self.match(self.SEMI)
                self.state = 584
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 583 
                    self.expression(0)


                self.state = 586
                self.match(self.RIGHT_PAREN)
                self.state = 587 
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JumpStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_jumpStatement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterJumpStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitJumpStatement(self)




    def jumpStatement(self):

        localctx = HerocParserParser.JumpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.state = 600
            token = self._input.LA(1)
            if token in [self.CONTINUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self.match(self.CONTINUE)
                self.state = 592
                self.match(self.SEMI)

            elif token in [self.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.match(self.T__2)
                self.state = 594
                self.match(self.SEMI)

            elif token in [self.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 595
                self.match(self.RETURN)
                self.state = 597
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 596 
                    self.expression(0)


                self.state = 599
                self.match(self.SEMI)

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
        self._predicates[1] = self.source_sempred
        self._predicates[3] = self.initVariableDeclarationList_sempred
        self._predicates[6] = self.initializerList_sempred
        self._predicates[9] = self.directDeclarator_sempred
        self._predicates[11] = self.parameterList_sempred
        self._predicates[13] = self.identifierList_sempred
        self._predicates[15] = self.declarationList_sempred
        self._predicates[16] = self.initDeclaratorList_sempred
        self._predicates[21] = self.expression_sempred
        self._predicates[24] = self.logicalOrExpression_sempred
        self._predicates[25] = self.logicalAndExpression_sempred
        self._predicates[26] = self.bitwiseOrExpression_sempred
        self._predicates[27] = self.bitwiseXOrExpression_sempred
        self._predicates[28] = self.andExpression_sempred
        self._predicates[29] = self.equalityExpression_sempred
        self._predicates[30] = self.relationalExpression_sempred
        self._predicates[31] = self.shiftExpression_sempred
        self._predicates[32] = self.additiveExpression_sempred
        self._predicates[33] = self.multiplicativeExpression_sempred
        self._predicates[35] = self.postfixExpression_sempred
        self._predicates[36] = self.argumentExpressionList_sempred
        self._predicates[40] = self.blockItemList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def identifierList_sempred(self, localctx:IdentifierListContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         

    def shiftExpression_sempred(self, localctx:ShiftExpressionContext, predIndex:int):
            if predIndex == 23:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 1)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 25:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 1)
         

    def relationalExpression_sempred(self, localctx:RelationalExpressionContext, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 1)
         

    def declarationList_sempred(self, localctx:DeclarationListContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         

    def source_sempred(self, localctx:SourceContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def logicalOrExpression_sempred(self, localctx:LogicalOrExpressionContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         

    def multiplicativeExpression_sempred(self, localctx:MultiplicativeExpressionContext, predIndex:int):
            if predIndex == 27:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 28:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 1)
         

    def directDeclarator_sempred(self, localctx:DirectDeclaratorContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def bitwiseXOrExpression_sempred(self, localctx:BitwiseXOrExpressionContext, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 1)
         

    def bitwiseOrExpression_sempred(self, localctx:BitwiseOrExpressionContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def andExpression_sempred(self, localctx:AndExpressionContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 1)
         

    def blockItemList_sempred(self, localctx:BlockItemListContext, predIndex:int):
            if predIndex == 35:
                return self.precpred(self._ctx, 1)
         

    def initVariableDeclarationList_sempred(self, localctx:InitVariableDeclarationListContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def logicalAndExpression_sempred(self, localctx:LogicalAndExpressionContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         

    def equalityExpression_sempred(self, localctx:EqualityExpressionContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 1)
         

    def argumentExpressionList_sempred(self, localctx:ArgumentExpressionListContext, predIndex:int):
            if predIndex == 34:
                return self.precpred(self._ctx, 1)
         

    def parameterList_sempred(self, localctx:ParameterListContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def initDeclaratorList_sempred(self, localctx:InitDeclaratorListContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 1)
         

    def postfixExpression_sempred(self, localctx:PostfixExpressionContext, predIndex:int):
            if predIndex == 32:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 33:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 5)
         

    def initializerList_sempred(self, localctx:InitializerListContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         



