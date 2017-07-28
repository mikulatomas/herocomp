import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node
from tree.nodes.types.VariableType import VariableType


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

        # if self.variable_type == VariableType.VARIABLE:
            # If variable has assignment
        if len(self.statements) != 0:
            for statement in self.statements:
                code += statement.get_code()
        else:
            pass

            # if len(self.statements) == 1:
            #     assignment = self.statements[0]
                # assignment
                # if isinstance(assignment.statements[0], tree.Number.Number):
                #     code += movq(assignment.statements[0].get_asm_value(), str(self.variable_offset) + Registers.RBP.dereference())
                # elif isinstance(assignment.statements[0], tree.nodes.types.Identifier.Identifier):
                #     code += movq(assignment.statements[0].get_asm_value(), str(self.variable_offset) + Registers.RBP.dereference())
        # elif self.variable_type == VariableType.ARRAY:

        return code

    def get_global_code(self):
        code = ""

        if self.variable_type is VariableType.ARRAY:
            assignment = self.statements[0]
            array = assignment.statements[1]

            if len(array.statements) > 0:
                code += label(self.identifier.name)
                for item in array.statements:
                    value = item.value
                    code += quad_directive(value)
            else:
                code += global_array(self.identifier.name, array.array_size.value)
        else:
            code += label(self.identifier.name)
            if len(self.statements) > 0:
                assignment = self.statements[0]
                value = assignment.statements[1]
                if isinstance(value, tree.nodes.types.Number.Number):
                    code += quad_directive(value.value)
                elif isinstance(value, tree.nodes.types.Identifier.Identifier):
                    code += quad_directive(value.name)
                elif isinstance(value, tree.nodes.operations.UnaryOperation.UnaryOperation):
                    code += quad_directive(value.statements[0].name)
            else:
                code += quad_directive(0)

        return code

    def __str__(self):
        valuesString = self.printStatements()
        self.identifier.depth = self.depth + 1

        return "Variable {}: \n{} {}".format(self.variable_type,
                                             self.identifier.generateTabsForDepth() + str(self.identifier),
                                             valuesString)
