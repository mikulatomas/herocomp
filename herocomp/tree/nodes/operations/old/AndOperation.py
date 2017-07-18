from tree.nodes.operations.BinaryOperation import BinaryOperation
from tree.nodes.operations.OperationType import OperationType


class AndOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(AndOperation, self).__init__(operation=operation,
                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "AndOperation {}: {}".format(self.operation,
                                                 statementsString)
