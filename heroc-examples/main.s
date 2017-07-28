	.file	"main.c"
	.global	main
	.text
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	subq	$88, %rsp
	movq	$0, -16(%rbp)
	movq	$0, -24(%rbp)
	movq	$0, -32(%rbp)
	movq	$0, -40(%rbp)
	movq	$0, -48(%rbp)
	movq	$0, -56(%rbp)
	movq	$0, -64(%rbp)
	movq	$0, -72(%rbp)
	movq	$0, -80(%rbp)
	movq	$0, -88(%rbp)
	leaq	-88(%rbp), %rax
	movq	%rax, %r15
	movq	%r15, -8(%rbp)
	movq	$8, %rax
	movq	%rax, %r15
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	$0, %rax
	popq	%r12
	imulq	$8, %rax
	addq	%rax, %r12
	movq	%r12, %rax
	movq	%r15, (%rax)
	movq	$9, %rax
	movq	%rax, %r15
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	$1, %rax
	popq	%r12
	imulq	$8, %rax
	addq	%rax, %r12
	movq	%r12, %rax
	movq	%r15, (%rax)
	movq	$10, %rax
	movq	%rax, %r15
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	$2, %rax
	popq	%r12
	imulq	$8, %rax
	addq	%rax, %r12
	movq	%r12, %rax
	movq	%r15, (%rax)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	$2, %rax
	popq	%r12
	imulq	$8, %rax
	addq	%rax, %r12
	movq	(%r12), %rax
	movq	%rax, %rdi
	call	print_long
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

