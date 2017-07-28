import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node


class Array(Node):
    def __init__(self, array_size=None, parent=None):
        self.array_size = array_size

        if self.array_size is not None:
            self.array_size.parent = self

        super(Array, self).__init__(parent)

    def setArraySize(self, array_size):
        self.array_size = array_size
        self.array_size.parent = self

    def __str__(self):
        valuesString = self.printStatements()
        # self.array_size.depth = self.depth + 1

        return "Array: {}".format(valuesString)
        # return "Array: \n{} {}".format(self.array_size.generateTabsForDepth() + str(self.array_size), valuesString)

    def get_code(self):
        code = ""

        # Find parent Block
        block = self.find_parent_block()

        # stack_offset = block.get_variable_offset()
        # code += "OFFSET {0}\n".format(stack_offset)

        code += instruction("subq", number_constant((self.array_size.value + 1) * 8), Registers.RSP)

        stack_offset = block.get_variable_offset()

        # # First value
        # i = len(self.statements) - 1
        # code += self.statements[i].get_code()
        # code += instruction("movq", Registers.RAX, str(stack_offset + 8) + Registers.RBP.dereference())


        if len(self.statements) == 0:
            for i in range(self.array_size.value - 1):
                code += instruction("movq", number_constant(0), str(stack_offset) + Registers.RBP.dereference())
                stack_offset = block.get_variable_offset()

            code += instruction("movq", number_constant(0), str(stack_offset) + Registers.RBP.dereference())
        else:
            # Rest of the values
            for i in range(len(self.statements) - 1, 0, -1):
                code += self.statements[i].get_code()
                code += instruction("movq", Registers.RAX, str(stack_offset) + Registers.RBP.dereference())
                stack_offset = block.get_variable_offset()

            # Last value
            code += self.statements[0].get_code()
            code += instruction("movq", Registers.RAX, str(stack_offset) + Registers.RBP.dereference())


        code += instruction("leaq", str(stack_offset) + Registers.RBP.dereference(), Registers.RAX)

        return code
