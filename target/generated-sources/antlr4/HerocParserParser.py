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
        buf.write("\u024e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\7\2")
        buf.write("\\\n\2\f\2\16\2_\13\2\3\2\7\2b\n\2\f\2\16\2e\13\2\5\2")
        buf.write("g\n\2\3\3\3\3\5\3k\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\7\4u\n\4\f\4\16\4x\13\4\3\5\3\5\3\5\3\5\3\5\5\5\177\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008b\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u0093\n\7\f\7\16\7\u0096")
        buf.write("\13\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a0\n\t\3")
        buf.write("\t\3\t\3\t\5\t\u00a5\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u00b0\n\t\3\t\7\t\u00b3\n\t\f\t\16\t\u00b6")
        buf.write("\13\t\3\n\3\n\3\n\3\n\3\n\5\n\u00bd\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\7\13\u00c5\n\13\f\13\16\13\u00c8\13\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00d2\n\r\f\r\16")
        buf.write("\r\u00d5\13\r\3\16\3\16\5\16\u00d9\n\16\3\16\3\16\3\17")
        buf.write("\3\17\5\17\u00df\n\17\3\17\3\17\3\17\3\17\5\17\u00e5\n")
        buf.write("\17\3\17\7\17\u00e8\n\17\f\17\16\17\u00eb\13\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\7\20\u00f3\n\20\f\20\16\20\u00f6")
        buf.write("\13\20\3\21\3\21\3\21\3\21\3\21\5\21\u00fd\n\21\3\22\3")
        buf.write("\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u010b\n\25\f\25\16\25\u010e\13\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u0115\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u011d\n\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30")
        buf.write("\u0125\n\30\f\30\16\30\u0128\13\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\7\31\u0130\n\31\f\31\16\31\u0133\13\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u013b\n\32\f\32\16\32\u013e")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0146\n\33\f")
        buf.write("\33\16\33\u0149\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7")
        buf.write("\34\u0151\n\34\f\34\16\34\u0154\13\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\7\35\u015f\n\35\f\35\16\35")
        buf.write("\u0162\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0173\n\36\f\36")
        buf.write("\16\36\u0176\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\7\37\u0181\n\37\f\37\16\37\u0184\13\37\3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \7 \u018f\n \f \16 \u0192\13 \3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\7!\u01a0\n!\f!\16!")
        buf.write("\u01a3\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u01b3\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\5#\u01c0\n#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u01ca\n")
        buf.write("#\3#\3#\3#\3#\3#\7#\u01d1\n#\f#\16#\u01d4\13#\3$\3$\3")
        buf.write("$\3$\3$\3$\7$\u01dc\n$\f$\16$\u01df\13$\3%\3%\3%\6%\u01e4")
        buf.write("\n%\r%\16%\u01e5\3%\3%\3%\3%\5%\u01ec\n%\3&\3&\3&\3&\3")
        buf.write("&\5&\u01f3\n&\3\'\3\'\5\'\u01f7\n\'\3\'\3\'\3(\3(\3(\3")
        buf.write("(\3(\7(\u0200\n(\f(\16(\u0203\13(\3)\3)\5)\u0207\n)\3")
        buf.write("*\5*\u020a\n*\3*\3*\3+\3+\3+\3+\3+\3+\3+\5+\u0215\n+\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u0228")
        buf.write("\n,\3,\3,\5,\u022c\n,\3,\3,\5,\u0230\n,\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u0238\n,\3,\3,\5,\u023c\n,\3,\3,\3,\5,\u0241\n")
        buf.write(",\3-\3-\3-\3-\3-\3-\5-\u0249\n-\3-\5-\u024c\n-\3-\2\27")
        buf.write("\6\f\20\24\30\34\36(.\60\62\64\668:<>@DFN.\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVX\2\4\b\2\6\6\25\25\30\30\32\32\35\35\63\63")
        buf.write("\r\2\24\24\27\27\31\31\34\34\37\37!!%%\'\',,//\61\61\u0273")
        buf.write("\2f\3\2\2\2\4h\3\2\2\2\6n\3\2\2\2\b~\3\2\2\2\n\u008a\3")
        buf.write("\2\2\2\f\u008c\3\2\2\2\16\u0097\3\2\2\2\20\u009f\3\2\2")
        buf.write("\2\22\u00bc\3\2\2\2\24\u00be\3\2\2\2\26\u00c9\3\2\2\2")
        buf.write("\30\u00cb\3\2\2\2\32\u00d6\3\2\2\2\34\u00dc\3\2\2\2\36")
        buf.write("\u00ec\3\2\2\2 \u00fc\3\2\2\2\"\u00fe\3\2\2\2$\u0100\3")
        buf.write("\2\2\2&\u0102\3\2\2\2(\u0104\3\2\2\2*\u0114\3\2\2\2,\u0116")
        buf.write("\3\2\2\2.\u011e\3\2\2\2\60\u0129\3\2\2\2\62\u0134\3\2")
        buf.write("\2\2\64\u013f\3\2\2\2\66\u014a\3\2\2\28\u0155\3\2\2\2")
        buf.write(":\u0163\3\2\2\2<\u0177\3\2\2\2>\u0185\3\2\2\2@\u0193\3")
        buf.write("\2\2\2B\u01b2\3\2\2\2D\u01bf\3\2\2\2F\u01d5\3\2\2\2H\u01eb")
        buf.write("\3\2\2\2J\u01f2\3\2\2\2L\u01f4\3\2\2\2N\u01fa\3\2\2\2")
        buf.write("P\u0206\3\2\2\2R\u0209\3\2\2\2T\u020d\3\2\2\2V\u0240\3")
        buf.write("\2\2\2X\u024b\3\2\2\2Z\\\5\4\3\2[Z\3\2\2\2\\_\3\2\2\2")
        buf.write("][\3\2\2\2]^\3\2\2\2^g\3\2\2\2_]\3\2\2\2`b\5\32\16\2a")
        buf.write("`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2dg\3\2\2\2ec\3")
        buf.write("\2\2\2f]\3\2\2\2fc\3\2\2\2g\3\3\2\2\2hj\7\r\2\2ik\5\6")
        buf.write("\4\2ji\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\7:\2\2m\5\3\2\2\2")
        buf.write("no\b\4\1\2op\5\b\5\2pv\3\2\2\2qr\f\3\2\2rs\7;\2\2su\5")
        buf.write("\b\5\2tq\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\7\3\2")
        buf.write("\2\2xv\3\2\2\2y\177\5\16\b\2z{\5\16\b\2{|\7\'\2\2|}\5")
        buf.write("\n\6\2}\177\3\2\2\2~y\3\2\2\2~z\3\2\2\2\177\t\3\2\2\2")
        buf.write("\u0080\u008b\5*\26\2\u0081\u0082\78\2\2\u0082\u0083\5")
        buf.write("\f\7\2\u0083\u0084\79\2\2\u0084\u008b\3\2\2\2\u0085\u0086")
        buf.write("\78\2\2\u0086\u0087\5\f\7\2\u0087\u0088\7;\2\2\u0088\u0089")
        buf.write("\79\2\2\u0089\u008b\3\2\2\2\u008a\u0080\3\2\2\2\u008a")
        buf.write("\u0081\3\2\2\2\u008a\u0085\3\2\2\2\u008b\13\3\2\2\2\u008c")
        buf.write("\u008d\b\7\1\2\u008d\u008e\5\n\6\2\u008e\u0094\3\2\2\2")
        buf.write("\u008f\u0090\f\3\2\2\u0090\u0091\7;\2\2\u0091\u0093\5")
        buf.write("\n\6\2\u0092\u008f\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092")
        buf.write("\3\2\2\2\u0094\u0095\3\2\2\2\u0095\r\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0097\u0098\5\20\t\2\u0098\17\3\2\2\2\u0099\u009a")
        buf.write("\b\t\1\2\u009a\u00a0\7<\2\2\u009b\u009c\7\3\2\2\u009c")
        buf.write("\u009d\5\16\b\2\u009d\u009e\7\65\2\2\u009e\u00a0\3\2\2")
        buf.write("\2\u009f\u0099\3\2\2\2\u009f\u009b\3\2\2\2\u00a0\u00b4")
        buf.write("\3\2\2\2\u00a1\u00a2\f\5\2\2\u00a2\u00a4\7\66\2\2\u00a3")
        buf.write("\u00a5\5*\26\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00b3\7\67\2\2\u00a7\u00a8")
        buf.write("\f\4\2\2\u00a8\u00a9\7\3\2\2\u00a9\u00aa\5\22\n\2\u00aa")
        buf.write("\u00ab\7\65\2\2\u00ab\u00b3\3\2\2\2\u00ac\u00ad\f\3\2")
        buf.write("\2\u00ad\u00af\7\3\2\2\u00ae\u00b0\5\30\r\2\u00af\u00ae")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\u00b3\7\65\2\2\u00b2\u00a1\3\2\2\2\u00b2\u00a7\3\2\2")
        buf.write("\2\u00b2\u00ac\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\21\3\2\2\2\u00b6\u00b4")
        buf.write("\3\2\2\2\u00b7\u00bd\5\24\13\2\u00b8\u00b9\5\24\13\2\u00b9")
        buf.write("\u00ba\7;\2\2\u00ba\u00bb\7\5\2\2\u00bb\u00bd\3\2\2\2")
        buf.write("\u00bc\u00b7\3\2\2\2\u00bc\u00b8\3\2\2\2\u00bd\23\3\2")
        buf.write("\2\2\u00be\u00bf\b\13\1\2\u00bf\u00c0\5\26\f\2\u00c0\u00c6")
        buf.write("\3\2\2\2\u00c1\u00c2\f\3\2\2\u00c2\u00c3\7;\2\2\u00c3")
        buf.write("\u00c5\5\26\f\2\u00c4\u00c1\3\2\2\2\u00c5\u00c8\3\2\2")
        buf.write("\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\25\3")
        buf.write("\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\5\16\b\2\u00ca")
        buf.write("\27\3\2\2\2\u00cb\u00cc\b\r\1\2\u00cc\u00cd\7<\2\2\u00cd")
        buf.write("\u00d3\3\2\2\2\u00ce\u00cf\f\3\2\2\u00cf\u00d0\7;\2\2")
        buf.write("\u00d0\u00d2\7<\2\2\u00d1\u00ce\3\2\2\2\u00d2\u00d5\3")
        buf.write("\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\31")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d8\5\16\b\2\u00d7")
        buf.write("\u00d9\5\34\17\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2")
        buf.write("\2\u00d9\u00da\3\2\2\2\u00da\u00db\5L\'\2\u00db\33\3\2")
        buf.write("\2\2\u00dc\u00de\b\17\1\2\u00dd\u00df\5\36\20\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e1\7:\2\2\u00e1\u00e9\3\2\2\2\u00e2\u00e4\f")
        buf.write("\3\2\2\u00e3\u00e5\5\36\20\2\u00e4\u00e3\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8\7:\2\2")
        buf.write("\u00e7\u00e2\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3")
        buf.write("\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\35\3\2\2\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00ec\u00ed\b\20\1\2\u00ed\u00ee\5 \21\2\u00ee")
        buf.write("\u00f4\3\2\2\2\u00ef\u00f0\f\3\2\2\u00f0\u00f1\7;\2\2")
        buf.write("\u00f1\u00f3\5 \21\2\u00f2\u00ef\3\2\2\2\u00f3\u00f6\3")
        buf.write("\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\37")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00fd\5\16\b\2\u00f8")
        buf.write("\u00f9\5\16\b\2\u00f9\u00fa\7\'\2\2\u00fa\u00fb\5\n\6")
        buf.write("\2\u00fb\u00fd\3\2\2\2\u00fc\u00f7\3\2\2\2\u00fc\u00f8")
        buf.write("\3\2\2\2\u00fd!\3\2\2\2\u00fe\u00ff\t\2\2\2\u00ff#\3\2")
        buf.write("\2\2\u0100\u0101\t\3\2\2\u0101%\3\2\2\2\u0102\u0103\5")
        buf.write(",\27\2\u0103\'\3\2\2\2\u0104\u0105\b\25\1\2\u0105\u0106")
        buf.write("\5*\26\2\u0106\u010c\3\2\2\2\u0107\u0108\f\3\2\2\u0108")
        buf.write("\u0109\7;\2\2\u0109\u010b\5*\26\2\u010a\u0107\3\2\2\2")
        buf.write("\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3")
        buf.write("\2\2\2\u010d)\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0115")
        buf.write("\5,\27\2\u0110\u0111\5B\"\2\u0111\u0112\5$\23\2\u0112")
        buf.write("\u0113\5*\26\2\u0113\u0115\3\2\2\2\u0114\u010f\3\2\2\2")
        buf.write("\u0114\u0110\3\2\2\2\u0115+\3\2\2\2\u0116\u011c\5.\30")
        buf.write("\2\u0117\u0118\7-\2\2\u0118\u0119\5(\25\2\u0119\u011a")
        buf.write("\7\"\2\2\u011a\u011b\5,\27\2\u011b\u011d\3\2\2\2\u011c")
        buf.write("\u0117\3\2\2\2\u011c\u011d\3\2\2\2\u011d-\3\2\2\2\u011e")
        buf.write("\u011f\b\30\1\2\u011f\u0120\5\60\31\2\u0120\u0126\3\2")
        buf.write("\2\2\u0121\u0122\f\3\2\2\u0122\u0123\7\62\2\2\u0123\u0125")
        buf.write("\5\60\31\2\u0124\u0121\3\2\2\2\u0125\u0128\3\2\2\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127/\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0129\u012a\b\31\1\2\u012a\u012b\5\62\32")
        buf.write("\2\u012b\u0131\3\2\2\2\u012c\u012d\f\3\2\2\u012d\u012e")
        buf.write("\7\26\2\2\u012e\u0130\5\62\32\2\u012f\u012c\3\2\2\2\u0130")
        buf.write("\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\61\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\b\32")
        buf.write("\1\2\u0135\u0136\5\64\33\2\u0136\u013c\3\2\2\2\u0137\u0138")
        buf.write("\f\3\2\2\u0138\u0139\7\60\2\2\u0139\u013b\5\64\33\2\u013a")
        buf.write("\u0137\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d\63\3\2\2\2\u013e\u013c\3\2")
        buf.write("\2\2\u013f\u0140\b\33\1\2\u0140\u0141\5\66\34\2\u0141")
        buf.write("\u0147\3\2\2\2\u0142\u0143\f\3\2\2\u0143\u0144\7.\2\2")
        buf.write("\u0144\u0146\5\66\34\2\u0145\u0142\3\2\2\2\u0146\u0149")
        buf.write("\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\65\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\b\34\1\2\u014b")
        buf.write("\u014c\58\35\2\u014c\u0152\3\2\2\2\u014d\u014e\f\3\2\2")
        buf.write("\u014e\u014f\7\25\2\2\u014f\u0151\58\35\2\u0150\u014d")
        buf.write("\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152")
        buf.write("\u0153\3\2\2\2\u0153\67\3\2\2\2\u0154\u0152\3\2\2\2\u0155")
        buf.write("\u0156\b\35\1\2\u0156\u0157\5:\36\2\u0157\u0160\3\2\2")
        buf.write("\2\u0158\u0159\f\4\2\2\u0159\u015a\7(\2\2\u015a\u015f")
        buf.write("\5:\36\2\u015b\u015c\f\3\2\2\u015c\u015d\7\22\2\2\u015d")
        buf.write("\u015f\5:\36\2\u015e\u0158\3\2\2\2\u015e\u015b\3\2\2\2")
        buf.write("\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3")
        buf.write("\2\2\2\u01619\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0164")
        buf.write("\b\36\1\2\u0164\u0165\5<\37\2\u0165\u0174\3\2\2\2\u0166")
        buf.write("\u0167\f\6\2\2\u0167\u0168\7#\2\2\u0168\u0173\5<\37\2")
        buf.write("\u0169\u016a\f\5\2\2\u016a\u016b\7)\2\2\u016b\u0173\5")
        buf.write("<\37\2\u016c\u016d\f\4\2\2\u016d\u016e\7&\2\2\u016e\u0173")
        buf.write("\5<\37\2\u016f\u0170\f\3\2\2\u0170\u0171\7*\2\2\u0171")
        buf.write("\u0173\5<\37\2\u0172\u0166\3\2\2\2\u0172\u0169\3\2\2\2")
        buf.write("\u0172\u016c\3\2\2\2\u0172\u016f\3\2\2\2\u0173\u0176\3")
        buf.write("\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175;")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\b\37\1\2\u0178")
        buf.write("\u0179\5> \2\u0179\u0182\3\2\2\2\u017a\u017b\f\4\2\2\u017b")
        buf.write("\u017c\7$\2\2\u017c\u0181\5> \2\u017d\u017e\f\3\2\2\u017e")
        buf.write("\u017f\7+\2\2\u017f\u0181\5> \2\u0180\u017a\3\2\2\2\u0180")
        buf.write("\u017d\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183=\3\2\2\2\u0184\u0182\3\2\2")
        buf.write("\2\u0185\u0186\b \1\2\u0186\u0187\5@!\2\u0187\u0190\3")
        buf.write("\2\2\2\u0188\u0189\f\4\2\2\u0189\u018a\7\32\2\2\u018a")
        buf.write("\u018f\5@!\2\u018b\u018c\f\3\2\2\u018c\u018d\7\35\2\2")
        buf.write("\u018d\u018f\5@!\2\u018e\u0188\3\2\2\2\u018e\u018b\3\2")
        buf.write("\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191?\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194")
        buf.write("\b!\1\2\u0194\u0195\5B\"\2\u0195\u01a1\3\2\2\2\u0196\u0197")
        buf.write("\f\5\2\2\u0197\u0198\7\30\2\2\u0198\u01a0\5B\"\2\u0199")
        buf.write("\u019a\f\4\2\2\u019a\u019b\7 \2\2\u019b\u01a0\5B\"\2\u019c")
        buf.write("\u019d\f\3\2\2\u019d\u019e\7\23\2\2\u019e\u01a0\5B\"\2")
        buf.write("\u019f\u0196\3\2\2\2\u019f\u0199\3\2\2\2\u019f\u019c\3")
        buf.write("\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2A\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01b3")
        buf.write("\5D#\2\u01a5\u01a6\7\33\2\2\u01a6\u01b3\5B\"\2\u01a7\u01a8")
        buf.write("\7\36\2\2\u01a8\u01b3\5B\"\2\u01a9\u01aa\5\"\22\2\u01aa")
        buf.write("\u01ab\5B\"\2\u01ab\u01b3\3\2\2\2\u01ac\u01ad\7\17\2\2")
        buf.write("\u01ad\u01ae\7\3\2\2\u01ae\u01af\7\r\2\2\u01af\u01b3\7")
        buf.write("\65\2\2\u01b0\u01b1\7\26\2\2\u01b1\u01b3\7<\2\2\u01b2")
        buf.write("\u01a4\3\2\2\2\u01b2\u01a5\3\2\2\2\u01b2\u01a7\3\2\2\2")
        buf.write("\u01b2\u01a9\3\2\2\2\u01b2\u01ac\3\2\2\2\u01b2\u01b0\3")
        buf.write("\2\2\2\u01b3C\3\2\2\2\u01b4\u01b5\b#\1\2\u01b5\u01c0\5")
        buf.write("H%\2\u01b6\u01b7\78\2\2\u01b7\u01b8\5\f\7\2\u01b8\u01b9")
        buf.write("\79\2\2\u01b9\u01c0\3\2\2\2\u01ba\u01bb\78\2\2\u01bb\u01bc")
        buf.write("\5\f\7\2\u01bc\u01bd\7;\2\2\u01bd\u01be\79\2\2\u01be\u01c0")
        buf.write("\3\2\2\2\u01bf\u01b4\3\2\2\2\u01bf\u01b6\3\2\2\2\u01bf")
        buf.write("\u01ba\3\2\2\2\u01c0\u01d2\3\2\2\2\u01c1\u01c2\f\b\2\2")
        buf.write("\u01c2\u01c3\7\66\2\2\u01c3\u01c4\5(\25\2\u01c4\u01c5")
        buf.write("\7\67\2\2\u01c5\u01d1\3\2\2\2\u01c6\u01c7\f\7\2\2\u01c7")
        buf.write("\u01c9\7\3\2\2\u01c8\u01ca\5F$\2\u01c9\u01c8\3\2\2\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01d1\7\65\2")
        buf.write("\2\u01cc\u01cd\f\6\2\2\u01cd\u01d1\7\33\2\2\u01ce\u01cf")
        buf.write("\f\5\2\2\u01cf\u01d1\7\36\2\2\u01d0\u01c1\3\2\2\2\u01d0")
        buf.write("\u01c6\3\2\2\2\u01d0\u01cc\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3")
        buf.write("\2\2\2\u01d3E\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d6")
        buf.write("\b$\1\2\u01d6\u01d7\5*\26\2\u01d7\u01dd\3\2\2\2\u01d8")
        buf.write("\u01d9\f\3\2\2\u01d9\u01da\7;\2\2\u01da\u01dc\5*\26\2")
        buf.write("\u01db\u01d8\3\2\2\2\u01dc\u01df\3\2\2\2\u01dd\u01db\3")
        buf.write("\2\2\2\u01dd\u01de\3\2\2\2\u01deG\3\2\2\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01e0\u01ec\7<\2\2\u01e1\u01ec\7=\2\2\u01e2\u01e4")
        buf.write("\7B\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01ec\3\2\2\2")
        buf.write("\u01e7\u01e8\7\3\2\2\u01e8\u01e9\5(\25\2\u01e9\u01ea\7")
        buf.write("\65\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e0\3\2\2\2\u01eb")
        buf.write("\u01e1\3\2\2\2\u01eb\u01e3\3\2\2\2\u01eb\u01e7\3\2\2\2")
        buf.write("\u01ecI\3\2\2\2\u01ed\u01f3\5L\'\2\u01ee\u01f3\5R*\2\u01ef")
        buf.write("\u01f3\5T+\2\u01f0\u01f3\5V,\2\u01f1\u01f3\5X-\2\u01f2")
        buf.write("\u01ed\3\2\2\2\u01f2\u01ee\3\2\2\2\u01f2\u01ef\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3K\3\2\2")
        buf.write("\2\u01f4\u01f6\78\2\2\u01f5\u01f7\5N(\2\u01f6\u01f5\3")
        buf.write("\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9")
        buf.write("\79\2\2\u01f9M\3\2\2\2\u01fa\u01fb\b(\1\2\u01fb\u01fc")
        buf.write("\5P)\2\u01fc\u0201\3\2\2\2\u01fd\u01fe\f\3\2\2\u01fe\u0200")
        buf.write("\5P)\2\u01ff\u01fd\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202O\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0204\u0207\5\4\3\2\u0205\u0207\5J&\2\u0206\u0204")
        buf.write("\3\2\2\2\u0206\u0205\3\2\2\2\u0207Q\3\2\2\2\u0208\u020a")
        buf.write("\5(\25\2\u0209\u0208\3\2\2\2\u0209\u020a\3\2\2\2\u020a")
        buf.write("\u020b\3\2\2\2\u020b\u020c\7:\2\2\u020cS\3\2\2\2\u020d")
        buf.write("\u020e\7\f\2\2\u020e\u020f\7\3\2\2\u020f\u0210\5(\25\2")
        buf.write("\u0210\u0211\7\65\2\2\u0211\u0214\5J&\2\u0212\u0213\7")
        buf.write("\n\2\2\u0213\u0215\5J&\2\u0214\u0212\3\2\2\2\u0214\u0215")
        buf.write("\3\2\2\2\u0215U\3\2\2\2\u0216\u0217\7\20\2\2\u0217\u0218")
        buf.write("\7\3\2\2\u0218\u0219\5(\25\2\u0219\u021a\7\65\2\2\u021a")
        buf.write("\u021b\5J&\2\u021b\u0241\3\2\2\2\u021c\u021d\7\t\2\2\u021d")
        buf.write("\u021e\5J&\2\u021e\u021f\7\20\2\2\u021f\u0220\7\3\2\2")
        buf.write("\u0220\u0221\5(\25\2\u0221\u0222\7\65\2\2\u0222\u0223")
        buf.write("\7:\2\2\u0223\u0241\3\2\2\2\u0224\u0225\7\13\2\2\u0225")
        buf.write("\u0227\7\3\2\2\u0226\u0228\5(\25\2\u0227\u0226\3\2\2\2")
        buf.write("\u0227\u0228\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b\7")
        buf.write(":\2\2\u022a\u022c\5(\25\2\u022b\u022a\3\2\2\2\u022b\u022c")
        buf.write("\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\7:\2\2\u022e")
        buf.write("\u0230\5(\25\2\u022f\u022e\3\2\2\2\u022f\u0230\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231\u0232\7\65\2\2\u0232\u0241")
        buf.write("\5J&\2\u0233\u0234\7\13\2\2\u0234\u0235\7\3\2\2\u0235")
        buf.write("\u0237\5\4\3\2\u0236\u0238\5(\25\2\u0237\u0236\3\2\2\2")
        buf.write("\u0237\u0238\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023b\7")
        buf.write(":\2\2\u023a\u023c\5(\25\2\u023b\u023a\3\2\2\2\u023b\u023c")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\7\65\2\2\u023e")
        buf.write("\u023f\5J&\2\u023f\u0241\3\2\2\2\u0240\u0216\3\2\2\2\u0240")
        buf.write("\u021c\3\2\2\2\u0240\u0224\3\2\2\2\u0240\u0233\3\2\2\2")
        buf.write("\u0241W\3\2\2\2\u0242\u0243\7\b\2\2\u0243\u024c\7:\2\2")
        buf.write("\u0244\u0245\7\4\2\2\u0245\u024c\7:\2\2\u0246\u0248\7")
        buf.write("\16\2\2\u0247\u0249\5(\25\2\u0248\u0247\3\2\2\2\u0248")
        buf.write("\u0249\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024c\7:\2\2")
        buf.write("\u024b\u0242\3\2\2\2\u024b\u0244\3\2\2\2\u024b\u0246\3")
        buf.write("\2\2\2\u024cY\3\2\2\2@]cfjv~\u008a\u0094\u009f\u00a4\u00af")
        buf.write("\u00b2\u00b4\u00bc\u00c6\u00d3\u00d8\u00de\u00e4\u00e9")
        buf.write("\u00f4\u00fc\u010c\u0114\u011c\u0126\u0131\u013c\u0147")
        buf.write("\u0152\u015e\u0160\u0172\u0174\u0180\u0182\u018e\u0190")
        buf.write("\u019f\u01a1\u01b2\u01bf\u01c9\u01d0\u01d2\u01dd\u01e5")
        buf.write("\u01eb\u01f2\u01f6\u0201\u0206\u0209\u0214\u0227\u022b")
        buf.write("\u022f\u0237\u023b\u0240\u0248\u024b")
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
    RULE_directDeclarator = 7
    RULE_parameterTypeList = 8
    RULE_parameterList = 9
    RULE_parameterDeclaration = 10
    RULE_identifierList = 11
    RULE_functionDefinition = 12
    RULE_declarationList = 13
    RULE_initDeclaratorList = 14
    RULE_initDeclarator = 15
    RULE_unaryOperator = 16
    RULE_assignmentOperator = 17
    RULE_constantExpression = 18
    RULE_expression = 19
    RULE_assignmentExpression = 20
    RULE_conditionalExpression = 21
    RULE_logicalOrExpression = 22
    RULE_logicalAndExpression = 23
    RULE_bitwiseOrExpression = 24
    RULE_bitwiseXOrExpression = 25
    RULE_andExpression = 26
    RULE_equalityExpression = 27
    RULE_relationalExpression = 28
    RULE_shiftExpression = 29
    RULE_additiveExpression = 30
    RULE_multiplicativeExpression = 31
    RULE_unaryExpression = 32
    RULE_postfixExpression = 33
    RULE_argumentExpressionList = 34
    RULE_primaryExpression = 35
    RULE_statement = 36
    RULE_compoundStatement = 37
    RULE_blockItemList = 38
    RULE_blockItem = 39
    RULE_expressionStatement = 40
    RULE_selectionStatement = 41
    RULE_iterationStatement = 42
    RULE_jumpStatement = 43

    ruleNames =  [ "program", "variableDeclaration", "initVariableDeclarationList", 
                   "initDeclaratorVariable", "initializer", "initializerList", 
                   "declarator", "directDeclarator", "parameterTypeList", 
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

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HerocParserParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(HerocParserParser.VariableDeclarationContext,i)


        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HerocParserParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(HerocParserParser.FunctionDefinitionContext,i)


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
            self.state = 100
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HerocParserParser.LONG:
                    self.state = 88 
                    self.variableDeclaration()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HerocParserParser.T__3 or _la==HerocParserParser.IDENTIFIER:
                    self.state = 94 
                    self.functionDefinition()
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


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
            self.state = 102
            self.match(self.LONG)
            self.state = 104
            _la = self._input.LA(1)
            if _la==HerocParserParser.T__3 or _la==HerocParserParser.IDENTIFIER:
                self.state = 103 
                self.initVariableDeclarationList(0)


            self.state = 106
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
            self.state = 109 
            self.initDeclaratorVariable()
            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitVariableDeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initVariableDeclarationList)
                    self.state = 111
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 112
                    self.match(self.COMMA)
                    self.state = 113 
                    self.initDeclaratorVariable() 
                self.state = 118
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
            self.state = 124
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119 
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120 
                self.declarator()
                self.state = 121
                self.match(self.ASSIGN)
                self.state = 122 
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
            self.state = 136
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126 
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(self.LEFT_BRACE)
                self.state = 128 
                self.initializerList(0)
                self.state = 129
                self.match(self.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.match(self.LEFT_BRACE)
                self.state = 132 
                self.initializerList(0)
                self.state = 133
                self.match(self.COMMA)
                self.state = 134
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
            self.state = 139 
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 146
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 141
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 142
                    self.match(self.COMMA)
                    self.state = 143 
                    self.initializer() 
                self.state = 148
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149 
            self.directDeclarator(0)
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_directDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.state = 152
                self.match(self.IDENTIFIER)

            elif token in [self.T__3]:
                self.state = 153
                self.match(self.T__3)
                self.state = 154 
                self.declarator()
                self.state = 155
                self.match(self.RIGHT_PAREN)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 176
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 159
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 160
                        self.match(self.LEFT_BRACKET)
                        self.state = 162
                        _la = self._input.LA(1)
                        if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                            self.state = 161 
                            self.assignmentExpression()


                        self.state = 164
                        self.match(self.RIGHT_BRACKET)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 165
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 166
                        self.match(self.T__3)
                        self.state = 167 
                        self.parameterTypeList()
                        self.state = 168
                        self.match(self.RIGHT_PAREN)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 170
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 171
                        self.match(self.T__3)
                        self.state = 173
                        _la = self._input.LA(1)
                        if _la==HerocParserParser.IDENTIFIER:
                            self.state = 172 
                            self.identifierList(0)


                        self.state = 175
                        self.match(self.RIGHT_PAREN)
                        pass

             
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_parameterTypeList)
        try:
            self.state = 186
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181 
                self.parameterList(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182 
                self.parameterList(0)
                self.state = 183
                self.match(self.COMMA)
                self.state = 184
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_parameterList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189 
            self.parameterDeclaration()
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ParameterListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_parameterList)
                    self.state = 191
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 192
                    self.match(self.COMMA)
                    self.state = 193 
                    self.parameterDeclaration() 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_parameterDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199 
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_identifierList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(self.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.IdentifierListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_identifierList)
                    self.state = 204
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 205
                    self.match(self.COMMA)
                    self.state = 206
                    self.match(self.IDENTIFIER) 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212 
            self.declarator()
            self.state = 214
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__3) | (1 << self.SEMI) | (1 << self.IDENTIFIER))) != 0):
                self.state = 213 
                self.declarationList(0)


            self.state = 216 
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_declarationList, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if _la==HerocParserParser.T__3 or _la==HerocParserParser.IDENTIFIER:
                self.state = 219 
                self.initDeclaratorList(0)


            self.state = 222
            self.match(self.SEMI)
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.DeclarationListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_declarationList)
                    self.state = 224
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 226
                    _la = self._input.LA(1)
                    if _la==HerocParserParser.T__3 or _la==HerocParserParser.IDENTIFIER:
                        self.state = 225 
                        self.initDeclaratorList(0)


                    self.state = 228
                    self.match(self.SEMI) 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_initDeclaratorList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235 
            self.initDeclarator()
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitDeclaratorListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initDeclaratorList)
                    self.state = 237
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 238
                    self.match(self.COMMA)
                    self.state = 239 
                    self.initDeclarator() 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_initDeclarator)
        try:
            self.state = 250
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245 
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246 
                self.declarator()
                self.state = 247
                self.match(self.ASSIGN)
                self.state = 248 
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
        self.enterRule(localctx, 32, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
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
        self.enterRule(localctx, 34, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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
        self.enterRule(localctx, 36, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256 
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259 
            self.assignmentExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 261
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 262
                    self.match(self.COMMA)
                    self.state = 263 
                    self.assignmentExpression() 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_assignmentExpression)
        try:
            self.state = 274
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269 
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270 
                self.unaryExpression()
                self.state = 271 
                self.assignmentOperator()
                self.state = 272 
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
        self.enterRule(localctx, 42, self.RULE_conditionalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276 
            self.logicalOrExpression(0)
            self.state = 282
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 277
                self.match(self.QUESTION)
                self.state = 278 
                self.expression(0)
                self.state = 279
                self.match(self.COLON)
                self.state = 280 
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_logicalOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285 
            self.logicalAndExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 292
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                    self.state = 287
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 288
                    self.match(self.OR_OR)
                    self.state = 289 
                    self.logicalAndExpression(0) 
                self.state = 294
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_logicalAndExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296 
            self.bitwiseOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.LogicalAndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalAndExpression)
                    self.state = 298
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 299
                    self.match(self.AND_AND)
                    self.state = 300 
                    self.bitwiseOrExpression(0) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_bitwiseOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307 
            self.bitwiseXOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 314
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BitwiseOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseOrExpression)
                    self.state = 309
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 310
                    self.match(self.OR)
                    self.state = 311 
                    self.bitwiseXOrExpression(0) 
                self.state = 316
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_bitwiseXOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318 
            self.andExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BitwiseXOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseXOrExpression)
                    self.state = 320
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 321
                    self.match(self.CARET)
                    self.state = 322 
                    self.andExpression(0) 
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_andExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329 
            self.equalityExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.AndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpression)
                    self.state = 331
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 332
                    self.match(self.AND)
                    self.state = 333 
                    self.equalityExpression(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_equalityExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340 
            self.relationalExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 348
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 342
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 343
                        self.match(self.EQUAL)
                        self.state = 344 
                        self.relationalExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 345
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 346
                        self.match(self.NOT_EQUAL)
                        self.state = 347 
                        self.relationalExpression(0)
                        pass

             
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_relationalExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354 
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 368
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 356
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 357
                        self.match(self.LESS)
                        self.state = 358 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 359
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 360
                        self.match(self.GREATER)
                        self.state = 361 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 362
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 363
                        self.match(self.LESS_EQUAL)
                        self.state = 364 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 4:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 365
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 366
                        self.match(self.GREATER_EQUAL)
                        self.state = 367 
                        self.shiftExpression(0)
                        pass

             
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_shiftExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374 
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 382
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 376
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 377
                        self.match(self.LEFT_SHIFT)
                        self.state = 378 
                        self.additiveExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 379
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 380
                        self.match(self.RIGHT_SHIFT)
                        self.state = 381 
                        self.additiveExpression(0)
                        pass

             
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388 
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 396
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 390
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 391
                        self.match(self.PLUS)
                        self.state = 392 
                        self.multiplicativeExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 393
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 394
                        self.match(self.MINUS)
                        self.state = 395 
                        self.multiplicativeExpression(0)
                        pass

             
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_multiplicativeExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402 
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 413
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 404
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 405
                        self.match(self.STAR)
                        self.state = 406 
                        self.unaryExpression()
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 407
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 408
                        self.match(self.DIV)
                        self.state = 409 
                        self.unaryExpression()
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 410
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 411
                        self.match(self.MOD)
                        self.state = 412 
                        self.unaryExpression()
                        pass

             
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_unaryExpression)
        try:
            self.state = 432
            token = self._input.LA(1)
            if token in [self.T__3, self.LEFT_BRACE, self.IDENTIFIER, self.CONSTANT, self.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418 
                self.postfixExpression(0)

            elif token in [self.PLUS_PLUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.match(self.PLUS_PLUS)
                self.state = 420 
                self.unaryExpression()

            elif token in [self.MINUS_MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 421
                self.match(self.MINUS_MINUS)
                self.state = 422 
                self.unaryExpression()

            elif token in [self.T__0, self.AND, self.STAR, self.PLUS, self.MINUS, self.TILDE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 423 
                self.unaryOperator()
                self.state = 424 
                self.unaryExpression()

            elif token in [self.SIZEOF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 426
                self.match(self.SIZEOF)
                self.state = 427
                self.match(self.T__3)
                self.state = 428
                self.match(self.LONG)
                self.state = 429
                self.match(self.RIGHT_PAREN)

            elif token in [self.AND_AND]:
                self.enterOuterAlt(localctx, 6)
                self.state = 430
                self.match(self.AND_AND)
                self.state = 431
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_postfixExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 435 
                self.primaryExpression()
                pass

            elif la_ == 2:
                self.state = 436
                self.match(self.LEFT_BRACE)
                self.state = 437 
                self.initializerList(0)
                self.state = 438
                self.match(self.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.state = 440
                self.match(self.LEFT_BRACE)
                self.state = 441 
                self.initializerList(0)
                self.state = 442
                self.match(self.COMMA)
                self.state = 443
                self.match(self.RIGHT_BRACE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 464
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 462
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 447
                        if not self.precpred(self._ctx, 6):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 448
                        self.match(self.LEFT_BRACKET)
                        self.state = 449 
                        self.expression(0)
                        self.state = 450
                        self.match(self.RIGHT_BRACKET)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 452
                        if not self.precpred(self._ctx, 5):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 453
                        self.match(self.T__3)
                        self.state = 455
                        _la = self._input.LA(1)
                        if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                            self.state = 454 
                            self.argumentExpressionList(0)


                        self.state = 457
                        self.match(self.RIGHT_PAREN)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 458
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 459
                        self.match(self.PLUS_PLUS)
                        pass

                    elif la_ == 4:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 460
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 461
                        self.match(self.MINUS_MINUS)
                        pass

             
                self.state = 466
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_argumentExpressionList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468 
            self.assignmentExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ArgumentExpressionListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argumentExpressionList)
                    self.state = 470
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 471
                    self.match(self.COMMA)
                    self.state = 472 
                    self.assignmentExpression() 
                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_primaryExpression)
        try:
            self.state = 489
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(self.IDENTIFIER)

            elif token in [self.CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
                self.match(self.CONSTANT)

            elif token in [self.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 481 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 480
                        self.match(self.STRING)

                    else:
                        raise NoViableAltException(self)
                    self.state = 483 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,46,self._ctx)


            elif token in [self.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 485
                self.match(self.T__3)
                self.state = 486 
                self.expression(0)
                self.state = 487
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
        self.enterRule(localctx, 72, self.RULE_statement)
        try:
            self.state = 496
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491 
                self.compoundStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 492 
                self.expressionStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 493 
                self.selectionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 494 
                self.iterationStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 495 
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
        self.enterRule(localctx, 74, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(self.LEFT_BRACE)
            self.state = 500
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__2 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.CONTINUE - 1)) | (1 << (self.DO - 1)) | (1 << (self.FOR - 1)) | (1 << (self.IF - 1)) | (1 << (self.LONG - 1)) | (1 << (self.RETURN - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.WHILE - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.SEMI - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                self.state = 499 
                self.blockItemList(0)


            self.state = 502
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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_blockItemList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505 
            self.blockItem()
            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BlockItemListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_blockItemList)
                    self.state = 507
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 508 
                    self.blockItem() 
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_blockItem)
        try:
            self.state = 516
            token = self._input.LA(1)
            if token in [self.LONG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514 
                self.variableDeclaration()

            elif token in [self.T__3, self.T__2, self.T__0, self.CONTINUE, self.DO, self.FOR, self.IF, self.RETURN, self.SIZEOF, self.WHILE, self.AND, self.AND_AND, self.STAR, self.PLUS, self.PLUS_PLUS, self.MINUS, self.MINUS_MINUS, self.TILDE, self.LEFT_BRACE, self.SEMI, self.IDENTIFIER, self.CONSTANT, self.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515 
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
        self.enterRule(localctx, 80, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            _la = self._input.LA(1)
            if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                self.state = 518 
                self.expression(0)


            self.state = 521
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
        self.enterRule(localctx, 82, self.RULE_selectionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(self.IF)
            self.state = 524
            self.match(self.T__3)
            self.state = 525 
            self.expression(0)
            self.state = 526
            self.match(self.RIGHT_PAREN)
            self.state = 527 
            self.statement()
            self.state = 530
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 528
                self.match(self.ELSE)
                self.state = 529 
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
        self.enterRule(localctx, 84, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 574
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(self.WHILE)
                self.state = 533
                self.match(self.T__3)
                self.state = 534 
                self.expression(0)
                self.state = 535
                self.match(self.RIGHT_PAREN)
                self.state = 536 
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.match(self.DO)
                self.state = 539 
                self.statement()
                self.state = 540
                self.match(self.WHILE)
                self.state = 541
                self.match(self.T__3)
                self.state = 542 
                self.expression(0)
                self.state = 543
                self.match(self.RIGHT_PAREN)
                self.state = 544
                self.match(self.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 546
                self.match(self.FOR)
                self.state = 547
                self.match(self.T__3)
                self.state = 549
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 548 
                    self.expression(0)


                self.state = 551
                self.match(self.SEMI)
                self.state = 553
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 552 
                    self.expression(0)


                self.state = 555
                self.match(self.SEMI)
                self.state = 557
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 556 
                    self.expression(0)


                self.state = 559
                self.match(self.RIGHT_PAREN)
                self.state = 560 
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 561
                self.match(self.FOR)
                self.state = 562
                self.match(self.T__3)
                self.state = 563 
                self.variableDeclaration()
                self.state = 565
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 564 
                    self.expression(0)


                self.state = 567
                self.match(self.SEMI)
                self.state = 569
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 568 
                    self.expression(0)


                self.state = 571
                self.match(self.RIGHT_PAREN)
                self.state = 572 
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
        self.enterRule(localctx, 86, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.state = 585
            token = self._input.LA(1)
            if token in [self.CONTINUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.match(self.CONTINUE)
                self.state = 577
                self.match(self.SEMI)

            elif token in [self.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
                self.match(self.T__2)
                self.state = 579
                self.match(self.SEMI)

            elif token in [self.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 580
                self.match(self.RETURN)
                self.state = 582
                _la = self._input.LA(1)
                if ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (self.T__3 - 1)) | (1 << (self.T__0 - 1)) | (1 << (self.SIZEOF - 1)) | (1 << (self.AND - 1)) | (1 << (self.AND_AND - 1)) | (1 << (self.STAR - 1)) | (1 << (self.PLUS - 1)) | (1 << (self.PLUS_PLUS - 1)) | (1 << (self.MINUS - 1)) | (1 << (self.MINUS_MINUS - 1)) | (1 << (self.TILDE - 1)) | (1 << (self.LEFT_BRACE - 1)) | (1 << (self.IDENTIFIER - 1)) | (1 << (self.CONSTANT - 1)) | (1 << (self.STRING - 1)))) != 0):
                    self.state = 581 
                    self.expression(0)


                self.state = 584
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
        self._predicates[7] = self.directDeclarator_sempred
        self._predicates[9] = self.parameterList_sempred
        self._predicates[11] = self.identifierList_sempred
        self._predicates[13] = self.declarationList_sempred
        self._predicates[14] = self.initDeclaratorList_sempred
        self._predicates[19] = self.expression_sempred
        self._predicates[22] = self.logicalOrExpression_sempred
        self._predicates[23] = self.logicalAndExpression_sempred
        self._predicates[24] = self.bitwiseOrExpression_sempred
        self._predicates[25] = self.bitwiseXOrExpression_sempred
        self._predicates[26] = self.andExpression_sempred
        self._predicates[27] = self.equalityExpression_sempred
        self._predicates[28] = self.relationalExpression_sempred
        self._predicates[29] = self.shiftExpression_sempred
        self._predicates[30] = self.additiveExpression_sempred
        self._predicates[31] = self.multiplicativeExpression_sempred
        self._predicates[33] = self.postfixExpression_sempred
        self._predicates[34] = self.argumentExpressionList_sempred
        self._predicates[38] = self.blockItemList_sempred
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
         



