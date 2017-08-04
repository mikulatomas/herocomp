from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.loops.Loop import Loop
from tree.nodes.types.VariableType import VariableType


class WhileLoop(Loop):
    def __init__(self, parent=None):
        super(WhileLoop, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "WhileLoop: {}".format(valuesString)

    def get_code(self):
        code = ""

        code += label(self.start_label())

        # Condition
        code += self.statements[0].get_code()
        code += instruction("cmpq", number_constant(0), Registers.RAX)
        code += instruction("je", self.end_label())

        # Body
        block_code, has_return = self.statements[1].get_code()
        code += block_code

        code += instruction("jmp", self.start_label())
        code += label(self.end_label())

        return code
