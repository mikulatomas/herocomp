from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node
from tree.nodes.types.VariableType import VariableType


class IfStatement(Node):
    def __init__(self, parent=None):
        super(IfStatement, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "IfStatement: {}".format(valuesString)

    def get_code(self):
        code = ""

        code += self.statements[0].get_code()
        code += instruction("cmpq", number_constant(0), Registers.RAX)
        code += instruction("je", self.else_label())
        # then block
        block_code, has_return = self.statements[1].get_code()
        code += block_code
        code += instruction("jmp", self.end_label())
        code += label(self.else_label())

        # else block
        if len(self.statements) == 3:
            block_code, has_return = self.statements[2].get_code()
            code += block_code

        code += label(self.end_label())

        return code

    def else_label(self):
        return "IF{0}_ELSE".format(self.number)

    def end_label(self):
        return "IF{0}_END".format(self.number)
