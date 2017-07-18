from tree.nodes.operations.OperationType import OperationType
from tree.nodes.operations.UnaryOperation import UnaryOperation


class BitwiseNotOperation(UnaryOperation):
    def __init__(self, operation, parent=None):
        super(BitwiseNotOperation, self).__init__(operation=operation,
                                                  parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "BitwiseNotOperation {}: {}".format(self.operation,
                                                   statementsString)
