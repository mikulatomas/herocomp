# Base class for storing Node informations in AST

class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.statements = []
