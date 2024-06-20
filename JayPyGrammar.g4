grammar JayPyGrammar;

program: methodDeclaration* 'int' 'main' '(' ')' '{' statement* '}' methodDeclaration* EOF;

memberDeclaration:
methodDeclaration
|
fieldDeclaration
;





methodDeclaration
 //: typeTypeOrVoid identifier formalParameters ('[' ']')*  methodBody
    : typeTypeOrVoid identifier  formalParameters  ('[' ']')*  methodBody
    | VOID identifier formalParameters methodBody
   // | typeTypeOrVoid identifier '(' ')' methodBody
    | typeTypeOrVoid identifier LPAREN RPAREN methodBody
    ;

methodBody
    : block
    | ';'
    ;

typeTypeOrVoid
    : typeType
    | VOID
    ;
typeTypeOrVar
    : typeType
    | VAR
    ;


fieldDeclaration
    : typeType variableDeclarators ';'
    ;
variableDeclarators
    : variableDeclarator (',' variableDeclarator)*
    ;

variableDeclarator
    : variableDeclaratorId ('=' variableInitializer)?
    ;

variableDeclaratorId
    : identifier ('[' ']')*
    ;

variableInitializer
    : arrayInitializer
    | expression
    ;

arrayInitializer
    : '{' (variableInitializer (',' variableInitializer)* ','?)? '}'
    ;
qualifiedNameList
    : qualifiedName (',' qualifiedName)*
    ;

formalParameters
    : LPAREN (
        receiverParameter?
        | receiverParameter (',' formalParameterList)?
        | formalParameterList?
    ) RPAREN
    ;

receiverParameter
    : typeType (identifier '.')*
    ;

formalParameterList
    : formalParameter (',' formalParameter)* (',' lastFormalParameter)?
    | lastFormalParameter
    ;

formalParameter
    : typeType variableDeclaratorId
    ;

lastFormalParameter
    : typeType '...' variableDeclaratorId
    ;


qualifiedName
    : identifier ('.' identifier)*
    ;

literal
   // : integerLiteral
    : floatLiteral
    | CHAR_LITERAL
    | STRING_LITERAL
    | BOOL_LITERAL
    | NULL_LITERAL
    | INT_LITERAL
    ;


//integerLiteral
  //  : INTEGER_LITERAL
   // | DECIMAL_LITERAL
    //;

floatLiteral
    : FLOAT_LITERAL
    ;
elementValuePairs
    : elementValuePair (',' elementValuePair)*
    ;

elementValuePair
    : identifier '=' elementValue
    ;

elementValue
    : expression
    | elementValueArrayInitializer
    ;

elementValueArrayInitializer
    : '{' (elementValue (',' elementValue)*)? ','? '}'
    ;
block
    : '{' blockStatement* '}'
    ;

blockStatement
    : localVariableDeclaration ';'
    | statement
    ;

localVariableDeclaration
   : typeTypeOrVar identifier ('=' expression)?
  // | typeType variableDeclarators ('=' variableInitializer)?
   // : (VAR identifier '=' expression | typeType variableDeclarators '=' expression | typeType variableDeclarators)
    //| 'int' variableDeclarators '=' INTEGER_LITERAL)
   ;


identifier
    : IDENTIFIER
    | VAR
    ;

typeIdentifier
    : IDENTIFIER
    ;

printStatement: PRINT LPAREN expression RPAREN SEMI;

printlnStatement: PRINTLN LPAREN expression RPAREN SEMI;

statement
    : blockLabel = block
    //| ASSERT expression (':' expression)? ';'
    | memberDeclaration
    | IF parExpression statement (ELSE statement)?
    | FOR '(' forControl ')' statement
    | WHILE parExpression statement
    | DO statement WHILE parExpression ';'
    | SWITCH parExpression '{' switchBlockStatementGroup* switchLabel* '}'
    | RETURN expression? ';'
    | BREAK identifier? ';'
    | CONTINUE identifier? ';'
    | statementExpression = expression ';'
    | switchExpression ';'?
    | identifierLabel = identifier ':' statement
    | FOR '(' typeTypeOrVar identifier IN expression ')' statement
    | printStatement
    | printlnStatement
    ;
