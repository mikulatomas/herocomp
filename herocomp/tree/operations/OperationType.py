from enum import Enum


class OperationType(Enum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    MODULO = '%'

    LEFT_SHIFT = '<<'
    RIGHT_SHIFT = '>>'

    LESS = '<'
    LESS_EQUAL = '<='
    GREATER = '>'
    GREATER_EQUAL = '>='

    EQUAL = '=='
    NOT_EQUAL = '!='

    AND = '&'
    OR = '|'
    XOR = '^'

    LOGICAL_AND = '&&'
    LOGICAL_OR = '||'

    LOGICAL_NOT = '!'
    REFERENCE = '*'
    DEREFERENCE = '&'
    BITWISE_NOT = '~'
    INCREMENT = '++'
    DECREMENT = '--'

    SUBSCRIPT = '[]'

    def __str__(self):
        return 'operation(' + self.value + ')'
