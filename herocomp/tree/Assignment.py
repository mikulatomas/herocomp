import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.Node import Node
from tree.operations.OperationType import OperationType


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
        
        if not isinstance(destination, tree.Identifier.Identifier):
            raise ValueError("Left side of assignment {0} has to be identifier!")

        value = self.statements[1]

        code += value.get_code()
        # Maybe for dereference
        code += mov(Registers.RAX, Registers.R15)

        if isinstance(destination, tree.Identifier.Identifier):
            if isinstance(self.parent, tree.Variable.Variable):
                code += mov(Registers.R15, str(self.parent.variable_offset) + Registers.RBP.dereference())
            else:
                code += mov(Registers.R15, str(destination.get_stack_offset()) + Registers.RBP.dereference())

        return code
