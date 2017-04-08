from tree.Node import Node


class Identifier(Node):
    def __init__(self, name, parent=None):
        self.name = name
        super(Identifier, self).__init__(parent)

    def __str__(self):
        return "Identifier: {}".format(self.name)
