# Base class for storing Node informations in AST


class Node():
    def __init__(self, parent=None):
        self.parent = parent
        self.statements = []
        self.depth = 0

    def addStatement(self, statementNode):
        self.statements.append(statementNode)
        statementNode.parent = self

    def addStatementList(self, statementNodeList):
        for node in statementNodeList:
            self.addStatement(node)

    def printStatements(self):
        statementsString = ""

        if self.statements is not None:
            for statement in self.statements:
                statement.depth = self.depth + 1
                statementsString += "\n"
                statementsString += statement.generateTabsForDepth()
                statementsString += str(statement)

        return statementsString

    def generateTabsForDepth(self):
        tabs = ""
        for i in range(self.depth):
            tabs += "   "
        return tabs
