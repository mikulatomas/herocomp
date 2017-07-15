from tree.Node import Node


class FunctionCall(Node):
    def __init__(self, identifier=None, parent=None):
        self.identifier = identifier
        super(FunctionCall, self).__init__(parent)

    def __str__(self):
        argumentsString = self.printStatements()
        self.identifier.depth = self.depth + 1

        return "FunctionCall: \n{} {}".format(self.identifier.generateTabsForDepth() + str(self.identifier), argumentsString,)
