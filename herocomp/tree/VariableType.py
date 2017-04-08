from enum import Enum


class VariableType(Enum):
    VARIABLE = 'variable'
    POINTER = 'pointer'
    ARRAY = 'array'

    def __str__(self):
        return 'type(' + self.value + ')'
