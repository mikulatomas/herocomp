from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.loops.Loop import Loop
from tree.nodes.types.VariableType import VariableType


class DoWhileLoop(Loop):
    def __init__(self, parent=None):
        super(DoWhileLoop, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "DoWhileLoop: {}".format(valuesString)

    def get_code(self):
        code = ""

        code += label(self.start_label())
        # Body
        block_code, has_return = self.statements[0].get_code()
        code += block_code
        # Condition
        code += self.statements[1].get_code()
        code += instruction("cmpq", number_constant(0), Registers.RAX)
        code += instruction("je", self.end_label())

        code += instruction("jmp", self.start_label())
        code += label(self.end_label())

        return code
