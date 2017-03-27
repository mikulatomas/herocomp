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
        buf.write("\u0258\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\7\2_\n\2\f\2\16\2b\13\2\3\2\3\2\7\2f\n\2\f\2\16")
        buf.write("\2i\13\2\5\2k\n\2\3\3\3\3\5\3o\n\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\4y\n\4\f\4\16\4|\13\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u0083\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\5\6\u008f\n\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0097\n\7")
        buf.write("\f\7\16\7\u009a\13\7\3\b\5\b\u009d\n\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00aa\n\n\3\n\3\n\3\n")
        buf.write("\5\n\u00af\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u00ba\n\n\3\n\7\n\u00bd\n\n\f\n\16\n\u00c0\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00c7\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\7\f\u00cf\n\f\f\f\16\f\u00d2\13\f\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\7\16\u00dc\n\16\f\16\16\16\u00df")
        buf.write("\13\16\3\17\3\17\5\17\u00e3\n\17\3\17\3\17\3\20\3\20\5")
        buf.write("\20\u00e9\n\20\3\20\3\20\3\20\3\20\5\20\u00ef\n\20\3\20")
        buf.write("\7\20\u00f2\n\20\f\20\16\20\u00f5\13\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\7\21\u00fd\n\21\f\21\16\21\u0100\13\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\5\22\u0107\n\22\3\23\3\23\3")
        buf.write("\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26")
        buf.write("\u0115\n\26\f\26\16\26\u0118\13\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u011f\n\27\3\30\3\30\3\30\3\30\3\30\3\30\5")
        buf.write("\30\u0127\n\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u012f")
        buf.write("\n\31\f\31\16\31\u0132\13\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\7\32\u013a\n\32\f\32\16\32\u013d\13\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\7\33\u0145\n\33\f\33\16\33\u0148")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0150\n\34\f")
        buf.write("\34\16\34\u0153\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7")
        buf.write("\35\u015b\n\35\f\35\16\35\u015e\13\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\7\36\u0169\n\36\f\36\16\36")
        buf.write("\u016c\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u017d\n\37\f\37")
        buf.write("\16\37\u0180\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \7 \u018b")
        buf.write("\n \f \16 \u018e\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\7!\u0199")
        buf.write("\n!\f!\16!\u019c\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u01aa\n\"\f\"\16\"\u01ad\13\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u01bd\n#\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01ca\n$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\5$\u01d4\n$\3$\3$\3$\3$\3$\7$\u01db\n$\f$\16")
        buf.write("$\u01de\13$\3%\3%\3%\3%\3%\3%\7%\u01e6\n%\f%\16%\u01e9")
        buf.write("\13%\3&\3&\3&\6&\u01ee\n&\r&\16&\u01ef\3&\3&\3&\3&\5&")
        buf.write("\u01f6\n&\3\'\3\'\3\'\3\'\3\'\5\'\u01fd\n\'\3(\3(\5(\u0201")
        buf.write("\n(\3(\3(\3)\3)\3)\3)\3)\7)\u020a\n)\f)\16)\u020d\13)")
        buf.write("\3*\3*\5*\u0211\n*\3+\5+\u0214\n+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\5,\u021f\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\5-\u0232\n-\3-\3-\5-\u0236\n-\3-\3-\5")
        buf.write("-\u023a\n-\3-\3-\3-\3-\3-\3-\5-\u0242\n-\3-\3-\5-\u0246")
        buf.write("\n-\3-\3-\3-\5-\u024b\n-\3.\3.\3.\3.\3.\3.\5.\u0253\n")
        buf.write(".\3.\5.\u0256\n.\3.\2\27\6\f\22\26\32\36 *\60\62\64\66")
        buf.write("8:<>@BFHP/\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\2\4\b\2\6\6\25\25")
        buf.write("\30\30\32\32\35\35\63\63\r\2\24\24\27\27\31\31\34\34\37")
        buf.write("\37!!%%\'\',,//\61\61\u027d\2j\3\2\2\2\4l\3\2\2\2\6r\3")
        buf.write("\2\2\2\b\u0082\3\2\2\2\n\u008e\3\2\2\2\f\u0090\3\2\2\2")
        buf.write("\16\u009c\3\2\2\2\20\u00a0\3\2\2\2\22\u00a9\3\2\2\2\24")
        buf.write("\u00c6\3\2\2\2\26\u00c8\3\2\2\2\30\u00d3\3\2\2\2\32\u00d5")
        buf.write("\3\2\2\2\34\u00e0\3\2\2\2\36\u00e6\3\2\2\2 \u00f6\3\2")
        buf.write("\2\2\"\u0106\3\2\2\2$\u0108\3\2\2\2&\u010a\3\2\2\2(\u010c")
        buf.write("\3\2\2\2*\u010e\3\2\2\2,\u011e\3\2\2\2.\u0120\3\2\2\2")
        buf.write("\60\u0128\3\2\2\2\62\u0133\3\2\2\2\64\u013e\3\2\2\2\66")
        buf.write("\u0149\3\2\2\28\u0154\3\2\2\2:\u015f\3\2\2\2<\u016d\3")
        buf.write("\2\2\2>\u0181\3\2\2\2@\u018f\3\2\2\2B\u019d\3\2\2\2D\u01bc")
        buf.write("\3\2\2\2F\u01c9\3\2\2\2H\u01df\3\2\2\2J\u01f5\3\2\2\2")
        buf.write("L\u01fc\3\2\2\2N\u01fe\3\2\2\2P\u0204\3\2\2\2R\u0210\3")
        buf.write("\2\2\2T\u0213\3\2\2\2V\u0217\3\2\2\2X\u024a\3\2\2\2Z\u0255")
        buf.write("\3\2\2\2\\`\5\4\3\2]_\5\2\2\2^]\3\2\2\2_b\3\2\2\2`^\3")
        buf.write("\2\2\2`a\3\2\2\2ak\3\2\2\2b`\3\2\2\2cg\5\34\17\2df\5\2")
        buf.write("\2\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2hk\3\2\2\2")
        buf.write("ig\3\2\2\2j\\\3\2\2\2jc\3\2\2\2k\3\3\2\2\2ln\7\r\2\2m")
        buf.write("o\5\6\4\2nm\3\2\2\2no\3\2\2\2op\3\2\2\2pq\7:\2\2q\5\3")
        buf.write("\2\2\2rs\b\4\1\2st\5\b\5\2tz\3\2\2\2uv\f\3\2\2vw\7;\2")
        buf.write("\2wy\5\b\5\2xu\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{")
        buf.write("\7\3\2\2\2|z\3\2\2\2}\u0083\5\16\b\2~\177\5\16\b\2\177")
        buf.write("\u0080\7\'\2\2\u0080\u0081\5\n\6\2\u0081\u0083\3\2\2\2")
        buf.write("\u0082}\3\2\2\2\u0082~\3\2\2\2\u0083\t\3\2\2\2\u0084\u008f")
        buf.write("\5,\27\2\u0085\u0086\78\2\2\u0086\u0087\5\f\7\2\u0087")
        buf.write("\u0088\79\2\2\u0088\u008f\3\2\2\2\u0089\u008a\78\2\2\u008a")
        buf.write("\u008b\5\f\7\2\u008b\u008c\7;\2\2\u008c\u008d\79\2\2\u008d")
        buf.write("\u008f\3\2\2\2\u008e\u0084\3\2\2\2\u008e\u0085\3\2\2\2")
        buf.write("\u008e\u0089\3\2\2\2\u008f\13\3\2\2\2\u0090\u0091\b\7")
        buf.write("\1\2\u0091\u0092\5\n\6\2\u0092\u0098\3\2\2\2\u0093\u0094")
        buf.write("\f\3\2\2\u0094\u0095\7;\2\2\u0095\u0097\5\n\6\2\u0096")
        buf.write("\u0093\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2")
        buf.write("\u0098\u0099\3\2\2\2\u0099\r\3\2\2\2\u009a\u0098\3\2\2")
        buf.write("\2\u009b\u009d\5\20\t\2\u009c\u009b\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\5\22\n\2\u009f")
        buf.write("\17\3\2\2\2\u00a0\u00a1\7\30\2\2\u00a1\u00a2\5\20\t\2")
        buf.write("\u00a2\21\3\2\2\2\u00a3\u00a4\b\n\1\2\u00a4\u00aa\7<\2")
        buf.write("\2\u00a5\u00a6\7\3\2\2\u00a6\u00a7\5\16\b\2\u00a7\u00a8")
        buf.write("\7\65\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a3\3\2\2\2\u00a9")
        buf.write("\u00a5\3\2\2\2\u00aa\u00be\3\2\2\2\u00ab\u00ac\f\5\2\2")
        buf.write("\u00ac\u00ae\7\66\2\2\u00ad\u00af\5,\27\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\u00bd\7\67\2\2\u00b1\u00b2\f\4\2\2\u00b2\u00b3\7\3\2")
        buf.write("\2\u00b3\u00b4\5\24\13\2\u00b4\u00b5\7\65\2\2\u00b5\u00bd")
        buf.write("\3\2\2\2\u00b6\u00b7\f\3\2\2\u00b7\u00b9\7\3\2\2\u00b8")
        buf.write("\u00ba\5\32\16\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2")
        buf.write("\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\7\65\2\2\u00bc\u00ab")
        buf.write("\3\2\2\2\u00bc\u00b1\3\2\2\2\u00bc\u00b6\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\23\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c7\5\26")
        buf.write("\f\2\u00c2\u00c3\5\26\f\2\u00c3\u00c4\7;\2\2\u00c4\u00c5")
        buf.write("\7\5\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c1\3\2\2\2\u00c6")
        buf.write("\u00c2\3\2\2\2\u00c7\25\3\2\2\2\u00c8\u00c9\b\f\1\2\u00c9")
        buf.write("\u00ca\5\30\r\2\u00ca\u00d0\3\2\2\2\u00cb\u00cc\f\3\2")
        buf.write("\2\u00cc\u00cd\7;\2\2\u00cd\u00cf\5\30\r\2\u00ce\u00cb")
        buf.write("\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\27\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3")
        buf.write("\u00d4\5\16\b\2\u00d4\31\3\2\2\2\u00d5\u00d6\b\16\1\2")
        buf.write("\u00d6\u00d7\7<\2\2\u00d7\u00dd\3\2\2\2\u00d8\u00d9\f")
        buf.write("\3\2\2\u00d9\u00da\7;\2\2\u00da\u00dc\7<\2\2\u00db\u00d8")
        buf.write("\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\33\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0")
        buf.write("\u00e2\5\16\b\2\u00e1\u00e3\5\36\20\2\u00e2\u00e1\3\2")
        buf.write("\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5")
        buf.write("\5N(\2\u00e5\35\3\2\2\2\u00e6\u00e8\b\20\1\2\u00e7\u00e9")
        buf.write("\5 \21\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00eb\7:\2\2\u00eb\u00f3\3\2\2\2")
        buf.write("\u00ec\u00ee\f\3\2\2\u00ed\u00ef\5 \21\2\u00ee\u00ed\3")
        buf.write("\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f2")
        buf.write("\7:\2\2\u00f1\u00ec\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\37\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00f7\b\21\1\2\u00f7\u00f8\5\"\22")
        buf.write("\2\u00f8\u00fe\3\2\2\2\u00f9\u00fa\f\3\2\2\u00fa\u00fb")
        buf.write("\7;\2\2\u00fb\u00fd\5\"\22\2\u00fc\u00f9\3\2\2\2\u00fd")
        buf.write("\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff!\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0107\5\16\b")
        buf.write("\2\u0102\u0103\5\16\b\2\u0103\u0104\7\'\2\2\u0104\u0105")
        buf.write("\5\n\6\2\u0105\u0107\3\2\2\2\u0106\u0101\3\2\2\2\u0106")
        buf.write("\u0102\3\2\2\2\u0107#\3\2\2\2\u0108\u0109\t\2\2\2\u0109")
        buf.write("%\3\2\2\2\u010a\u010b\t\3\2\2\u010b\'\3\2\2\2\u010c\u010d")
        buf.write("\5.\30\2\u010d)\3\2\2\2\u010e\u010f\b\26\1\2\u010f\u0110")
        buf.write("\5,\27\2\u0110\u0116\3\2\2\2\u0111\u0112\f\3\2\2\u0112")
        buf.write("\u0113\7;\2\2\u0113\u0115\5,\27\2\u0114\u0111\3\2\2\2")
        buf.write("\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3")
        buf.write("\2\2\2\u0117+\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011f")
        buf.write("\5.\30\2\u011a\u011b\5D#\2\u011b\u011c\5&\24\2\u011c\u011d")
        buf.write("\5,\27\2\u011d\u011f\3\2\2\2\u011e\u0119\3\2\2\2\u011e")
        buf.write("\u011a\3\2\2\2\u011f-\3\2\2\2\u0120\u0126\5\60\31\2\u0121")
        buf.write("\u0122\7-\2\2\u0122\u0123\5*\26\2\u0123\u0124\7\"\2\2")
        buf.write("\u0124\u0125\5.\30\2\u0125\u0127\3\2\2\2\u0126\u0121\3")
        buf.write("\2\2\2\u0126\u0127\3\2\2\2\u0127/\3\2\2\2\u0128\u0129")
        buf.write("\b\31\1\2\u0129\u012a\5\62\32\2\u012a\u0130\3\2\2\2\u012b")
        buf.write("\u012c\f\3\2\2\u012c\u012d\7\62\2\2\u012d\u012f\5\62\32")
        buf.write("\2\u012e\u012b\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\61\3\2\2\2\u0132\u0130")
        buf.write("\3\2\2\2\u0133\u0134\b\32\1\2\u0134\u0135\5\64\33\2\u0135")
        buf.write("\u013b\3\2\2\2\u0136\u0137\f\3\2\2\u0137\u0138\7\26\2")
        buf.write("\2\u0138\u013a\5\64\33\2\u0139\u0136\3\2\2\2\u013a\u013d")
        buf.write("\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\63\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\b\33\1\2\u013f")
        buf.write("\u0140\5\66\34\2\u0140\u0146\3\2\2\2\u0141\u0142\f\3\2")
        buf.write("\2\u0142\u0143\7\60\2\2\u0143\u0145\5\66\34\2\u0144\u0141")
        buf.write("\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\65\3\2\2\2\u0148\u0146\3\2\2\2\u0149")
        buf.write("\u014a\b\34\1\2\u014a\u014b\58\35\2\u014b\u0151\3\2\2")
        buf.write("\2\u014c\u014d\f\3\2\2\u014d\u014e\7.\2\2\u014e\u0150")
        buf.write("\58\35\2\u014f\u014c\3\2\2\2\u0150\u0153\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\67\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0154\u0155\b\35\1\2\u0155\u0156\5:\36")
        buf.write("\2\u0156\u015c\3\2\2\2\u0157\u0158\f\3\2\2\u0158\u0159")
        buf.write("\7\25\2\2\u0159\u015b\5:\36\2\u015a\u0157\3\2\2\2\u015b")
        buf.write("\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d9\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\b\36\1")
        buf.write("\2\u0160\u0161\5<\37\2\u0161\u016a\3\2\2\2\u0162\u0163")
        buf.write("\f\4\2\2\u0163\u0164\7(\2\2\u0164\u0169\5<\37\2\u0165")
        buf.write("\u0166\f\3\2\2\u0166\u0167\7\22\2\2\u0167\u0169\5<\37")
        buf.write("\2\u0168\u0162\3\2\2\2\u0168\u0165\3\2\2\2\u0169\u016c")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write(";\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e\b\37\1\2\u016e")
        buf.write("\u016f\5> \2\u016f\u017e\3\2\2\2\u0170\u0171\f\6\2\2\u0171")
        buf.write("\u0172\7#\2\2\u0172\u017d\5> \2\u0173\u0174\f\5\2\2\u0174")
        buf.write("\u0175\7)\2\2\u0175\u017d\5> \2\u0176\u0177\f\4\2\2\u0177")
        buf.write("\u0178\7&\2\2\u0178\u017d\5> \2\u0179\u017a\f\3\2\2\u017a")
        buf.write("\u017b\7*\2\2\u017b\u017d\5> \2\u017c\u0170\3\2\2\2\u017c")
        buf.write("\u0173\3\2\2\2\u017c\u0176\3\2\2\2\u017c\u0179\3\2\2\2")
        buf.write("\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3")
        buf.write("\2\2\2\u017f=\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182")
        buf.write("\b \1\2\u0182\u0183\5@!\2\u0183\u018c\3\2\2\2\u0184\u0185")
        buf.write("\f\4\2\2\u0185\u0186\7$\2\2\u0186\u018b\5@!\2\u0187\u0188")
        buf.write("\f\3\2\2\u0188\u0189\7+\2\2\u0189\u018b\5@!\2\u018a\u0184")
        buf.write("\3\2\2\2\u018a\u0187\3\2\2\2\u018b\u018e\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d?\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018f\u0190\b!\1\2\u0190\u0191\5B\"\2\u0191")
        buf.write("\u019a\3\2\2\2\u0192\u0193\f\4\2\2\u0193\u0194\7\32\2")
        buf.write("\2\u0194\u0199\5B\"\2\u0195\u0196\f\3\2\2\u0196\u0197")
        buf.write("\7\35\2\2\u0197\u0199\5B\"\2\u0198\u0192\3\2\2\2\u0198")
        buf.write("\u0195\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019bA\3\2\2\2\u019c\u019a\3\2\2")
        buf.write("\2\u019d\u019e\b\"\1\2\u019e\u019f\5D#\2\u019f\u01ab\3")
        buf.write("\2\2\2\u01a0\u01a1\f\5\2\2\u01a1\u01a2\7\30\2\2\u01a2")
        buf.write("\u01aa\5D#\2\u01a3\u01a4\f\4\2\2\u01a4\u01a5\7 \2\2\u01a5")
        buf.write("\u01aa\5D#\2\u01a6\u01a7\f\3\2\2\u01a7\u01a8\7\23\2\2")
        buf.write("\u01a8\u01aa\5D#\2\u01a9\u01a0\3\2\2\2\u01a9\u01a3\3\2")
        buf.write("\2\2\u01a9\u01a6\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01acC\3\2\2\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ae\u01bd\5F$\2\u01af\u01b0\7\33\2\2\u01b0")
        buf.write("\u01bd\5D#\2\u01b1\u01b2\7\36\2\2\u01b2\u01bd\5D#\2\u01b3")
        buf.write("\u01b4\5$\23\2\u01b4\u01b5\5D#\2\u01b5\u01bd\3\2\2\2\u01b6")
        buf.write("\u01b7\7\17\2\2\u01b7\u01b8\7\3\2\2\u01b8\u01b9\7\r\2")
        buf.write("\2\u01b9\u01bd\7\65\2\2\u01ba\u01bb\7\26\2\2\u01bb\u01bd")
        buf.write("\7<\2\2\u01bc\u01ae\3\2\2\2\u01bc\u01af\3\2\2\2\u01bc")
        buf.write("\u01b1\3\2\2\2\u01bc\u01b3\3\2\2\2\u01bc\u01b6\3\2\2\2")
        buf.write("\u01bc\u01ba\3\2\2\2\u01bdE\3\2\2\2\u01be\u01bf\b$\1\2")
        buf.write("\u01bf\u01ca\5J&\2\u01c0\u01c1\78\2\2\u01c1\u01c2\5\f")
        buf.write("\7\2\u01c2\u01c3\79\2\2\u01c3\u01ca\3\2\2\2\u01c4\u01c5")
        buf.write("\78\2\2\u01c5\u01c6\5\f\7\2\u01c6\u01c7\7;\2\2\u01c7\u01c8")
        buf.write("\79\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01be\3\2\2\2\u01c9")
        buf.write("\u01c0\3\2\2\2\u01c9\u01c4\3\2\2\2\u01ca\u01dc\3\2\2\2")
        buf.write("\u01cb\u01cc\f\b\2\2\u01cc\u01cd\7\66\2\2\u01cd\u01ce")
        buf.write("\5*\26\2\u01ce\u01cf\7\67\2\2\u01cf\u01db\3\2\2\2\u01d0")
        buf.write("\u01d1\f\7\2\2\u01d1\u01d3\7\3\2\2\u01d2\u01d4\5H%\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u01db\7\65\2\2\u01d6\u01d7\f\6\2\2\u01d7\u01db")
        buf.write("\7\33\2\2\u01d8\u01d9\f\5\2\2\u01d9\u01db\7\36\2\2\u01da")
        buf.write("\u01cb\3\2\2\2\u01da\u01d0\3\2\2\2\u01da\u01d6\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da\3")
        buf.write("\2\2\2\u01dc\u01dd\3\2\2\2\u01ddG\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01df\u01e0\b%\1\2\u01e0\u01e1\5,\27\2\u01e1")
        buf.write("\u01e7\3\2\2\2\u01e2\u01e3\f\3\2\2\u01e3\u01e4\7;\2\2")
        buf.write("\u01e4\u01e6\5,\27\2\u01e5\u01e2\3\2\2\2\u01e6\u01e9\3")
        buf.write("\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8I")
        buf.write("\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01f6\7<\2\2\u01eb")
        buf.write("\u01f6\7=\2\2\u01ec\u01ee\7B\2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f6\3\2\2\2\u01f1\u01f2\7\3\2\2\u01f2\u01f3\5")
        buf.write("*\26\2\u01f3\u01f4\7\65\2\2\u01f4\u01f6\3\2\2\2\u01f5")
        buf.write("\u01ea\3\2\2\2\u01f5\u01eb\3\2\2\2\u01f5\u01ed\3\2\2\2")
        buf.write("\u01f5\u01f1\3\2\2\2\u01f6K\3\2\2\2\u01f7\u01fd\5N(\2")
        buf.write("\u01f8\u01fd\5T+\2\u01f9\u01fd\5V,\2\u01fa\u01fd\5X-\2")
        buf.write("\u01fb\u01fd\5Z.\2\u01fc\u01f7\3\2\2\2\u01fc\u01f8\3\2")
        buf.write("\2\2\u01fc\u01f9\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fb")
        buf.write("\3\2\2\2\u01fdM\3\2\2\2\u01fe\u0200\78\2\2\u01ff\u0201")
        buf.write("\5P)\2\u0200\u01ff\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202")
        buf.write("\3\2\2\2\u0202\u0203\79\2\2\u0203O\3\2\2\2\u0204\u0205")
        buf.write("\b)\1\2\u0205\u0206\5R*\2\u0206\u020b\3\2\2\2\u0207\u0208")
        buf.write("\f\3\2\2\u0208\u020a\5R*\2\u0209\u0207\3\2\2\2\u020a\u020d")
        buf.write("\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write("Q\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u0211\5\4\3\2\u020f")
        buf.write("\u0211\5L\'\2\u0210\u020e\3\2\2\2\u0210\u020f\3\2\2\2")
        buf.write("\u0211S\3\2\2\2\u0212\u0214\5*\26\2\u0213\u0212\3\2\2")
        buf.write("\2\u0213\u0214\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0216")
        buf.write("\7:\2\2\u0216U\3\2\2\2\u0217\u0218\7\f\2\2\u0218\u0219")
        buf.write("\7\3\2\2\u0219\u021a\5*\26\2\u021a\u021b\7\65\2\2\u021b")
        buf.write("\u021e\5L\'\2\u021c\u021d\7\n\2\2\u021d\u021f\5L\'\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021fW\3\2\2\2\u0220")
        buf.write("\u0221\7\20\2\2\u0221\u0222\7\3\2\2\u0222\u0223\5*\26")
        buf.write("\2\u0223\u0224\7\65\2\2\u0224\u0225\5L\'\2\u0225\u024b")
        buf.write("\3\2\2\2\u0226\u0227\7\t\2\2\u0227\u0228\5L\'\2\u0228")
        buf.write("\u0229\7\20\2\2\u0229\u022a\7\3\2\2\u022a\u022b\5*\26")
        buf.write("\2\u022b\u022c\7\65\2\2\u022c\u022d\7:\2\2\u022d\u024b")
        buf.write("\3\2\2\2\u022e\u022f\7\13\2\2\u022f\u0231\7\3\2\2\u0230")
        buf.write("\u0232\5*\26\2\u0231\u0230\3\2\2\2\u0231\u0232\3\2\2\2")
        buf.write("\u0232\u0233\3\2\2\2\u0233\u0235\7:\2\2\u0234\u0236\5")
        buf.write("*\26\2\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u0239\7:\2\2\u0238\u023a\5*\26\2\u0239")
        buf.write("\u0238\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023b\3\2\2\2")
        buf.write("\u023b\u023c\7\65\2\2\u023c\u024b\5L\'\2\u023d\u023e\7")
        buf.write("\13\2\2\u023e\u023f\7\3\2\2\u023f\u0241\5\4\3\2\u0240")
        buf.write("\u0242\5*\26\2\u0241\u0240\3\2\2\2\u0241\u0242\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u0245\7:\2\2\u0244\u0246\5")
        buf.write("*\26\2\u0245\u0244\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247")
        buf.write("\3\2\2\2\u0247\u0248\7\65\2\2\u0248\u0249\5L\'\2\u0249")
        buf.write("\u024b\3\2\2\2\u024a\u0220\3\2\2\2\u024a\u0226\3\2\2\2")
        buf.write("\u024a\u022e\3\2\2\2\u024a\u023d\3\2\2\2\u024bY\3\2\2")
        buf.write("\2\u024c\u024d\7\b\2\2\u024d\u0256\7:\2\2\u024e\u024f")
        buf.write("\7\4\2\2\u024f\u0256\7:\2\2\u0250\u0252\7\16\2\2\u0251")
        buf.write("\u0253\5*\26\2\u0252\u0251\3\2\2\2\u0252\u0253\3\2\2\2")
        buf.write("\u0253\u0254\3\2\2\2\u0254\u0256\7:\2\2\u0255\u024c\3")
        buf.write("\2\2\2\u0255\u024e\3\2\2\2\u0255\u0250\3\2\2\2\u0256[")
        buf.write("\3\2\2\2A`gjnz\u0082\u008e\u0098\u009c\u00a9\u00ae\u00b9")
        buf.write("\u00bc\u00be\u00c6\u00d0\u00dd\u00e2\u00e8\u00ee\u00f3")
        buf.write("\u00fe\u0106\u0116\u011e\u0126\u0130\u013b\u0146\u0151")
        buf.write("\u015c\u0168\u016a\u017c\u017e\u018a\u018c\u0198\u019a")
        buf.write("\u01a9\u01ab\u01bc\u01c9\u01d3\u01da\u01dc\u01e7\u01ef")
        buf.write("\u01f5\u01fc\u0200\u020b\u0210\u0213\u021e\u0231\u0235")
        buf.write("\u0239\u0241\u0245\u024a\u0252\u0255")
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
    RULE_variableDeclaration = 1
    RULE_initVariableDeclarationList = 2
    RULE_initDeclaratorVariable = 3
    RULE_initializer = 4
    RULE_initializerList = 5
    RULE_declarator = 6
    RULE_pointer = 7
    RULE_directDeclarator = 8
    RULE_parameterTypeList = 9
    RULE_parameterList = 10
    RULE_parameterDeclaration = 11
    RULE_identifierList = 12
    RULE_functionDefinition = 13
    RULE_declarationList = 14
    RULE_initDeclaratorList = 15
    RULE_initDeclarator = 16
    RULE_unaryOperator = 17
    RULE_assignmentOperator = 18
    RULE_constantExpression = 19
    RULE_expression = 20
    RULE_assignmentExpression = 21
    RULE_conditionalExpression = 22
    RULE_logicalOrExpression = 23
    RULE_logicalAndExpression = 24
    RULE_bitwiseOrExpression = 25
    RULE_bitwiseXOrExpression = 26
    RULE_andExpression = 27
    RULE_equalityExpression = 28
    RULE_relationalExpression = 29
    RULE_shiftExpression = 30
    RULE_additiveExpression = 31
    RULE_multiplicativeExpression = 32
    RULE_unaryExpression = 33
    RULE_postfixExpression = 34
    RULE_argumentExpressionList = 35
    RULE_primaryExpression = 36
    RULE_statement = 37
    RULE_compoundStatement = 38
    RULE_blockItemList = 39
    RULE_blockItem = 40
    RULE_expressionStatement = 41
    RULE_selectionStatement = 42
    RULE_iterationStatement = 43
    RULE_jumpStatement = 44

    ruleNames =  [ "program", "variableDeclaration", "initVariableDeclarationList", 
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

        def program(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HerocParserParser.ProgramContext)
            else:
                return self.getTypedRuleContext(HerocParserParser.ProgramContext,i)


        def variableDeclaration(self):
            return self.getTypedRuleContext(HerocParserParser.VariableDeclarationContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(HerocParserParser.FunctionDefinitionContext,0)


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
        try:
            self.state = 104
            token = self._input.LA(1)
            if token in [self.LONG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90 
                self.variableDeclaration()
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 91 
                        self.program() 
                    self.state = 96
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)


            elif token in [self.T__3, self.STAR, self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97 
                self.functionDefinition()
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 98 
                        self.program() 
                    self.state = 103
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 2, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(self.LONG)
            self.state = 108
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.STAR) | (1 << self.IDENTIFIER))) != 0):
                self.state = 107 
                self.initVariableDeclarationList(0)


            self.state = 110
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_initVariableDeclarationList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113 
            self.initDeclaratorVariable()
            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitVariableDeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initVariableDeclarationList)
                    self.state = 115
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 116
                    self.match(self.COMMA)
                    self.state = 117 
                    self.initDeclaratorVariable() 
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_initDeclaratorVariable)
        try:
            self.state = 128
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123 
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124 
                self.declarator()
                self.state = 125
                self.match(self.ASSIGN)
                self.state = 126 
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
        self.enterRule(localctx, 8, self.RULE_initializer)
        try:
            self.state = 140
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130 
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(self.LEFT_BRACE)
                self.state = 132 
                self.initializerList(0)
                self.state = 133
                self.match(self.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.match(self.LEFT_BRACE)
                self.state = 136 
                self.initializerList(0)
                self.state = 137
                self.match(self.COMMA)
                self.state = 138
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_initializerList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143 
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 145
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 146
                    self.match(self.COMMA)
                    self.state = 147 
                    self.initializer() 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if _la==HerocParserParser.STAR:
                self.state = 153 
                self.pointer()


            self.state = 156 
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
        self.enterRule(localctx, 14, self.RULE_pointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(self.STAR)
            self.state = 159 
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_directDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.state = 162
                self.match(self.IDENTIFIER)

            elif token in [self.T__3]:
                self.state = 163
                self.match(self.T__3)
                self.state = 164 
                self.declarator()
                self.state = 165
                self.match(self.RIGHT_PAREN)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 186
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 169
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 170
                        self.match(self.LEFT_BRACKET)
                        self.state = 172
                        _la = self._input.LA(1)
                        if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                            self.state = 171 
                            self.assignmentExpression()


                        self.state = 174
                        self.match(self.RIGHT_BRACKET)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 175
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 176
                        self.match(self.T__3)
                        self.state = 177 
                        self.parameterTypeList()
                        self.state = 178
                        self.match(self.RIGHT_PAREN)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 180
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 181
                        self.match(self.T__3)
                        self.state = 183
                        _la = self._input.LA(1)
                        if _la==HerocParserParser.IDENTIFIER:
                            self.state = 182 
                            self.identifierList(0)


                        self.state = 185
                        self.match(self.RIGHT_PAREN)
                        pass

             
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_parameterTypeList)
        try:
            self.state = 196
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191 
                self.parameterList(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192 
                self.parameterList(0)
                self.state = 193
                self.match(self.COMMA)
                self.state = 194
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_parameterList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199 
            self.parameterDeclaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ParameterListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterList)
                    self.state = 201
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 202
                    self.match(self.COMMA)
                    self.state = 203 
                    self.parameterDeclaration() 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_parameterDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209 
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_identifierList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(self.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.IdentifierListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_identifierList)
                    self.state = 214
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 215
                    self.match(self.COMMA)
                    self.state = 216
                    self.match(self.IDENTIFIER) 
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222 
            self.declarator()
            self.state = 224
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.STAR) | (1 << self.SEMI) | (1 << self.IDENTIFIER))) != 0):
                self.state = 223 
                self.declarationList(0)


            self.state = 226 
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_declarationList, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.STAR) | (1 << self.IDENTIFIER))) != 0):
                self.state = 229 
                self.initDeclaratorList(0)


            self.state = 232
            self.match(self.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.DeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationList)
                    self.state = 234
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 236
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.STAR) | (1 << self.IDENTIFIER))) != 0):
                        self.state = 235 
                        self.initDeclaratorList(0)


                    self.state = 238
                    self.match(self.SEMI) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_initDeclaratorList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245 
            self.initDeclarator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitDeclaratorListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initDeclaratorList)
                    self.state = 247
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 248
                    self.match(self.COMMA)
                    self.state = 249 
                    self.initDeclarator() 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_initDeclarator)
        try:
            self.state = 260
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255 
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256 
                self.declarator()
                self.state = 257
                self.match(self.ASSIGN)
                self.state = 258 
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
        self.enterRule(localctx, 34, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
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
        self.enterRule(localctx, 36, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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
        self.enterRule(localctx, 38, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266 
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269 
            self.assignmentExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 271
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 272
                    self.match(self.COMMA)
                    self.state = 273 
                    self.assignmentExpression() 
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_assignmentExpression)
        try:
            self.state = 284
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279 
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280 
                self.unaryExpression()
                self.state = 281 
                self.assignmentOperator()
                self.state = 282 
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
        self.enterRule(localctx, 44, self.RULE_conditionalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286 
            self.logicalOrExpression(0)
            self.state = 292
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 287
                self.match(self.QUESTION)
                self.state = 288 
                self.expression(0)
                self.state = 289
                self.match(self.COLON)
                self.state = 290 
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_logicalOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295 
            self.logicalAndExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                    self.state = 297
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 298
                    self.match(self.OR_OR)
                    self.state = 299 
                    self.logicalAndExpression(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_logicalAndExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306 
            self.bitwiseOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.LogicalAndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalAndExpression)
                    self.state = 308
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 309
                    self.match(self.AND_AND)
                    self.state = 310 
                    self.bitwiseOrExpression(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_bitwiseOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317 
            self.bitwiseXOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BitwiseOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseOrExpression)
                    self.state = 319
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 320
                    self.match(self.OR)
                    self.state = 321 
                    self.bitwiseXOrExpression(0) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_bitwiseXOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328 
            self.andExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BitwiseXOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseXOrExpression)
                    self.state = 330
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 331
                    self.match(self.CARET)
                    self.state = 332 
                    self.andExpression(0) 
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_andExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339 
            self.equalityExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.AndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpression)
                    self.state = 341
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 342
                    self.match(self.AND)
                    self.state = 343 
                    self.equalityExpression(0) 
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_equalityExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350 
            self.relationalExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 358
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 352
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 353
                        self.match(self.EQUAL)
                        self.state = 354 
                        self.relationalExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 355
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 356
                        self.match(self.NOT_EQUAL)
                        self.state = 357 
                        self.relationalExpression(0)
                        pass

             
                self.state = 362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_relationalExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364 
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 378
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 366
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 367
                        self.match(self.LESS)
                        self.state = 368 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 369
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 370
                        self.match(self.GREATER)
                        self.state = 371 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 372
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 373
                        self.match(self.LESS_EQUAL)
                        self.state = 374 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 4:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 375
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 376
                        self.match(self.GREATER_EQUAL)
                        self.state = 377 
                        self.shiftExpression(0)
                        pass

             
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_shiftExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384 
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 392
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 386
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 387
                        self.match(self.LEFT_SHIFT)
                        self.state = 388 
                        self.additiveExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 389
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 390
                        self.match(self.RIGHT_SHIFT)
                        self.state = 391 
                        self.additiveExpression(0)
                        pass

             
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398 
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 406
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 400
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 401
                        self.match(self.PLUS)
                        self.state = 402 
                        self.multiplicativeExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 403
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 404
                        self.match(self.MINUS)
                        self.state = 405 
                        self.multiplicativeExpression(0)
                        pass

             
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_multiplicativeExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412 
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 423
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 414
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 415
                        self.match(self.STAR)
                        self.state = 416 
                        self.unaryExpression()
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 417
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 418
                        self.match(self.DIV)
                        self.state = 419 
                        self.unaryExpression()
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 420
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 421
                        self.match(self.MOD)
                        self.state = 422 
                        self.unaryExpression()
                        pass

             
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_unaryExpression)
        try:
            self.state = 442
            token = self._input.LA(1)
            if token in [self.T__3, self.LEFT_BRACE, self.IDENTIFIER, self.CONSTANT, self.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428 
                self.postfixExpression(0)

            elif token in [self.PLUS_PLUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.match(self.PLUS_PLUS)
                self.state = 430 
                self.unaryExpression()

            elif token in [self.MINUS_MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.match(self.MINUS_MINUS)
                self.state = 432 
                self.unaryExpression()

            elif token in [self.T__0, self.AND, self.STAR, self.PLUS, self.MINUS, self.TILDE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 433 
                self.unaryOperator()
                self.state = 434 
                self.unaryExpression()

            elif token in [self.SIZEOF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 436
                self.match(self.SIZEOF)
                self.state = 437
                self.match(self.T__3)
                self.state = 438
                self.match(self.LONG)
                self.state = 439
                self.match(self.RIGHT_PAREN)

            elif token in [self.AND_AND]:
                self.enterOuterAlt(localctx, 6)
                self.state = 440
                self.match(self.AND_AND)
                self.state = 441
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_postfixExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 445 
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.state = 446
                self.match(self.LEFT_BRACE)
                self.state = 447 
                self.initializerList(0)
                self.state = 448
                self.match(self.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.state = 450
                self.match(self.LEFT_BRACE)
                self.state = 451 
                self.initializerList(0)
                self.state = 452
                self.match(self.COMMA)
                self.state = 453
                self.match(self.RIGHT_BRACE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 474
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 472
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 457
                        if not self.precpred(self._ctx, 6):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 458
                        self.match(self.LEFT_BRACKET)
                        self.state = 459 
                        self.expression(0)
                        self.state = 460
                        self.match(self.RIGHT_BRACKET)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 462
                        if not self.precpred(self._ctx, 5):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 463
                        self.match(self.T__3)
                        self.state = 465
                        _la = self._input.LA(1)
                        if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                            self.state = 464 
                            self.argumentExpressionList(0)


                        self.state = 467
                        self.match(self.RIGHT_PAREN)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 468
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 469
                        self.match(self.PLUS_PLUS)
                        pass

                    elif la_ == 4:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 470
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 471
                        self.match(self.MINUS_MINUS)
                        pass

             
                self.state = 476
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_argumentExpressionList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478 
            self.assignmentExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 485
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ArgumentExpressionListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argumentExpressionList)
                    self.state = 480
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 481
                    self.match(self.COMMA)
                    self.state = 482 
                    self.assignmentExpression() 
                self.state = 487
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        self.enterRule(localctx, 72, self.RULE_primaryExpression)
        try:
            self.state = 499
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.match(self.IDENTIFIER)

            elif token in [self.CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(self.CONSTANT)

            elif token in [self.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 491 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 490
                        self.match(self.STRING)

                    else:
                        raise NoViableAltException(self)
                    self.state = 493 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)


            elif token in [self.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 495
                self.match(self.T__3)
                self.state = 496 
                self.expression(0)
                self.state = 497
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
        self.enterRule(localctx, 74, self.RULE_statement)
        try:
            self.state = 506
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501 
                self.compoundStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502 
                self.expressionStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 503 
                self.selectionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 504 
                self.iterationStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 505 
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
        self.enterRule(localctx, 76, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(self.LEFT_BRACE)
            self.state = 510
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__2 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.CONTINUE - 1)) | (1 << (self.DO - 1)) | (1 << (self.FOR - 1)) | (1 << (self.IF - 1)) | (1 << (self.LONG - 1)) | (1 << (self.RETURN - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.WHILE - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.SEMI - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                self.state = 509 
                self.blockItemList(0)


            self.state = 512
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_blockItemList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515 
            self.blockItem()
            self._ctx.stop = self._input.LT(-1)
            self.state = 521
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BlockItemListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_blockItemList)
                    self.state = 517
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 518 
                    self.blockItem() 
                self.state = 523
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_blockItem)
        try:
            self.state = 526
            token = self._input.LA(1)
            if token in [self.LONG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 524 
                self.variableDeclaration()

            elif token in [self.T__3, self.T__2, self.T__0, self.CONTINUE, self.DO, self.FOR, self.IF, self.RETURN, self.SIZEOF, self.WHILE, self.AND, self.AND_AND, self.STAR, self.PLUS, self.PLUS_PLUS, self.MINUS, self.MINUS_MINUS, self.TILDE, self.LEFT_BRACE, self.SEMI, self.IDENTIFIER, self.CONSTANT, self.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 525 
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
        self.enterRule(localctx, 82, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                self.state = 528 
                self.expression(0)


            self.state = 531
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
        self.enterRule(localctx, 84, self.RULE_selectionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(self.IF)
            self.state = 534
            self.match(self.T__3)
            self.state = 535 
            self.expression(0)
            self.state = 536
            self.match(self.RIGHT_PAREN)
            self.state = 537 
            self.statement()
            self.state = 540
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 538
                self.match(self.ELSE)
                self.state = 539 
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
        self.enterRule(localctx, 86, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 584
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.match(self.WHILE)
                self.state = 543
                self.match(self.T__3)
                self.state = 544 
                self.expression(0)
                self.state = 545
                self.match(self.RIGHT_PAREN)
                self.state = 546 
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.match(self.DO)
                self.state = 549 
                self.statement()
                self.state = 550
                self.match(self.WHILE)
                self.state = 551
                self.match(self.T__3)
                self.state = 552 
                self.expression(0)
                self.state = 553
                self.match(self.RIGHT_PAREN)
                self.state = 554
                self.match(self.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.match(self.FOR)
                self.state = 557
                self.match(self.T__3)
                self.state = 559
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 558 
                    self.expression(0)


                self.state = 561
                self.match(self.SEMI)
                self.state = 563
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 562 
                    self.expression(0)


                self.state = 565
                self.match(self.SEMI)
                self.state = 567
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 566 
                    self.expression(0)


                self.state = 569
                self.match(self.RIGHT_PAREN)
                self.state = 570 
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 571
                self.match(self.FOR)
                self.state = 572
                self.match(self.T__3)
                self.state = 573 
                self.variableDeclaration()
                self.state = 575
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 574 
                    self.expression(0)


                self.state = 577
                self.match(self.SEMI)
                self.state = 579
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 578 
                    self.expression(0)


                self.state = 581
                self.match(self.RIGHT_PAREN)
                self.state = 582 
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
        self.enterRule(localctx, 88, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.state = 595
            token = self._input.LA(1)
            if token in [self.CONTINUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                self.match(self.CONTINUE)
                self.state = 587
                self.match(self.SEMI)

            elif token in [self.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.match(self.T__2)
                self.state = 589
                self.match(self.SEMI)

            elif token in [self.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 590
                self.match(self.RETURN)
                self.state = 592
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 591 
                    self.expression(0)


                self.state = 594
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
        self._predicates[2] = self.initVariableDeclarationList_sempred
        self._predicates[5] = self.initializerList_sempred
        self._predicates[8] = self.directDeclarator_sempred
        self._predicates[10] = self.parameterList_sempred
        self._predicates[12] = self.identifierList_sempred
        self._predicates[14] = self.declarationList_sempred
        self._predicates[15] = self.initDeclaratorList_sempred
        self._predicates[20] = self.expression_sempred
        self._predicates[23] = self.logicalOrExpression_sempred
        self._predicates[24] = self.logicalAndExpression_sempred
        self._predicates[25] = self.bitwiseOrExpression_sempred
        self._predicates[26] = self.bitwiseXOrExpression_sempred
        self._predicates[27] = self.andExpression_sempred
        self._predicates[28] = self.equalityExpression_sempred
        self._predicates[29] = self.relationalExpression_sempred
        self._predicates[30] = self.shiftExpression_sempred
        self._predicates[31] = self.additiveExpression_sempred
        self._predicates[32] = self.multiplicativeExpression_sempred
        self._predicates[34] = self.postfixExpression_sempred
        self._predicates[35] = self.argumentExpressionList_sempred
        self._predicates[39] = self.blockItemList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def identifierList_sempred(self, localctx:IdentifierListContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         

    def shiftExpression_sempred(self, localctx:ShiftExpressionContext, predIndex:int):
            if predIndex == 21:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 1)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 23:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 1)
         

    def relationalExpression_sempred(self, localctx:RelationalExpressionContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 1)
         

    def declarationList_sempred(self, localctx:DeclarationListContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         

    def logicalOrExpression_sempred(self, localctx:LogicalOrExpressionContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 1)
         

    def multiplicativeExpression_sempred(self, localctx:MultiplicativeExpressionContext, predIndex:int):
            if predIndex == 25:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 26:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 27:
                return self.precpred(self._ctx, 1)
         

    def directDeclarator_sempred(self, localctx:DirectDeclaratorContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def bitwiseXOrExpression_sempred(self, localctx:BitwiseXOrExpressionContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         

    def bitwiseOrExpression_sempred(self, localctx:BitwiseOrExpressionContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         

    def andExpression_sempred(self, localctx:AndExpressionContext, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def blockItemList_sempred(self, localctx:BlockItemListContext, predIndex:int):
            if predIndex == 33:
                return self.precpred(self._ctx, 1)
         

    def initVariableDeclarationList_sempred(self, localctx:InitVariableDeclarationListContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def logicalAndExpression_sempred(self, localctx:LogicalAndExpressionContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 1)
         

    def equalityExpression_sempred(self, localctx:EqualityExpressionContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         

    def argumentExpressionList_sempred(self, localctx:ArgumentExpressionListContext, predIndex:int):
            if predIndex == 32:
                return self.precpred(self._ctx, 1)
         

    def parameterList_sempred(self, localctx:ParameterListContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def initDeclaratorList_sempred(self, localctx:InitDeclaratorListContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

    def postfixExpression_sempred(self, localctx:PostfixExpressionContext, predIndex:int):
            if predIndex == 28:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 29:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 30:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 31:
                return self.precpred(self._ctx, 3)
         

    def initializerList_sempred(self, localctx:InitializerListContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         



