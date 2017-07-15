
###############################################################################
# iterative version of fibonacci sequence
# compile and link with: gcc -m64 -o example example.s herocio.c
###############################################################################

	.global main

	.text
main:
	movq    $20, %rcx
	movq	$0, %rax
	movq	$1, %rbx
next:
	pushq   %rax
	pushq   %rcx
	movq    %rax, %rdi
	call    print_long
	call	print_nl
	popq    %rcx
	popq    %rax
	movq    %rax, %rdx
	movq    %rbx, %rax
	addq    %rdx, %rbx
	decq    %rcx
	jnz     next
	movq	$0, %rax
	ret
