import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.Node import Node
from tree.VariableType import VariableType


class Variable(Node):
    def __init__(self,
                 identifier,
                 variable_type=VariableType.VARIABLE,
                 parent=None):

        self.identifier = identifier
        self.identifier.parent = self
        self.variable_type = variable_type
        self.variable_offset = None

        super(Variable, self).__init__(parent=parent)

    def get_code(self):
        code = ""

        if self.variable_type == VariableType.VARIABLE:
            # If variable has assignment
            for statement in self.statements:
                code += statement.get_code()
            # if len(self.statements) == 1:
            #     assignment = self.statements[0]
                # assignment
                # if isinstance(assignment.statements[0], tree.Number.Number):
                #     code += mov(assignment.statements[0].get_asm_value(), str(self.variable_offset) + Registers.RBP.dereference())
                # elif isinstance(assignment.statements[0], tree.Identifier.Identifier):
                #     code += mov(assignment.statements[0].get_asm_value(), str(self.variable_offset) + Registers.RBP.dereference())


        return code

    def __str__(self):
        valuesString = self.printStatements()
        self.identifier.depth = self.depth + 1

        return "Variable {}: \n{} {}".format(self.variable_type,
                                             self.identifier.generateTabsForDepth() + str(self.identifier),
                                             valuesString)
