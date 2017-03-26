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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3A")
        buf.write("A\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\3\3\3\5")
        buf.write("\3\33\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5$\n\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\5\6-\n\6\3\7\3\7\5\7\61\n\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\7\b:\n\b\f\b\16\b=\13\b\3\t\3\t")
        buf.write("\3\t\2\3\16\n\2\4\6\b\n\f\16\20\2\2>\2\25\3\2\2\2\4\32")
        buf.write("\3\2\2\2\6\34\3\2\2\2\b \3\2\2\2\n,\3\2\2\2\f.\3\2\2\2")
        buf.write("\16\64\3\2\2\2\20>\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2")
        buf.write("\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2")
        buf.write("\2\27\25\3\2\2\2\30\33\5\6\4\2\31\33\5\b\5\2\32\30\3\2")
        buf.write("\2\2\32\31\3\2\2\2\33\5\3\2\2\2\34\35\7\n\2\2\35\36\7")
        buf.write("9\2\2\36\37\7\67\2\2\37\7\3\2\2\2 !\79\2\2!#\7\3\2\2\"")
        buf.write("$\5\n\6\2#\"\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\62\2\2&\'")
        buf.write("\5\f\7\2\'\t\3\2\2\2(-\79\2\2)*\79\2\2*+\78\2\2+-\5\n")
        buf.write("\6\2,(\3\2\2\2,)\3\2\2\2-\13\3\2\2\2.\60\7\65\2\2/\61")
        buf.write("\5\16\b\2\60/\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63")
        buf.write("\7\66\2\2\63\r\3\2\2\2\64\65\b\b\1\2\65\66\5\20\t\2\66")
        buf.write(";\3\2\2\2\678\f\3\2\28:\5\20\t\29\67\3\2\2\2:=\3\2\2\2")
        buf.write(";9\3\2\2\2;<\3\2\2\2<\17\3\2\2\2=;\3\2\2\2>?\5\6\4\2?")
        buf.write("\21\3\2\2\2\b\25\32#,\60;")
        return buf.getvalue()
		

class HerocParserParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__0=1
    BREAK=2
    CONTINUE=3
    DO=4
    ELSE=5
    FOR=6
    IF=7
    LONG=8
    RETURN=9
    SIZEOF=10
    WHILE=11
    NOT=12
    NOT_EQUAL=13
    MOD=14
    MOD_ASIGN=15
    AND=16
    AND_AND=17
    AND_ASSIGN=18
    STAR=19
    STAR_ASSIGN=20
    PLUS=21
    PLUS_PLUS=22
    PLUS_ASSIGN=23
    MINUS=24
    MINUS_MINUS=25
    MINUS_ASSIGN=26
    DIV=27
    DIV_ASSIGN=28
    COLON=29
    LESS=30
    LEFT_SHIFT=31
    LEFT_SHIFT_ASSIGN=32
    LESS_EQUAL=33
    ASSIGN=34
    EQUAL=35
    GREATER=36
    GREATER_EQUAL=37
    RIGHT_SHIFT=38
    RIGHT_SHIFT_ASSIGN=39
    QUESTION=40
    CARET=41
    XOR_ASSIGN=42
    OR=43
    OR_ASSIGN=44
    OR_OR=45
    TILDE=46
    LEFT_PAREN=47
    RIGHT_PAREN=48
    LEFT_BRACKET=49
    RIGHT_BRACKET=50
    LEFT_BRACE=51
    RIGHT_BRACE=52
    SEMI=53
    COMMA=54
    IDENTIFIER=55
    CONSTANT=56
    OCTAL_CONSTANT=57
    HEX_CONSTANT=58
    CHAR=59
    STRING=60
    WHITESPACE=61
    NEWLINE=62
    COMMENT=63

    tokenNames = [ "<INVALID>", "'('", "BREAK", "'continue'", "'do'", "'else'", 
                   "'for'", "'if'", "'long'", "'return'", "'sizeof'", "'while'", 
                   "NOT", "'!='", "'%'", "'%='", "'&'", "'&&'", "'&='", 
                   "'*'", "'*='", "'+'", "'++'", "'+='", "'-'", "'--'", 
                   "'-='", "'/'", "'/='", "':'", "'<'", "'<<'", "'<<='", 
                   "'<='", "'='", "'=='", "'>'", "'>='", "'>>'", "'>>='", 
                   "'?'", "'^'", "'^='", "'|'", "'|='", "'||'", "'~'", "LEFT_PAREN", 
                   "')'", "'['", "']'", "'{'", "'}'", "';'", "','", "IDENTIFIER", 
                   "CONSTANT", "OCTAL_CONSTANT", "HEX_CONSTANT", "CHAR", 
                   "STRING", "WHITESPACE", "NEWLINE", "COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_declarationVariable = 2
    RULE_declarationFunction = 3
    RULE_functionArgsList = 4
    RULE_compoundStatement = 5
    RULE_blockItemList = 6
    RULE_blockItem = 7

    ruleNames =  [ "program", "declaration", "declarationVariable", "declarationFunction", 
                   "functionArgsList", "compoundStatement", "blockItemList", 
                   "blockItem" ]

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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HerocParserParser.LONG or _la==HerocParserParser.IDENTIFIER:
                self.state = 16 
                self.declaration()
                self.state = 21
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
            self.state = 24
            token = self._input.LA(1)
            if token in [self.LONG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22 
                self.declarationVariable()

            elif token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23 
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
            self.state = 26
            self.match(self.LONG)
            self.state = 27
            self.match(self.IDENTIFIER)
            self.state = 28
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

        def functionArgsList(self):
            return self.getTypedRuleContext(HerocParserParser.FunctionArgsListContext,0)


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
            self.state = 30
            self.match(self.IDENTIFIER)
            self.state = 31
            self.match(self.T__0)
            self.state = 33
            _la = self._input.LA(1)
            if _la==HerocParserParser.IDENTIFIER:
                self.state = 32 
                self.functionArgsList()


            self.state = 35
            self.match(self.RIGHT_PAREN)
            self.state = 36 
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionArgsListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionArgsList(self):
            return self.getTypedRuleContext(HerocParserParser.FunctionArgsListContext,0)


        def IDENTIFIER(self):
            return self.getToken(HerocParserParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return HerocParserParser.RULE_functionArgsList

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.enterFunctionArgsList(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, HerocParserListener ):
                listener.exitFunctionArgsList(self)




    def functionArgsList(self):

        localctx = HerocParserParser.FunctionArgsListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionArgsList)
        try:
            self.state = 42
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(self.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(self.IDENTIFIER)
                self.state = 40
                self.match(self.COMMA)
                self.state = 41 
                self.functionArgsList()
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
        self.enterRule(localctx, 10, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(self.LEFT_BRACE)
            self.state = 46
            _la = self._input.LA(1)
            if _la==HerocParserParser.LONG:
                self.state = 45 
                self.blockItemList(0)


            self.state = 48
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_blockItemList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51 
            self.blockItem()
            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HerocParserParser.BlockItemListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_blockItemList)
                    self.state = 53
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 54 
                    self.blockItem() 
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_blockItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60 
            self.declarationVariable()
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
        self._predicates[6] = self.blockItemList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def blockItemList_sempred(self, localctx:BlockItemListContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         



