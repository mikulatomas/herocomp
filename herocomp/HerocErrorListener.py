import sys

from antlr4.error.ErrorListener import ErrorListener


class HerocErrorListener( ErrorListener ):

    def __init__(self):
        super(HerocErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("line " + str(line) + ":" + str(column) + " " + msg, file=sys.stderr)
        raise Exception("Oh no!!")

    # def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    #     raise Exception("Oh no!!")
    #
    # def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    #     raise Exception("Oh no!!")
    #
    # def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    #     raise Exception("Oh no!!")
