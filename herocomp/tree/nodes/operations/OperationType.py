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
    REFERENCE = '&'
    DEREFERENCE = '*'
    BITWISE_NOT = '~'
    INCREMENT = '++'
    DECREMENT = '--'

    SUBSCRIPT = '[]'

    def __str__(self):
        return 'operation(' + self.value + ')'

    def get_binary_operation_code(self):
        # Shift
        if ((self.name == self.LEFT_SHIFT.name) or
            (self.name == self.RIGHT_SHIFT.name)):
            return self._shift_code()
        # Logic
        elif ((self.name == self.OR.name) or
              (self.name == self.XOR.name)):
            return self._logic_code()
        # Arithmetic
        elif ((self.name == self.MINUS.name) or
              (self.name == self.PLUS.name)):
            return self._arithmetic_code()
        # Relational
        elif ((self.name == self.LESS.name) or
              (self.name == self.LESS_EQUAL.name) or
              (self.name == self.GREATER.name) or
              (self.name == self.GREATER_EQUAL.name) or
              (self.name == self.EQUAL.name) or
              (self.name == self.NOT_EQUAL.name)):
            return self._relational_code()
        else:
            # delete later
            return "{0} : not implemented\n".format(self.value)

    def get_unary_operation_code(self, is_postfix, operand):
        # Incremental/Decremental
        if ((self.name == self.DECREMENT.name) or
            (self.name == self.INCREMENT.name)):
            return self._incremental_or_decremental_code(is_postfix, operand)
        # Dereference *
        elif (self.name == self.DEREFERENCE.name):
            return self._dereference_code(operand)
        # Reference &
        elif (self.name == self.REFERENCE.name):
            return self._reference_code(operand)
        # Negation
        elif (self.name == self.LOGICAL_NOT.name):
            return self._negation_code(operand)
        else:
            # delete later
            return "{0} : not implemented\n".format(self.value)

    def _negation_code(self, operand):
        code = ""

        code += operand.get_code()
        code += instruction("cmpq", number_constant(0), Registers.RAX)
        code += instruction("movq", number_constant(0), Registers.RAX)
        code += instruction("movq", number_constant(1), Registers.R12)
        code += instruction("cmove", Registers.R12, Registers.RAX)

        return code

    def _reference_code(self, operand):
        code = ""

        code += instruction("leaq", operand.get_value_address(), Registers.RAX)

        return code

    def _dereference_code(self, operand):
        code = ""

        # code += "operand code\n"
        code += operand.get_code()
        # code += "////operand code\n"
        code += instruction("movq", Registers.RAX.dereference(), Registers.RAX)

        return code

    def _incremental_or_decremental_code(self, is_postfix, operand):
        code = ""

        code += operand.get_code()

        if (self.name == self.INCREMENT.name):
            operator = "incq"
        else:
            operator = "decq"

        if is_postfix:
            code += instruction("pushq", Registers.RAX)

        code += instruction(operator, Registers.RAX)
        
        # Probably only for inc/dec
        code += instruction("movq", Registers.RAX, operand.get_value_address())

        if is_postfix:
            code += instruction("popq", Registers.RAX)

        return code


    def _relational_code(self):
        code = ""

        code += instruction("popq", Registers.R11)
        code += instruction("popq", Registers.R10)
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
            operation = "subq"
        elif (self.name == self.PLUS.name):
            operation = "addq"

        code += instruction(operation, Registers.R10, Registers.R11)

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

        if self.name == self.OR.name:
            operation = "orq"
        elif self.name == self.XOR.name:
            operation = "xorq"
        elif self.name == self.AND.name:
            operation = "andq"
        code += instruction(operation, Registers.R10, Registers.R11)

        code += instruction("pushq", Registers.R11)

        return code
