	.file	"example10.heroc"
	.global	main
	.text
line_of_stars:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$24, %rsp
	movq	-8(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)
LOOP33:

	movq	$0, %rax
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
	movq	$0, %rax
	movq	$1, %r12
	cmove	%r12, %rax
	cmpq	$0, %rax
	je	LOOP33_END

	movq	-8(%rbp), %rax
	cmpq	$0, %rax
	movq	$0, %rax
	movq	$1, %r12
	cmove	%r12, %rax
	pushq	%rax


	movq	-24(%rbp), %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmove	%r12, %rax
	pushq	%rax


	movq	-16(%rbp), %rax
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
	orq	%r10, %r11
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

	popq	%rax
	cmpq	$0, %rax
	je	IF16_ELSE
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$42, %rax
	movq	%rax, %rdi
	call	print_char
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	LOOP33_NEXT
	jmp	IF16_END
IF16_ELSE:
IF16_END:
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$32, %rax
	movq	%rax, %rdi
	call	print_char
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
LOOP33_NEXT:
	movq	-8(%rbp), %rax
	pushq	%rax
	decq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax
	jmp	LOOP33
LOOP33_END:
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
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$16, %rsp
	movq	$9, %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
	movq	$1, %rax
	movq	%rax, %r12
	movq	%r12, -16(%rbp)
LOOP47:
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	movq	-16(%rbp), %rax
	movq	%rax, %rsi
	call	line_of_stars
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, -16(%rbp)
	movq	-8(%rbp), %rax
	pushq	%rax
	decq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax

	movq	$0, %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovge	%r12, %rax
	pushq	%rax

	popq	%rax
	cmpq	$0, %rax
	je	LOOP47_END
	jmp	LOOP47
LOOP47_END:
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

