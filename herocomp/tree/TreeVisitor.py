import inspect
import logging
import sys

import antlr4
from HerocLexer import HerocLexer
from HerocParser import HerocParser
from HerocVisitor import HerocVisitor
from tree.AST import AST
from tree.nodes.Assignment import Assignment
from tree.nodes.AssignmentType import AssignmentType
from tree.nodes.Block import Block
from tree.nodes.ConditionalStatement import ConditionalStatement
from tree.nodes.Function import Function
from tree.nodes.FunctionCall import FunctionCall
from tree.nodes.IfStatement import IfStatement
from tree.nodes.loops.DoWhileLoop import DoWhileLoop
from tree.nodes.loops.ForLoop import ForLoop
from tree.nodes.loops.JumpStatement import JumpStatement
from tree.nodes.loops.JumpStatementType import JumpStatementType
from tree.nodes.loops.WhileLoop import WhileLoop
from tree.nodes.Node import Node
from tree.nodes.operations.BinaryOperation import BinaryOperation
# from tree.nodes.operations.AdditiveOperation import AdditiveOperation
# from tree.nodes.operations.AndOperation import AndOperation
# from tree.nodes.operations.BitwiseNotOperation import BitwiseNotOperation
# from tree.nodes.operations.BitwiseOrOperation import BitwiseOrOperation
# from tree.nodes.operations.BitwiseXOrOperation import BitwiseXOrOperation
# from tree.nodes.operations.EqualityOperation import EqualityOperation
# from tree.nodes.operations.IncrementalOperation import IncrementalOperation
# from tree.nodes.operations.LogicalAndOperation import LogicalAndOperation
# from tree.nodes.operations.LogicalNotOperation import LogicalNotOperation
# from tree.nodes.operations.LogicalOrOperation import LogicalOrOperation
# from tree.nodes.operations.MultiplicativeOperation import MultiplicativeOperation
from tree.nodes.operations.OperationType import OperationType
from tree.nodes.operations.UnaryOperation import UnaryOperation
from tree.nodes.types.Array import Array
from tree.nodes.types.Identifier import Identifier
from tree.nodes.types.Number import Number
# from tree.nodes.operations.PointerOperation import PointerOperation
# from tree.nodes.operations.RelationalOperation import RelationalOperation
# from tree.nodes.operations.ShiftOperation import ShiftOperation
# from tree.nodes.operations.SubscriptOperation import SubscriptOperation
# from tree.nodes.operations.UnaryAdditiveOperation import UnaryAdditiveOperation
from tree.nodes.types.String import String
from tree.nodes.types.Variable import Variable
from tree.nodes.types.VariableType import VariableType


