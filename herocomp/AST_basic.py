from antlr4 import Token
from HerocLexer import HerocLexer


class AST:

    def __init__(self, parse_tree, parent=None, children=None):
        self.payload = AST.getPayLoad(parse_tree)
        self.parent = parent

        if children is None:
            self.children = []
        else:
            self.children = children


        if parent is None:
            AST.walk(parse_tree, self)
        else:
            parent.children.append(self)

    @staticmethod
    def getPayLoad(parse_tree):
        if parse_tree.getChildCount() == 0:
            return parse_tree.getPayload()
        else:
            rule_name = type(parse_tree).__name__.replace('Context', '')
            return rule_name

    @staticmethod
    def walk(parse_tree, ast):
        # In case of leaf
        if parse_tree.getChildCount() == 0:
            AST(parent=ast, parse_tree=parse_tree)

        # In case of node with one child
        elif parse_tree.getChildCount() == 1:
            child = parse_tree.getChild(0)

            AST.walk(child, ast)

        elif parse_tree.getChildCount() > 1:
            for child in parse_tree.getChildren():
                tmp = AST(parent=ast, parse_tree=child)

                if not isinstance(tmp.payload, Token):
                    AST.walk(child, tmp)

    def __str__(self, level=0):
        if isinstance(self.payload, Token):
            result = level * "  " + "TOKEN:" + repr(self.payload.text) + "\n"
        else:
            result = level * "  " + str(self.payload) + "\n"
        # print(self.children)
        for child in self.children:
            result += child.__str__(level+1)
        return result
