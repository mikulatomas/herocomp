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
            error_string = "Variable {0} is not declared a".format(self.name)
            raise ValueError(error_string)

        return offset

    def _get_argument_location(self):
        parent = self.parent
        location = None

        while parent.parent != None:
            if isinstance(parent, tree.nodes.Function.Function):
                location = parent.arguments_table.get(self.name)
                break

            parent = parent.parent

        if location is None:
            error_string = "Variable {0} is not an argument of the function".format(self.name)
            raise ValueError(error_string)

        return location

    def get_value_address(self):
        try:
            offset = self.get_stack_offset()
            return str(offset) + Registers.RBP.dereference()
        except Exception as e:
            # Try to find in function argument
            try:
                return self._get_argument_location()
            except Exception as e:
                raise

    def get_code(self):
        return instruction("movq", self.get_value_address(), Registers.RAX)

    # def fill_operation_stack(self):
    #     stack = []
    #     stack.append(self)
    #     return stack
