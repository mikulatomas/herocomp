	.file	"main.c"
	.global	main
	.text
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	movq	$4, %rax
	movq	%rax, %r15
	movq	%r15, -8(%rbp)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$5, %rax
	pushq	%rax
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	$6, %rax
	pushq	%rax
	popq	%r10
	popq	%r11
	pushq	%rdx
	pushq	%rcx
	movq	%r11, %rcx
	movq	%r10, %rdx
	sall	%cl, %edx
	movl	%edx, %eax
	cltq
	popq	%rcx
	popq	%rdx
	pushq	%rax
	popq	%r10
	popq	%r11
	cmpq	$0, %r10
	movq	$0, %r12
	cmove	%r12, %r10
	cmpq	$0, %r11
	movq	$0, %r12
	cmove	%r12, %r11
	orq	%r10, %r11
	pushq	%r11
	popq	%rax
	movq	%rax, %rdi
	call	print_char
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave
	ret
	.ident	"HEROCOMP - Tomas Mikula 2017"

