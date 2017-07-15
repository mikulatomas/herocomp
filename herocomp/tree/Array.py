from tree.Node import Node


class Array(Node):
    def __init__(self, array_size=None, parent=None):
        self.array_size = array_size

        if self.array_size is not None:
            self.array_size.parent = self

        super(Array, self).__init__(parent)

    def setArraySize(self, array_size):
        self.array_size = array_size
        self.array_size.parent = self

    def __str__(self):
        valuesString = self.printStatements()
        self.array_size.depth = self.depth + 1
        
        return "Array: \n{} {}".format(self.array_size.generateTabsForDepth() + str(self.array_size),
                                     valuesString)
