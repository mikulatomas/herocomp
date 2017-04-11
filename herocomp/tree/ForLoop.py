from tree.Node import Node
from tree.VariableType import VariableType


class ForLoop(Node):
    def __init__(self, parent=None):
        super(ForLoop, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "ForLoop: {}".format(valuesString)
