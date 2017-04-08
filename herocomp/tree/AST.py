from tree.Node import Node
from tree.Program import Program


class AST():
    def __init__(self):
        self.root = Program()

    def __str__(self):
        return str(self.root)
