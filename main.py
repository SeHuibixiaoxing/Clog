
# Build the lexer
import ply.lex as lex
import ply.yacc as yacc
import sys
import token_rules
from token_rules import *
from parser_rules import *
start = 'compUnit'
def print_token(lexer):
    while True:
        tok = lexer.token()

        if not tok:
            break  # No more input

        print(tok)

def test_file(filename, debug=False, encoding='utf-8'):
    f = open(filename, encoding=encoding)
    data = f.read()
    lexer = lex.lex(module=token_rules, debug=debug)
    lexer.input(data)
    print_token(lexer)

    parser1 = yacc.yacc()
    result = parser1.parse(input=data, lexer=lexer)
    print(result)


def test_lexer_ALU(debug=False):
    print("######example/ALU.cv")
    test_file("example/ALU.cv", debug, 'utf-8')

def test_lexer_bundle(debug=False):
    print("######example/bundle_test.cv")
    test_file("example/bundle_test.cv", debug, 'utf-8')

def test_lexer_regfile(debug=False):
    print("######example/regfile.cv")
    test_file("example/regfile.cv", debug, 'utf-8')

def test_lexer_tools(debug=False):
    print("######example/tools.cv")
    test_file("example/tools.cv", debug, 'utf-8')

def test_lexer_all(debug=False):
    test_lexer_ALU(debug)
    test_lexer_bundle(debug)
    test_lexer_regfile(debug)
    test_lexer_tools(debug)

def lexer_main(debug = False):
    for i in range(1, len(sys.argv)):
        mode = sys.argv[i]
        if mode == 'alu':
            test_lexer_ALU(debug)
        elif mode == 'bundle':
            test_lexer_bundle(debug)
        elif mode == 'regfile':
            test_lexer_regfile(debug)
        elif mode == 'tools':
            test_lexer_tools(debug)
        elif mode == 'all':
            test_lexer_all(debug)

if __name__ == '__main__':
    lexer_main(True)




