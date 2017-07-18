from tree.nodes.operations.BinaryOperation import BinaryOperation
from tree.nodes.operations.OperationType import OperationType


class AdditiveOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(AdditiveOperation, self).__init__(operation=operation,
                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "AdditiveOperation {}: {}".format(self.operation,
                                                 statementsString)
