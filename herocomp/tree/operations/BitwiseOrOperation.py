from asm.Asm import *
from asm.Registers import Registers
from tree.operations.BinaryOperation import BinaryOperation
from tree.operations.OperationType import OperationType


class BitwiseOrOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(BitwiseOrOperation, self).__init__(operation=operation,

                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "BitwiseOrOperation {}: {}".format(self.operation,
                                                 statementsString)

    def get_operation_code(self):
        code = ""

        code += pop(Registers.R10)
        code += pop(Registers.R11)

        code += cmp("$0", Registers.R10)
        # code += movq("$1", Registers.R10)
        code += movq("$0", Registers.R12)
        code += cmove(Registers.R12, Registers.R10)

        code += cmp("$0", Registers.R11)
        # code += cmp("$1", Registers.R11)
        code += movq("$0", Registers.R12)
        code += cmove(Registers.R12, Registers.R11)

        code += orq(Registers.R10, Registers.R11)

        code += push(Registers.R11)

        return code
