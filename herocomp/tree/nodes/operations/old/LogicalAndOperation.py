from tree.nodes.operations.BinaryOperation import BinaryOperation
from tree.nodes.operations.OperationType import OperationType


class LogicalAndOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(LogicalAndOperation, self).__init__(operation=operation,

                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "LogicalAndOperation {}: {}".format(self.operation,
                                                 statementsString)
