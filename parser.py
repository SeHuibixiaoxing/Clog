import ply.yacc as yacc
import AST

from token_rules import tokens


def p_empty(p):
    """empty :"""
    pass


def p_compUnit_repeat(p):
    """compUnit : empty
                | compUnit compUnit"""

    p[0] = AST.CompUnitNode()
    if len(p) == 3:
        p[0].merge(p[1], p[2])


def p_compUnit(p):
    """compUnit : decl
                | cir_function
                | function
                | module
                | bundle"""

    p[0] = AST.CompUnitNode(p[1])


def p_comp_decl(p):
    """decl : constDecl
            | varDecl
            | cirDecl
            | modDecl
            | bundleDecl"""

    p[0] = AST.CompUnitNode(p[1])


def p_constDecl_repeat(p):
    """constDef_repeat : empty
                        | ',' comseDef constDef_repeat"""
    p[0] = AST.ConstDeclNode()
    if len(p) == 3:
        p[0].add_child(p[2])
        p[0].merge(p[3])


def p_constDecl(p):
    """constDecl : CONST val_type constDef constDecl_repeat ';'"""
    p[0] = AST.ConstDeclNode(p[2], p[3])
    p[0].merge(p[4])


def p_cir_type(p):
    """cir_type : REG
                | WIRE
                | CLOCK"""

    p[0] = AST.CirTypeNode()
    p[0].type = p[1]


def p_val_type(p):
    """val_type : INT
                  | FLOAT"""

    p[0] = AST.ValTypeNode()
    p[0].type = p[1]


def p_type_def(p):
    """value_type : val_type
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
    """constInitVal : constExp"""
    p[0] = AST.ConstInitValNode(p[1])


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
    """modDecl : ID ID '( module_R_params ')"""
    p[0] = AST.ModDeclNode(p[4])
    p[0].type = p[1]
    p[0].name = p[2]


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
                              | ','  p_module_R_params_item p_module_R_params_repeat"""
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
                         : ',' bundleDef bundleDecl_repeat"""
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


def p_initVal(p):
    """initVal : exp ';'"""
    p[0] = AST.InitValNode(p[1])


def p_cirDecl_repeat(p):
    """cirDecl_repeat : empty
                      | ',' cirDef cirDecl_repeat"""
    p[0] = AST.ASTNode()
    if len(p) == 4:
        p[0].add_child(p[2])
        p[0].merge(p[3])

def p_cirDecl(p):
    """cirDecl : cir_type cirDef p_cirDecl_repeat ';'"""
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
    """cir_funcParam : type_def ID array"""
    p[0]  =AST.CirFuncFParamNode(p[1])
    p[0].name = p[2]

def p_funcFParam(p):
    """funcFParam : val_type ID array"""
    p[0] = AST.FuncFParamNode(p[1])
    p[0].name = p[2]


def p_module_para_para(p):
    """module_para_para : empty
                   | 'PARA' ID ',' module_para_para"""
    p[0] = AST.ASTNode()
    if len(p) == 5:
        tmp = AST.ModuleParaParaNode()
        tmp.name = p[2]
        p[0].add_child(tmp)
        p[0].merge(p[4])

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
    """module : MODULE ID '(' module_para_para port_def ID p_module_para_port"""

    p[0] = AST.ModuleNode()
    p[0].merge(p[4])
    tmp = AST.ModuleParaPortNode()
    tmp.name = p[6]
    tmp.add_child(p[5])
    p[0].add_child(tmp)
    p[0].merge(p[7])

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
    """seqLogStmt : WHEN '(' ID ') stmt
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
    """elseStmt : ELSE 'stmt'"""
    p[0] = AST.ElseStmtNode(p[3])

def p_ifStmt(p):
    """ifStmt : IF '(' exp ')' stmt elifStmt elseStmt"""
    p[0] = AST.IfStmtNode(p[3], p[5], p[6], p[7])
