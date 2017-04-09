import inspect
import logging
import sys

from HerocLexer import HerocLexer
from HerocParser import HerocParser
from HerocVisitor import HerocVisitor
from tree.AST import AST
from tree.Identifier import Identifier
from tree.Node import Node
from tree.Number import Number
from tree.operations.AdditiveOperation import AdditiveOperation
from tree.operations.AndOperation import AndOperation
from tree.operations.BitwiseOrOperation import BitwiseOrOperation
from tree.operations.BitwiseXOrOperation import BitwiseXOrOperation
from tree.operations.EqualityOperation import EqualityOperation
from tree.operations.IncrementalOperation import IncrementalOperation
from tree.operations.LogicalAndOperation import LogicalAndOperation
from tree.operations.LogicalNotOperation import LogicalNotOperation
from tree.operations.LogicalOrOperation import LogicalOrOperation
from tree.operations.MultiplicativeOperation import MultiplicativeOperation
from tree.operations.OperationType import OperationType
from tree.operations.PointerOperation import PointerOperation
from tree.operations.RelationalOperation import RelationalOperation
from tree.operations.ShiftOperation import ShiftOperation
from tree.Variable import Variable
from tree.VariableType import VariableType


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
                ast.root.addVariableList(r)
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

        # If have a value
        if ctx.getChildCount() == 3:
            # Expression
            init_value = self.visit(ctx.getChild(2))
        else:
            # Default value to 0
            init_value = Number()

        variable = Variable(identifier=identifier,
                            variable_type=VariableType.VARIABLE)

        variable.addStatementList([init_value])
        return variable

    def visitInitDeclaratorArray(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        identifier = Identifier(str(ctx.getChild(0)))
        array_size = None
        values = []

        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, HerocParser.ExpressionContext):
                array_size = self.visit(child)
            elif isinstance(child, HerocParser.InitializerListContext):
                values = self.visit(child)

        # QUESTION Here I can throw error when len(values) is > than array_size
        if array_size is None:
            if len(values) > 0:
                array_size = Number(len(values))
            else:
                array_size = Number()

        variable = Variable(identifier=identifier,
                            variable_type=VariableType.ARRAY,
                            array_size=array_size)

        variable.addStatementList(values)
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
        if isinstance(ctx.getChild(0), HerocParser.ConditionalExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitConditionalExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.LogicalOrExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitLogicalOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.OR_OR: OperationType.LOGICAL_OR}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=LogicalOrOperation,
                                                  operation_dict=operation_dict)

    def visitLogicalAndExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.AND_AND: OperationType.LOGICAL_AND}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=LogicalAndOperation,
                                                  operation_dict=operation_dict)

    def visitBitwiseOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.OR: OperationType.OR}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BitwiseOrOperation,
                                                  operation_dict=operation_dict)

    def visitBitwiseXOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.CARET: OperationType.XOR}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=BitwiseXOrOperation,
                                                  operation_dict=operation_dict)

    def visitAndExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.AND: OperationType.AND}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=AndOperation,
                                                  operation_dict=operation_dict)

    def visitEqualityExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.EQUAL: OperationType.EQUAL,
                          HerocLexer.NOT_EQUAL: OperationType.NOT_EQUAL}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=EqualityOperation,
                                                  operation_dict=operation_dict)

    def visitRelationalExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.LESS: OperationType.LESS,
                          HerocLexer.LESS_EQUAL: OperationType.LESS_EQUAL,
                          HerocLexer.GREATER: OperationType.GREATER,
                          HerocLexer.GREATER_EQUAL: OperationType.GREATER_EQUAL}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=RelationalOperation,
                                                  operation_dict=operation_dict)

    def visitShiftExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.LEFT_SHIFT: OperationType.LEFT_SHIFT,
                          HerocLexer.RIGHT_SHIFT: OperationType.RIGHT_SHIFT}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=ShiftOperation,
                                                  operation_dict=operation_dict)

    def visitAdditiveExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.PLUS: OperationType.PLUS,
                          HerocLexer.MINUS: OperationType.MINUS}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=AdditiveOperation,
                                                  operation_dict=operation_dict)

    def visitMultiplicativeExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        operation_dict = {HerocLexer.STAR: OperationType.MULTIPLY,
                          HerocLexer.DIV: OperationType.DIVIDE,
                          HerocLexer.MOD: OperationType.MODULO}

        return self.__visitBinaryExpressionHelper(ctx=ctx,
                                                  operation_class=MultiplicativeOperation,
                                                  operation_dict=operation_dict)

    def visitUnaryExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif isinstance(ctx.getChild(0), HerocParser.UnaryOperatorContext):
            operation_type = self.visit(ctx.getChild(0))
            operation = None

            # TODO finish another operations
            if operation_type is OperationType.LOGICAL_NOT:
                operation = LogicalNotOperation(operation=operation_type)
            elif operation_type is OperationType.REFERENCE:
                operation = PointerOperation(operation=operation_type)
            elif operation_type is OperationType.DEREFERENCE:
                operation = PointerOperation(operation=operation_type)
            elif operation_type is OperationType.BITWISE_NOT:
                operation = BitwiseNotOperation(operation=operation_type)
            elif operation_type is OperationType.INCREMENT:
                operation = IncrementalOperation(operation=operation_type)
            elif operation_type is OperationType.DECREMENT:
                operation = IncrementalOperation(operation=operation_type)

            operation.addStatement(self.visit(ctx.getChild(1)))
            return operation

        # TODO - sizeof

    def visitUnaryOperator(self, ctx):
        operation_type = ctx.getChild(0).getSymbol().type

        operations = {HerocLexer.NOT: OperationType.LOGICAL_NOT,
                      HerocLexer.STAR: OperationType.REFERENCE,
                      HerocLexer.AND: OperationType.DEREFERENCE,
                      HerocLexer.TILDE: OperationType.BITWISE_NOT,
                      HerocLexer.PLUS_PLUS: OperationType.INCREMENT,
                      HerocLexer.MINUS_MINUS: OperationType.DECREMENT}

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

            operation = IncrementalOperation(operation=operations.get(operation_type),
                                             postfix=True)

            operation.addStatement(self.visit(ctx.getChild(0)))
            return operation
        # TODO rest of the postfix

    def visitPrimaryExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))
        child = ctx.getChild(0)
        token_type = child.getSymbol().type

        if token_type is HerocLexer.IDENTIFIER:
            return Identifier(name=str(child))
        elif token_type is HerocLexer.CONSTANT:
            # TODO implemet hexa number init
            return Number(value=int(str(child)))
        elif token_type is HerocLexer.STRING:
            # TODO implement String Node
            pass
        else:
            return self.visit(ctx.getChild(1))
