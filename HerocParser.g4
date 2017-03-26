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
	:	IDENTIFIER '(' expressionList? ')' ';'
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

binaryMathOperations: PLUS | MINUS | STAR | DIV;
unaryMathOperations: PLUS_PLUS | MINUS_MINUS;

// Add pointer later
expression
	:	IDENTIFIER
	|	CONSTANT
	|	OCTAL_CONSTANT
	|	HEX_CONSTANT
	|	CHAR
	|	STRING
	|	expression unaryMathOperations
	|	expression binaryMathOperations expression
	;

expressionList
	:	expression
	|	expression ',' expressionList
	;




