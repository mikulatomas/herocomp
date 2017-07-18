from tree.nodes.Node import Node
from tree.nodes.types.VariableType import VariableType


class DoWhileLoop(Node):
    def __init__(self, parent=None):
        super(DoWhileLoop, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "DoWhileLoop: {}".format(valuesString)
