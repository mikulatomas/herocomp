from tree.Node import Node


class Function(Node):
    def __init__(self, identifier, parent=None):
        self.identifier = identifier
        self.arguments = []
        super(Function, self).__init__(parent)

    def addArgument(self, argumentNode):
        self.arguments.append(argumentNode)
        argumentNode.parent = self

    def addArgumentsList(self, argumentNodeList):
        for node in argumentNodeList:
            self.addArgument(node)

    def __str__(self):
        return "Function: {}".format(self.name)

    def printArguments(self):
        argumentsString = ""

        if self.arguments is not None:
            for argument in self.arguments:
                argument.depth = self.depth + 1
                argumentsString += "\n"
                argumentsString += argument.generateTabsForDepth()
                argumentsString += str(argument)

        return argumentsString

    def __str__(self):
        blockString = self.printStatements()
        argumentsString = self.printArguments()
        self.identifier.depth = self.depth + 1

        return "Function: \n{} {} {}".format(self.identifier.generateTabsForDepth() + str(self.identifier),
                                           argumentsString,
                                           blockString)
