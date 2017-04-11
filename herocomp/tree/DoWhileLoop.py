from tree.Node import Node
from tree.VariableType import VariableType


class DoWhileLoop(Node):
    def __init__(self, parent=None):
        super(DoWhileLoop, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "DoWhileLoop: {}".format(valuesString)
