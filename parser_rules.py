import ply.yacc as yacc
import AST

from token_rules import tokens


def p_empty(p):
    """empty :"""
    pass


def p_compUnit_repeat(p):
    """compUnit_repeat : empty
                | compUnit compUnit_repeat"""

    p[0] = AST.ASTNode()
    if len(p) == 3:
        p[0].add_child(p[1])
        p[0].merge(p[2])


def p_compUnit(p):
    """compUnit : decl compUnit_repeat
                | cir_function compUnit_repeat
                | function compUnit_repeat
                | module compUnit_repeat
                | bundle compUnit_repeat"""

    p[0] = AST.CompUnitNode(p[1])
    p[0].merge(p[2])


def p_comp_decl(p):
    """decl : constDecl
            | varDecl
            | cirDecl
            | modDecl
            | bundleDecl"""

    p[0] = AST.CompUnitNode(p[1])


def p_constDecl_repeat(p):
    """constDecl_repeat : empty
                        | ',' constDef constDecl_repeat"""
    p[0] = AST.ConstDeclNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_constDecl(p):
    """constDecl : CONST val_type constDef constDecl_repeat ';'"""
    p[0] = AST.ConstDeclNode(p[2], p[3])
    p[0].merge(p[4])


def p_cir_basic_type(p):
    """cir_basic_type : REG
                      | WIRE
                      | CLOCK
                      | ID"""
    p[0] = AST.CirBasicTypeNode()
    p[0].type = p[1]

def p_cir_type(p):
    """cir_type : cir_basic_type
                | cir_basic_type '[' exp ']'"""
    p[0] = AST.CirTypeNode()
    p[0].type = p[1]
    if len(p) == 5:
        p[0].add_child(p[3])


def p_val_type(p):
    """val_type : INT
                  | FLOAT"""

    p[0] = AST.ValTypeNode()
    p[0].type = p[1]


def p_type_def(p):
    """type_def : val_type
                | cir_type"""

    p[0] = AST.TypeDefNode(p[1])


def p_array(p):
    """array : empty
             | '[' constExp ']' array"""
    p[0] = AST.ArrayNode()
    if len(p) == 5:
        p[0].add_child(p[2])
        p[0].merge(p[4])


def p_constDef(p):
    """constDef : ID array ASSIGN constInitVal"""
    p[0] = AST.ConstDefNode(p[2], p[4])


def p_constInitVal_repeat(p):
    """constInitVal_repeat : empty
                            | ',' constInitVal constInitVal_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_constInitVal(p):
    """constInitVal : constExp
                    | '{' constInitVal constInitVal_repeat '}'"""
    if len(p) == 2:
        p[0] = AST.ConstInitValNode(p[1])
    elif len(p) == 5:
        p[0] = AST.ConstInitValNode(p[2])
        p[0].merge(p[3])


def p_varDef_repeat(p):
    """varDef_repeat : empty
                      | ',' varDef varDef_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_varDecl(p):
    """varDecl : val_type varDef varDef_repeat ';'"""
    p[0] = AST.VarDeclNode(p[1], p[2], p[3])


def p_varDef(p):
    """varDef : ID array
              | ID array ASSIGN initVal"""
    p[0] = AST.VarDefNode(p[2])
    p[0].identifier = p[1]
    p[0].isInit = False
    if len(p) == 5:
        p[0].add_child(p[4])
        p[0].isInit = True


def p_modDecl(p):
    """modDecl : ID '(' module_R_params ')' ID array ';'"""
    p[0] = AST.ModDeclNode(p[3], p[6])
    p[0].type = p[1]
    p[0].name = p[5]



def p_R_port_def(p):
    """R_port_def : IN '.'
                  | OUT '.'
                  | INOUT '.'"""
    p[0] = AST.RPortDefNode()
    p[0].direct = p[1]


def p_module_R_params_item(p):
    """p_module_R_params_item : R_port_def ID '(' ID ')'"""
    p[0] = AST.ModuleRparamsItemNode()
    p[0].formal_para = p[2]
    p[0].actual_para = p[4]


def p_module_R_params_repeat(p):
    """module_R_params_repeat : empty
                              | ','  p_module_R_params_item module_R_params_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 8:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_module_R_params(p):
    """module_R_params : p_module_R_params_item  module_R_params_repeat"""
    p[0] = AST.ModuleRParams(p[1])
    p[0].merge(p[2])


def p_bundleDecl_repeat(p):
    """bundleDecl_repeat : empty
                         | ',' bundleDef bundleDecl_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_bundleDecl(p):
    """bundleDecl : ID bundleDef bundleDecl_repeat"""
    p[0] = AST.BundleDeclNode(p[2])
    p[0].merge(p[3])
    p[0].type = p[1]


