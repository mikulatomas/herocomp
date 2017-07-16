from asm.Asm import *
from asm.Registers import Registers
from tree.Node import Node


class Number(Node):
    def __init__(self, value=None, parent=None):
        self.value = value
        super(Number, self).__init__(parent)

    def __str__(self):
        return "Number: {0}".format(self.value)

    def get_asm_value(self):
        return "$" + str(self.value)

    def get_code(self):
        return mov(self.get_asm_value(), Registers.RAX)
