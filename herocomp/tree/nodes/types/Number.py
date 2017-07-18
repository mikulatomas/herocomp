from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node


class Number(Node):
    def __init__(self, value=None, parent=None):
        self.value = value
        super(Number, self).__init__(parent)

    def __str__(self):
        return "Number: {0}".format(self.value)

    def get_code(self):
        return instruction("movq", number_constant(self.value), Registers.RAX)

    def fill_operation_stack(self):
        stack = []
        stack.append(self)
        return stack
