.file	"main.c"
.global	main
.text
main:
pushq	%rbp
movq	%rsp, %rbp
movq	$1, %rax
movq	%rax, %r15
movq	%r15, -8(%rbp)
movq	$10, %rax
movq	%rax, %r15
movq	%r15, -16(%rbp)
movq	-8(%rbp), %rax
movq	%rax, %r15
movq	%r15, -40(%rbp)
movq	%rax, %r15
movq	%r15, -32(%rbp)
movq	%rax, %r15
movq	%r15, -24(%rbp)
leave
ret
.ident	"HEROCOMP - Tomas Mikula 2017"
