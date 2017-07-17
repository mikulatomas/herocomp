import logging
import sys
from os.path import basename

from antlr4 import *
from HerocErrorListener import HerocErrorListener
# from AST_first import AST
from HerocLexer import HerocLexer
# from HerocListener import HerocListener
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
    # logging.basicConfig(level=logging.INFO)
    filename = sys.argv[1]
    show_ast = sys.argv[2]
    compile_code = sys.argv[3]
    ast = load_source_to_ast(filename)

    if show_ast == str(1):
        print(ast)

    if compile_code == str(1):
        print(ast.get_code(basename(filename)))


if __name__ == '__main__':
    main(sys.argv)
