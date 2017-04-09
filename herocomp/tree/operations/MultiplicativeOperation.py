from tree.operations.BinaryOperation import BinaryOperation
from tree.operations.OperationType import OperationType


class MultiplicativeOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(MultiplicativeOperation, self).__init__(operation=operation,
                                                
                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "MultiplicativeOperation {}: {}".format(self.operation,
                                                 statementsString)
