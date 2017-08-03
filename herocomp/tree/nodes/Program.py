import tree
from asm.Asm import *
from tools.VariablesTable import VariablesTable
from tree.nodes.Node import Node


class Program(Node):
    def __init__(self, parent=None):
        self.variables = []
        self.variables_table = VariablesTable()
        self.functions_table = []
        super(Program, self).__init__(parent)

    def addVariable(self, variableNode):
        self.variables.append(variableNode)
        variableNode.parent = self

    def addVariableList(self, variableNodeList):
        for node in variableNodeList:
            self.addVariable(node)

    def get_code(self):
        code = ""

        code += global_directive("main")

        if len(self.variables) > 0:
            code += data_directive()

            # Global variables
            for variable in self.variables:
                self.variables_table.add_variable(variable.identifier.name, variable.identifier.name, variable.variable_type)
                code += variable.get_global_code()

        code += text_directive()

        for statement in self.statements:
            if isinstance(statement, tree.nodes.Function.Function):
                self.functions_table.append(statement.identifier.name)
            code += statement.get_code()

        return code

    def __str__(self):
        variablesString = ""

        for var in self.variables:
            var.depth = self.depth + 1
            variablesString += "\n"
            variablesString += var.generateTabsForDepth()
            variablesString += str(var)

        functionsString = self.printStatements()

        return "Program: {0} {1}".format(variablesString, functionsString)
