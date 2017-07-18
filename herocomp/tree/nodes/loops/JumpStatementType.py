from enum import Enum


class JumpStatementType(Enum):
    BREAK = 'break'
    CONTINUE = 'continue'
    RETURN = 'return'

    def __str__(self):
        return 'type(' + self.value + ')'
