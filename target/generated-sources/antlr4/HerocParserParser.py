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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3C")
        buf.write("\u0175\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\7\2B\n\2\f\2\16\2E\13\2\3\3\3\3\5")
        buf.write("\3I\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5R\n\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\5\6[\n\6\3\7\3\7\3\7\5\7`\n\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\5\bg\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\tp\n\t\f\t\16\ts\13\t\3\n\3\n\5\nw\n\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0085")
        buf.write("\n\16\f\16\16\16\u0088\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u008f\n\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u0097")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u009f\n\21\f")
        buf.write("\21\16\21\u00a2\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7")
        buf.write("\22\u00aa\n\22\f\22\16\22\u00ad\13\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\7\23\u00b5\n\23\f\23\16\23\u00b8\13\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\7\24\u00c0\n\24\f\24\16\24")
        buf.write("\u00c3\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00cb")
        buf.write("\n\25\f\25\16\25\u00ce\13\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u00d9\n\26\f\26\16\26\u00dc")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\7\27\u00ed\n\27\f\27\16\27")
        buf.write("\u00f0\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\7\30\u00fb\n\30\f\30\16\30\u00fe\13\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0109\n\31\f\31")
        buf.write("\16\31\u010c\13\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u011a\n\32\f\32\16\32\u011d")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u012d\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u013a\n")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\7\34\u0141\n\34\f\34\16\34")
        buf.write("\u0144\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u014c")
        buf.write("\n\35\f\35\16\35\u014f\13\35\3\36\3\36\3\36\6\36\u0154")
        buf.write("\n\36\r\36\16\36\u0155\3\36\3\36\3\36\3\36\5\36\u015c")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u0168\n\37\3 \3 \3 \3 \3 \3 \7 \u0170\n \f \16 ")
        buf.write("\u0173\13 \3 \2\21\20\32 \"$&(*,.\60\62\668>!\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>\2\4\b\2\4\4\23\23\26\26\30\30\33\33\61\61\r\2\22\22")
        buf.write("\25\25\27\27\32\32\35\35\37\37##%%**--//\u0184\2C\3\2")
        buf.write("\2\2\4H\3\2\2\2\6J\3\2\2\2\bN\3\2\2\2\nZ\3\2\2\2\f\\\3")
        buf.write("\2\2\2\16d\3\2\2\2\20j\3\2\2\2\22v\3\2\2\2\24x\3\2\2\2")
        buf.write("\26z\3\2\2\2\30|\3\2\2\2\32~\3\2\2\2\34\u008e\3\2\2\2")
        buf.write("\36\u0090\3\2\2\2 \u0098\3\2\2\2\"\u00a3\3\2\2\2$\u00ae")
        buf.write("\3\2\2\2&\u00b9\3\2\2\2(\u00c4\3\2\2\2*\u00cf\3\2\2\2")
        buf.write(",\u00dd\3\2\2\2.\u00f1\3\2\2\2\60\u00ff\3\2\2\2\62\u010d")
        buf.write("\3\2\2\2\64\u012c\3\2\2\2\66\u012e\3\2\2\28\u0145\3\2")
        buf.write("\2\2:\u015b\3\2\2\2<\u0167\3\2\2\2>\u0169\3\2\2\2@B\5")
        buf.write("\4\3\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\3\3\2")
        buf.write("\2\2EC\3\2\2\2FI\5\6\4\2GI\5\b\5\2HF\3\2\2\2HG\3\2\2\2")
        buf.write("I\5\3\2\2\2JK\7\13\2\2KL\7:\2\2LM\78\2\2M\7\3\2\2\2NO")
        buf.write("\7:\2\2OQ\7\3\2\2PR\5\n\6\2QP\3\2\2\2QR\3\2\2\2RS\3\2")
        buf.write("\2\2ST\7\63\2\2TU\5\16\b\2U\t\3\2\2\2V[\7:\2\2WX\7:\2")
        buf.write("\2XY\79\2\2Y[\5\n\6\2ZV\3\2\2\2ZW\3\2\2\2[\13\3\2\2\2")
        buf.write("\\]\7:\2\2]_\7\3\2\2^`\5\32\16\2_^\3\2\2\2_`\3\2\2\2`")
        buf.write("a\3\2\2\2ab\7\63\2\2bc\78\2\2c\r\3\2\2\2df\7\66\2\2eg")
        buf.write("\5\20\t\2fe\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\7\67\2\2i\17")
        buf.write("\3\2\2\2jk\b\t\1\2kl\5\22\n\2lq\3\2\2\2mn\f\3\2\2np\5")
        buf.write("\22\n\2om\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\21\3")
        buf.write("\2\2\2sq\3\2\2\2tw\5\6\4\2uw\5\f\7\2vt\3\2\2\2vu\3\2\2")
        buf.write("\2w\23\3\2\2\2xy\t\2\2\2y\25\3\2\2\2z{\t\3\2\2{\27\3\2")
        buf.write("\2\2|}\5\36\20\2}\31\3\2\2\2~\177\b\16\1\2\177\u0080\5")
        buf.write("\34\17\2\u0080\u0086\3\2\2\2\u0081\u0082\f\3\2\2\u0082")
        buf.write("\u0083\79\2\2\u0083\u0085\5\34\17\2\u0084\u0081\3\2\2")
        buf.write("\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\33\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008f")
        buf.write("\5\36\20\2\u008a\u008b\5\64\33\2\u008b\u008c\5\26\f\2")
        buf.write("\u008c\u008d\5\34\17\2\u008d\u008f\3\2\2\2\u008e\u0089")
        buf.write("\3\2\2\2\u008e\u008a\3\2\2\2\u008f\35\3\2\2\2\u0090\u0096")
        buf.write("\5 \21\2\u0091\u0092\7+\2\2\u0092\u0093\5\32\16\2\u0093")
        buf.write("\u0094\7 \2\2\u0094\u0095\5\36\20\2\u0095\u0097\3\2\2")
        buf.write("\2\u0096\u0091\3\2\2\2\u0096\u0097\3\2\2\2\u0097\37\3")
        buf.write("\2\2\2\u0098\u0099\b\21\1\2\u0099\u009a\5\"\22\2\u009a")
        buf.write("\u00a0\3\2\2\2\u009b\u009c\f\3\2\2\u009c\u009d\7\60\2")
        buf.write("\2\u009d\u009f\5\"\22\2\u009e\u009b\3\2\2\2\u009f\u00a2")
        buf.write("\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("!\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\b\22\1\2\u00a4")
        buf.write("\u00a5\5$\23\2\u00a5\u00ab\3\2\2\2\u00a6\u00a7\f\3\2\2")
        buf.write("\u00a7\u00a8\7\24\2\2\u00a8\u00aa\5$\23\2\u00a9\u00a6")
        buf.write("\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac#\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae")
        buf.write("\u00af\b\23\1\2\u00af\u00b0\5&\24\2\u00b0\u00b6\3\2\2")
        buf.write("\2\u00b1\u00b2\f\3\2\2\u00b2\u00b3\7.\2\2\u00b3\u00b5")
        buf.write("\5&\24\2\u00b4\u00b1\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7%\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b9\u00ba\b\24\1\2\u00ba\u00bb\5(\25")
        buf.write("\2\u00bb\u00c1\3\2\2\2\u00bc\u00bd\f\3\2\2\u00bd\u00be")
        buf.write("\7,\2\2\u00be\u00c0\5(\25\2\u00bf\u00bc\3\2\2\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\'\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\b\25")
        buf.write("\1\2\u00c5\u00c6\5*\26\2\u00c6\u00cc\3\2\2\2\u00c7\u00c8")
        buf.write("\f\3\2\2\u00c8\u00c9\7\23\2\2\u00c9\u00cb\5*\26\2\u00ca")
        buf.write("\u00c7\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cd)\3\2\2\2\u00ce\u00cc\3\2\2")
        buf.write("\2\u00cf\u00d0\b\26\1\2\u00d0\u00d1\5,\27\2\u00d1\u00da")
        buf.write("\3\2\2\2\u00d2\u00d3\f\4\2\2\u00d3\u00d4\7&\2\2\u00d4")
        buf.write("\u00d9\5,\27\2\u00d5\u00d6\f\3\2\2\u00d6\u00d7\7\20\2")
        buf.write("\2\u00d7\u00d9\5,\27\2\u00d8\u00d2\3\2\2\2\u00d8\u00d5")
        buf.write("\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db+\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd")
        buf.write("\u00de\b\27\1\2\u00de\u00df\5.\30\2\u00df\u00ee\3\2\2")
        buf.write("\2\u00e0\u00e1\f\6\2\2\u00e1\u00e2\7!\2\2\u00e2\u00ed")
        buf.write("\5.\30\2\u00e3\u00e4\f\5\2\2\u00e4\u00e5\7\'\2\2\u00e5")
        buf.write("\u00ed\5.\30\2\u00e6\u00e7\f\4\2\2\u00e7\u00e8\7$\2\2")
        buf.write("\u00e8\u00ed\5.\30\2\u00e9\u00ea\f\3\2\2\u00ea\u00eb\7")
        buf.write("(\2\2\u00eb\u00ed\5.\30\2\u00ec\u00e0\3\2\2\2\u00ec\u00e3")
        buf.write("\3\2\2\2\u00ec\u00e6\3\2\2\2\u00ec\u00e9\3\2\2\2\u00ed")
        buf.write("\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2")
        buf.write("\u00ef-\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\b\30\1")
        buf.write("\2\u00f2\u00f3\5\60\31\2\u00f3\u00fc\3\2\2\2\u00f4\u00f5")
        buf.write("\f\4\2\2\u00f5\u00f6\7\"\2\2\u00f6\u00fb\5\60\31\2\u00f7")
        buf.write("\u00f8\f\3\2\2\u00f8\u00f9\7)\2\2\u00f9\u00fb\5\60\31")
        buf.write("\2\u00fa\u00f4\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fb\u00fe")
        buf.write("\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("/\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\b\31\1\2\u0100")
        buf.write("\u0101\5\62\32\2\u0101\u010a\3\2\2\2\u0102\u0103\f\4\2")
        buf.write("\2\u0103\u0104\7\30\2\2\u0104\u0109\5\62\32\2\u0105\u0106")
        buf.write("\f\3\2\2\u0106\u0107\7\33\2\2\u0107\u0109\5\62\32\2\u0108")
        buf.write("\u0102\3\2\2\2\u0108\u0105\3\2\2\2\u0109\u010c\3\2\2\2")
        buf.write("\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\61\3\2")
        buf.write("\2\2\u010c\u010a\3\2\2\2\u010d\u010e\b\32\1\2\u010e\u010f")
        buf.write("\5\64\33\2\u010f\u011b\3\2\2\2\u0110\u0111\f\5\2\2\u0111")
        buf.write("\u0112\7\26\2\2\u0112\u011a\5\64\33\2\u0113\u0114\f\4")
        buf.write("\2\2\u0114\u0115\7\36\2\2\u0115\u011a\5\64\33\2\u0116")
        buf.write("\u0117\f\3\2\2\u0117\u0118\7\21\2\2\u0118\u011a\5\64\33")
        buf.write("\2\u0119\u0110\3\2\2\2\u0119\u0113\3\2\2\2\u0119\u0116")
        buf.write("\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\63\3\2\2\2\u011d\u011b\3\2\2\2\u011e")
        buf.write("\u012d\5\66\34\2\u011f\u0120\7\31\2\2\u0120\u012d\5\64")
        buf.write("\33\2\u0121\u0122\7\34\2\2\u0122\u012d\5\64\33\2\u0123")
        buf.write("\u0124\5\24\13\2\u0124\u0125\5\64\33\2\u0125\u012d\3\2")
        buf.write("\2\2\u0126\u0127\7\r\2\2\u0127\u0128\7\3\2\2\u0128\u0129")
        buf.write("\7\13\2\2\u0129\u012d\7\63\2\2\u012a\u012b\7\24\2\2\u012b")
        buf.write("\u012d\7:\2\2\u012c\u011e\3\2\2\2\u012c\u011f\3\2\2\2")
        buf.write("\u012c\u0121\3\2\2\2\u012c\u0123\3\2\2\2\u012c\u0126\3")
        buf.write("\2\2\2\u012c\u012a\3\2\2\2\u012d\65\3\2\2\2\u012e\u012f")
        buf.write("\b\34\1\2\u012f\u0130\5:\36\2\u0130\u0142\3\2\2\2\u0131")
        buf.write("\u0132\f\6\2\2\u0132\u0133\7\64\2\2\u0133\u0134\5\32\16")
        buf.write("\2\u0134\u0135\7\65\2\2\u0135\u0141\3\2\2\2\u0136\u0137")
        buf.write("\f\5\2\2\u0137\u0139\7\3\2\2\u0138\u013a\58\35\2\u0139")
        buf.write("\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u0141\7\63\2\2\u013c\u013d\f\4\2\2\u013d\u0141")
        buf.write("\7\31\2\2\u013e\u013f\f\3\2\2\u013f\u0141\7\34\2\2\u0140")
        buf.write("\u0131\3\2\2\2\u0140\u0136\3\2\2\2\u0140\u013c\3\2\2\2")
        buf.write("\u0140\u013e\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140\3")
        buf.write("\2\2\2\u0142\u0143\3\2\2\2\u0143\67\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0145\u0146\b\35\1\2\u0146\u0147\5\34\17\2\u0147")
        buf.write("\u014d\3\2\2\2\u0148\u0149\f\3\2\2\u0149\u014a\79\2\2")
        buf.write("\u014a\u014c\5\34\17\2\u014b\u0148\3\2\2\2\u014c\u014f")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("9\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u015c\7:\2\2\u0151")
        buf.write("\u015c\7;\2\2\u0152\u0154\7@\2\2\u0153\u0152\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u015c\3\2\2\2\u0157\u0158\7\3\2\2\u0158\u0159\5")
        buf.write("\32\16\2\u0159\u015a\7\63\2\2\u015a\u015c\3\2\2\2\u015b")
        buf.write("\u0150\3\2\2\2\u015b\u0151\3\2\2\2\u015b\u0153\3\2\2\2")
        buf.write("\u015b\u0157\3\2\2\2\u015c;\3\2\2\2\u015d\u0168\5\34\17")
        buf.write("\2\u015e\u015f\7\66\2\2\u015f\u0160\5> \2\u0160\u0161")
        buf.write("\7\67\2\2\u0161\u0168\3\2\2\2\u0162\u0163\7\66\2\2\u0163")
        buf.write("\u0164\5> \2\u0164\u0165\79\2\2\u0165\u0166\7\67\2\2\u0166")
        buf.write("\u0168\3\2\2\2\u0167\u015d\3\2\2\2\u0167\u015e\3\2\2\2")
        buf.write("\u0167\u0162\3\2\2\2\u0168=\3\2\2\2\u0169\u016a\b \1\2")
        buf.write("\u016a\u016b\5<\37\2\u016b\u0171\3\2\2\2\u016c\u016d\f")
        buf.write("\3\2\2\u016d\u016e\79\2\2\u016e\u0170\5<\37\2\u016f\u016c")
        buf.write("\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172?\3\2\2\2\u0173\u0171\3\2\2\2%CHQ")
        buf.write("Z_fqv\u0086\u008e\u0096\u00a0\u00ab\u00b6\u00c1\u00cc")
        buf.write("\u00d8\u00da\u00ec\u00ee\u00fa\u00fc\u0108\u010a\u0119")
        buf.write("\u011b\u012c\u0139\u0140\u0142\u014d\u0155\u015b\u0167")
        buf.write("\u0171")
        return buf.getvalue()
		

class HerocParserParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__1=1
    T__0=2
    BREAK=3
    CONTINUE=4
    DO=5
    ELSE=6
    FOR=7
    IF=8
    LONG=9
    RETURN=10
    SIZEOF=11
    WHILE=12
    NOT=13
    NOT_EQUAL=14
    MOD=15
    MOD_ASIGN=16
    AND=17
    AND_AND=18
    AND_ASSIGN=19
    STAR=20
    STAR_ASSIGN=21
    PLUS=22
    PLUS_PLUS=23
    PLUS_ASSIGN=24
    MINUS=25
    MINUS_MINUS=26
    MINUS_ASSIGN=27
    DIV=28
    DIV_ASSIGN=29
    COLON=30
    LESS=31
    LEFT_SHIFT=32
    LEFT_SHIFT_ASSIGN=33
    LESS_EQUAL=34
    ASSIGN=35
    EQUAL=36
    GREATER=37
    GREATER_EQUAL=38
    RIGHT_SHIFT=39
    RIGHT_SHIFT_ASSIGN=40
    QUESTION=41
    CARET=42
    XOR_ASSIGN=43
    OR=44
    OR_ASSIGN=45
    OR_OR=46
    TILDE=47
    LEFT_PAREN=48
    RIGHT_PAREN=49
    LEFT_BRACKET=50
    RIGHT_BRACKET=51
    LEFT_BRACE=52
    RIGHT_BRACE=53
    SEMI=54
    COMMA=55
    IDENTIFIER=56
    CONSTANT=57
    INT_CONSTANT=58
    OCTAL_CONSTANT=59
    HEX_CONSTANT=60
    CHAR_CONSTANT=61
    STRING=62
    WHITESPACE=63
    NEWLINE=64
    COMMENT=65

    tokenNames = [ "<INVALID>", "'('", "'!'", "BREAK", "'continue'", "'do'", 
                   "'else'", "'for'", "'if'", "'long'", "'return'", "'sizeof'", 
                   "'while'", "NOT", "'!='", "'%'", "'%='", "'&'", "'&&'", 
                   "'&='", "'*'", "'*='", "'+'", "'++'", "'+='", "'-'", 
                   "'--'", "'-='", "'/'", "'/='", "':'", "'<'", "'<<'", 
                   "'<<='", "'<='", "'='", "'=='", "'>'", "'>='", "'>>'", 
                   "'>>='", "'?'", "'^'", "'^='", "'|'", "'|='", "'||'", 
                   "'~'", "LEFT_PAREN", "')'", "'['", "']'", "'{'", "'}'", 
                   "';'", "','", "IDENTIFIER", "CONSTANT", "INT_CONSTANT", 
                   "OCTAL_CONSTANT", "HEX_CONSTANT", "CHAR_CONSTANT", "STRING", 
                   "WHITESPACE", "NEWLINE", "COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_declarationVariable = 2
    RULE_declarationFunction = 3
    RULE_functionDeclarationArgsList = 4
    RULE_functionCall = 5
    RULE_compoundStatement = 6
    RULE_blockItemList = 7
    RULE_blockItem = 8
    RULE_unaryOperator = 9
    RULE_assignmentOperator = 10
    RULE_constantExpression = 11
    RULE_expression = 12
    RULE_assignmentExpression = 13
    RULE_conditionalExpression = 14
    RULE_logicalOrExpression = 15
    RULE_logicalAndExpression = 16
    RULE_bitwiseOrExpression = 17
    RULE_bitwiseXOrExpression = 18
    RULE_andExpression = 19
    RULE_equalityExpression = 20
    RULE_relationalExpression = 21
    RULE_shiftExpression = 22
    RULE_additiveExpression = 23
    RULE_multiplicativeExpression = 24
    RULE_unaryExpression = 25
    RULE_postfixExpression = 26
    RULE_argumentExpressionList = 27
    RULE_primaryExpression = 28
    RULE_initializer = 29
    RULE_initializerList = 30

    ruleNames =  [ "program", "declaration", "declarationVariable", "declarationFunction", 
                   "functionDeclarationArgsList", "functionCall", "compoundStatement", 
                   "blockItemList", "blockItem", "unaryOperator", "assignmentOperator", 
                   "constantExpression", "expression", "assignmentExpression", 
                   "conditionalExpression", "logicalOrExpression", "logicalAndExpression", 
                   "bitwiseOrExpression", "bitwiseXOrExpression", "andExpression", 
                   "equalityExpression", "relationalExpression", "shiftExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "postfixExpression", "argumentExpressionList", "primaryExpression", 
                   "initializer", "initializerList" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HerocParserParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(HerocParserParser.DeclarationContext,i)


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
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HerocParserParser.LONG or _la==HerocParserParser.IDENTIFIER:
                self.state = 62 
                self.declaration()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationVariable(self):
            return self.getTypedRuleContext(HerocParserParser.DeclarationVariableContext,0)


        def declarationFunction(self):
            return self.getTypedRuleContext(HerocParserParser.DeclarationFunctionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = HerocParserParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 70
            token = self._input.LA(1)
            if token in [self.LONG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68 
                self.declarationVariable()

            elif token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69 
                self.declarationFunction()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationVariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LONG(self):
            return self.getToken(HerocParserParser.LONG, 0)

        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return HerocParserParser.RULE_declarationVariable

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterDeclarationVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitDeclarationVariable(self)




    def declarationVariable(self):

        localctx = HerocParserParser.DeclarationVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declarationVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(self.LONG)
            self.state = 73
            self.match(self.IDENTIFIER)
            self.state = 74
            self.match(self.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclarationArgsList(self):
            return self.getTypedRuleContext(HerocParserParser.FunctionDeclarationArgsListContext,0)


        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def compoundStatement(self):
            return self.getTypedRuleContext(HerocParserParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_declarationFunction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterDeclarationFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitDeclarationFunction(self)




    def declarationFunction(self):

        localctx = HerocParserParser.DeclarationFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declarationFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(self.IDENTIFIER)
            self.state = 77
            self.match(self.T__1)
            self.state = 79
            _la = self._input.LA(1)
            if _la==HerocParserParser.IDENTIFIER:
                self.state = 78 
                self.functionDeclarationArgsList()


            self.state = 81
            self.match(self.RIGHT_PAREN)
            self.state = 82 
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationArgsListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclarationArgsList(self):
            return self.getTypedRuleContext(HerocParserParser.FunctionDeclarationArgsListContext,0)


        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return HerocParserParser.RULE_functionDeclarationArgsList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterFunctionDeclarationArgsList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitFunctionDeclarationArgsList(self)




    def functionDeclarationArgsList(self):

        localctx = HerocParserParser.FunctionDeclarationArgsListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionDeclarationArgsList)
        try:
            self.state = 88
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(self.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(self.IDENTIFIER)
                self.state = 86
                self.match(self.COMMA)
                self.state = 87 
                self.functionDeclarationArgsList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(HerocParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return HerocParserParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = HerocParserParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(self.IDENTIFIER)
            self.state = 91
            self.match(self.T__1)
            self.state = 93
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__1) | (1 << self.T__0) | (1 << self.SIZEOF) | (1 << self.AND) | (1 << self.AND_AND) | (1 << self.STAR) | (1 << self.PLUS) | (1 << self.PLUS_PLUS) | (1 << self.MINUS) | (1 << self.MINUS_MINUS) | (1 << self.TILDE) | (1 << self.IDENTIFIER) | (1 << self.CONSTANT) | (1 << self.STRING))) != 0):
                self.state = 92 
                self.expression(0)


            self.state = 95
            self.match(self.RIGHT_PAREN)
            self.state = 96
            self.match(self.SEMI)
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
        self.enterRule(localctx, 12, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(self.LEFT_BRACE)
            self.state = 100
            _la = self._input.LA(1)
            if _la==HerocParserParser.LONG or _la==HerocParserParser.IDENTIFIER:
                self.state = 99 
                self.blockItemList(0)


            self.state = 102
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_blockItemList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105 
            self.blockItem()
            self._ctx.stop = self._input.LT(-1)
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BlockItemListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_blockItemList)
                    self.state = 107
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 108 
                    self.blockItem() 
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def functionCall(self):
            return self.getTypedRuleContext(HerocParserParser.FunctionCallContext,0)


        def declarationVariable(self):
            return self.getTypedRuleContext(HerocParserParser.DeclarationVariableContext,0)


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
        self.enterRule(localctx, 16, self.RULE_blockItem)
        try:
            self.state = 116
            token = self._input.LA(1)
            if token in [self.LONG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114 
                self.declarationVariable()

            elif token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115 
                self.functionCall()

            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 18, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
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
        self.enterRule(localctx, 20, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
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
        self.enterRule(localctx, 22, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122 
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125 
            self.assignmentExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 127
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 128
                    self.match(self.COMMA)
                    self.state = 129 
                    self.assignmentExpression() 
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_assignmentExpression)
        try:
            self.state = 140
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135 
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136 
                self.unaryExpression()
                self.state = 137 
                self.assignmentOperator()
                self.state = 138 
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
        self.enterRule(localctx, 28, self.RULE_conditionalExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142 
            self.logicalOrExpression(0)
            self.state = 148
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 143
                self.match(self.QUESTION)
                self.state = 144 
                self.expression(0)
                self.state = 145
                self.match(self.COLON)
                self.state = 146 
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_logicalOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151 
            self.logicalAndExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                    self.state = 153
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 154
                    self.match(self.OR_OR)
                    self.state = 155 
                    self.logicalAndExpression(0) 
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_logicalAndExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162 
            self.bitwiseOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.LogicalAndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalAndExpression)
                    self.state = 164
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 165
                    self.match(self.AND_AND)
                    self.state = 166 
                    self.bitwiseOrExpression(0) 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_bitwiseOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173 
            self.bitwiseXOrExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BitwiseOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseOrExpression)
                    self.state = 175
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 176
                    self.match(self.OR)
                    self.state = 177 
                    self.bitwiseXOrExpression(0) 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_bitwiseXOrExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184 
            self.andExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BitwiseXOrExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bitwiseXOrExpression)
                    self.state = 186
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 187
                    self.match(self.CARET)
                    self.state = 188 
                    self.andExpression(0) 
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_andExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195 
            self.equalityExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.AndExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andExpression)
                    self.state = 197
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 198
                    self.match(self.AND)
                    self.state = 199 
                    self.equalityExpression(0) 
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_equalityExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206 
            self.relationalExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 214
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 208
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 209
                        self.match(self.EQUAL)
                        self.state = 210 
                        self.relationalExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.EqualityExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpression)
                        self.state = 211
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 212
                        self.match(self.NOT_EQUAL)
                        self.state = 213 
                        self.relationalExpression(0)
                        pass

             
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_relationalExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220 
            self.shiftExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 234
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 222
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 223
                        self.match(self.LESS)
                        self.state = 224 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 225
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 226
                        self.match(self.GREATER)
                        self.state = 227 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 228
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 229
                        self.match(self.LESS_EQUAL)
                        self.state = 230 
                        self.shiftExpression(0)
                        pass

                    elif la_ == 4:
                        localctx = HerocParserParser.RelationalExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpression)
                        self.state = 231
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 232
                        self.match(self.GREATER_EQUAL)
                        self.state = 233 
                        self.shiftExpression(0)
                        pass

             
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_shiftExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240 
            self.additiveExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 248
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 242
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 243
                        self.match(self.LEFT_SHIFT)
                        self.state = 244 
                        self.additiveExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.ShiftExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_shiftExpression)
                        self.state = 245
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 246
                        self.match(self.RIGHT_SHIFT)
                        self.state = 247 
                        self.additiveExpression(0)
                        pass

             
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254 
            self.multiplicativeExpression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 262
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 256
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 257
                        self.match(self.PLUS)
                        self.state = 258 
                        self.multiplicativeExpression(0)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 259
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 260
                        self.match(self.MINUS)
                        self.state = 261 
                        self.multiplicativeExpression(0)
                        pass

             
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_multiplicativeExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268 
            self.unaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 279
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 270
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 271
                        self.match(self.STAR)
                        self.state = 272 
                        self.unaryExpression()
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 273
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 274
                        self.match(self.DIV)
                        self.state = 275 
                        self.unaryExpression()
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.MultiplicativeExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpression)
                        self.state = 276
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 277
                        self.match(self.MOD)
                        self.state = 278 
                        self.unaryExpression()
                        pass

             
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 50, self.RULE_unaryExpression)
        try:
            self.state = 298
            token = self._input.LA(1)
            if token in [self.T__1, self.IDENTIFIER, self.CONSTANT, self.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284 
                self.postfixExpression(0)

            elif token in [self.PLUS_PLUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.match(self.PLUS_PLUS)
                self.state = 286 
                self.unaryExpression()

            elif token in [self.MINUS_MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(self.MINUS_MINUS)
                self.state = 288 
                self.unaryExpression()

            elif token in [self.T__0, self.AND, self.STAR, self.PLUS, self.MINUS, self.TILDE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 289 
                self.unaryOperator()
                self.state = 290 
                self.unaryExpression()

            elif token in [self.SIZEOF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 292
                self.match(self.SIZEOF)
                self.state = 293
                self.match(self.T__1)
                self.state = 294
                self.match(self.LONG)
                self.state = 295
                self.match(self.RIGHT_PAREN)

            elif token in [self.AND_AND]:
                self.enterOuterAlt(localctx, 6)
                self.state = 296
                self.match(self.AND_AND)
                self.state = 297
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_postfixExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301 
            self.primaryExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 318
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 303
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 304
                        self.match(self.LEFT_BRACKET)
                        self.state = 305 
                        self.expression(0)
                        self.state = 306
                        self.match(self.RIGHT_BRACKET)
                        pass

                    elif la_ == 2:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 308
                        if not self.precpred(self._ctx, 3):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 309
                        self.match(self.T__1)
                        self.state = 311
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__1) | (1 << self.T__0) | (1 << self.SIZEOF) | (1 << self.AND) | (1 << self.AND_AND) | (1 << self.STAR) | (1 << self.PLUS) | (1 << self.PLUS_PLUS) | (1 << self.MINUS) | (1 << self.MINUS_MINUS) | (1 << self.TILDE) | (1 << self.IDENTIFIER) | (1 << self.CONSTANT) | (1 << self.STRING))) != 0):
                            self.state = 310 
                            self.argumentExpressionList(0)


                        self.state = 313
                        self.match(self.RIGHT_PAREN)
                        pass

                    elif la_ == 3:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 314
                        if not self.precpred(self._ctx, 2):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 315
                        self.match(self.PLUS_PLUS)
                        pass

                    elif la_ == 4:
                        localctx = HerocParserParser.PostfixExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpression)
                        self.state = 316
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 317
                        self.match(self.MINUS_MINUS)
                        pass

             
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_argumentExpressionList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324 
            self.assignmentExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.ArgumentExpressionListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_argumentExpressionList)
                    self.state = 326
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 327
                    self.match(self.COMMA)
                    self.state = 328 
                    self.assignmentExpression() 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 56, self.RULE_primaryExpression)
        try:
            self.state = 345
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(self.IDENTIFIER)

            elif token in [self.CONSTANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(self.CONSTANT)

            elif token in [self.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 337 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 336
                        self.match(self.STRING)

                    else:
                        raise NoViableAltException(self)
                    self.state = 339 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)


            elif token in [self.T__1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 341
                self.match(self.T__1)
                self.state = 342 
                self.expression(0)
                self.state = 343
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
        self.enterRule(localctx, 58, self.RULE_initializer)
        try:
            self.state = 357
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347 
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(self.LEFT_BRACE)
                self.state = 349 
                self.initializerList(0)
                self.state = 350
                self.match(self.RIGHT_BRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 352
                self.match(self.LEFT_BRACE)
                self.state = 353 
                self.initializerList(0)
                self.state = 354
                self.match(self.COMMA)
                self.state = 355
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_initializerList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360 
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 362
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 363
                    self.match(self.COMMA)
                    self.state = 364 
                    self.initializer() 
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.blockItemList_sempred
        self._predicates[12] = self.expression_sempred
        self._predicates[15] = self.logicalOrExpression_sempred
        self._predicates[16] = self.logicalAndExpression_sempred
        self._predicates[17] = self.bitwiseOrExpression_sempred
        self._predicates[18] = self.bitwiseXOrExpression_sempred
        self._predicates[19] = self.andExpression_sempred
        self._predicates[20] = self.equalityExpression_sempred
        self._predicates[21] = self.relationalExpression_sempred
        self._predicates[22] = self.shiftExpression_sempred
        self._predicates[23] = self.additiveExpression_sempred
        self._predicates[24] = self.multiplicativeExpression_sempred
        self._predicates[26] = self.postfixExpression_sempred
        self._predicates[27] = self.argumentExpressionList_sempred
        self._predicates[30] = self.initializerList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def shiftExpression_sempred(self, localctx:ShiftExpressionContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         

    def relationalExpression_sempred(self, localctx:RelationalExpressionContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         

    def logicalOrExpression_sempred(self, localctx:LogicalOrExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def multiplicativeExpression_sempred(self, localctx:MultiplicativeExpressionContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def bitwiseXOrExpression_sempred(self, localctx:BitwiseXOrExpressionContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def bitwiseOrExpression_sempred(self, localctx:BitwiseOrExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def andExpression_sempred(self, localctx:AndExpressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def blockItemList_sempred(self, localctx:BlockItemListContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def logicalAndExpression_sempred(self, localctx:LogicalAndExpressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def equalityExpression_sempred(self, localctx:EqualityExpressionContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         

    def argumentExpressionList_sempred(self, localctx:ArgumentExpressionListContext, predIndex:int):
            if predIndex == 24:
                return self.precpred(self._ctx, 1)
         

    def postfixExpression_sempred(self, localctx:PostfixExpressionContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 1)
         

    def initializerList_sempred(self, localctx:InitializerListContext, predIndex:int):
            if predIndex == 25:
                return self.precpred(self._ctx, 1)
         



