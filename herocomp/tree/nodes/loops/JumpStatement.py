import tree
from asm.Asm import *
from asm.Registers import Registers
from tree.nodes.loops.JumpStatementType import JumpStatementType
from tree.nodes.Node import Node


class JumpStatement(Node):
    def __init__(self, jump_statement_type=JumpStatementType.RETURN, parent=None):
        self.jump_statement_type = jump_statement_type
        super(JumpStatement, self).__init__(parent=parent)

    def __str__(self):
        valuesString = self.printStatements()

        return "JumpStatement {}: {}".format(self.jump_statement_type, valuesString)

    def _get_outer_loop(self):
        parent = self.parent
        loop = None

        while parent.parent is not None:
            if isinstance(parent, tree.nodes.loops.Loop.Loop):
                loop = parent
                break

            parent = parent.parent

        if loop is None:
            error_string = "Jump statement out of loop"
            raise ValueError(error_string)

        return loop

    def get_code(self):
        code = ""
        if self.jump_statement_type == JumpStatementType.RETURN:
            if len(self.statements) > 0:
                code += self.statements[0].get_code()
            else:
                code += instruction("movq", number_constant(0), Registers.RAX)
            code += instruction("leave")
            code += instruction("ret")
        elif self.jump_statement_type == JumpStatementType.BREAK:
            outer_loop = self._get_outer_loop()
            code += instruction("jmp", outer_loop.end_label())
        elif self.jump_statement_type == JumpStatementType.CONTINUE:
            outer_loop = self._get_outer_loop()
            code += instruction("jmp", outer_loop.next_label())

        return code
