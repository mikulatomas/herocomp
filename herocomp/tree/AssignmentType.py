from enum import Enum


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
