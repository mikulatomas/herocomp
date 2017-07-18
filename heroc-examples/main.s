	.file	"main.c"
	.global	main
	.text
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	movq	$120, %rax
	movq	%rax, %r15
	movq	%r15, -8(%rbp)
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	movq	$1, %rax
	pushq	%rax
	movq	-8(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11
	pop	%rax
	movq	%rax, %rdi
	movq	$2, %rax
	pushq	%rax
	movq	-8(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11
	pop	%rax
	movq	%rax, %rsi
	call	print_two_longs
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