class TreeVisitor(HerocVisitor):
    def visitSourcefile(self, ctx):
        ast = AST()

        logging.info(str(sys._getframe().f_code.co_name))

        # 0 - Source, 1 - EOF Token
        child = ctx.getChild(0)
        results = self.visit(child)
        logging.info("All results: {}".format(results))

        for r in results:
            # Variables are recieved in list
            if isinstance(r, list):
                logging.info("Adding variables")
                # ast.root.addVariableList(r)
                for variable in r:
                    ast.root.addStatement(variable)
            else:
                logging.info("Adding statement")
                ast.root.addStatement(r)

        # In case of empty source file
        return ast

    def visitSource(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        results = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, HerocParser.SourceContext):
                source = self.visit(child)
                # Flattening
                for r in source:
                    results.append(r)
            else:
                results.append(self.visit(child))

        return results

    def visitVariableDeclaration(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Skip "long"
        return self.visit(ctx.getChild(1))

    def visitInitVariableDeclarationList(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        variables = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, HerocParser.InitDeclaratorVariableContext):
                variables.append(self.visit(child))

        logging.info("Returning variables, count: {0}".format(len(variables)))
        return variables

    def visitInitDeclaratorVariable(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        if isinstance(ctx.getChild(0), HerocParser.PointerContext):
            pointer = True
            variable = self.visit(ctx.getChild(1))
        else:
            pointer = None
            variable = self.visit(ctx.getChild(0))

        if pointer is not None:
            variable.variable_type = VariableType.POINTER

        return variable

    def visitInitDeclaratorVariableSimple(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        identifier = Identifier(str(ctx.getChild(0)))

        variable = Variable(identifier=identifier,
                            variable_type=VariableType.VARIABLE)

        # If have a value
        if ctx.getChildCount() == 3:
            # Expression
            assignment = Assignment(AssignmentType.ASSIGN)
            init_value = self.visit(ctx.getChild(2))
            assignment.addStatement(identifier)
            assignment.addStatement(init_value)
            variable.addStatement(assignment)
        # else:
        #     # Default value to 0
        #     init_value = Number()
        #     variable.addStatement(init_)

        return variable

    def visitInitDeclaratorArray(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        identifier = Identifier(str(ctx.getChild(0)))
        array_size = None
        array_values = []
        array = Array()

        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, HerocParser.ExpressionContext):
                array_size = self.visit(child)
            elif isinstance(child, HerocParser.InitializerListContext):
                array_values = self.visit(child)

        # QUESTION Here I can throw error when len(values) is > than array_size
        if array_size is None:
            if len(array_values) > 0:
                array_size = Number(len(array_values))
            else:
                array_size = Number(0)

        array.setArraySize(array_size)
        if array_size.value > 0 and len(array_values) == 0:
            for i in range(array_size.value):
                array_values.append(Number(0))

        array.addStatementList(array_values)
        assignment = Assignment(AssignmentType.ASSIGN)
        assignment.addStatement(identifier)
        assignment.addStatement(array)


        variable = Variable(identifier=identifier,
                            variable_type=VariableType.ARRAY)

        variable.addStatement(assignment)
        return variable

    def visitInitializerList(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        values = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, HerocParser.InitializerContext):
                values.append(self.visit(child))

        return values

    def visitInitializer(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        if isinstance(ctx.getChild(0), HerocParser.ExpressionContext):
            return self.visit(ctx.getChild(0))
        else:
            # Skip { bracket and visit initializerList
            return self.visit(ctx.getChild(1))

    def __visitBinaryExpressionHelper(self, ctx, operation_class, operation_dict):
        # Go to next layer
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            operation_type = ctx.getChild(1).getSymbol().type

            operation = operation_dict.get(operation_type)

            operation_node = operation_class(operation=operation)

            first_operand = self.visit(ctx.getChild(0))
            second_operand = self.visit(ctx.getChild(2))

            operation_node.addStatement(first_operand)
            operation_node.addStatement(second_operand)

            return operation_node

    def visitExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to ConditionalExpression
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            # Assign
            left_side = self.visit(ctx.getChild(0))
            assignment_operator = self.visit(ctx.getChild(1))
            right_side = self.visit(ctx.getChild(2))

            assignment = Assignment(operation=assignment_operator)
            assignment.addStatement(left_side)
            assignment.addStatement(right_side)

            return assignment

    def visitAssignmentOperator(self, ctx):
        operation_type = ctx.getChild(0).getSymbol().type

        operations = {HerocLexer.ASSIGN: AssignmentType.ASSIGN,
                      HerocLexer.STAR_ASSIGN: AssignmentType.MULTIPLY_ASSIGN,
                      HerocLexer.DIV_ASSIGN: AssignmentType.DIV_ASSIGN,
                      HerocLexer.MOD_ASSIGN: AssignmentType.MOD_ASSIGN,
                      HerocLexer.PLUS_ASSIGN: AssignmentType.PLUS_ASSIGN,
                      HerocLexer.MINUS_ASSIGN: AssignmentType.MINUS_ASSIGN,
                      HerocLexer.LEFT_SHIFT_ASSIGN: AssignmentType.LEFT_SHIFT_ASSIGN,
                      HerocLexer.RIGHT_SHIFT_ASSIGN: AssignmentType.RIGHT_SHIFT_ASSIGN,
                      HerocLexer.AND_ASSIGN: AssignmentType.AND_ASSIGN,
                      HerocLexer.XOR_ASSIGN: AssignmentType.XOR_ASSIGN,
                      HerocLexer.OR_ASSIGN: AssignmentType.OR_ASSIGN}

        return operations.get(operation_type)

    def visitConditionalExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            conditional_statement = ConditionalStatement()

            conditional_statement.addStatement(self.visit(ctx.getChild(0)))
            conditional_statement.addStatement(self.visit(ctx.getChild(2)))
            conditional_statement.addStatement(self.visit(ctx.getChild(4)))

            return conditional_statement

    def visitLogicalOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.OR_OR: OperationType.LOGICAL_OR}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitLogicalAndExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.AND_AND: OperationType.LOGICAL_AND}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitBitwiseOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.OR: OperationType.OR}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitBitwiseXOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.CARET: OperationType.XOR}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitAndExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.AND: OperationType.AND}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitEqualityExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.EQUAL: OperationType.EQUAL,
                          HerocLexer.NOT_EQUAL: OperationType.NOT_EQUAL}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitRelationalExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.LESS: OperationType.LESS,
                          HerocLexer.LESS_EQUAL: OperationType.LESS_EQUAL,
                          HerocLexer.GREATER: OperationType.GREATER,
                          HerocLexer.GREATER_EQUAL: OperationType.GREATER_EQUAL}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitShiftExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.LEFT_SHIFT: OperationType.LEFT_SHIFT,
                          HerocLexer.RIGHT_SHIFT: OperationType.RIGHT_SHIFT}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitAdditiveExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.PLUS: OperationType.PLUS,
                          HerocLexer.MINUS: OperationType.MINUS}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitMultiplicativeExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.STAR: OperationType.MULTIPLY,
                          HerocLexer.DIV: OperationType.DIVIDE,
                          HerocLexer.MOD: OperationType.MODULO}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BinaryOperation,
                                                  operation_dict=operation_dict)

    def visitUnaryExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif isinstance(ctx.getChild(0), HerocParser.UnaryOperatorContext):
            operation_type = self.visit(ctx.getChild(0))
            operation = UnaryOperation(operation=operation_type)

            # if operation_type is OperationType.LOGICAL_NOT:
            #     operation = LogicalNotOperation(operation=operation_type)
            # elif operation_type is OperationType.REFERENCE:
            #     operation = PointerOperation(operation=operation_type)
            # elif operation_type is OperationType.DEREFERENCE:
            #     operation = PointerOperation(operation=operation_type)
            # elif operation_type is OperationType.BITWISE_NOT:
            #     operation = BitwiseNotOperation(operation=operation_type)
            # elif operation_type is OperationType.INCREMENT:
            #     operation = IncrementalOperation(operation=operation_type)
            # elif operation_type is OperationType.DECREMENT:
            #     operation = IncrementalOperation(operation=operation_type)
            # elif operation_type is OperationType.PLUS:
            #     operation = UnaryAdditiveOperation(operation=operation_type)
            # elif operation_type is OperationType.MINUS:
            #     operation = UnaryAdditiveOperation(operation=operation_type)

            operation.addStatement(self.visit(ctx.getChild(1)))
            return operation
        else:
            # sizeof return constant value - 8
            return Number(8)

    def visitUnaryOperator(self, ctx):
        operation_type = ctx.getChild(0).getSymbol().type

        operations = {HerocLexer.NOT: OperationType.LOGICAL_NOT,
                      HerocLexer.AND: OperationType.REFERENCE,
                      HerocLexer.STAR: OperationType.DEREFERENCE,
                      HerocLexer.TILDE: OperationType.BITWISE_NOT,
                      HerocLexer.PLUS_PLUS: OperationType.INCREMENT,
                      HerocLexer.MINUS_MINUS: OperationType.DECREMENT,
                      HerocLexer.MINUS: OperationType.MINUS,
                      HerocLexer.PLUS: OperationType.PLUS}

        return operations.get(operation_type)

    def visitPostfixExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.getChildCount() == 2:
            # Postfix operation
            operation_type = ctx.getChild(1).getSymbol().type
            operations = {HerocLexer.PLUS_PLUS: OperationType.INCREMENT,
                          HerocLexer.MINUS_MINUS: OperationType.DECREMENT}

            operation = UnaryOperation(operation=operations.get(operation_type),
                                             postfix=True)

            operation.addStatement(self.visit(ctx.getChild(0)))
            return operation
        elif isinstance(ctx.getChild(2), HerocParser.ExpressionContext):
            # Subscript postfix operation
            operation = UnaryOperation(operation=OperationType.SUBSCRIPT)
            operation.addStatement(self.visit(ctx.getChild(0)))

            operation.addStatement(self.visit(ctx.getChild(2)))
            return operation
        elif isinstance(ctx.getChild(1), HerocParser.InitializerListContext):
            array = Array()
            array_values = self.visit(ctx.getChild(1))

            if len(array_values) > 0:
                array_size = Number(len(array_values))
            else:
                array_size = Number(0)

            array.setArraySize(array_size)

            if array_size.value > 0 and len(array_values) == 0:
                for i in range(array_size.value):
                    array_values.append(Number(0))

            array.addStatementList(array_values)

            return array
        elif ctx.getChildCount() >= 3 and not isinstance(ctx.getChild(2), HerocParser.ExpressionContext):
            # Function call
            child = ctx.getChild(0)

            if isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):
                identifier = Identifier(str(ctx.getChild(0)))
            else:
                identifier = self.visit(child)

            arguments = []

            for i in range(1, ctx.getChildCount()):
                child = ctx.getChild(i)

                if isinstance(child, HerocParser.ArgumentExpressionListContext):

                    arguments = self.visit(child)

            function_call = FunctionCall(identifier=identifier)
            function_call.addStatementList(arguments)
            return function_call

    def visitPrimaryExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))
        child = ctx.getChild(0)
        token_type = child.getSymbol().type

        if token_type is HerocLexer.IDENTIFIER:
            return Identifier(name=str(child))
        elif token_type is HerocLexer.CONSTANT:
            number = str(child)

            # Case of char
            if '\'' in number:
                return Number(ord(number[1]))

            if number[0] is '0' and len(number) > 1:
                if 'x' in number.lower():
                    return Number(int(number, 16))
                else:
                    return Number(int(number, 8))
            else:
                return Number(value=int(number))

        elif token_type is HerocLexer.STRING:
            return String(value=str(child))
        else:
            return self.visit(ctx.getChild(1))

    def visitCompoundStatement(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        block = Block()

        if isinstance(ctx.getChild(1), HerocParser.BlockItemListContext):
            items = self.visit(ctx.getChild(1))

            for item in items:
                # In case of variable
                if isinstance(item, list):
                    # block.addVariableList(item)
                    for variable in item:
                        block.addStatement(variable)
                else:
                    block.addStatement(item)

        return block

    def visitBlockItemList(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        items = []

        for i in range(ctx.getChildCount()):
            items.append(self.visit(ctx.getChild(i)))

        return items

    def visitBlockItem(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        return self.visit(ctx.getChild(0))

    def visitFunctionDefinition(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        identifier = Identifier(str(ctx.getChild(0)))
        arguments = []

        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, HerocParser.IdentifierListContext):
                arguments = self.visit(child)
            elif isinstance(child, HerocParser.CompoundStatementContext):
                block = self.visit(child)

        function = Function(identifier=identifier)
        function.addArgumentsList(arguments)
        function.addStatement(block)

        return function

    def visitIdentifierList(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        identifiers = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            token_type = child.getSymbol().type

            if token_type is HerocLexer.IDENTIFIER:
                identifiers.append(Identifier(name=str(child)))

        return identifiers

    # def visitFunctionCallStatement(self, ctx):
    #     logging.info(str(sys._getframe().f_code.co_name))
    #
    #     identifier = Identifier(str(ctx.getChild(0)))
    #     arguments = []
    #
    #     for i in range(1, ctx.getChildCount()):
    #         child = ctx.getChild(i)
    #
    #         if isinstance(child, HerocParser.ArgumentExpressionListContext):
    #             arguments = self.visit(child)
    #
    #     function_call = FunctionCall(identifier=identifier)
    #     function_call.addStatementList(arguments)
    #
    #     return function_call

    def visitArgumentExpressionList(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        arguments = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, HerocParser.ArgumentExpressionContext):
                arguments.append(self.visit(child))

        return arguments

    def visitArgumentExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        return self.visit(ctx.getChild(0))

    def visitStatement(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        child = ctx.getChild(0)
        return self.visit(child)

    def visitExpressionStatement(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        return self.visit(ctx.getChild(0))

    def visitIterationStatement(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        loop_type = str(ctx.getChild(0))
        loop = None

        if loop_type == 'for':
            inicialization = None
            condition = None
            incrementation = None
            body = None

            for i in range(1, ctx.getChildCount()):
                if not isinstance(ctx.getChild(i), antlr4.tree.Tree.TerminalNodeImpl):
                    previous_char = ctx.getChild(i-1).getText()
                    try:
                        next_char = ctx.getChild(i+1).getText()
                    except Exception as e:
                        next_char = None


                    if previous_char == "(":
                        inicialization = self.visit(ctx.getChild(i))
                    elif previous_char == ";" and next_char == ";":
                        condition = self.visit(ctx.getChild(i))
                    elif previous_char == ";" and next_char == ")":
                        incrementation = self.visit(ctx.getChild(i))
                    else:
                        body = self.visit(ctx.getChild(i))



            loop = ForLoop(inicialization, condition, incrementation)

            if body is not None:
                loop.addStatement(body)

            return loop
        elif loop_type == 'while':
            loop = WhileLoop()
        elif loop_type == 'do':
            loop = DoWhileLoop()

        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
            if not isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):

                loop.addStatement(self.visit(child))

        return loop

    def visitSelectionStatement(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        if_statement = IfStatement()

        for i in range(2, ctx.getChildCount()):
            child = ctx.getChild(i)

            if not isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):
                if_statement.addStatement(self.visit(child))

        return if_statement

    def visitJumpStatement(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        jump_statement = JumpStatement()

        jump_statement_type = ctx.getChild(0).getSymbol().type

        jump_statement_types = {HerocLexer.RETURN: JumpStatementType.RETURN,
                               HerocLexer.CONTINUE: JumpStatementType.CONTINUE,
                               HerocLexer.BREAK: JumpStatementType.BREAK}

        jump_statement.jump_statement_type = jump_statement_types.get(jump_statement_type)

        if ctx.getChildCount() > 2:
            jump_statement.addStatement(self.visit(ctx.getChild(1)))

        return jump_statement
