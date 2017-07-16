from asm.Asm import *
from asm.Registers import Registers
from tree.Node import Node


class FunctionCall(Node):
    def __init__(self, identifier=None, parent=None):
        self.identifier = identifier
        super(FunctionCall, self).__init__(parent)

    def __str__(self):
        argumentsString = self.printStatements()
        self.identifier.depth = self.depth + 1

        return "FunctionCall: \n{} {}".format(self.identifier.generateTabsForDepth() + str(self.identifier), argumentsString,)

    def get_code(self):
        code = ""

        # Save Registers
        not_save_registers = [Registers.RDI, Registers.RSI, Registers.RDX, Registers.RCX, Registers.R8, Registers.R9]

        for register in not_save_registers:
            code += push(register)

        code += call(self.identifier.name)

        # Restore Registers
        for register in reversed(not_save_registers):
            code += pop(register)

        return code
