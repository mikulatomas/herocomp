# Base class for storing Node informations in AST
import tree


class Node():
    node_number = 0
    def __init__(self, parent=None):
        self.number = Node.node_number
        Node.node_number += 1
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

    def fill_operation_stack(self):
        stack = []
        stack.append(self)
        return stack

    def find_parent_block(self):
        parent = self.parent
        while parent.parent is not None:
            if isinstance(parent, tree.nodes.Block.Block):
                block = parent
                break
            parent = parent.parent

        return parent

    def find_parent_function(self):
        parent = self.parent
        while parent.parent is not None:
            if isinstance(parent, tree.nodes.Function.Function):
                block = parent
                break
            parent = parent.parent

        return parent
