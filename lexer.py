import ply.lex as lex
#   Mots clés

reserved_words = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE'
}


#   Liste des tokens

tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUAL',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    'LBRACE', 'RBRACE', 'SEMI'
] + list(reserved_words.values())


#  Expressions régulières

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='

t_LE  = r'<='
t_LT  = r'<'
t_GE  = r'>='
t_GT  = r'>'
t_EQ  = r'=='
t_NE  = r'!='

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI   = r';'


#  Identifiant
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t


#  Nombres
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#  Ignorer espaces
t_ignore = " \t\n"


#  Gestion erreurs

def t_error(t):
    print("Caractère illégal :", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()