from antlr4 import Token


class AST:

    def __init__(self, parse_tree, parent=None, children=[]):
        self.payload = self.__getPayload(parse_tree)
        self.children = children
        self.parent = parent

        if parent is None:
            AST.walk(parse_tree, self)
        else:
            parent.children.append(self)

    def __getPayload(self, parse_tree):
        return parse_tree.getPayload()
        # if parse_tree.getChildCount() == 0:
        #
        # else:
        #     rule_name = parse_tree.getNodeText()

    @staticmethod
    def walk(parse_tree, ast):
        if parse_tree.getChildCount() == 0:
            AST(parent=ast, parse_tree=parse_tree)
        elif parse_tree.getChildCount() == 1:
            AST.walk(list(parse_tree.getChildren())[0], ast)
        elif parse_tree.getChildCount() > 1:
            for child in parse_tree.getChildren():
                tmp = AST(parent=ast, parse_tree=child)

                if not isinstance(tmp.payload, Token):
                    AST.walk(child, tmp)
