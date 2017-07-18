from asm.Asm import *
from asm.Registers import Registers
from tree.Node import Node
from tree.VariableType import VariableType


class Loop(Node):
    def __init__(self, parent=None):
        super(Loop, self).__init__(parent=parent)

    def start_label(self):
        return "LOOP{0}".format(self.number)

    def next_label(self):
        return "LOOP{0}_NEXT".format(self.number)

    def end_label(self):
        return "LOOP{0}_END".format(self.number)
