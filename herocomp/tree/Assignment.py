from tree.Node import Node
from tree.operations.OperationType import OperationType


class Assignment(Node):
    def __init__(self, operation, parent=None):
        self.operation = operation
        super(Assignment, self).__init__(parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "Assignment {}: {}".format(self.operation,
                                                 statementsString)
