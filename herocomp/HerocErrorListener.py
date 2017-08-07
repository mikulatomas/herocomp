import sys

from antlr4.error.ErrorListener import ErrorListener
from tools.ErrorOutput import eprint


class HerocErrorListener( ErrorListener ):

    def __init__(self):
        super(HerocErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        eprint("SYNTAX ERROR: line " + str(line) + ":" + str(column) + " " + msg)
        raise Exception("AST Error")
