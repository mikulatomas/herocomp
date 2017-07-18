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
        # Arithmetic
        elif (self.name == self.MINUS.name):
            return self._arithmetic_code()
        elif (self.name == self.LESS.name):
            return self._relational_code()
        else:
            # delete later
            return "not implemented\n"

    def _relational_code(self):
        code = ""

        code += instruction("pop", Registers.R11)
        code += instruction("pop", Registers.R10)
        code += instruction("cmpq", Registers.R10, Registers.R11)
        code += instruction("movq", number_constant(0), Registers.RAX)
        code += instruction("movq", number_constant(1), Registers.R12)

        if self.name == self.LESS.name:
            operation = "cmovlq"
        elif self.name == self.LESS_EQUAL.name:
            operation = "cmovleq"
        elif self.name == self.GREATER.name:
            operation = "cmovg"
        elif self.name == self.GREATER_EQUAL.name:
            operation = "cmovge"
        elif self.name == self.EQUAL.name:
            operation = "cmove"
        elif self.name == self.NOT_EQUAL.name:
            operation = "cmovne"

        code += instruction(operation, Registers.R12, Registers.RAX)

        code += instruction("pushq", Registers.RAX)

        return code

    def _arithmetic_code(self):
        code = ""

        code += instruction("popq", Registers.R11)
        code += instruction("popq", Registers.R10)

        if (self.name == self.MINUS.name):
            code += instruction("subq", Registers.R10, Registers.R11)

        code += instruction("pushq", Registers.R11)

        return code

    def _shift_code(self):
        code = ""

        code += instruction("popq", Registers.R10)
        code += instruction("popq", Registers.R11)
        code += instruction("pushq", Registers.RDX)
        code += instruction("pushq", Registers.RCX)

        code += instruction("movq", Registers.R11, Registers.RCX)
        code += instruction("movq", Registers.R10, Registers.RDX)

        if self.name == self.LEFT_SHIFT.name:
            code += instruction("sall", Registers.CL, Registers.EDX)
        elif self.name == self.RIGHT_SHIFT.name:
            code += instruction("sarl", Registers.CL, Registers.EDX)

        code += instruction("movl", Registers.EDX, Registers.EAX)

        # Promote to 64bit
        code += instruction("cltq")
        
        code += instruction("popq", Registers.RCX)
        code += instruction("popq", Registers.RDX)
        code += instruction("pushq", Registers.RAX)

        return code

    def _logic_code(self):
        code = ""

        code += instruction("popq", Registers.R10)
        code += instruction("popq", Registers.R11)

        code += instruction("cmpq", number_constant(0), Registers.R10)
        # code += movq("$1", Registers.R10)
        code += instruction("movq", number_constant(0), Registers.R12)
        code += instruction("cmove", Registers.R12, Registers.R10)

        code += instruction("cmpq", number_constant(0), Registers.R11)
        # code += cmpq("$1", Registers.R11)
        code += instruction("movq", number_constant(0), Registers.R12)
        code += instruction("cmove", Registers.R12, Registers.R11)

        code += instruction("orq", Registers.R10, Registers.R11)

        code += instruction("pushq", Registers.R11)

        return code
