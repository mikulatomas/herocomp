# Generated from Heroc.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HerocParser import HerocParser
else:
    from HerocParser import HerocParser

# This class defines a complete generic visitor for a parse tree produced by HerocParser.

class HerocVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HerocParser#sourcefile.
    def visitSourcefile(self, ctx:HerocParser.SourcefileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#source.
    def visitSource(self, ctx:HerocParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:HerocParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#initVariableDeclarationList.
    def visitInitVariableDeclarationList(self, ctx:HerocParser.InitVariableDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#initDeclaratorVariable.
    def visitInitDeclaratorVariable(self, ctx:HerocParser.InitDeclaratorVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#initDeclaratorVariableSimple.
    def visitInitDeclaratorVariableSimple(self, ctx:HerocParser.InitDeclaratorVariableSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#initDeclaratorArray.
    def visitInitDeclaratorArray(self, ctx:HerocParser.InitDeclaratorArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#initializer.
    def visitInitializer(self, ctx:HerocParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#initializerList.
    def visitInitializerList(self, ctx:HerocParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#pointer.
    def visitPointer(self, ctx:HerocParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#identifierList.
    def visitIdentifierList(self, ctx:HerocParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:HerocParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#unaryOperator.
    def visitUnaryOperator(self, ctx:HerocParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:HerocParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#constantExpression.
    def visitConstantExpression(self, ctx:HerocParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#expression.
    def visitExpression(self, ctx:HerocParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:HerocParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:HerocParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:HerocParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#bitwiseOrExpression.
    def visitBitwiseOrExpression(self, ctx:HerocParser.BitwiseOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#bitwiseXOrExpression.
    def visitBitwiseXOrExpression(self, ctx:HerocParser.BitwiseXOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#andExpression.
    def visitAndExpression(self, ctx:HerocParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#equalityExpression.
    def visitEqualityExpression(self, ctx:HerocParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#relationalExpression.
    def visitRelationalExpression(self, ctx:HerocParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#shiftExpression.
    def visitShiftExpression(self, ctx:HerocParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:HerocParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:HerocParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#unaryExpression.
    def visitUnaryExpression(self, ctx:HerocParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#postfixExpression.
    def visitPostfixExpression(self, ctx:HerocParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:HerocParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#argumentExpression.
    def visitArgumentExpression(self, ctx:HerocParser.ArgumentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:HerocParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#statement.
    def visitStatement(self, ctx:HerocParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#compoundStatement.
    def visitCompoundStatement(self, ctx:HerocParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#blockItemList.
    def visitBlockItemList(self, ctx:HerocParser.BlockItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#blockItem.
    def visitBlockItem(self, ctx:HerocParser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#expressionStatement.
    def visitExpressionStatement(self, ctx:HerocParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#selectionStatement.
    def visitSelectionStatement(self, ctx:HerocParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#iterationStatement.
    def visitIterationStatement(self, ctx:HerocParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HerocParser#jumpStatement.
    def visitJumpStatement(self, ctx:HerocParser.JumpStatementContext):
        return self.visitChildren(ctx)



del HerocParser