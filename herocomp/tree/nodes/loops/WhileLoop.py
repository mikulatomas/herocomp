from tree.nodes.Node import Node
from tree.nodes.types.VariableType import VariableType


class WhileLoop(Node):
    def __init__(self, parent=None):
        super(WhileLoop, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "WhileLoop: {}".format(valuesString)
