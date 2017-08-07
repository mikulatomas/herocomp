	.file	"example31.heroc"
	.global	main
	.text
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$40, %rsp
	movq	$20, %rax
	movq	%rax, %r12
	movq	%r12, -16(%rbp)
	movq	$30, %rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)
	movq	$10, %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)

	movq	$2, %rax
	pushq	%rax


	movq	-16(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)

	movq	$16, %rax
	pushq	%rax


	movq	-16(%rbp), %rax
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

	popq	%rax
	movq	%rax, %r12
	movq	%r12, -16(%rbp)

	movq	$5, %rax
	pushq	%rax


	movq	-24(%rbp), %rax
	pushq	%rax


/ : not implemented

	popq	%rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)

	movq	$1, %rax
	pushq	%rax


	movq	-16(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, -16(%rbp)
	movq	-8(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax
	movq	-16(%rbp), %rax
	decq	%rax
	movq	%rax, -16(%rbp)

	movq	-8(%rbp), %rax
	decq	%rax
	movq	%rax, -8(%rbp)
	pushq	%rax


	movq	-16(%rbp), %rax
	pushq	%rax
	decq	%rax
	movq	%rax, -16(%rbp)
	popq	%rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)

	movq	$20, %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	decq	%rax
	movq	%rax, -8(%rbp)
	pushq	%rax


	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, -32(%rbp)
	movq	-8(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax

	movq	$20, %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax
	decq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax
	pushq	%rax


	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, -40(%rbp)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	call	print_nl
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-16(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	call	print_nl
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	call	print_nl
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-32(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	call	print_nl
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-40(%rbp), %rax
	movq	%rax, %rdi
	call	print_long
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	call	print_nl
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

