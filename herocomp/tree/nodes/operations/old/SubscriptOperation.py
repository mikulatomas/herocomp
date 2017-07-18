from tree.nodes.operations.OperationType import OperationType
from tree.nodes.operations.UnaryOperation import UnaryOperation


class SubscriptOperation(UnaryOperation):
    def __init__(self, operation, parent=None):
        super(SubscriptOperation, self).__init__(postfix=True,
                                                 operation=operation,
                                                 parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "SubscriptOperation {}: {}".format(self.operation,
                                                   statementsString)
