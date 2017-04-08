from tree.Node import Node


class Program(Node):
    def __init__(self, parent=None):
        self.variables = []
        super(Program, self).__init__(parent)

    def addVariable(self, variableNode):
        self.variables.append(variableNode)
        variableNode.parent = self

    def addVariableList(self, variableNodeList):
        for node in variableNodeList:
            self.addVariable(node)

    def __str__(self):
        variablesString = ""

        for var in self.variables:
            var.depth = self.depth + 1
            variablesString += "\n"
            variablesString += var.generateTabsForDepth()
            variablesString += str(var)

        functionsString = self.printStatements()

        return "Program: {0} {1}".format(variablesString, functionsString)
