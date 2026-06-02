import ply.yacc as yacc
from lexer import tokens

#  PROGRAMME

def p_program(p):
    "program : BEGIN block END"
    print("Programme correct !")


#  BLOCK
def p_block_single(p):
    "block : statement"
    pass

def p_block_multi(p):
    "block : statement SEMI block"
    pass

#  STATEMENT

def p_statement_affect(p):
    "statement : affectation"
    pass

def p_statement_structure(p):
    "statement : structure"
    pass


#  AFFECTATION
def p_affectation(p):
    "affectation : ID EQUAL expression"
    pass

#  STRUCTURES (WHILE, IF)

def p_structure_while(p):
    "structure : WHILE condition LBRACE block RBRACE"
    pass

def p_structure_if_else(p):
    "structure : IF condition THEN LBRACE block RBRACE ELSE LBRACE block RBRACE"
    pass

def p_structure_if(p):
    "structure : IF condition THEN LBRACE block RBRACE"
    pass


#  EXPRESSIONS

def p_expression_number(p):
    "expression : NUMBER"
    pass

def p_expression_id(p):
    "expression : ID"
    pass

def p_expression_add(p):
    "expression : expression PLUS expression"
    pass

def p_expression_minus(p):
    "expression : expression MINUS expression"
    pass

def p_expression_times(p):
    "expression : expression TIMES expression"
    pass

def p_expression_div(p):
    "expression : expression DIVIDE expression"
    pass


#  CONDITIONS

def p_condition(p):
    """condition : expression LT expression
                 | expression LE expression
                 | expression EQ expression
                 | expression GE expression
                 | expression GT expression
                 | expression NE expression"""
    pass


#  ERREURS

def p_error(p):
    print("Erreur syntaxique :", p)

parser = yacc.yacc()


#  LOOP INPUT
while True:
    try:
        data = input(">>> ")
    except EOFError:
        break
    if not data:
        continue
    parser.parse(data)