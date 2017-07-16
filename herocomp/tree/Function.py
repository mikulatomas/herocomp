import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.Node import Node


class Function(Node):
    def __init__(self, identifier, parent=None):
        self.identifier = identifier
        self.arguments = []
        self.variables_offset = 0
        super(Function, self).__init__(parent)

    def addArgument(self, argumentNode):
        self.arguments.append(argumentNode)
        argumentNode.parent = self

    def addArgumentsList(self, argumentNodeList):
        for node in argumentNodeList:
            self.addArgument(node)

    def printArguments(self):
        argumentsString = ""

        if self.arguments is not None:
            for argument in self.arguments:
                argument.depth = self.depth + 1
                argumentsString += "\n"
                argumentsString += argument.generateTabsForDepth()
                argumentsString += str(argument)

        return argumentsString

    def get_code(self):
        code = ""

        code += label(self.identifier.name)
        code += push(Registers.RBP)
        code += mov(Registers.RSP, Registers.RBP)

        for statement in self.statements:
            if isinstance(statement, tree.Block.Block):
                block_code, has_return = statement.get_code()
                code += block_code
        # code += pop(Registers.RBP)
        # code += ret()

        return code

    def __str__(self):
        blockString = self.printStatements()
        argumentsString = self.printArguments()
        self.identifier.depth = self.depth + 1

        return "Function: \n{} {} {}".format(self.identifier.generateTabsForDepth() + str(self.identifier),
                                           argumentsString,
                                           blockString)
