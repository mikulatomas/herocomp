from asm.Asm import *
from tree.JumpStatementType import JumpStatementType
from tree.Node import Node


class JumpStatement(Node):
    def __init__(self, jump_statement_type=JumpStatementType.RETURN, parent=None):
        self.jump_statement_type = jump_statement_type
        super(JumpStatement, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "JumpStatement {}: {}".format(self.jump_statement_type, valuesString)

    def get_code(self):
        code = ""
        if self.jump_statement_type == JumpStatementType.RETURN:
            code += leave()
            code += ret()
        return code
