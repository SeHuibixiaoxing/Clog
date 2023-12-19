import ply.yacc as yacc

from token_rules import tokens


class ASTNode():
    def __init__(self, parent = None):
        self.parent = parent
        self.child = []


    def add_child(self, child):
        child.parent = self
        self.child.append(child)


class CompunitNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class DeclNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ConstDeclNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class CirNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ValNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class TypeDefNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ConstDefNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ConstInitValIDNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class VarDeclNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class VarDefNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ModDeclNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class RPortDefNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ModelRParamNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class BundleDeclNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class BundleRParamNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class InitValNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class CirDeclNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class CirDefNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class CirFunctionNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class FunctionNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class CirFuncFParamsNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class FuncFParamsNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class CirFuncFParamNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class FuncFParamNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ModuleNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class BlockNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class BlockItemNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class StmtNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class SeqLogStmtNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class IfStmtNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ForStmtNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class LValNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class PrimaryExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class NumberNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class UnaryExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class UnaryOpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class FuncRParamsNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class MulExpExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class AddExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ShiftExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class RelExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class EqExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class RedExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class LAndExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class LOrExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ConstExpNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class IntegerConstNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class FloatConstNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class CircuitConstNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class BinaryConstNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class CirTypeNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class ValTypeNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)

class PortDefNode(ASTNode):
    def __init__(self, parent = None):
        super().__init__(parent)
