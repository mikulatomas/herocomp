from enum import Enum

from asm.Asm import *
from asm.Registers import Registers


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

    def get_operation_code(self):
        # Shift
        if (self.name == self.LEFT_SHIFT.name) or (self.name == self.RIGHT_SHIFT.name):
            return self._shift_code()
        # Logic
        elif (self.name == self.OR.name):
            return self._logic_code()

    def _shift_code(self):
        code = ""

        code += pop(Registers.R10)
        code += pop(Registers.R11)
        code += push(Registers.RDX)
        code += push(Registers.RCX)

        code += movq(Registers.R11, Registers.RCX)
        code += movq(Registers.R10, Registers.RDX)

        if self.name == self.LEFT_SHIFT.name:
            code += sall(Registers.CL, Registers.EDX)
        elif self.name == self.RIGHT_SHIFT.name:
            code += sarl(Registers.CL, Registers.EDX)

        code += movl(Registers.EDX, Registers.EAX)

        # Promote to 64bit
        code += cltq()

        code += pop(Registers.RCX)
        code += pop(Registers.RDX)
        code += push(Registers.RAX)

        return code

    def _logic_code(self):
        code = ""

        code += pop(Registers.R10)
        code += pop(Registers.R11)

        code += cmp("$0", Registers.R10)
        # code += movq("$1", Registers.R10)
        code += movq("$0", Registers.R12)
        code += cmove(Registers.R12, Registers.R10)

        code += cmp("$0", Registers.R11)
        # code += cmp("$1", Registers.R11)
        code += movq("$0", Registers.R12)
        code += cmove(Registers.R12, Registers.R11)

        code += orq(Registers.R10, Registers.R11)

        code += push(Registers.R11)

        return code
