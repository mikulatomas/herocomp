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
from tree.Variable import Variable
from tree.VariableType import VariableType


# from Node import Node


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
            print(init_value)
        else:
            # Default value to 0
            init_value = Number()
            print(init_value)

        return Variable(identifier=identifier,
                        variable_type=VariableType.VARIABLE,
                        values=[init_value])

    # def visitInitDeclaratorVariableSimpleWithValue(self, ctx):
    #     logging.info(str(sys._getframe().f_code.co_name))
    #
    #     identifier = Identifier(str(ctx.getChild(0)))
    #     value = self.visit(ctx.getChild(2))
    #
    #     return Variable(identifier=identifier,
    #                     variable_type=VariableType.VARIABLE,
    #                     values=[value])

    # def visitInitDeclaratorArray(self, ctx):
    #     logging.info(str(sys._getframe().f_code.co_name))
    #
    #     identifier = Identifier(str(ctx.getChild(0)))
    #     array_size = Number(value=0)
    #
    #     if isinstance(ctx.getChild(2), HerocParser.ExpressionContext):
    #         array_size = self.visit(ctx.getChild(2))
    #
    #     return Variable(identifier=identifier,
    #                     variable_type=VariableType.ARRAY,
    #                     array_size=array_size,
    #                     values=[])

    def visitInitDeclaratorArray(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        identifier = Identifier(str(ctx.getChild(0)))
        array_size = Number(value=0)
        values = []

        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)

            if isinstance(child, HerocParser.ExpressionContext):
                array_size = self.visit(child)
            elif isinstance(child, HerocParser.InitializerListContext):
                values = self.visit(child)

        if len(values) > 0:
            array_size = Number(len(values))

        return Variable(identifier=identifier,
                        variable_type=VariableType.ARRAY,
                        array_size=array_size,
                        values=[])

    def visitInitializer(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

    def visitExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.ConditionalExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitConditionalExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.LogicalOrExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitLogicalOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.LogicalAndExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitLogicalAndExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.BitwiseOrExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitBitwiseOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.BitwiseXOrExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitBitwiseXOrExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.AndExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitAndExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.EqualityExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitEqualityExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.RelationalExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitRelationalExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.ShiftExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitShiftExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.AdditiveExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitAdditiveExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.MultiplicativeExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitMultiplicativeExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.UnaryExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitUnaryExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.PostfixExpressionContext):
            return self.visit(ctx.getChild(0))

    def visitPostfixExpression(self, ctx):
        logging.info(str(sys._getframe().f_code.co_name))

        # Go to next layer
        if isinstance(ctx.getChild(0), HerocParser.PrimaryExpressionContext):
            return self.visit(ctx.getChild(0))

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
            # TODO no idea if this is right
            return self.visitChild(1)
