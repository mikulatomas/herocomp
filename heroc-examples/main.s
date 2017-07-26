	.file	"main.c"
	.global	main
	.text
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	subq	$24, %rsp
	movq	$3, %rax
	movq	%rax, -16(%rbp)
	leaq	-24(%rbp), %rax
	movq	%rax, %r15
	movq	%r15, -8(%rbp)
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