switchBlockStatementGroup
    : switchLabel+ blockStatement+
    ;

switchLabel
    : CASE (
        constantExpression = expression
        | typeType varName = identifier
    ) ':'
    | DEFAULT ':'
    ;

forControl
    : enhancedForControl
    | forInit? ';' expression? ';' forUpdate = expressionList?
    ;

forInit
    : localVariableDeclaration
   // | expressionList
    ;

enhancedForControl
    : (typeType | VAR) variableDeclaratorId ':' expression
    ;

// EXPRESSIONS

parExpression
    : '(' expression ')'
    ;

expressionList
    : expression (',' expression)*
    ;

methodCall
    : (identifier) arguments
    ;
expression
    : primary
    | expression '[' expression ']'
    | expression bop = '.' (
        identifier
        | methodCall
    )
    | methodCall
    | expression  typeArguments? identifier
    | typeType  (typeArguments? identifier)
    | switchExpression

    | expression postfix = ('++' | '--')

    | prefix = ('+' | '-' | '++' | '--' | '~' | '!') expression

    | literal

    | expression bop = ('**'|'*' | '/' | '%' | 'DOT' ) expression
    | expression bop = ('+' | '-') expression
    | expression ('<' '<' | '>' '>' '>' | '>' '>') expression
    | expression bop = ('<=' | '>=' | '>' | '<') expression
    | expression bop = INSTANCEOF (typeType | pattern)
    | expression bop = ('==' | '!=') expression
    | expression bop = '&' expression
    | expression bop = '^' expression
    | expression bop = '|' expression
    | expression bop = '&&' expression
    | expression bop = '||' expression
    | expression bop = 'OR' expression
    | expression bop = 'AND' expression
    | <assoc = right> expression bop = '?' expression ':' expression
    | <assoc = right> expression bop = (
        '='
        | '+='
        | '-='
        | '*='
        | '/='
        | '&='
        | '|='
        | '^='
        | '>>='
        | '>>>='
        | '<<='
        | '%='
    ) expression


    | lambdaExpression
    ;

lambdaParameters
    : identifier
    | '(' formalParameterList? ')'
    | '(' identifier (',' identifier)* ')'
    | '(' lambdaLVTIList? ')'
    ;
lambdaExpression
    : lambdaParameters '->' lambdaBody
    ;

lambdaBody
    : expression
    | block
    ;

lambdaLVTIList
    : lambdaLVTIParameter (',' lambdaLVTIParameter)*
    ;

lambdaLVTIParameter
    : VAR identifier
    ;

pattern
    : typeType identifier
    ;

primary
    : '(' expression ')'
    | literal
    | identifier
    ;
switchExpression
    : SWITCH parExpression '{' switchLabeledRule* '}'
    ;

switchLabeledRule
    : CASE (expressionList | NULL_LITERAL | guardedPattern) (ARROW | COLON) switchRuleOutcome
    | DEFAULT (ARROW | COLON) switchRuleOutcome
    ;


guardedPattern
    : '(' guardedPattern ')'
    |  typeType identifier ('&&' expression)*
    | guardedPattern '&&' expression
    ;

switchRuleOutcome
    : block
    | blockStatement*
    ;
arrayCreatorRest
    : ('[' ']')+ arrayInitializer
    | ('[' expression ']')+ ('[' ']')*
    ;
primitiveType
    : BOOLEAN
    | INT
    | CHAR
    | BYTE
    | SHORT
    //| INTEGER
    | LONG
    | FLOAT
    | DOUBLE
    | VOID
    | STRING
    ;

typeArguments
    : '<' typeArgument (',' typeArgument)* '>'
    ;
arguments
    : '(' expressionList? ')'
    ;

typeArgument
    : typeType
    ;

