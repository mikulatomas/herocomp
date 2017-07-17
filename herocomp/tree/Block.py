import tree
from tools.VariablesTable import VariablesTable
from tree.Function import Function
from tree.JumpStatement import JumpStatement
from tree.JumpStatementType import JumpStatementType
from tree.Node import Node
from tree.Variable import Variable


class Block(Node):
    def __init__(self, parent=None):
        # self.variables = []
        self.variables_table = VariablesTable()
        super(Block, self).__init__(parent)

    # def addVariable(self, variableNode):
    #     self.variables.append(variableNode)
    #     variableNode.parent = self
    #
    # def addVariableList(self, variableNodeList):
    #     for node in variableNodeList:
    #         self.addVariable(node)

    def __str__(self):
        # variablesString = ""

        # for var in self.variables:
        #     var.depth = self.depth + 1
        #     variablesString += "\n"
        #     variablesString += var.generateTabsForDepth()
        #     variablesString += str(var)

        statementsString = self.printStatements()

        # return "Block: {0} {1}".format(variablesString, statementsString)
        return "Block: {0}".format(statementsString)

    def get_variable_offset(self):
        parent = self.parent

        while not isinstance(parent, Function):
            if parent.parent != None:
                parent = parent.parent
            else:
                break

        parent.variables_offset -= 8
        return parent.variables_offset

    def get_code(self):
        code = ""

        for statement in self.statements:
            if isinstance(statement, tree.JumpStatement.JumpStatement):
                if statement.jump_statement_type == JumpStatementType.RETURN:
                    code += statement.get_code()
                    return code, True
            elif isinstance(statement, tree.Variable.Variable):
                statement.variable_offset = self.get_variable_offset()
                self. variables_table.add_variable(statement.identifier.name, statement.variable_offset)
                code += statement.get_code()
            elif isinstance(statement, tree.Block.Block):
                block_code, has_return = statement.get_code()
                code += block_code
                if has_return:
                    return code, True
            else:
                code += statement.get_code()

        return code, False
