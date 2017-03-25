# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .herocListener import herocListener
else:
    from herocListener import herocListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\5")
        buf.write("\b\4\2\t\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\6\2\4\3\2\2\2\4")
        buf.write("\5\7\3\2\2\5\6\7\4\2\2\6\3\3\2\2\2\2")
        return buf.getvalue()
		

class herocParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__0=1
    ID=2
    WS=3

    tokenNames = [ "<INVALID>", "'hello'", "ID", "WS" ]

    RULE_r = 0

    ruleNames =  [ "r" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(herocParser.ID, 0)

        def getRuleIndex(self):
            return herocParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, herocListener ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, herocListener ):
                listener.exitR(self)




    def r(self):

        localctx = herocParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(self.T__0)
            self.state = 3
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




