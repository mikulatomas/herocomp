from tree.Node import Node
from tree.operations.OperationType import OperationType


class UnaryOperation(Node):
    def __init__(self, operation, postfix=False, parent=None):
        self.operation = operation
        self.postfix = postfix
        super(UnaryOperation, self).__init__(parent=parent)

    def get_code(self):
        return "not_implemented"

    def __str__(self):
        statementsString = self.printStatements()
        return "UnaryOperation {}: {}".format(self.operation,
                                                 statementsString)