def p_bundleDef(p):
    """bundleDef : ID array"""
    p[0] = AST.BundleDefNode(p[2])
    p[0].name = p[1]


def p_initVal_repeat(p):
    """initVal_repeat : empty
                      | ',' initVal initVal_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_initVal(p):
    """initVal : exp
               | '{' initVal initVal_repeat '}'"""
    p[0] = AST.InitValNode()
    if len(p) == 2:
        p[0] = AST.InitValNode(p[1])
    elif len(p) == 5:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_cirDecl_repeat(p):
    """cirDecl_repeat : empty
                      | ',' cirDef cirDecl_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])

def p_cirDecl(p):
    """cirDecl : cir_type cirDef cirDecl_repeat ';'"""
    p[0] = AST.CirDeclNode(p[1], p[2], p[3])


def p_cirDef(p):
    """cirDef : ID array
              | ID array ASSIGN initVal"""
    p[0] = AST.CirDeclNode(p[2])
    p[0].name = p[1]
    p[0].isInit = False
    if len(p) == 5:
        p[0].add_child(p[4])
        p[0].isInit = True


def p_cir_function(p):
    """cir_function : cir_type ID '(' cir_funcFParams ')' block"""
    p[0] = AST.CirFunctionNode(p[1], p[4], p[6])
    p[0].name = p[2]


def p_function(p):
    """function : val_type ID '(' funcFParams ')' block"""
    p[0] = AST.FunctionNode(p[1], p[4], p[6])
    p[0].name = p[2]


def p_cir_funcFParams_repeat(p):
    """cir_funcFParams_repeat : empty
                              | ',' cir_funcFParam cir_funcFParams_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_cir_funcFParams(p):
    """cir_funcFParams : cir_funcFParam cir_funcFParams_repeat"""
    p[0] = AST.cir_funcFParams(p[1])
    p[0].merge(p[2])


def p_funcFParams_repeat(p):
    """funcFParams_repeat : empty
                          | ',' funcFParam funcFParams_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_funcFParams(p):
    """funcFParams : funcFParam funcFParams_repeat"""
    p[0] = AST.FuncFParamsNode(p[1])
    p[0].merge(p[2])


def p_cir_funcFParam(p):
    """cir_funcFParam : type_def ID array"""
    p[0]  =AST.CirFuncFParamNode(p[1])
    p[0].name = p[2]

def p_funcFParam(p):
    """funcFParam : val_type ID array"""
    p[0] = AST.FuncFParamNode(p[1])
    p[0].name = p[2]


def p_module_para_para(p):
    """module_para_para : empty
                   | PARA val_type ID ','
                   | PARA val_type ID ',' module_para_para"""
    p[0] = AST.ASTNode()
    if len(p) >= 5:
        tmp = AST.ModuleParaParaNode()
        tmp.name = p[3]
        tmp.type = p[2]
        p[0].add_child(tmp)
        if len(p) == 6:
            p[0].merge(p[5])

def p_module_para_port(p):
    """p_module_para_port : empty
                          | ',' port_def ID p_module_para_port"""
    p[0] = AST.ASTNode()
    if len(p) == 5:
        tmp = AST.ModuleParaPortNode()
        tmp.name = p[3]
        tmp.add_child(p[2])
        p[0].add_child(tmp)
        p[0].merge(p[4])


def p_module(p):
    """module : MODULE ID '(' module_para_para port_def ID p_module_para_port ')' block"""

    p[0] = AST.ModuleNode()
    p[0].merge(p[4])
    tmp = AST.ModuleParaPortNode()
    tmp.name = p[6]
    tmp.add_child(p[5])
    p[0].add_child(tmp)
    p[0].merge(p[7])
    p[0].name = p[2]

    p[0].add_child(p[9])

def p_bundle_repeat(p):
    """bundle_repeat : empty
                      | ',' cir_type ID bundle_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 5:
        tmp = AST.BundleParaNode()
        tmp.name = p[3]
        tmp.type = p[2]
        p[0].add_child(tmp)
        p[0].merge(p[4])

def p_bundle(p):
    """bundle : BUNDLE ID '(' cir_type ID bundle_repeat ')'"""

    tmp = AST.BundleParaNode()
    tmp.name = p[5]
    tmp.type = p[4]

    p[0] = AST.BundleNode(tmp)
    p[0].merge(p[6])
    p[0].name = p[2]


def p_block_repeat(p):
    """block_repeat : empty
                    | blockItem block_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 3:
        p[0].add_child(p[1])
        p[0].merge(p[2])

