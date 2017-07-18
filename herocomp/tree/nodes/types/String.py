from tree.nodes.Node import Node


class String(Node):
    def __init__(self, value="", parent=None):
        self.value = value
        super(String, self).__init__(parent)

    def __str__(self):
        return "String: {0}".format(self.value)
