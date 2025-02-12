// 2213046

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    self.lastTokenType = self.type
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// LEXER

IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

// Built-in functions
GET_INT: 'getInt';
PUT_INT: 'putInt';
PUT_INT_LN: 'putIntLn';
GET_FLOAT: 'getFloat';
PUT_FLOAT: 'putFloat';
PUT_FLOAT_LN: 'putFloatLn';
GET_BOOL: 'getBool';
PUT_BOOL: 'putBool';
PUT_BOOL_LN: 'putBoolLn';
GET_STRING: 'getString';
PUT_STRING: 'putString';
PUT_STRING_LN: 'putStringLn';
PUT_LN: 'putLn';

// newline
NEWLINE: '\r'?'\n' 
    {
    if hasattr(self, 'lastTokenType') and self.lastTokenType in [
        self.ID, self.INT_LIT, self.HEX_LIT, self.BIN_LIT, self.OCT_LIT, self.FLOAT_LIT, self.BOOLEAN, self.STRING_LIT, 
        self.RPAREN, self.RBRACKET, self.RBRACE, self.STRING, self.INT, self.FLOAT, self.BOOLEAN, self.NIL, self.TRUE, self.FALSE,
        self.RETURN, self.CONTINUE, self.BREAK
    ]:
        self.type = self.SEMICOLON
        self.text = ';'
    else:
        self.skip()
};


// identifier

ID: [a-zA-Z_][a-zA-Z0-9_]*;

// operators

// arithmetic 
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';


// relational
EQ: '==';
NEQ: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';

// logical
AND: '&&';
OR: '||';
NOT: '!';

// assignment
ASSIGN: '=';
SHORT_ASSIGN: ':='; // short assignment
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';

// dot
DOT: '.';

// separator
COMMA: ',';
SEMICOLON: ';';
COLON: ':';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';

// literals

// int
INT_LIT: '0' | [1-9][0-9]*; // decimal
HEX_LIT: '0' [xX] [0-9a-fA-F]+ /* {
    self.text = str(int(self.text, 16))
} */; // hexadecimal
OCT_LIT: '0' [oO] [0-7]+ /* {
    self.text = str(int(self.text, 8))
} */; // octal
BIN_LIT: '0' [bB] [01]+ /* {
    self.text = str(int(self.text, 2))
} */; // binary

// float
fragment Digit: [0-9];
fragment Exponent: [eE] [+-]? Digit+;
FLOAT_LIT: (Digit+ '.' Digit* Exponent?
         | Digit+ '.' Exponent
         | Digit+ '.');
        //{self.text = str(float(self.text))} ;


WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs 

// string
fragment DOUBTED_QUOTE: '"';
STRING_LIT: '"' (~[\n\\"] | '\\' [rnt"\\] | '\'"')* '"' /* {
    self.text = self.text[1:-1]
} */;

// comment
LINE_COMMENT: '//' ~[\r\n]* -> skip;
// allow nested block comments
BLOCK_COMMENT: '/*' (BLOCK_COMMENT|.)*? '*/' -> skip;

