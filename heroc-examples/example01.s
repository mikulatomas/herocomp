    .global main

    .text
main:
    // movq    $72, %rdi
    movq    $72, %rax
    pushq   %rax
    call    print_char
    // call    print_nl
    ret
    
