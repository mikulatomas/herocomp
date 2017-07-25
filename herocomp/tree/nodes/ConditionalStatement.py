from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node
from tree.nodes.types.VariableType import VariableType


class ConditionalStatement(Node):
    def __init__(self, parent=None):
        super(ConditionalStatement, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "ConditionalStatement: {}".format(valuesString)

    def else_label(self):
        return "TERNARY{0}_ELSE".format(self.number)

    def end_label(self):
        return "TERNARY{0}_END".format(self.number)

    def get_code(self):
        code = ""

        # Condition
        code += self.statements[0].get_code()
        code += instruction("cmpq", number_constant(0), Registers.RAX)
        code += instruction("je", self.else_label())
        # Expression
        code += self.statements[1].get_code()
        code += instruction("jmp", self.end_label())
        code += label(self.else_label())
        # Else
        code += self.statements[2].get_code()
        code += label(self.end_label())

        return code
