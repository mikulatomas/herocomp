lexer grammar HerocLexer;

options {
	language = Python3;
}

/** Klíčová slova */
BREAK   : 'break';
CONTINUE: 'continue';
DO      : 'do';
ELSE    : 'else';
FOR     : 'for';
IF      : 'if';
LONG    : 'long';
RETURN  : 'return';
SIZEOF  : 'sizeof';
WHILE   : 'while';

/** Operátory */
NOT :           '!';
NOT_EQUAL :      '!=';
 
MOD :           '%';
MOD_ASIGN :     '%=';
 
AND :           '&';
AND_AND :        '&&';
AND_ASSIGN :     '&=';
 
STAR :          '*';
STAR_ASSIGN :    '*=';
 
PLUS :          '+';
PLUS_PLUS :      '++';
PLUS_ASSIGN :    '+=';
 
MINUS :         '-';
MINUS_MINUS :    '--';
MINUS_ASSIGN :   '-=';
 
DIV :           '/';
DIV_ASSIGN :     '/=';
 
COLON :         ':';
 
LESS :          '<';
LEFT_SHIFT :     '<<';
LEFT_SHIFT_ASSIGN :   '<<=';
LESS_EQUAL :     '<=';
 
ASSIGN :        '=';
EQUAL :         '==';
 
GREATER :       '>';
GREATER_EQUAL :  '>=';
RIGHT_SHIFT :    '>>';
RIGHT_SHIFT_ASSIGN :  '>>=';
 
QUESTION :      '?';
 
CARET :         '^';
XOR_ASSIGN :     '^=';
 
OR :            '|';
OR_ASSIGN :      '|=';
OR_OR :          '||';
 
TILDE :         '~';

/** Pomocné znaky */
LEFT_PAREN :     '(';
RIGHT_PAREN :    ')';
LEFT_BRACKET :   '[';
RIGHT_BRACKET :  ']';
LEFT_BRACE :     '{';
RIGHT_BRACE :    '}';
SEMI :          ';';
COMMA:          ',';

/** Identifikátory */
IDENTIFIER
//	:	IDENTIFIER_PREFIX (IDENTIFIER_PREFIX | DIGIT)*
	:	IDENTIFIER_NONDIGIT 
		(IDENTIFIER_NONDIGIT | DIGIT)*
	;

fragment
IDENTIFIER_NONDIGIT
	:	[a-zA-Z_]
	;

	
/** Čísla */
CONSTANT:               DIGIT+;
OCTAL_CONSTANT:         '0' OCTAL_DIGIT+ ;
 
HEX_CONSTANT:           HEX_PREFIX HEX_DIGIT+;
fragment HEX_PREFIX:     '0' [xX];
 
fragment DIGIT:         [0-9];
fragment NONZERO_DIGIT:  [1-9];
fragment OCTAL_DIGIT:    [0-7];
fragment HEX_DIGIT:      [0-9a-fA-F];

/** ASCII a string */
CHAR:                   '\'' CHAR_SYMBOL '\'';
STRING:                 '\"' (CHAR_SYMBOL | ESCAPE)* '\"';
fragment ESCAPE:        '\\' CHAR_SYMBOL;
fragment CHAR_SYMBOL:    '\u0000' .. '\u007F';

/** Ignorované whitespacy a komentáře */
WHITESPACE:             [ \t]+ -> skip;
NEWLINE:                '\r'? '\n' -> skip;
COMMENT:           		'/*' .*? '*/' -> skip;