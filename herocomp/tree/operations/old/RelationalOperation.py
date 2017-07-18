from tree.operations.BinaryOperation import BinaryOperation
from tree.operations.OperationType import OperationType


class RelationalOperation(BinaryOperation):
    def __init__(self, operation, parent=None):
        super(RelationalOperation, self).__init__(operation=operation,
                                                
                                                parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "RelationalOperation {}: {}".format(self.operation,
                                                 statementsString)
