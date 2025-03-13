import ply.lex as lex 
import re
import sys

# Lista de tokens
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'ID',
   'EQUALS'
)

# Definição das expressões regulares para os tokens
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Converte para inteiro
    return t

# 1.5)
def t_PLUS(t):
    r'\+'
    print("Operador encontrado")
    return t

def t_EQUALS(t):
    r'\='
    print("Operador encontrado")
    return t

def t_MINUS(t):
    r'\-'
    print("Operador encontrado")
    return t

def t_TIMES(t):
    r'\*'
    print("Operador encontrado")
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
