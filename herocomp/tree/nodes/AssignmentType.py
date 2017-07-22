from enum import Enum

from tree.nodes.operations.OperationType import OperationType


class AssignmentType(Enum):
    ASSIGN = '='

    MULTIPLY_ASSIGN = '*='
    DIV_ASSIGN = '/='
    MOD_ASSIGN = '%='

    PLUS_ASSIGN = '+='
    MINUS_ASSIGN = '-='

    LEFT_SHIFT_ASSIGN = '<<='
    RIGHT_SHIFT_ASSIGN = '>>='

    AND_ASSIGN = '&='
    OR_ASSIGN = '|='
    XOR_ASSIGN = '^='


    def __str__(self):
        return 'assignment(' + self.value + ')'

    def get_operation(self):
        if self.name == self.MULTIPLY_ASSIGN.name:
            return OperationType.MULTIPLY
        elif self.name == self.DIV_ASSIGN.name:
            return OperationType.DIVIDE
        elif self.name == self.MOD_ASSIGN.name:
            return OperationType.MODULO
        elif self.name == self.PLUS_ASSIGN.name:
            return OperationType.PLUS
        elif self.name == self.MINUS_ASSIGN.name:
            return OperationType.MINUS
        elif self.name == self.LEFT_SHIFT_ASSIGN.name:
            return OperationType.LEFT_SHIFT
        elif self.name == self.RIGHT_SHIFT_ASSIGN.name:
            return OperationType.RIGHT_SHIFT
        elif self.name == self.AND_ASSIGN.name:
            return OperationType.AND
        elif self.name == self.OR_ASSIGN.name:
            return OperationType.OR
        elif self.name == self.XOR_ASSIGN.name:
            return OperationType.XOR
