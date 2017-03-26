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
	:	IDENTIFIER '(' functionArgsList? ')'
		compoundStatement
	;

functionArgsList
	:	IDENTIFIER
	|	IDENTIFIER ',' functionArgsList
	;

compoundStatement
	:	'{' blockItemList? '}'
	;
	
blockItemList
	:	blockItem
	|	blockItemList blockItem
	;

blockItem
	:	declarationVariable
	;









//declaration
//	:	LONG initDeclaratorList SEMI
//	;
//
//initDeclaratorList
//	:	initDeclarator
//	|	initDeclaratorList ',' initDeclarator
//	;
//	
//initDeclarator
//	:	declarator
//	|	declarator '=' initializer
//	;
//
//initializer
//    :   assignmentExpression
//    |   '{' initializerList '}'
//    |   '{' initializerList ',' '}'
//    ;
//
//// WTF designation?
//initializerList
//    :   initializer
//    |   initializerList ',' initializer
//    ;
//
//// Pridat pointer 'pointer?'
//declarator
//    :   IDENTIFIER
//    ;
//    
//conditionalExpression
//    :   logicalOrExpression ('?' expression ':' conditionalExpression)?
//    ;