// error

ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE 
    :  '"' ( '\\' [ntr"\\] | ~["\\\r\n] )* '\\' ~[ntr"\\]
        {
            raise IllegalEscape(self.text);
        }
    ;
UNCLOSE_STRING: '"' (~[\n\\"] | '\\' [rnt"\\] | '\'"')* (EOF | '\n') {
    if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[0:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[0:-1])
    else:
        raise UncloseString(self.text)
};


// PARSER

program : program_list EOF ;

program_list
    : NEWLINE program_list  // Allow leading newlines
    | decl_or_stmt          // Require at least one decl/stmt
    ;

decl_or_stmt
    : decl                  // Base case: declaration
    | stmt_primary          // Base case: statement
    | decl_or_stmt NEWLINE  // Allow newlines after decl/stmt
    | decl_or_stmt decl     // Add another declaration
    | decl_or_stmt stmt_primary     // Add another statement
    | expr // testing part 1 task 3
    ;
            

decl: (struct_decl 
    | interface_decl
    | const_decl 
    | var_decl 
    | array_decl
    | var_decl_no_init
    | short_decl 
    | func_decl 
    | method_decl) (SEMICOLON | newlines);

/* decl_in_block: (struct_decl 
    | interface_decl
    | const_decl 
    | var_decl 
    | array_decl
    | var_decl_no_init
    | short_decl 
    | func_decl 
    | method_decl) (SEMICOLON | newlines); */


newlines: NEWLINE
		| newlines NEWLINE
		;

eos: SEMICOLON | NEWLINE;

expr: logical_expr ;

logical_expr: logical_expr (AND | OR) equality_expr | equality_expr ;

equality_expr: equality_expr (EQ | NEQ) relational_expr | relational_expr ;

relational_expr: relational_expr (LT | LE | GT | GE) additive_expr | additive_expr ;

additive_expr: additive_expr (ADD | SUB) multiplicative_expr | multiplicative_expr ;

multiplicative_expr: multiplicative_expr (MUL | DIV | MOD) primary_expr | primary_expr ;

primary_expr: signed_tail (field_access | atom_arr_access)  ;

field_access: field_access DOT (ID | function_call | array_access) | atom_arr_access;

atom_arr_access: atom_arr_access LBRACKET index_expr RBRACKET | atom; 

atom: atom_value
    | LPAREN expr RPAREN
    | ID
	| function_call eos?
    | array_literal
    | struct_literal
    | assignment_stmt eos
	| struct_field_access eos?
	| struct_field_access_no_func eos?
    | array_access
    ;

atom_value: number
    | TRUE
    | FALSE
    | NIL
    | STRING_LIT;

atom_list: LPAREN expr_list RPAREN 
            | LBRACE expr_list RBRACE ;
expr_list : expr
            | struct_literal
            | atom_list
            |(expr | struct_literal | atom_list) COMMA expr_list  // Recursive case: expr followed by comma and another expr_list
          ;

literal: array_literal | struct_literal;

int_number: INT_LIT | HEX_LIT | OCT_LIT | BIN_LIT;
number: int_number | FLOAT_LIT;

// array
array_access: secondary_index_expr array_access_tail ;
array_access_tail: 
    LBRACKET index_expr RBRACKET array_access_tail? ;

// Index-specific expressions (no FLOAT_LIT allowed)
index_expr: logical_index_expr ;

logical_index_expr: logical_index_expr (AND | OR) equality_index_expr | equality_index_expr ;

equality_index_expr: equality_index_expr (EQ | NEQ) relational_index_expr | relational_index_expr ;

relational_index_expr: relational_index_expr (LT | LE | GT | GE) additive_index_expr | additive_index_expr ;

additive_index_expr: additive_index_expr (ADD | SUB) multiplicative_index_expr | multiplicative_index_expr;

multiplicative_index_expr: multiplicative_index_expr (MUL | DIV | MOD) primary_index_expr | primary_index_expr  ;

primary_index_expr: // here is what can be before and inside the []
                    secondary_index_expr 
                    // below are for what inside the []
                  | array_access
                  | int_number
                  | signed_tail int_number
                  | LPAREN index_expr RPAREN
                  | array_literal
                  | struct_literal
                  ;


secondary_index_expr: ID // this is for what before the []
                      | STRING_LIT // kinda unsure about this
                      | function_call
                      ;

signed_tail: 
            | signed_tail ADD
            | signed_tail SUB
            | signed_tail NOT
            ;

array_literal: array_literal_tail3 (primitiveType | compositeType) LBRACE array_literal_tail RBRACE ;
array_literal_tail: (expr | atom_list ) (COMMA array_literal_tail )? ;
array_literal_tail3: LBRACKET index_expr RBRACKET array_literal_tail3?; // for multi dimensions

// struct
struct_literal: ID LBRACE struct_literal_tail RBRACE;
struct_literal_tail: ( field_init struct_literal_tail2 )?  ;
struct_literal_tail2: ( COMMA field_init struct_literal_tail2 )? ;

field_init: ID COLON expr ;

struct_field_access
    : struct_field_access DOT (ID | function_call | array_access) | ID | function_call | array_access;

struct_field_access_no_func: struct_field_access_no_func DOT (ID | array_access) | ID | array_access;

stmt_primary: (function_call
    | array_access 
    | struct_field_access 
    | struct_field_access_no_func 
    | if_stmt 
    | for_stmt 
    | assignment_stmt) eos 
    ;

stmt_in_block: decl // removed expr for testing
    | stmt_primary
    | (break_stmt // for testing purpose
    | continue_stmt // for testing purpose
    | return_stmt) eos // for testing purpose
    ;

/* loop_stmt: stmt_in_block
         | break_stmt
         | continue_stmt
         ;

func_stmt: stmt_in_block
         | return_stmt
         ; */

stmt_list: stmt_in_block
		| stmt_list stmt_in_block
        | stmt_list NEWLINE
		;

/* loop_stmt_list:
		| loop_stmt_list loop_stmt
		;

func_stmt_list:
		| func_stmt_list func_stmt
		; */

assignment_stmt: lhs assignment_operator expr;
assignment_operator: ASSIGN
                   | ADD_ASSIGN
                   | SUB_ASSIGN
                   | MUL_ASSIGN
                   | DIV_ASSIGN
                   | MOD_ASSIGN
                   ;

// Assignment expressions (needs special handling)
assignment_expr: lhs (ASSIGN | SHORT_ASSIGN) (expr | struct_literal) ; // redundant

// LHS for assignments (no function calls allowed)
lhs: ID | array_access | struct_field_access_no_func;

if_stmt: IF LPAREN expr RPAREN newlines? block if_stmt_tail ;
if_stmt_tail: ( ELSE IF LPAREN expr RPAREN newlines? block if_stmt_tail )? 
            | ( ELSE newlines? block )?
            ;

for_stmt: FOR for_init SEMICOLON expr SEMICOLON for_update newlines? block
        | FOR ID COMMA ID SHORT_ASSIGN RANGE atom newlines? block
        | FOR expr newlines? block
        ;

for_init: short_decl | var_decl | array_decl | func_decl  ; // equivalent to short_decl
for_update: assignment_stmt | short_decl ;
for_condition: expr ; // redundant

return_stmt: RETURN expr? ;
continue_stmt: CONTINUE ;
break_stmt: BREAK ;

var_decl: VAR ID types? ASSIGN expr ;
var_decl_no_init: VAR ID types;
short_decl: (lhs | (ID dimensions types)) SHORT_ASSIGN expr ;
const_decl: CONST ID ASSIGN expr ;

types: primitiveType | compositeType | compositeType | arrayType;
primitiveType: INT | FLOAT | STRING | BOOLEAN ;
arrayType: array_access_tail types;
compositeType: ID ;

array_decl: VAR ID dimensions (primitiveType | compositeType) (ASSIGN array_init)? ;
dimensions: LBRACKET INT_LIT RBRACKET dimensions? ;
array_init: LBRACE array_init_tail RBRACE | expr ;
array_init_tail: ( (expr | atom_list) (COMMA array_init_tail)? )?  ;

struct_decl: TYPE ID STRUCT LBRACE newlines? field_decl_list RBRACE ;
field_decl_list:  ((field_decl | struct_decl | interface_decl | method_decl) eos | NEWLINE ) field_decl_list?;
field_decl: ID types;

interface_decl: TYPE ID INTERFACE LBRACE newlines? method_in_decl RBRACE ;
method_in_decl: ((ID LPAREN param_decl? RPAREN types? eos) | NEWLINE) method_in_decl?; // inside interface

// for declaring params in interface
param_decl: (ID param_decl_tail types) (COMMA param_decl)? ;
param_decl_tail: (COMMA ID param_decl_tail)? ;

// for declaring params in function and method (outside interface)
//param_decl: ID types (COMMA param_decl)? ;

// declare params like x, y int, z float

function_call: ID LPAREN expr_list? RPAREN | built_in_function_call ;
func_decl: FUNC ID LPAREN param_decl? RPAREN types? block  ;
method_decl: FUNC LPAREN ID compositeType RPAREN ID LPAREN param_decl? RPAREN types? block ;

// block
block: LBRACE NEWLINE? stmt_list RBRACE ;
/* loop_block: LBRACE NEWLINE? stmt_list RBRACE ;
func_block: LBRACE NEWLINE? stmt_list RBRACE ; */

built_in_function_call: GET_INT LPAREN RPAREN                      # GetIntCall
                      | PUT_INT LPAREN expr RPAREN                 # PutIntCall
                      | PUT_INT_LN LPAREN expr RPAREN              # PutIntLnCall
                      | GET_FLOAT LPAREN RPAREN                    # GetFloatCall
                      | PUT_FLOAT LPAREN expr RPAREN               # PutFloatCall
                      | PUT_FLOAT_LN LPAREN expr RPAREN            # PutFloatLnCall
                      | GET_BOOL LPAREN RPAREN                     # GetBoolCall
                      | PUT_BOOL LPAREN expr RPAREN                # PutBoolCall
                      | PUT_BOOL_LN LPAREN expr RPAREN             # PutBoolLnCall
                      | GET_STRING LPAREN RPAREN                   # GetStringCall
                      | PUT_STRING LPAREN expr RPAREN              # PutStringCall
                      | PUT_STRING_LN LPAREN expr RPAREN           # PutStringLnCall
                      | PUT_LN LPAREN RPAREN                       # PutLnCall ;

