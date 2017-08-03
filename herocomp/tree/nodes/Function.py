import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.Node import Node


class Function(Node):
    def __init__(self, identifier, parent=None):
        self.identifier = identifier
        self.arguments = []
        self.variables_offset = 0
        self.arguments_table = {}
        self.has_return_statement = False
        self.number_of_local_variables = 0
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

    def get_number_of_local_variables(self, statement, number_of_variables=0):
        for node in statement.statements:
            if isinstance(node, tree.nodes.types.Variable.Variable):
                number_of_variables += 1
            elif isinstance(node, tree.nodes.loops.JumpStatement.JumpStatement):
                if node.jump_statement_type == tree.nodes.loops.JumpStatementType.JumpStatementType.RETURN:
                    return number_of_variables, True
            else:
                number_of_variables, has_return = self.get_number_of_local_variables(node, number_of_variables)
                if has_return:
                    break

        return number_of_variables, False

    def build_arguments_table(self):
        table = {}

        arguments_register_order = [Registers.RDI, Registers.RSI, Registers.RDX, Registers.RCX, Registers.R8, Registers.R9]
        stack_offset = 16

        for i in range(len(self.arguments)):
            if i < 7:
                location = str(arguments_register_order[i])
            else:
                location = str(stack_offset) + Registers.RBP.dereference()
                stack_offset += 8

            table[self.arguments[i].name] = location

        return table


    def get_code(self):
        code = ""

        code += label(self.identifier.name)
        code += instruction("pushq", Registers.RBP)
        code += instruction("movq", Registers.RSP, Registers.RBP)

        self.arguments_table = self.build_arguments_table()

        for statement in self.statements:
            if isinstance(statement, tree.nodes.Block.Block):
                body = statement
                break

        self.number_of_local_variables, has_return = self.get_number_of_local_variables(self)


        for argument in self.arguments:
            self.variables_offset -= 8
            body.variables_table.add_variable(argument.name, self.variables_offset)
            code += instruction("movq", self.arguments_table.get(argument.name), str(self.variables_offset) + Registers.RBP.dereference())
            self.number_of_local_variables += 1

        block_code, has_return = body.get_code()

        code += instruction("subq", number_constant(self.number_of_local_variables * 8), Registers.RSP)

        # for statement in self.statements:
        #     if isinstance(statement, tree.nodes.Block.Block):

        code += block_code
        self.has_return_statement = has_return

        if not has_return:
            code += instruction("leave")
            code += instruction("ret")
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
