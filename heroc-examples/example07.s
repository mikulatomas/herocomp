	.file	"example07.heroc"
	.global	main
	.text
line_of_stars:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	subq	$16, %rsp
LOOP18:
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

	movq	$0, %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovleq	%r12, %rax
	pushq	%rax

	popq	%rax
	cmpq	$0, %rax
	je	IF12_ELSE
	jmp	LOOP18_END
	jmp	IF12_END
IF12_ELSE:
IF12_END:
LOOP18_NEXT:
	movq	-8(%rbp), %rax
	pushq	%rax
	decq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax
	jmp	LOOP18
LOOP18_END:
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
	subq	$8, %rsp
	movq	$1, %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
LOOP43:
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9

	movq	-8(%rbp), %rax
	pushq	%rax


	movq	$10, %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %rdi
	call	line_of_stars
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	movq	-8(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax

	movq	$10, %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovg	%r12, %rax
	pushq	%rax

	popq	%rax
	cmpq	$0, %rax
	je	IF37_ELSE
	jmp	LOOP43_END
	jmp	IF37_END
IF37_ELSE:
IF37_END:
	jmp	LOOP43
LOOP43_END:
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

