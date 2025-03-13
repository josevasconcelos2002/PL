import ply.lex as lex 
import re
import sys


literals = ['{', '}' , ',', '=', '"']

# Lista de tokens
tokens = (
   'AUTHOR',
   'EDITOR',
   'TITLE',
   'URL',
   'TYPE',
   'INSTITUTION',
   'YEAR',
   'KEYWORD',
   'TECHREPORT',
   'ATEXT',
   'BTEXT',
   'NUMBER',
   'ID'
)


def t_AUTHOR(t):
    r'author'
    return t


def t_PLUS(t):
    r'editor'
    return t

def t_TITLE(t):
    r'title'
    return t

def t_URL(t):
    r'url'
    return t

def t_TYPE(t):
    r'type'
    return t

def t_INSTITUTION(t):
    r'institution'
    return t

def t_YEAR(t):
    r'year'
    return t

def t_KEYWORD(t):
    r'keyword'
    return t

def t_TECHREPORT(t):
    r'@techreport'
    return t

def t_ATEXT(t):
    r'"(.*)"'
    t.value = t.group(1)
    return t


# 1.4)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # Corrigido para evitar conflito com números
    print(f'Variável {t.value}')
    return t


# 1.6)
def t_newline(t):
    r'\n+'
    print("\\", end="")
    print("n")
    t.lexer.lineno += len(t.value)

# Caracteres ignorados (espaços e tabulações)
t_ignore = ' \t'

# 1.2)
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Criar o analisador léxico (lexer)
lexer = lex.lex()

# Entrada de teste
data = '''
x = a + 1
b = 2
a = b - 1
a *= 2
'''

# Alimentar o lexer com a entrada

# 1.3)
while True:
    token = sys.stdin.read()
    if re.match(r'STOP', token):
        break
    else:
        lexer.input(token)
        while True:
            tok = lexer.token()
            if not tok:
                break  # Sem mais tokens
            print(tok)
