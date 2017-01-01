from HerocVisitor import HerocVisitor


# from Node import Node


class TreeVisitor(HerocVisitor):
    def visitSourcefile(self, ctx):
        print("Source file visited!")
        return self.visitChildren(ctx)

    def visitSource(self, ctx):
        print("Source is visited")
        return self.visitChildren(ctx)
