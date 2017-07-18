from tree.operations.OperationType import OperationType
from tree.operations.UnaryOperation import UnaryOperation


class PointerOperation(UnaryOperation):
    def __init__(self, operation, parent=None):
        super(PointerOperation, self).__init__(operation=operation,
                                                  parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "PointerOperation {}: {}".format(self.operation,
                                                   statementsString)
