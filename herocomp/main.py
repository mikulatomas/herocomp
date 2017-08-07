import logging
import sys
from os.path import basename

from antlr4 import *
from HerocErrorListener import HerocErrorListener
from HerocLexer import HerocLexer
from HerocParser import HerocParser
from tree.TreeVisitor import TreeVisitor


def load_source_to_ast(filename):
    input_stream = FileStream(filename)
    lexer = HerocLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HerocParser(stream)
    parser._listeners = [HerocErrorListener()]

    try:
        tree = parser.sourcefile()
    except:
        return None

    treeVisitor = TreeVisitor()
    ast = treeVisitor.visit(tree)

    return ast


def main(argv):
    filename = sys.argv[1]

    ast = load_source_to_ast(filename)

    if ast is not None:
        code = ast.get_code(basename(filename))
        print(code)


if __name__ == '__main__':
    main(sys.argv)
