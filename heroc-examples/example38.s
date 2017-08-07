	.file	"example38.heroc"
	.global	main
	.text
fubar:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$88, %rsp
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
LOOP41:

	movq	$4, %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovlq	%r12, %rax
	pushq	%rax

	popq	%rax
	cmpq	$0, %rax
	je	LOOP41_END
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$40, %rax
	movq	%rax, -16(%rbp)
	movq	$30, %rax
	movq	%rax, -24(%rbp)
	movq	$20, %rax
	movq	%rax, -32(%rbp)
	movq	$10, %rax
	movq	%rax, -40(%rbp)
	leaq	-40(%rbp), %rax
	pushq	%rax
	movq	-8(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
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

	movq	$8, %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11


	movq	$40, %rax
	movq	%rax, -48(%rbp)
	movq	$30, %rax
	movq	%rax, -56(%rbp)
	movq	$20, %rax
	movq	%rax, -64(%rbp)
	movq	$10, %rax
	movq	%rax, -72(%rbp)
	leaq	-72(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	(%rax), %rax
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
LOOP41_NEXT:
	movq	-8(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax
	jmp	LOOP41
LOOP41_END:
	leave	
	ret	
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$0, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	subq	$112, %rsp
	movq	$33, %rax
	movq	%rax, -8(%rbp)
	movq	$100, %rax
	movq	%rax, -16(%rbp)
	movq	$108, %rax
	movq	%rax, -24(%rbp)
	movq	$114, %rax
	movq	%rax, -32(%rbp)
	movq	$111, %rax
	movq	%rax, -40(%rbp)
	movq	$87, %rax
	movq	%rax, -48(%rbp)
	movq	$32, %rax
	movq	%rax, -56(%rbp)
	movq	$44, %rax
	movq	%rax, -64(%rbp)
	movq	$111, %rax
	movq	%rax, -72(%rbp)
	movq	$108, %rax
	movq	%rax, -80(%rbp)
	movq	$108, %rax
	movq	%rax, -88(%rbp)
	movq	$101, %rax
	movq	%rax, -96(%rbp)
	movq	$72, %rax
	movq	%rax, -104(%rbp)
	leaq	-104(%rbp), %rax
	pushq	%rax
	movq	$0, %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	movq	%rax, %rdi
	call	print_char
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
	call	fubar
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