def p_block(p):
    """block : '{' block_repeat '}'"""
    p[0] = AST.BlockNode()
    p[0].merge(p[2])

def p_blockItem(p):
    """blockItem : decl
                 | stmt"""
    p[0] = AST.BlockItemNode(p[1])

def p_stmt(p):
    """stmt : lVal ASSIGN exp ';'
            | lVal CONNECT exp ';'
            | ';'
            | exp
            | block
            | seqLogStmt
            | ifStmt
            | forStmt
            | RETURN exp ';'"""
    p[0] = AST.StmtNode()
    p[0].type = "empty"
    if len(p) == 1 and p[1] != ';':
        p[0].add_child(p[1])
        p[0].type = "other"
    elif len(p) == 4:
        p[0].type = "return"
        p[0].add_child(p[2])
    elif len(p) == 5 and p[2] == '=':
        p[0].type = "assign"
        p[0].add_child(p[1], p[3])
    elif len(p) == 5 and p[2] == ':=':
        p[0].type = "connect"
        p[0].add_child(p[1], p[3])

def p_seqLogStmt(p):
    """seqLogStmt : WHEN '(' ID ')' stmt
                  | WHEN '(' ID '.' RISING ')' stmt
                  | WHEN '(' ID '.' FALLING ')' stmt"""
    p[0] = AST.SeqLogStmtNode()
    p[0].clock = p[3]

    if len(p) == 6:
        p[0].actoin = "both"
        p[0].add_child(p[5])
    elif len(p) == 8:
        p[0].action = p[5]
        p[0].add_child(p[7])


def p_elifStmt(p):
    """elifStmt : ELIF '(' exp ')' stmt elifStmt
                | empty"""
    p[0] = AST.ASTNode()
    if len(p) == 7:
        tmp = AST.ElifStmtNode(p[3], p[5])
        p[0].add_child(tmp)
        p[0].merge(p[6])


def p_elseStmt(p):
    """elseStmt : ELSE stmt
                | empty"""
    if len(p) == 3:
        p[0] = AST.ElseStmtNode(p[3])

def p_ifStmt(p):
    """ifStmt : IF '(' exp ')' stmt elifStmt elseStmt"""
    p[0] = AST.IfStmtNode(p[3], p[5], p[6], p[7])


def p_forStmt(p):
    """
     forStmt : FOR '(' varDecl exp ';' stmt ')' stmt
            | GENERATE FOR '(' varDecl exp ';' exp ')' COLON ID stmt
    """
    if p[1] == "generate":
        p[0] = AST.ForStmtNode(p[4], p[6], p[8], p[11],p[12])
        p[0].is_generate = True
    else:
        p[0] = AST.ForStmtNode(p[3],p[5],p[7],p[9])

def p_exp(p):
    """
    exp : lOrExp
    """
    p[0] = p[1]

def p_lVal(p):
    """
    lVal : ID array_exp_repeat1
        | ID array_exp_repeat2
        | '{' ID array_exp_repeat1 lVal_repeat '}'
        | '{' ID array_exp_repeat2 lVal_repeat '}'
        | MUX '(' exp ',' exp ',' exp ')'
        | lVal '.' ID
    """
    p[0] = AST.LValNode()
    if len(p) == 3:
        p[0].add_child(p[1],p[2])
    if len(p) == 6:
        p[0].add_child(p[2],p[3],p[4])
    if len(p) == 8:
        p[0].add_child(p[3],p[5],p[7])
    if len(p) == 4:
        p[0].add_child(p[1],p[3])

def p_primaryExp(p):
    """
    primaryExp : '(' exp ')'
            | lVal
            | number
    """
    if len(p) == 4:
        p[0] = AST.PrimaryExpNode(p[2])
        p[0].flag = 'add brace'
    else:
        p[0] = AST.PrimaryExpNode(p[1])

def p_lVal_repeat(p):
    """
    lVal_repeat : empty
                | ',' lVal  lVal_repeat
    """
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])

def p_array_exp_repeat1(p):
    """
    array_exp_repeat1 : empty
                        | '[' exp ']' array_exp_repeat1
    """
    p[0] = AST.ASTNode()
    if len(p) == 5:
        p[0].add_child(p[2])
        p[0].merge(p[4])
    p[0].flag = 'repeat_1'

def p_array_exp_repeat2(p):
    """
    array_exp_repeat2 : empty
                        | '[' exp COLON exp ']' array_exp_repeat2
    """
    p[0] = AST.ASTNode()
    if len(p) == 7:
        p[0].add_child(p[2],p[4])
        p[0].merge(p[6])
    p[0].flag = 'repeat_2'

