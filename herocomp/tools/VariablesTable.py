
class VariablesTable():
    def __init__(self):
        self.table = {}

    def add_variable(self, identifier, offset):
        if not self.check_variable(identifier):
            self.table[identifier] = offset
        else:
            error_string = "Variable with name {0} already exists in this scope!".format(identifier)
            raise ValueError(error_string)

    def check_variable(self, identifier):
        return identifier in self.table.keys()

    def get_variable_offset(self, identifier):
        if self.check_variable(identifier):
            return self.table.get(identifier)
        else:
            error_string = "Variable with name {0} is not in this scope!".format(identifier)
            raise ValueError(error_string)
