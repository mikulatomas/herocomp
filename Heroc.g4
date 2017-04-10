/**
 * Define a grammar called Hello
 */
grammar Heroc;
import Lexer;

options { 
	language=Python3;
}

sourcefile
	:	source? EOF
	;

source
	:	variableDeclaration
	|	functionDefinition
	|	source variableDeclaration
	|	source functionDefinition
	;

variableDeclaration
	:	LONG initVariableDeclarationList SEMI
	;
	

initVariableDeclarationList
	:	initDeclaratorVariable (',' initDeclaratorVariable)*
	;

initDeclaratorVariable
	:	pointer? initDeclaratorVariableSimple
//	|	pointer? initDeclaratorVariableSimpleWithValue
	|	pointer? initDeclaratorArray
//	|	pointer? initDeclaratorArrayWithValue
	;

initDeclaratorVariableSimple
	:	IDENTIFIER
	|	IDENTIFIER '=' expression
	;

//initDeclaratorVariableSimpleWithValue
//	: 	IDENTIFIER '=' expression
//	;
	
initDeclaratorArray
	:	IDENTIFIER ('[' expression? ']')+
	|	IDENTIFIER ('[' expression? ']')+ '=' '{' (initializerList)? '}'
	;

//initDeclaratorArrayWithValue
//	: 	IDENTIFIER ('[' expression? ']')+ '=' '{' (initializerList)? '}'
//	;

initializer
    :   expression
    |   '{' initializerList '}'
    |   '{' initializerList ',' '}'
    ;

initializerList
    :   initializer (',' initializer)*
    ;
   
pointer
    :   '*'+
    ;


identifierList
    :   IDENTIFIER (',' IDENTIFIER)*
    ;

functionDefinition
    :   IDENTIFIER '(' identifierList? ')' compoundStatement
    ;

// ------------------------------------------------------------------
// EXPRESSIONS
// ------------------------------------------------------------------

unaryOperator
    :   '&' | '*' | '~' | '!' | '--' | '++'
    ;
    
assignmentOperator
    :   '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
    ;

// If expression is constant skip assignment operators in priorities table
constantExpression
	:	conditionalExpression
	;

// Start table of operators from bottom (from lowest priority)
//expression
//	:	assignmentExpression
//	|	expression ',' assignmentExpression
//	;

// Continue to conditionalExpressions in table or create assignment
expression
    :   conditionalExpression
    |   unaryExpression assignmentOperator expression
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
    |   unaryOperator unaryExpression
    |   'sizeof' '(' LONG ')'
//    |   '&&' IDENTIFIER // GCC extension address of label - IDK if we need it for HEROC
    //    |   'sizeof' unaryExpression - NOT POSSIBLE IN HEROC
    ;

postfixExpression
    :   primaryExpression
    |   postfixExpression '[' expression ']'
// Probably not required
//    |   postfixExpression '(' argumentExpressionList? ')'
    |   postfixExpression '++'
    |   postfixExpression '--'
//   Assign array to variable
    |   '{' initializerList '}'
    |   '{' initializerList ',' '}'
//    |   postfixExpression '.' IDENTIFIER -- NOT POSSIBLE IN HEROC
//    |   postfixExpression '->' IDENTIFIER -- NOT POSSIBLE IN HEROC
    ;

argumentExpressionList
    :   expression (',' expression)*
//    |   argumentExpressionList ',' assignmentExpression
    ;

primaryExpression
    :   IDENTIFIER
    |   CONSTANT
    |   STRING+
    |   '(' expression ')'
    ;
 
// ------------------------------------------------------------------
// Main block of codes
// ------------------------------------------------------------------    

statement
    :   compoundStatement
    |	functionCallStatement
    |   expressionStatement
    |   selectionStatement
    |   iterationStatement
    |   jumpStatement
    ;

compoundStatement
	:	'{' blockItemList? '}'
	;
	
blockItemList
	:	blockItem+
	;

blockItem
	:	variableDeclaration
	|	statement
	;

functionCallStatement
	:	IDENTIFIER '(' argumentExpressionList? ')' SEMI
	;

expressionStatement
    :   expression? SEMI
    ;

selectionStatement
    :   'if' '(' expression ')' compoundStatement ('else' compoundStatement)?
    ;

iterationStatement
    :   'while' '(' expression ')' statement
    |   'do' statement 'while' '(' expression ')' SEMI
    |   'for' '(' expression? SEMI expression? SEMI expression? ')' statement
    |   'for' '(' variableDeclaration expression? SEMI expression? ')' statement
    ;

jumpStatement
    :   'continue' SEMI
    |   'break' SEMI
    |   'return' expression? SEMI
    ;