///LEXER
BOOLEAN      : 'boolean';
BREAK        : 'break';
BYTE         : 'byte';
CASE         : 'case';
CHAR         : 'char';
CONST        : 'const';
CONTINUE     : 'continue';
DEFAULT      : 'default';
DO           : 'do';
PRINT        : 'print';
PRINTLN      : 'println';
DOUBLE       : 'double';
ELSE         : 'else';
/// nie wiem czy dodajemy enum,aENUM         : 'enum';
FLOAT        : 'float';
FOR          : 'for';
IF           : 'if';
GOTO         : 'goto';
IMPORT       : 'import';
INSTANCEOF   : 'instanceof';
INT          : 'int';
//INTEGER      : 'int';
LONG         : 'long';
RETURN       : 'return';
SHORT        : 'short';
STATIC       : 'static';
SWITCH       : 'switch';
VOID         : 'void';
WHILE        : 'while';
IN           : 'in';
STRING       : 'String';
VAR          : 'var';


INT_LITERAL: Digits;

DECIMAL_LITERAL_FOR_ARRAY: ([1-9] (Digits? | '_'+ Digits)) [lL]?;
DECIMAL_LITERAL : ('0' | [1-9] (Digits? | '_'+ Digits)) [lL]?;
HEX_LITERAL     : '0' [xX] [0-9a-fA-F] ([0-9a-fA-F_]* [0-9a-fA-F])? [lL]?;
BINARY_LITERAL  : '0' [bB] [01] ([01_]* [01])? [lL]?;

FLOAT_LITERAL:
    (Digits '.' Digits? | '.' Digits) ExponentPart? [fFdD]?
    | Digits (ExponentPart [fFdD]? | [fFdD])
;
HEX_FLOAT_LITERAL: '0' [xX] (HexDigits '.'? | HexDigits? '.' HexDigits) [pP] [+-]? Digits [fFdD]?;

BOOL_LITERAL: 'true' | 'false' | 'True' | 'False' | '0' | '1';

CHAR_LITERAL: '\'' (~['\\\r\n] | EscapeSequence) '\'';

STRING_LITERAL: '"' (~["\\\r\n] | EscapeSequence)* '"';



//INTEGER_LITERAL: DecimalDigits;

NULL_LITERAL: 'null';

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMI   : ';';
COMMA  : ',';
DOT    : '.';

ASSIGN   : '=';
GT       : '>';
LT       : '<';
BANG     : '!';
TILDE    : '~';
QUESTION : '?';
COLON    : ':';
EQUAL    : '==';
LE       : '<=';
GE       : '>=';
NOTEQUAL : '!=';
AND      : '&&' | 'AND';
OR       : '||' | 'OR';
INC      : '++';
DEC      : '--';
ADD      : '+';
SUB      : '-';
MUL      : '*';
DIV      : '/';
BITAND   : '&';
BITOR    : '|';
CARET    : '^';
MOD      : '%';

ADD_ASSIGN     : '+=';
SUB_ASSIGN     : '-=';
MUL_ASSIGN     : '*=';
DIV_ASSIGN     : '/=';
AND_ASSIGN     : '&=';
OR_ASSIGN      : '|=';
XOR_ASSIGN     : '^=';
MOD_ASSIGN     : '%=';
LSHIFT_ASSIGN  : '<<=';
RSHIFT_ASSIGN  : '>>=';
URSHIFT_ASSIGN : '>>>=';

ARROW      : '->';

WS           : [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT      : '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT : '//' ~[\r\n]*    -> channel(HIDDEN);

IDENTIFIER: Letter LetterOrDigit*;



fragment ExponentPart: [eE] [+-]? Digits;

fragment EscapeSequence:
    '\\' 'u005c'? [btnfr"'\\]
    | '\\' 'u005c'? ([0-3]? [0-7])? [0-7]
    | '\\' 'u'+ HexDigit HexDigit HexDigit HexDigit
;

fragment HexDigits: HexDigit ((HexDigit | '_')* HexDigit)?;

fragment HexDigit: [0-9a-fA-F];

fragment Digits: [0-9] ([0-9_]* [0-9])?;

fragment DecimalDigits: '0' | NonZeroDigit (Digits)* ;

fragment NonZeroDigit: [1-9];

fragment LetterOrDigit: Letter | [0-9];

fragment Letter:
    [a-zA-Z$_]
    | ~[\u0000-\u007F\uD800-\uDBFF]
    | [\uD800-\uDBFF] [\uDC00-\uDFFF]
;

typeList
    : typeType (',' typeType)*
    ;

typeType
    :  primitiveType ('[' ']')*
    ;
//String : S T R I N G;
