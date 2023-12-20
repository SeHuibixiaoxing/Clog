import ply.yacc as yacc

from token_rules import tokens


class ASTNode():
    def __init__(self, *childs):
        self.parent = None
        self.child = []
        self.add_child(childs)

    def add_child(self, *childs):
        for child in childs:
            self.add_child(child)

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def merge(self, *nodes):
        for node in nodes:
            for child in node.child:
                self.add_child(child)

    def print_node_info(self):
        print(f"{type(self)}", end="")
        for attr_name in dir(self):
            if not attr_name.startswith("__"):
                attr_value = getattr(self, attr_name)
                print(f",{attr_name}: {attr_value}", end="")


class CompUnitNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class ArrayNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class DeclNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class ConstDeclNode(ASTNode):
    # childs[0] : val_type
    # childs[1...] : constDef

    def __init__(self, *childs):
        super().__init__(childs)


class CirNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class ValNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class TypeDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class ConstDefNode(ASTNode):
    # child[0]: array
    # child[1]: constInitVal"""

    def __init__(self, *childs):
        super().__init__(childs)

        self.identifier = ""


class ConstInitValNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class VarDeclNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class VarDefNode(ASTNode):
    """varDef : ID array
              | ID array ASSIGN initVal"""

    def __init__(self, *childs):
        super().__init__(childs)

        self.identifier = ""
        self.isInit = False


class ModDeclNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.type = ""
        self.name = ""


class RPortDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.direct = 'unknown'


class ModuleRparamsItemNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.formal_para = ""
        self.actual_para = ""


class ModuleRParams(ASTNode):
    # childs: a list of ModuleRparamsItemNode

    def __init__(self, *childs):
        super().__init__(childs)


class BundleDeclNode(ASTNode):
    # child[0]: BundleRParams
    # child[1]: array
    def __init__(self, *childs):
        super().__init__(childs)

        self.type = ""


class BundleDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""


class InitValNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class CirDeclNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""
        self.isInit = False


class CirDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class CirFunctionNode(ASTNode):
    # child[0]: cir_type
    # child[1]: cir_funcFParams
    # child[2]: block
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""


class FunctionNode(ASTNode):
    # child[0]: val_type
    # child[1]: ID
    # child[2]: block
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""


class CirFuncFParamsNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class FuncFParamsNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class CirFuncFParamNode(ASTNode):
    # child[0]: type_def
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""


class FuncFParamNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""


class ModuleNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""

class ModuleParaParaNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""

class ModuleParaPortNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.name = ""

class BlockNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class BlockItemNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class StmtNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.type = ""


class SeqLogStmtNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.clock = ""
        self.action = ""


class IfStmtNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class ElifStmtNode(ASTNode):
    # child[0]: exp
    # child[1]: stmt
    def __init__(self, *childs):
        super().__init__(childs)

class ElseStmtNode(ASTNode):
    # child[0]: exp
    def __init__(self, *childs):
        super().__init__(childs)


class ForStmtNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class ExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class LValNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class PrimaryExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class NumberNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class UnaryExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class UnaryOpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class FuncRParamsNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class MulExpExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class AddExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class ShiftExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class RelExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class EqExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class RedExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class LAndExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class LOrExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class ConstExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class IntegerConstNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class FloatConstNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class CircuitConstNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class BinaryConstNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)


class CirTypeNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.type = ""


class ValTypeNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)

        self.type = ""


class PortDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(childs)
