from tree.nodes.operations.BinaryOperation import BinaryOperation
from tree.nodes.operations.OperationType import OperationType


class LogicalOrOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(LogicalOrOperation, self).__init__(operation=operation,

                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "LogicalOrOperation {}: {}".format(self.operation,
                                                 statementsString)
