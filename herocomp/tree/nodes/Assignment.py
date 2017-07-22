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
            value.statements.append(destination)
            value.statements.append(self.statements[1])
            # value.addStatement(destination)
            # value.addStatement(self.statements[1])
        else:
            value = self.statements[1]

        if not (isinstance(destination, tree.nodes.types.Identifier.Identifier) or isinstance(destination, tree.nodes.operations.UnaryOperation.UnaryOperation)):
            raise ValueError("Left side of assignment has to be identifier or unary operation!")

        # code += "value\n"
        code += value.get_code()
        # code += "value/////\n"
        # Maybe for dereference
        code += instruction("movq", Registers.RAX, Registers.R15)


        # TODO FIX
        if isinstance(destination, tree.nodes.types.Identifier.Identifier):
            # TODO - prepsat na metodo z ident
            if isinstance(self.parent, tree.nodes.types.Variable.Variable):
                destination_addres = str(self.parent.variable_offset) + Registers.RBP.dereference()
            else:
                destination_addres = str(destination.get_stack_offset()) + Registers.RBP.dereference()

            code += instruction("movq", Registers.R15, destination_addres)
        # if destination is dereference
        elif isinstance(destination, tree.nodes.operations.UnaryOperation.UnaryOperation):
            if destination.operation is tree.nodes.operations.OperationType.OperationType.DEREFERENCE:
                # Code of operand
                code += destination.statements[0].get_code()
                code += instruction("movq", Registers.R15, Registers.RAX.dereference())


        return code
