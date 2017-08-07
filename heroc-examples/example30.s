	.file	"example30.heroc"
	.global	main
	.text
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

	movq	$4, %rax
	pushq	%rax


	movq	$3, %rax
	pushq	%rax


	movq	$2, %rax
	pushq	%rax


	movq	$1, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$65280, %rax
	pushq	%rax


	movq	$65535, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	andq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$678, %rax
	pushq	%rax


	movq	$12345, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$678, %rax
	pushq	%rax


	movq	$12345, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11


	movq	$891010, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$678, %rax
	pushq	%rax


	movq	$12345, %rax
	pushq	%rax


	movq	$891010, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$9, %rax
	pushq	%rax


	movq	$678, %rax
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


	movq	$12345, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11


	movq	$891010, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$9, %rax
	pushq	%rax


	movq	$678, %rax
	pushq	%rax


	movq	$12345, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11


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


	movq	$891010, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$9, %rax
	pushq	%rax


	movq	$678, %rax
	pushq	%rax


	movq	$12345, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11


	movq	$891010, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11


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

	movq	$9, %rax
	pushq	%rax


	movq	$678, %rax
	pushq	%rax


	movq	$12345, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11


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


	movq	$891010, %rax
	pushq	%rax


	movq	$10, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$9, %rax
	pushq	%rax


	movq	$678, %rax
	pushq	%rax


	movq	$12345, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11


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


	movq	$891010, %rax
	pushq	%rax


	movq	$10, %rax
	notq	%rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$9, %rax
	pushq	%rax


	movq	$678, %rax
	pushq	%rax


	movq	$12345, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	xorq	%r10, %r11
	pushq	%r11


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


	movq	$891010, %rax
	pushq	%rax


	movq	$10, %rax
	notq	%rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11


	popq	%r11
	popq	%r10
	orq	%r10, %r11
	pushq	%r11

	popq	%rax
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
	movq	$123, %rax
	notq	%rax
	notq	%rax
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

	movq	$40, %rax
	pushq	%rax


	movq	$40, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovleq	%r12, %rax
	pushq	%rax


	movq	$20, %rax
	pushq	%rax


	movq	$10, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovlq	%r12, %rax
	pushq	%rax


	popq	%r10
	popq	%r11
	cmpq	$0, %r10
	movq	$1, %r10
	movq	$0, %r12
	cmove	%r12, %r10
	cmpq	$0, %r11
	movq	$1, %r11
	movq	$0, %r12
	cmove	%r12, %r11
	andq	%r10, %r11
	pushq	%r11

	popq	%rax
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

	movq	$333, %rax
	pushq	%rax


	movq	$40, %rax
	pushq	%rax


	movq	$40, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovge	%r12, %rax
	pushq	%rax


	movq	$20, %rax
	pushq	%rax


	movq	$10, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovlq	%r12, %rax
	pushq	%rax


	popq	%r10
	popq	%r11
	cmpq	$0, %r10
	movq	$1, %r10
	movq	$0, %r12
	cmove	%r12, %r10
	cmpq	$0, %r11
	movq	$1, %r11
	movq	$0, %r12
	cmove	%r12, %r11
	andq	%r10, %r11
	pushq	%r11


	popq	%r10
	popq	%r11
	cmpq	$0, %r10
	movq	$1, %r10
	movq	$0, %r12
	cmove	%r12, %r10
	cmpq	$0, %r11
	movq	$1, %r11
	movq	$0, %r12
	cmove	%r12, %r11
	orq	%r10, %r11
	pushq	%r11


	movq	$10, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
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

