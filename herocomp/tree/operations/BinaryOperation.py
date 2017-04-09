from tree.Node import Node
from tree.operations.OperationType import OperationType


class BinaryOperation(Node):
    def __init__(self, operation, parent=None):
        self.operation = operation
        super(BinaryOperation, self).__init__(parent=parent)
