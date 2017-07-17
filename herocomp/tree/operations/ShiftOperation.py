from asm.Asm import *
from asm.Registers import Registers
from tree.operations.BinaryOperation import BinaryOperation
from tree.operations.OperationType import OperationType


class ShiftOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(ShiftOperation, self).__init__(operation=operation,
                                             parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "ShiftOperation {}: {}".format(self.operation,
                                              statementsString)

    def get_code(self):
        code = ""

        code += pop(Registers.R10)
        code += pop(Registers.R11)
        code += pop(Registers.RDX)
        code += pop(Registers.RCX)

        code += movq(Registers.R11, Registers.RCX)
        code += movq(Registers.R10, Registers.RDX)

        if self.operation is OperationType.LEFT_SHIFT:
            code += sall(Registers.CL, Registers.EDX)
        elif self.operation is OperationType.RIGHT_SHIFT:
            code += sarl(Registers.CL, Registers.EDX)

        code += movl(Registers.EDX, Registers.EAX)

        # Promote to 64bit
        code += cltq()

        code += pop(Registers.RCX)
        code += pop(Registers.RDX)
        code += push(Registers.RAX)

        return code
