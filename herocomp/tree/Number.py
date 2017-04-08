from tree.Node import Node


class Number(Node):
    def __init__(self, value=0, parent=None):
        self.value = value
        super(Number, self).__init__(parent)

    def __str__(self):
        return "Number: {0}".format(self.value)
