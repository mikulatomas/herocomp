from enum import Enum


class Registers(Enum):
    RAX = "%rax"
    EAX = "%eax"
    ECX = "%ecx"
    RBX = "%rbx"
    RCX = "%rcx"
    RDX = "%rdx"
    EDX = "%edx"
    RSI = "%rsi"
    RDI = "%rdi"
    RBP = "%rbp"
    RSP = "%rsp"
    RIP = "%rip"
    R8 = "%r8"
    R9 = "%r9"
    R10 = "%r10"
    R11 = "%r11"
    R11B = "%r11b"
    R12 = "%r12"
    R13 = "%r13"
    R14 = "%r14"
    R15 = "%r15"
    CL = "%cl"

    def __str__(self):
        return self.value

    def dereference(self):
        return "(" + self.value  + ")"
