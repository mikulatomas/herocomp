# Generated from Heroc.g4 by ANTLR 4.6
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .HerocParser import HerocParser
else:
    from HerocParser import HerocParser

# This class defines a complete listener for a parse tree produced by HerocParser.
class HerocListener(ParseTreeListener):

    # Enter a parse tree produced by HerocParser#program.
    def enterProgram(self, ctx:HerocParser.ProgramContext):
        print("enterProgram")

    # Exit a parse tree produced by HerocParser#program.
    def exitProgram(self, ctx:HerocParser.ProgramContext):
        pass


    # Enter a parse tree produced by HerocParser#source.
    def enterSource(self, ctx:HerocParser.SourceContext):
        pass

    # Exit a parse tree produced by HerocParser#source.
    def exitSource(self, ctx:HerocParser.SourceContext):
        pass


    # Enter a parse tree produced by HerocParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:HerocParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by HerocParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:HerocParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by HerocParser#initVariableDeclarationList.
    def enterInitVariableDeclarationList(self, ctx:HerocParser.InitVariableDeclarationListContext):
        pass

    # Exit a parse tree produced by HerocParser#initVariableDeclarationList.
    def exitInitVariableDeclarationList(self, ctx:HerocParser.InitVariableDeclarationListContext):
        pass


    # Enter a parse tree produced by HerocParser#initDeclaratorVariable.
    def enterInitDeclaratorVariable(self, ctx:HerocParser.InitDeclaratorVariableContext):
        pass

    # Exit a parse tree produced by HerocParser#initDeclaratorVariable.
    def exitInitDeclaratorVariable(self, ctx:HerocParser.InitDeclaratorVariableContext):
        pass


    # Enter a parse tree produced by HerocParser#initializer.
    def enterInitializer(self, ctx:HerocParser.InitializerContext):
        pass

    # Exit a parse tree produced by HerocParser#initializer.
    def exitInitializer(self, ctx:HerocParser.InitializerContext):
        pass


    # Enter a parse tree produced by HerocParser#initializerList.
    def enterInitializerList(self, ctx:HerocParser.InitializerListContext):
        pass

    # Exit a parse tree produced by HerocParser#initializerList.
    def exitInitializerList(self, ctx:HerocParser.InitializerListContext):
        pass


    # Enter a parse tree produced by HerocParser#declarator.
    def enterDeclarator(self, ctx:HerocParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by HerocParser#declarator.
    def exitDeclarator(self, ctx:HerocParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by HerocParser#pointer.
    def enterPointer(self, ctx:HerocParser.PointerContext):
        pass

    # Exit a parse tree produced by HerocParser#pointer.
    def exitPointer(self, ctx:HerocParser.PointerContext):
        pass


    # Enter a parse tree produced by HerocParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:HerocParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by HerocParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:HerocParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by HerocParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:HerocParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by HerocParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:HerocParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by HerocParser#parameterList.
    def enterParameterList(self, ctx:HerocParser.ParameterListContext):
        pass

    # Exit a parse tree produced by HerocParser#parameterList.
    def exitParameterList(self, ctx:HerocParser.ParameterListContext):
        pass


    # Enter a parse tree produced by HerocParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:HerocParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by HerocParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:HerocParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by HerocParser#identifierList.
    def enterIdentifierList(self, ctx:HerocParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by HerocParser#identifierList.
    def exitIdentifierList(self, ctx:HerocParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by HerocParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:HerocParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by HerocParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:HerocParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by HerocParser#declarationList.
    def enterDeclarationList(self, ctx:HerocParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by HerocParser#declarationList.
    def exitDeclarationList(self, ctx:HerocParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by HerocParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:HerocParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by HerocParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:HerocParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by HerocParser#initDeclarator.
    def enterInitDeclarator(self, ctx:HerocParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by HerocParser#initDeclarator.
    def exitInitDeclarator(self, ctx:HerocParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by HerocParser#unaryOperator.
    def enterUnaryOperator(self, ctx:HerocParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by HerocParser#unaryOperator.
    def exitUnaryOperator(self, ctx:HerocParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by HerocParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:HerocParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by HerocParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:HerocParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by HerocParser#constantExpression.
    def enterConstantExpression(self, ctx:HerocParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#constantExpression.
    def exitConstantExpression(self, ctx:HerocParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#expression.
    def enterExpression(self, ctx:HerocParser.ExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#expression.
    def exitExpression(self, ctx:HerocParser.ExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:HerocParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:HerocParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:HerocParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:HerocParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:HerocParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:HerocParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:HerocParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:HerocParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#bitwiseOrExpression.
    def enterBitwiseOrExpression(self, ctx:HerocParser.BitwiseOrExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#bitwiseOrExpression.
    def exitBitwiseOrExpression(self, ctx:HerocParser.BitwiseOrExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#bitwiseXOrExpression.
    def enterBitwiseXOrExpression(self, ctx:HerocParser.BitwiseXOrExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#bitwiseXOrExpression.
    def exitBitwiseXOrExpression(self, ctx:HerocParser.BitwiseXOrExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#andExpression.
    def enterAndExpression(self, ctx:HerocParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#andExpression.
    def exitAndExpression(self, ctx:HerocParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#equalityExpression.
    def enterEqualityExpression(self, ctx:HerocParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#equalityExpression.
    def exitEqualityExpression(self, ctx:HerocParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#relationalExpression.
    def enterRelationalExpression(self, ctx:HerocParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#relationalExpression.
    def exitRelationalExpression(self, ctx:HerocParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#shiftExpression.
    def enterShiftExpression(self, ctx:HerocParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#shiftExpression.
    def exitShiftExpression(self, ctx:HerocParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:HerocParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:HerocParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:HerocParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:HerocParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#unaryExpression.
    def enterUnaryExpression(self, ctx:HerocParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#unaryExpression.
    def exitUnaryExpression(self, ctx:HerocParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#postfixExpression.
    def enterPostfixExpression(self, ctx:HerocParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#postfixExpression.
    def exitPostfixExpression(self, ctx:HerocParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:HerocParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by HerocParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:HerocParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by HerocParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:HerocParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by HerocParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:HerocParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by HerocParser#statement.
    def enterStatement(self, ctx:HerocParser.StatementContext):
        pass

    # Exit a parse tree produced by HerocParser#statement.
    def exitStatement(self, ctx:HerocParser.StatementContext):
        pass


    # Enter a parse tree produced by HerocParser#compoundStatement.
    def enterCompoundStatement(self, ctx:HerocParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by HerocParser#compoundStatement.
    def exitCompoundStatement(self, ctx:HerocParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by HerocParser#blockItemList.
    def enterBlockItemList(self, ctx:HerocParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by HerocParser#blockItemList.
    def exitBlockItemList(self, ctx:HerocParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by HerocParser#blockItem.
    def enterBlockItem(self, ctx:HerocParser.BlockItemContext):
        pass

    # Exit a parse tree produced by HerocParser#blockItem.
    def exitBlockItem(self, ctx:HerocParser.BlockItemContext):
        pass


    # Enter a parse tree produced by HerocParser#expressionStatement.
    def enterExpressionStatement(self, ctx:HerocParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by HerocParser#expressionStatement.
    def exitExpressionStatement(self, ctx:HerocParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by HerocParser#selectionStatement.
    def enterSelectionStatement(self, ctx:HerocParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by HerocParser#selectionStatement.
    def exitSelectionStatement(self, ctx:HerocParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by HerocParser#iterationStatement.
    def enterIterationStatement(self, ctx:HerocParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by HerocParser#iterationStatement.
    def exitIterationStatement(self, ctx:HerocParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by HerocParser#jumpStatement.
    def enterJumpStatement(self, ctx:HerocParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by HerocParser#jumpStatement.
    def exitJumpStatement(self, ctx:HerocParser.JumpStatementContext):
        pass
