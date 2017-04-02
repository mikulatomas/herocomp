import sys
from AST import AST

from antlr4 import *
from HerocLexer import HerocLexer
from HerocListener import HerocListener
from HerocParser import HerocParser


def main(argv):
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = HerocLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HerocParser(stream)
    tree = parser.program()

    print(tree.toStringTree(recog=parser))

    listener = HerocListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(AST(tree))
    # print('result_stack=', listener.stack)


if __name__ == '__main__':
    main(sys.argv)
