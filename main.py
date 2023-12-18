
# Build the lexer
import ply.lex as lex
import sys
import token_rules

def print_token(lexer):
    while True:
        tok = lexer.token()

        if not tok:
            break  # No more input

        print(tok)

def test_file(filename, debug=False, encoding='utf-8'):
    lexer = lex.lex(module=token_rules, debug=debug)
    f = open(filename, encoding=encoding)
    data = f.read()
    lexer.input(data)
    print_token(lexer)


def test_ALU(debug=False):
    print("######example/ALU.cv")
    test_file("example/ALU.cv", debug, 'utf-8')

def test_bundle(debug=False):
    print("######example/bundle_test.cv")
    test_file("example/bundle_test.cv", debug, 'utf-8')

def test_regfile(debug=False):
    print("######example/regfile.cv")
    test_file("example/regfile.cv", debug, 'utf-8')

def test_tools(debug=False):
    print("######example/tools.cv")
    test_file("example/tools.cv", debug, 'utf-8')

def test_all(debug=False):
    test_ALU(debug)
    test_bundle(debug)
    test_regfile(debug)
    test_tools(debug)

if __name__ == '__main__':
    debug = False

    for i in range(1, len(sys.argv)):
        mode = sys.argv[i]
        if mode == 'alu':
            test_ALU(debug)
        elif mode == 'bundle':
            test_bundle(debug)
        elif mode == 'regfile':
            test_regfile(debug)
        elif mode == 'tools':
            test_tools(debug)
        elif mode == 'all':
            test_all(debug)




