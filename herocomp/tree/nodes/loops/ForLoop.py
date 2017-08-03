from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.loops.Loop import Loop
from tree.nodes.types.VariableType import VariableType


class ForLoop(Loop):
    def __init__(self, inicialization, condition, incrementation, parent=None):
        self.inicialization = inicialization
        if self.inicialization is not None:
            self.inicialization.parent = self
        self.condition = condition
        if self.condition is not None:
            self.condition.parent = self
        self.incrementation = incrementation
        if self.incrementation is not None:
            self.incrementation.parent = self
        super(ForLoop, self).__init__(parent=parent)

    def __str__(self):
        # TODO print
        valuesString = self.printStatements()

        return "ForLoop: {}".format(valuesString)

    def get_code(self):
        code = ""

        if self.inicialization is not None:
            code += self.inicialization.get_code()

        code += label(self.start_label())

        if self.condition is not None:
            code += self.condition.get_code()
            code += instruction("cmpq", number_constant(0), Registers.RAX)
            code += instruction("je", self.end_label())

        block_code, has_return = self.statements[0].get_code()
        code += block_code

        if self.incrementation is not None:
            code += label(self.next_label())
            code += self.incrementation.get_code()

        code += instruction("jmp", self.start_label())
        code += label(self.end_label())

        return code

    def next_label(self):
        return "LOOP{0}_NEXT".format(self.number)
