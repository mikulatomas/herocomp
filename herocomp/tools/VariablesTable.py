from tree.nodes.types.VariableType import VariableType


class VariablesTable():
    def __init__(self):
        self.table = {}

    def add_variable(self, identifier, offset, var_type=VariableType.VARIABLE):
        if not self.check_variable(identifier):
            self.table[identifier] = [offset,var_type]
        else:
            error_string = "Variable with name {0} already exists in this scope!".format(identifier)
            raise ValueError(error_string)

    def check_variable(self, identifier):
        # print(identifier)
        # print(self.table.keys())
        # print(identifier in self.table.keys())
        # print("////")
        return identifier in self.table.keys()

    def get_variable_offset(self, identifier):
        if self.check_variable(identifier):
            return self.table.get(identifier)[0]
        else:
            error_string = "Variable with name {0} is not in this scope!".format(identifier)
            raise ValueError(error_string)

    def get_variable_type(self, identifier):
        if self.check_variable(identifier):
            return self.table.get(identifier)[1]
        else:
            error_string = "Variable with name {0} is not in this scope!".format(identifier)
            raise ValueError(error_string)
