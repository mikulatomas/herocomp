from tree.Node import Node
from tree.VariableType import VariableType


class IfStatement(Node):
    def __init__(self, parent=None):
        super(IfStatement, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "IfStatement: {}".format(valuesString)
