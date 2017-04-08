import logging
import sys

from antlr4 import *
# from AST_first import AST
from HerocLexer import HerocLexer
# from HerocListener import HerocListener
from HerocParser import HerocParser
from tree.TreeVisitor import TreeVisitor


def main(argv):
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = HerocLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HerocParser(stream)
    tree = parser.sourcefile()

    # print(tree.toStringTree(recog=parser))
    
    # listener = HerocListener()
    treeVisitor = TreeVisitor()
    ast = treeVisitor.visit(tree);
    print()
    print(ast)

    # ast = AST(tree)
    #
    # print(ast)

if __name__ == '__main__':
    main(sys.argv)
