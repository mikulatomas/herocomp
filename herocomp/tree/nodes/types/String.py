from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node


class String(Node):
    def __init__(self, value="", parent=None):
        self.value = value
        super(String, self).__init__(parent)

    def __str__(self):
        return "String: {0}".format(self.value)

    def get_code(self):
        code = ""

        block = self.find_parent_block()

        code += instruction("subq", number_constant((len(self.value) + 1) * 8), Registers.RSP)

        stack_offset = block.get_variable_offset()

        # Rest of the values
        for i in range(len(self.statements) - 1, 0, -1):
            code += instruction("movq", number_constant(self.statements[i].value), Registers.RAX)
            code += instruction("movq", Registers.RAX, str(stack_offset) + Registers.RBP.dereference())
            stack_offset = block.get_variable_offset()

        # Last value
        code += instruction("movq", number_constant(self.statements[0].value), Registers.RAX)
        code += instruction("movq", Registers.RAX, str(stack_offset) + Registers.RBP.dereference())

        code += instruction("leaq", str(stack_offset) + Registers.RBP.dereference(), Registers.RAX)

        if len(self.statements) == 1:
            code += instruction("movq", Registers.RAX.dereference(), Registers.RAX)

        return code
