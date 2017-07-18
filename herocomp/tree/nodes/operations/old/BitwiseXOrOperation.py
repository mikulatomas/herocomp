from tree.nodes.operations.BinaryOperation import BinaryOperation
from tree.nodes.operations.OperationType import OperationType


class BitwiseXOrOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(BitwiseXOrOperation, self).__init__(operation=operation,
                                                
                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "BitwiseXOrOperation {}: {}".format(self.operation,
                                                 statementsString)
