	.file	"main.c"
	.global	main
	.text
main:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	$1, -8(%rbp)
	movq	$1, -16(%rbp)
	leave
	ret
	.ident	"HEROCOMP - Tomas Mikula 2017"
