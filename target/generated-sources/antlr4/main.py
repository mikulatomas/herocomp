import sys

from antlr4 import *
from HerocLexer import HerocLexer
from HerocParser import HerocParser


def main(argv):
    input = FileStream(argv[1])
    lexer = HerocLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HerocParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main(sys.argv)
