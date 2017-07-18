from tree.nodes.operations.OperationType import OperationType
from tree.nodes.operations.UnaryOperation import UnaryOperation


class LogicalNotOperation(UnaryOperation):
    def __init__(self, operation, parent=None):
        super(LogicalNotOperation, self).__init__(operation=operation,
                                                  parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "LogicalNotOperation {}: {}".format(self.operation,
                                                   statementsString)
