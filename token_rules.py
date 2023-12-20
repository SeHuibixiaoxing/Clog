literals = [',',
            ';',
            '[',
            ']',
            '{',
            '}',
            '(',
            ')',
            '.',
            ]

reserved = {
    'const': 'CONST',
    'reg': 'REG',
    'wire': 'WIRE',
    'clock': 'CLOCK',
    'int': 'INT',
    'float': 'FLOAT',
    'input': 'INPUT',
    'output': 'OUTPUT',
    'inout': 'INOUT',
    'module': 'MODULE',
    'para': 'PARA',
    'bundle': 'BUNDLE',
    'return': 'RETURN',
    'when': 'WHEN',
    'Mux': 'MUX',
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'for': 'FOR',
    'signal': 'SIGNAL',
    'rising': 'RISING',
    'falling': 'FALLING',
    'generate': 'GENERATE',
    'in': 'IN',
    'out': 'OUT',
}


tokens = [
    'ID',
    'BIT_WIDTH_NUMBER',
    'FLOAT_CONST',
    'CONNECT',
    'EQUAL',
    'ASSIGN',
    'POWER',
    'SLL',
    'SRL',
    'SRA',
    'LE',
    'GE',
    'NEQ',
    'LAND',
    'LOR',
    'COLON',
    'ADD',
    'SUB',
    'NOTL',
    'MUL',
    'DIV',
    'MOD',
    'LT',
    'GT',
    'AND',
    'OR',
    'INTEGER_CONST',
    'XOR',
    'XNOR',
    'NOT',
] + list(reserved.values())

# Comment
def t_COMMENT(t):
    r'(/\*([\s\S]*?)\*/)|(\/\/(.*))'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')

    return t

def t_XNOR(t):
    r'~\^'
    return t

def t_NOT(t):
    r'~'
    return t

def t_XOR(t):
    r'\^'
    return t

def t_MOD(t):
    r'%'
    return t

def t_DIV(t):
    r'/'
    return t

def t_ADD(t):
    r'\+'
    return t

def t_SUB(t):
    r'-'
    return t

def t_CONNECT(t):
    r':='
    return t

def t_COLON(t):
    r':'
    return t

def t_EQUAL(t):
    r'=='
    return t

def t_ASSIGN(t):
    r'='
    return t

def t_POWER(t):
    r'\*\*'
    return t

def t_MUL(t):
    r'\*'
    return t

def t_SLL(t):
    r'<<'
    return t

def t_SRL(t):
    r'>>'
    return t

def t_SRA(t):
    r'>>>'
    return t

def t_LE(t):
    r'<='
    return t

def t_GE(t):
    r'>='
    return t

def t_GT(t):
    r'>'
    return t

def t_LT(t):
    r'<'
    return t

def t_NEQ(t):
    r'!='
    return t

def t_NOTL(t):
    r'!'
    return t

def t_LAND(t):
    r'&&'
    return t

def t_AND(t):
    r'&'
    return t

def t_LOR(t):
    r'\|\|'
    return t

def t_OR(t):
    r'\|'
    return t

def t_BIT_WIDTH_NUMBER(t):
    r'\'(b|B|o|O|d|D|h|H)[\dabcdefABCDEF]+'
    return t

# A regular expression rule with some action code
def t_INTEGER_CONST(t):
    r'\d+'
    return t

def t_FLOAT_CONST(t):
    r'\d+\.\d+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


