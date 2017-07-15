from enum import Enum


class Registers(Enum):
    RBP = '%rbp'
    RSP = '%rsp'

    def __str__(self):
        return self.value
