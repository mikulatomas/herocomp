from tree.Node import Node
from tree.VariableType import VariableType


class ConditionalStatement(Node):
    def __init__(self, parent=None):
        super(ConditionalStatement, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "ConditionalStatement: {}".format(valuesString)
