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