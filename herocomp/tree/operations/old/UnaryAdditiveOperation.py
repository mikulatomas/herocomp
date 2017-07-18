from tree.operations.OperationType import OperationType
from tree.operations.UnaryOperation import UnaryOperation


class UnaryAdditiveOperation(UnaryOperation):
    def __init__(self, operation, parent=None):
        super(UnaryAdditiveOperation, self).__init__(operation=operation,
                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "UnaryAdditiveOperation {}: {}".format(self.operation,
                                                 statementsString)
