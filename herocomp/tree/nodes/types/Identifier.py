import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node


class Identifier(Node):
    def __init__(self, name, parent=None):
        self.name = name
        super(Identifier, self).__init__(parent)

    def __str__(self):
        return "Identifier: {}".format(self.name)

    def get_stack_offset(self):
        parent = self.parent
        offset = None

        while parent.parent != None:
            if isinstance(parent, tree.nodes.Block.Block):
                try:
                    offset = parent.variables_table.get_variable_offset(self.name)
                except ValueError as e:
                    pass
            parent = parent.parent

        if offset is None:
            error_string = "Variable {0} is not declared".format(self.name)
            raise ValueError(error_string)

        return offset

    def get_code(self):
        return instruction("movq", str(self.get_stack_offset()) + Registers.RBP.dereference(), Registers.RAX)

    def fill_operation_stack(self):
        stack = []
        stack.append(self)
        return stack
