from asm.Asm import *
from tree.Node import Node
from tree.Program import Program


class AST():
    def __init__(self):
        self.root = Program()

    def __str__(self):
        return str(self.root)

    def get_code(self, filename):
        code = ""

        code += filename_directive(filename)

        code += self.root.get_code()

        code += compiler_ident_directive()
        return code
