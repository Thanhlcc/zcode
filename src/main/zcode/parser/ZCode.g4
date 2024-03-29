//2052256
grammar ZCode;
@lexer::header {
from lexererr import *
}
options {
	language=Python3;
}

program: nullable_newlines decllist EOF;

// ------------ NEWLINES ----------------------
newlines: NEWLINE newlinetail | NEWLINE;
nullable_newlines: NEWLINE newlinetail | ;
newlinetail: NEWLINE newlinetail | ;
// ---------- DECLARATION ----------------------
decllist: decl decllist | decl;
decl: funcdecl | vardecl ;

// ------------Variable declaration ----------------
vardecl: (scalar_decl | array_decl) newlines;

primititve_types: STRING | NUMBER | BOOLEAN;
array_decl: primititve_types array_id (ASSIGN expression)?;

scalar_decl: (primititve_types | DYNAMIC) ID (ASSIGN expression)?
            | VAR ID ASSIGN expression;

single_vardecl: primititve_types varid;

array_id: ID LB numlist RB;
numlist: NUMBER_LIT numlisttail | NUMBER_LIT;
numlisttail: COMMA NUMBER_LIT numlisttail | ;

varid: ID | array_id;
array_access: ( ID | funcall_expr ) LB dimensions RB;
dimensions: expression COMMA dimensions | expression;



// ------------Functinon declaration ----------------
funcdecl: FUNC ID LP params RP nullable_newlines body;
// Paramter list is nullable and separated by COMMA
params: single_vardecl params_tail | ;
params_tail: COMMA single_vardecl params_tail | ;

// The third options is for empty func body. In that case, the function declaration must end with at least one newline
body: return_stmt | block_stmt | newlines;

// ------------ STATEMEMNT ---------------------
nullable_stmtlist: stmt nullable_stmtlist | ; 
stmt: 
    if_stmt
    | for_stmt
    | return_stmt
    | block_stmt
    | vardecl
    | asm_stmt
    | break_stmt
    | continue_stmt
    | funcall_expr newlines
    ;

asm_stmt: ( ID | array_access ) ASSIGN expression newlines;

// --------------- IF STATEMENT -------------------
if_stmt: 
    IF condition nullable_newlines stmt
    elif_clauses
    else_clause;

elif_clauses: elif_clause elif_clauses | ;
elif_clause: ELIF condition nullable_newlines stmt;

else_clause: (ELSE nullable_newlines stmt) | ;
condition: LP expression RP;
// ------------- FOR STATEMENT --------------------
for_stmt: FOR ID UNTIL expression BY expression nullable_newlines stmt;
// -------------- OTHER STATEMENTS ----------------
block_stmt: BEGIN newlines nullable_stmtlist END newlines;
return_stmt: RETURN (expression | ) newlines;
break_stmt: BREAK newlines;
continue_stmt: CONTINUE newlines;

funcall_expr: ID LP nullbale_args RP;
nullbale_args: expression args_tail | ;
args_tail: COMMA expression args_tail | ;

// -------------- EXPRESSION -------------------
expression: 
    relational_expr CONCAT relational_expr 
    | relational_expr;
relational_expr: 
    logical_expr (EQ | Double_EQ | NEQ | LT | LTE | GT | GTE) logical_expr 
    | logical_expr;
logical_expr: 
    logical_expr (AND | OR) add_expr 
    | add_expr;
add_expr: 
    add_expr (PLUS| MINUS) multiply_expr 
    | multiply_expr;
multiply_expr: 
    multiply_expr (DIV | MUL | MOD) logical_not 
    | logical_not;
logical_not: NOT logical_not 
    | sign_expr;
sign_expr: MINUS sign_expr 
    | subexpr;
subexpr: LP expression RP | operand;
operand:
    NUMBER_LIT
    | STRING_LIT
    | booleanlit
    | arraylit
    | ID
    | array_access
    | funcall_expr;
expression_list: expression COMMA expression_list | expression;
// -------------- LITERALS TYPES ---------------
arraylit: LB expression_list RB;
booleanlit: TRUE | FALSE;

//--------------- KEYWORDS ---------------------------
TRUE: 'true'; FALSE: 'false';
BOOLEAN: 'bool';
NUMBER: 'number';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY:'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if'; ELSE: 'else'; ELIF: 'elif';
BEGIN: 'begin'; END: 'end';
NOT: 'not'; AND: 'and'; OR: 'or';

// ------------ OPERATORS ----------------
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '='; NEQ: '!=';
ASSIGN: '<-';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '...';
Double_EQ: '==';

// ------------------ SEPARATORS --------------------
LP: '('; RP: ')';
LB: '['; RB: ']'; 

// };
NEWLINE: '\n';
COMMA: ',';
COMMENT: '##' ~[\n]* EOF? -> skip;
// ----------------------- NUMBER LITERAL -----------------------------
fragment Decimal_Part: '.' Digit*;
fragment Exponent_Part: [eE] (PLUS | MINUS)? Digit+;
NUMBER_LIT:  Digit+ Decimal_Part? Exponent_Part? ;
// ---------------------- STRING LITERAL ---------------------------------
fragment Allowed_Character: ~[\r\n\\"] | Escape_Char | [']["]?;

ILLEGAL_ESCAPE: ["] Allowed_Character* '\\'~[bfrnt\\'"] {raise IllegalEscape(self.text[1:])};
UNCLOSE_STRING: ["] Allowed_Character* {raise UncloseString(self.text[1:])};
STRING_LIT: UNCLOSE_STRING '\\'?["] {self.text = self.text[1:-1]};
// ---------------------- ARRAY LITERAL -----------------------------------
ID: (Charset | Underscore) (Underscore | Charset | Digit)*;
WS : [ \t\b\f]+ -> skip; // skip spaces, tabs

fragment Escape_Char: '\\'[bfrnt\\'];
fragment Underscore: '_';
fragment Charset: [a-zA-Z];
fragment Digit: [0-9];

ERROR_CHAR: . {raise ErrorToken(self.text)};