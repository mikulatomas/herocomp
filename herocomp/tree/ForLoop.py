from asm.Asm import *
from asm.Registers import Registers
from tree.Loop import Loop
from tree.VariableType import VariableType


class ForLoop(Loop):
    def __init__(self, parent=None):
        super(ForLoop, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "ForLoop: {}".format(valuesString)

    def get_code(self):
        code = ""

        code += self.statements[0].get_code()
        code += label(self.start_label())
        code += self.statements[1].get_code()
        code += instruction("cmpq", number_constant(0), Registers.RAX)
        code += instruction("je", self.end_label())
        block_code, has_return = self.statements[3].get_code()
        code += block_code
        code += label(self.next_label())
        code += self.statements[2].get_code()
        code += instruction("jmp", self.start_label())
        code += label(self.end_label())

        return code
