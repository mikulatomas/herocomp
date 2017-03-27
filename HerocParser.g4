/**
 * Define a grammar called Hello
 */
grammar HerocParser;
import HerocLexer;

options { 
	language=Python3;
}

program
	:	declaration*
	;

declaration
	:	declarationVariable
	|	declarationFunction
	;

declarationVariable
	:	LONG IDENTIFIER ';'
	;

declarationFunction
	:	IDENTIFIER '(' functionDeclarationArgsList? ')'
		compoundStatement
	;

// Used only in declarationFunction
functionDeclarationArgsList
	:	IDENTIFIER
	|	IDENTIFIER ',' functionDeclarationArgsList
	;

functionCall
	:	IDENTIFIER '(' expression? ')' ';'
	;

// Mainly for declarationFunction
compoundStatement
	:	'{' blockItemList? '}'
	;
	
blockItemList
	:	blockItem
	|	blockItemList blockItem
	;

blockItem
	:	declarationVariable
	|	functionCall
	;

// ------------------------------------------------------------------
// EXPRESSIONS
// ------------------------------------------------------------------

unaryOperator
    :   '&' | '*' | '+' | '-' | '~' | '!'
    ;
    
assignmentOperator
    :   '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
    ;

// If expression is constant skip assignment operators in priorities table
constantExpression
	:	conditionalExpression
	;

// Start table of operators from bottom (from lowest priority)
expression
	:	assignmentExpression
	|	expression ',' assignmentExpression
	;

// Continue to conditionalExpressions in table or create assignment
assignmentExpression
    :   conditionalExpression
    |   unaryExpression assignmentOperator assignmentExpression
    ;

// Conditional Expression is next in table of priority, we can skip to logical or expression
conditionalExpression
    :   logicalOrExpression ('?' expression ':' conditionalExpression)?
    ;

// Possible skip to AND expression or loop
logicalOrExpression
    :   logicalAndExpression
    |   logicalOrExpression '||' logicalAndExpression
    ;

// Possible skip to Bitwise OR expression or loop
logicalAndExpression
    :   bitwiseOrExpression
    |   logicalAndExpression '&&' bitwiseOrExpression
    ;

bitwiseOrExpression
    :   bitwiseXOrExpression
    |   bitwiseOrExpression '|' bitwiseXOrExpression
    ;

bitwiseXOrExpression
    :   andExpression
    |   bitwiseXOrExpression '^' andExpression
    ;

andExpression
    :   equalityExpression
    |   andExpression '&' equalityExpression
    ;

equalityExpression
    :   relationalExpression
    |   equalityExpression '==' relationalExpression
    |   equalityExpression '!=' relationalExpression
    ;

relationalExpression
    :   shiftExpression
    |   relationalExpression '<' shiftExpression
    |   relationalExpression '>' shiftExpression
    |   relationalExpression '<=' shiftExpression
    |   relationalExpression '>=' shiftExpression
    ;

shiftExpression
    :   additiveExpression
    |   shiftExpression '<<' additiveExpression
    |   shiftExpression '>>' additiveExpression
    ;

additiveExpression
    :   multiplicativeExpression
    |   additiveExpression '+' multiplicativeExpression
    |   additiveExpression '-' multiplicativeExpression
    ;

// Skipping castExpression here becouse of Heroc
multiplicativeExpression
    :   unaryExpression
    |   multiplicativeExpression '*' unaryExpression
    |   multiplicativeExpression '/' unaryExpression
    |   multiplicativeExpression '%' unaryExpression
    ;

unaryExpression
    :   postfixExpression
    |   '++' unaryExpression
    |   '--' unaryExpression
    |   unaryOperator unaryExpression
    |   'sizeof' '(' LONG ')'
    |   '&&' IDENTIFIER // GCC extension address of label - IDK if we need it for HEROC
    //    |   'sizeof' unaryExpression - NOT POSSIBLE IN HEROC
    ;

postfixExpression
    :   primaryExpression
    |   postfixExpression '[' expression ']'
    |   postfixExpression '(' argumentExpressionList? ')'
    |   postfixExpression '++'
    |   postfixExpression '--'
//    NO IDEA WHY I NEED THIS
//    |   '{' initializerList '}'
//    |   '{' initializerList ',' '}'
//    |   postfixExpression '.' IDENTIFIER -- NOT POSSIBLE IN HEROC
//    |   postfixExpression '->' IDENTIFIER -- NOT POSSIBLE IN HEROC
    ;

argumentExpressionList
    :   assignmentExpression
    |   argumentExpressionList ',' assignmentExpression
    ;

primaryExpression
    :   IDENTIFIER
    |   CONSTANT
    |   STRING+
    |   '(' expression ')'
    ;

// ------------------------------------------------------------------
// INITIALIZERS
// ------------------------------------------------------------------

initializer
    :   assignmentExpression
    |   '{' initializerList '}'
    |   '{' initializerList ',' '}'
    ;

initializerList
    :   initializer
    |   initializerList ',' initializer
    ;