import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.AssignmentType import AssignmentType
from tree.nodes.Node import Node
from tree.nodes.operations.OperationType import OperationType


class Assignment(Node):
    def __init__(self, operation, parent=None):
        self.operation = operation
        super(Assignment, self).__init__(parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "Assignment {}: {}".format(self.operation,
                                                 statementsString)

    def get_code(self):
        code = ""

        destination = self.statements[0]

        if self.operation is not AssignmentType.ASSIGN:
            arithmetic_operation = self.operation.get_operation()
            value = tree.nodes.operations.BinaryOperation.BinaryOperation(arithmetic_operation)
            value.addStatement(destination)
            value.addStatement(self.statements[1])
            value.parent = self
        else:
            value = self.statements[1]

        if not (isinstance(destination, tree.nodes.types.Identifier.Identifier) or isinstance(destination, tree.nodes.operations.UnaryOperation.UnaryOperation)):
            raise ValueError("Left side of assignment has to be identifier or unary operation!")

        code += value.get_code()

        # Restore original parent in case of binary operation
        destination.parent = self

        # Maybe for dereference
        code += instruction("movq", Registers.RAX, Registers.R12)

        if isinstance(destination, tree.nodes.types.Identifier.Identifier):
            destination_address = destination.get_value_address()

            code += instruction("movq", Registers.R12, destination_address)
        # if destination is dereference or array dereference
        elif isinstance(destination, tree.nodes.operations.UnaryOperation.UnaryOperation):
            if destination.operation is tree.nodes.operations.OperationType.OperationType.DEREFERENCE:
                # Code of operand
                code += destination.statements[0].get_code()
                code += instruction("movq", Registers.R12, Registers.RAX.dereference())
            if destination.operation is tree.nodes.operations.OperationType.OperationType.SUBSCRIPT:
                destination_address = destination.statements[0].get_value_address()
                code += destination.get_code()
                if Registers.RIP.value not in destination_address:
                    code += instruction("movq", Registers.R12, Registers.RAX.dereference())

        return code