def p_number(p):
    """
    number : INTEGER_CONST
    | FLOAT_CONST
    | circuit_const
    """
    p[0] = p[1]
def p_circuit_const(p):
    """
    circuit_const : exp BIT_WIDTH_NUMBER
    """
    p[0] = AST.CircuitConstNode(p[1],p[2])

def p_unaryExp(p):
    """
    unaryExp : primaryExp
                | ID '(' ')'
                | ID '(' funcRParams ')'
                | SIGNAL '(' unaryExp ')'
                | unaryOp unaryExp
    """
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 4:
        p[0] = AST.UnaryExpNode(p[1])
        p[0].flag = 'func no param'
    if len(p) == 5:
        if p[1] == 'Signal':
            p[0] = AST.UnaryExpNode(p[3])
            p[0].flag = 'signal'
        else:
            p[0] = AST.UnaryExpNode(p[1],p[3])
            p[0].flag = 'func with param'
    if len(p) == 3:
        p[0] = AST.UnaryExpNode(p[1], p[2])

def p_unaryOp(p):
    """
    unaryOp : ADD
    | SUB
    | NOT
    | NOTL
    """
    p[0] = AST.UnaryOpNode(p[1])


def p_exp_repeat(p):
    """
    exp_repeat : empty
               | ',' exp exp_repeat
    """

    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_children(p[2])
        p[0].merge(p[3])
        p[0].flag = 'exp repeat'


def p_funcRParams(p):
    """
    funcRParams : exp
                | exp exp_repeat
    """
    if len(p) == 2:
        p[0].add_children(p[1])
    else:
        p[0].add_children(p[1],p[2])



def p_mulExp(p):
    """
    mulExp : unaryExp
            | mulExp MUL unaryExp
            | mulExp DIV unaryExp
            | mulExp MOD unaryExp
            | mulExp POWER unaryExp
    """
    if len(p) == 2:
        p[0] = AST.MulExpExpNode(p[1])
    else:
        p[0] = AST.MulExpExpNode(p[1],p[2],p[3])

def p_addExp(p):
    """
    addExp : mulExp
            | addExp ADD mulExp
            | addExp SUB mulExp
    """
    if len(p) == 2:
        p[0] = AST.AddExpNode(p[1])
    else:
        p[0] = AST.AddExpNode(p[1],p[2],p[3])

def p_shiftExp(p):
    """
    shiftExp : addExp
            | shiftExp SLL addExp
            | shiftExp SRL addExp
            | shiftExp SRA addExp
    """
    if len(p) == 2:
        p[0] = AST.ShiftExpNode(p[1])
    else:
        p[0] = AST.ShiftExpNode(p[1],p[2],p[3])


def p_relExp(p):
    """
    relExp : shiftExp
            | relExp LT addExp
            | relExp GT addExp
            | relExp GE addExp
            | relExp LE addExp
    """
    if len(p) == 2:
        p[0] = AST.RelExpNode(p[1])
    else:
        p[0] = AST.RelExpNode(p[1],p[2],p[3])


def p_eqExp(p):
    """
    eqExp : relExp
            | eqExp EQUAL eqExp
            | eqExp NEQ eqExp
    """
    if len(p) == 2:
        p[0] = AST.EqExpNode(p[1])
    else:
        p[0] = AST.EqExpNode(p[1], p[2], p[3])

def p_redExp(p):
    """
    redExp : eqExp
            | redExp AND eqExp
            | redExp OR eqExp
            | redExp XOR eqExp
            | redExp XNOR eqExp

    """
    if len(p) == 2:
        p[0] = AST.RedExpNode(p[1])
    else:
        p[0] = AST.RedExpNode(p[1], p[2], p[3])

def p_lAndExp(p):
    """
    lAndExp : redExp
            | lAndExp LAND redExp
    """
    if len(p) == 2:
        p[0] = AST.LAndExpNode(p[1])
    else:
        p[0] = AST.LAndExpNode(p[1],p[2],p[3])

def p_lOrExp(p):
    """
    lOrExp : lAndExp
            | lOrExp LOR lAndExp
    """
    if len(p) == 2:
        p[0] = AST.LOrExpNode(p[1])
    else:
        p[0] = AST.LOrExpNode(p[1],p[2],p[3])


def p_port_def(p):
    """port_def : INPUT cir_type
                | OUTPUT cir_type
                | INOUT cir_type"""
    p[0] = AST.PortDefNode(p[1], p[2])


def p_constExp(p):
    """constExp : exp"""
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error!")
    print(p)