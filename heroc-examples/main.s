	.file	"example04.heroc"
	.global	main
	.text
swap:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$16, %rsp
	movq	-16(%rbp), %rax
	movq	(%rax), %rax
	pushq	%rax
	movq	-8(%rbp), %rax
	movq	(%rax), %rax
	pushq	%rax
	popq	%r10
	popq	%r11
	cmpq	$0, %r10
	movq	$0, %r12
	cmove	%r12, %r10
	cmpq	$0, %r11
	movq	$0, %r12
	cmove	%r12, %r11
	xorq	%r10, %r11
	pushq	%r11
	pop	%rax
	movq	%rax, %r15
	movq	-8(%rbp), %rax
	movq	%r15, (%rax)
	movq	-8(%rbp), %rax
	movq	(%rax), %rax
	pushq	%rax
	movq	-16(%rbp), %rax
	movq	(%rax), %rax
	pushq	%rax
	popq	%r10
	popq	%r11
	cmpq	$0, %r10
	movq	$0, %r12
	cmove	%r12, %r10
	cmpq	$0, %r11
	movq	$0, %r12
	cmove	%r12, %r11
	xorq	%r10, %r11
	pushq	%r11
	pop	%rax
	movq	%rax, %r15
	movq	-16(%rbp), %rax
	movq	%r15, (%rax)
	movq	-16(%rbp), %rax
	movq	(%rax), %rax
	pushq	%rax
	movq	-8(%rbp), %rax
	movq	(%rax), %rax
	pushq	%rax
	popq	%r10
	popq	%r11
	cmpq	$0, %r10
	movq	$0, %r12
	cmove	%r12, %r10
	cmpq	$0, %r11
	movq	$0, %r12
	cmove	%r12, %r11
	xorq	%r10, %r11
	pushq	%r11
	pop	%rax
	movq	%rax, %r15
	movq	-8(%rbp), %rax
	movq	%r15, (%rax)
	leave	
	ret	
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$24, %rsp
	movq	$666, %rax
	movq	%rax, %r15
	movq	%r15, -8(%rbp)
	movq	$999, %rax
	movq	%rax, %r15
	movq	%r15, -16(%rbp)
	leaq	-16(%rbp), %rax
	movq	%rax, %r15
	movq	%r15, -24(%rbp)
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	call	print_nl
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	movq	-16(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	call	print_nl
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	call	print_nl
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	leaq	-8(%rbp), %rax
	movq	%rax, %rdi
	movq	-24(%rbp), %rax
	movq	%rax, %rsi
	call	swap
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	call	print_nl
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	movq	-16(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	call	print_nl
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

