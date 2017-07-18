from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node
from tree.nodes.operations.OperationType import OperationType


class BinaryOperation(Node):
    def __init__(self, operation, parent=None):
        self.operation = operation
        super(BinaryOperation, self).__init__(parent=parent)

    def get_code(self):
        code = ""
        stack = self.fill_operation_stack()

        while len(stack) > 0:
            item = stack.pop()

            if isinstance(item, OperationType):
                # operation
                code += item.get_operation_code()
            else:
                # argumet
                code += item.get_code()
                code += instruction("pushq", Registers.RAX)

        code += instruction("pop", Registers.RAX)

        return code

    def fill_operation_stack(self):
        stack = []

        stack.append(self.operation)

        for statement in self.statements:
            for value in statement.fill_operation_stack():
                stack.append(value)

        return stack

    def __str__(self):
        statementsString = self.printStatements()
        return "BinaryOperation {}: {}".format(self.operation,
                                                 statementsString)
