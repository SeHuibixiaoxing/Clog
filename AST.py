import ply.yacc as yacc

from token_rules import tokens

in_seq = False
class ASTNode():
    def __init__(self, *childs):
        self.parent = None
        self.child = []
        self.flag = None
        self.add_child(*childs)
        self.isDef = False

    def add_child(self, *childs):
        for child in childs:
            if isinstance(child, ASTNode):
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

    def to_Verilog(self,file):
        if self.flag == 'repeat_1':
            for i in range(len(self.child)):
                if self.isDef:
                    file.write('[')
                    self.child[i].to_Verilog(file)
                    file.write('-1:0')
                    file.write(']')
                else:
                    file.write('[')
                    self.child[i].to_Verilog(file)
                    file.write(']')
        elif self.flag == 'repeat_2':
            for i in range(len(self.child)//2):
                file.write('[')
                self.child[2*i].to_Verilog(file)
                file.write(':')
                self.child[2*i+1].to_Verilog(file)
                file.write(']')
        elif self.flag == 'exp repeat':
            for i in range(len(self.child)):
                self.child[i].to_Verilog(file)
                if i < len(self.child)-1:
                    file.write(',')
        else:
            for c in self.child:
                if isinstance(c,str):
                    file.write(c)
                else:
                    c.to_Verilog(file)

class CompUnitNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        for c in self.child:
            c.to_Verilog(file)


class ArrayNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class DeclNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        self.child[0].to_Verilog(file)


class ConstDeclNode(ASTNode):
    # childs[0] : val_type
    # childs[1...] : constDef

    def __init__(self, *childs):
        super().__init__(*childs)


class CirNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class ValNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class TypeDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class ConstDefNode(ASTNode):
    # child[0]: array
    # child[1]: constInitVal"""

    def __init__(self, *childs):
        super().__init__(*childs)

        self.identifier = ""


class ConstInitValNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class VarDeclNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)




class VarDefNode(ASTNode):
    """varDef : ID array
              | ID array ASSIGN initVal"""

    def __init__(self, *childs):
        super().__init__(*childs)

        self.identifier = ""
        self.isInit = False


class ModDeclNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.type = ""
        self.name = ""


class RPortDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.direct = 'unknown'


class ModuleRparamsItemNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.formal_para = ""
        self.actual_para = ""


class ModuleRParams(ASTNode):
    # childs: a list of ModuleRparamsItemNode

    def __init__(self, *childs):
        super().__init__(*childs)

class BundleParaNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""
        self.type = ""

class BundleNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""


class BundleDeclNode(ASTNode):
    # child[0]: BundleRParams
    # child[1]: array
    def __init__(self, *childs):
        super().__init__(*childs)

        self.type = ""


class BundleDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""


class InitValNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class CirDeclNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""

    def to_Verilog(self,file):
        self.child[0].to_Verilog(file)
        file.write(' ')
        for i in range(1,len(self.child)):
            self.child[i].to_Verilog(file)
            if i<len(self.child)-1:
                file.write(',')
        file.write(';\n')



class CirDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
        self.isInit = False
        self.name = ""

    def to_Verilog(self,file):
        if not self.isInit:
            file.write(self.name)
            self.child[0].to_Verilog(file)
        else:
            file.write(self.name)
            self.child[0].to_Verilog(file)
            if in_seq:
                file.write('<=')
            else:
                file.write('=')
            self.child[1].to_Verilog(file)




class CirFunctionNode(ASTNode):
    # child[0]: cir_type
    # child[1]: cir_funcFParams
    # child[2]: block
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""


class FunctionNode(ASTNode):
    # child[0]: val_type
    # child[1]: ID
    # child[2]: block
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""


class CirFuncFParamsNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class FuncFParamsNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class CirFuncFParamNode(ASTNode):
    # child[0]: type_def
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""


class FuncFParamNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""


class ModuleNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""
    def to_Verilog(self,file):
        file.write(f"module {self.name}\n")
        para_cnt = 0
        for c in self.child:
            if hasattr(c,'type') and isinstance(c.type,ValTypeNode):
                para_cnt += 1
        #print 参数
        if para_cnt > 0:
            file.write("#(\n")
            for i in range(para_cnt):
                self.child[i].to_Verilog(file)
                if i < para_cnt-1:
                    file.write(",")
                file.write("\n")
            file.write(")\n")
        #print port
        file.write("(\n")
        for i in range(para_cnt,len(self.child)-1):
            self.child[i].to_Verilog(file)
            if i < len(self.child)-2:
                file.write(",")
            file.write("\n")
        file.write(");\n")
        self.child[-1].to_Verilog(file)
        file.write("endmodule\n")





class ModuleParaParaNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""
        self.type = ""
    def to_Verilog(self,file):
        file.write(f"parameter {self.name} = 32")

class ModuleParaPortNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.name = ""

    def to_Verilog(self,file):
        for c in self.child:
            c.to_Verilog(file)
        file.write(self.name)

class BlockNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

    def to_Verilog(self,file):
        print_b_e = True
        if isinstance(self.parent,ModuleNode):
            print_b_e = False
        if isinstance(self.parent.parent,ForStmtNode) and self.parent.parent.is_generate:
            print_b_e = False
        if print_b_e:
            file.write('begin\n')
        for c in self.child:
            c.to_Verilog(file)
        if print_b_e:
            file.write('end\n')

class BlockItemNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        for c in self.child:
            c.to_Verilog(file)

class StmtNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.type = ""

    def to_Verilog(self,file):
        if self.type == 'other':
            self.child[0].to_Verilog(file)
        if self.type == 'return':
            file.write('return ')
            self.child[0].to_Verilog(file)
            file.write(';\n')
        if self.type == 'assign':
            self.child[0].to_Verilog(file)
            if in_seq:
                file.write('<=')
            else:
                file.write('=')
            self.child[1].to_Verilog(file)
            file.write(';\n')
        if self.type == 'connect':
            if not in_seq:
                file.write('assign ')
            self.child[0].to_Verilog(file)
            if in_seq:
                file.write('<=')
            else:
                file.write('=')
            self.child[1].to_Verilog(file)
            file.write(';\n')

class SeqLogStmtNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.clock = ""
        self.action = ""

    def to_Verilog(self,file):
        if self.action == 'rising':
            file.write(f'always @(posedge {self.clock}) ')
        if self.action == 'falling':
            file.write(f'always @(negedge {self.clock}) ')
        if self.action == 'both':
            file.write(f'always @({self.clock}) ')
        global in_seq
        in_seq = True
        self.child[0].to_Verilog(file)
        in_seq = False



class IfStmtNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        file.write('if(')
        self.child[0].to_Verilog(file)
        file.write(')\n')
        self.child[1].to_Verilog(file)



class ElifStmtNode(ASTNode):
    # child[0]: exp
    # child[1]: stmt
    def __init__(self, *childs):
        super().__init__(*childs)

class ElseStmtNode(ASTNode):
    # child[0]: exp
    def __init__(self, *childs):
        super().__init__(*childs)


class ForStmtNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
        self.is_generate = False

    def to_Verilog(self,file):
        if self.is_generate:
            #读出genvar
            gen_variable = self.child[0].child[1].identifier
            file.write(f'genvar {gen_variable};\n')
            file.write('generate ')
            file.write(f'for ({gen_variable}=')
            self.child[0].child[1].child[1].child[0].to_Verilog(file)
            file.write(';')
            self.child[1].to_Verilog(file)
            file.write(';')
            file.write(f'{gen_variable}=')
            self.child[3].to_Verilog(file)
            file.write(f') begin: {self.child[4]}')
            file.write('\n')
            self.child[5].to_Verilog(file)
            file.write('end\n')
            file.write('endgenerate\n')

class ExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

    def to_Verilog(self,file):
        self.child[0].to_Verilog(file)


class LValNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

    def to_Verilog(self,file):
        if self.flag == 'type1':
            file.write(self.child[0])
            self.child[1].to_Verilog(file)
        if self.flag == 'type2':
            file.write(' (')
            self.child[0].to_Verilog(file)
            file.write(') ? ')
            self.child[1].to_Verilog(file)
            file.write(' : ')
            self.child[2].to_Verilog(file)

        if self.flag == 'type3':
            self.child[0].to_Verilog(file)
            file.write('.')
            file.write(self.child[0])
        if self.flag == 'type4':
            file.write('{')
            for i in range(len(self.child)):
                self.child[i].to_Verilog(file)
                if i < len(self.child)-1:
                    file.write(',')
            file.write('}')
        if self.flag == 'type5':
            self.child[0].to_Verilog(file)
            file.write('{')
            for i in range(1,len(self.child)):
                self.child[i].to_Verilog(file)
                if i < len(self.child)-1:
                    file.write(',')
            file.write('}')

class PrimaryExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

    def to_Verilog(self,file):
        if self.flag == 'add brace':
            file.write('(')
            self.child[0].to_Verilog(file)
            file.write(')')
        else:
            self.child[0].to_Verilog(file)

class NumberNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if isinstance(self.child[0],CircuitConstNode):
            self.child[0].to_Verilog(file)
        else:
            file.write(self.child[0])



class UnaryExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

    def to_Verilog(self,file):
        if self.flag == 'func no param':
            file.write(self.child[0])
            file.write('(')
            file.write(')')
        if self.flag == 'func with param':
            file.write(self.child[0])
            file.write('(')
            self.child[1].to_Verilog(file)
            file.write(')')
        if self.flag == 'unaryOp':
            self.child[0].to_Verilog(file)
            self.child[1].to_Verilog(file)




class UnaryOpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

    def to_Verilog(self,file):
        file.write(self.child[0])


class FuncRParamsNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class MulExpExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if len(self.child) == 3:
            self.child[0].to_Verilog(file)
            file.write(self.child[1])
            self.child[2].to_Verilog(file)
        else:
            self.child[0].to_Verilog(file)
class AddExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if len(self.child) == 3:
            self.child[0].to_Verilog(file)
            file.write(self.child[1])
            self.child[2].to_Verilog(file)
        else:
            self.child[0].to_Verilog(file)

class ShiftExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if len(self.child) == 3:
            self.child[0].to_Verilog(file)
            file.write(self.child[1])
            self.child[2].to_Verilog(file)
        else:
            self.child[0].to_Verilog(file)

class RelExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if len(self.child) == 3:
            self.child[0].to_Verilog(file)
            file.write(self.child[1])
            self.child[2].to_Verilog(file)
        else:
            self.child[0].to_Verilog(file)

class EqExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if len(self.child) == 3:
            self.child[0].to_Verilog(file)
            file.write(self.child[1])
            self.child[2].to_Verilog(file)
        else:
            self.child[0].to_Verilog(file)

class RedExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if len(self.child) == 3:
            self.child[0].to_Verilog(file)
            file.write(self.child[1])
            self.child[2].to_Verilog(file)
        else:
            self.child[0].to_Verilog(file)


class LAndExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if len(self.child) == 3:
            self.child[0].to_Verilog(file)
            file.write(self.child[1])
            self.child[2].to_Verilog(file)
        else:
            self.child[0].to_Verilog(file)


class LOrExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        if len(self.child) == 3:
            self.child[0].to_Verilog(file)
            file.write(self.child[1])
            self.child[2].to_Verilog(file)
        else:
            self.child[0].to_Verilog(file)


class ConstExpNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class IntegerConstNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class FloatConstNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)


class CircuitConstNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

    def to_Verilog(self,file):
        self.child[0].to_Verilog(file)
        file.write(self.child[1])



class BinaryConstNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

class CirBasicTypeNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.type = ""

    def to_Verilog(self,file):
        if self.type == 'clock':
            file.write('wire')
        else:
            file.write(self.type)

class CirTypeNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.type = ""

    def to_Verilog(self,file):
        self.type.to_Verilog(file)
        if len(self.child) == 1:
            #有exp
            file.write('[')
            self.child[0].to_Verilog(file)
            file.write('-1:0]')

class ValTypeNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)

        self.type = ""


class PortDefNode(ASTNode):
    def __init__(self, *childs):
        super().__init__(*childs)
    def to_Verilog(self,file):
        for c in self.child:
            if isinstance(c,str):
                file.write(c)
            else:
                c.to_Verilog(file)
            file.write(' ')

