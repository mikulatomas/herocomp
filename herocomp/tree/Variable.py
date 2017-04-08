from tree.Node import Node
from tree.VariableType import VariableType


class Variable(Node):
    def __init__(self,
                 identifier,
                 variable_type=VariableType.VARIABLE,
                 values=[],
                 array_size=None,
                 parent=None):

        self.variable_type = variable_type
        self.identifier = identifier
        self.identifier.parent = self
        self.array_size = array_size

        if self.variable_type is VariableType.ARRAY:
            self.array_size.parent = self

        super(Variable, self).__init__(statements=values, parent=parent)

    def __str__(self):
        valuesString = self.printStatements()
        self.identifier.depth = self.depth + 1

        if self.variable_type == VariableType.ARRAY:
            self.array_size.depth = self.depth + 1
            return "Variable {}: \n{}\n{} (size) {}".format(self.variable_type,
                                                           self.identifier.generateTabsForDepth() + str(self.identifier),
                                                           self.array_size.generateTabsForDepth() + str(self.array_size),
                                                           valuesString)
        else:
            return "Variable {}: \n{} {}".format(self.variable_type,
                                                 self.identifier.generateTabsForDepth() + str(self.identifier),
                                                 valuesString)
