from tree.operations.OperationType import OperationType
from tree.operations.UnaryOperation import UnaryOperation


class IncrementalOperation(UnaryOperation):
    def __init__(self, operation, postfix=False, parent=None):
        super(IncrementalOperation, self).__init__(operation=operation,
                                                   postfix=postfix,
                                                   parent=parent)

    def __str__(self):
        statementsString = self.printStatements()
        return "IncrementalOperation {} postfix({}): {}".format(self.operation,
                                                                self.postfix,
                                                                statementsString)
