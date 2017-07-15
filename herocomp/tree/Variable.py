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

        super(Variable, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()
        self.identifier.depth = self.depth + 1

        return "Variable {}: \n{} {}".format(self.variable_type,
                                             self.identifier.generateTabsForDepth() + str(self.identifier),
                                             valuesString)
