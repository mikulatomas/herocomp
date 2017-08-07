	.file	"example39.heroc"
	.global	main
	.data
pc:
	.quad	0
sp:
	.quad	0
prgm:
	.quad	0
	.comm stack,524288,32
	.text
print_stack:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$91, %rax
	movq	%rax, %rdi
	call	print_char
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
LOOP44:

	movq	sp(%rip), %rax
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
	je	LOOP44_END

	movq	$0, %rax
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
	je	IF28_ELSE
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$44, %rax
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
	movq	$32, %rax
	movq	%rax, %rdi
	call	print_char
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	IF28_END
IF28_ELSE:
IF28_END:
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	%rax, %rdi
	call	print_long
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
LOOP44_NEXT:
	movq	-8(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -8(%rbp)
	popq	%rax
	jmp	LOOP44
LOOP44_END:
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
push1:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	subq	$8, %rsp
	movq	-8(%rbp), %rax
	movq	%rax, %r12
	movq	sp(%rip), %rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	%r12, (%rdx,%rax)
	movq	sp(%rip), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, sp(%rip)
	popq	%rax
	leave	
	ret	
pop1:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	subq	$8, %rsp
	leave	
	ret	
jrz1:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	subq	$8, %rsp
	movq	sp(%rip), %rax
	pushq	%rax
	decq	%rax
	movq	%rax, sp(%rip)
	popq	%rax

	movq	$0, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	(%rdx,%rax), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmove	%r12, %rax
	pushq	%rax

	popq	%rax
	cmpq	$0, %rax
	je	IF68_ELSE

	movq	-8(%rbp), %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, pc(%rip)
	jmp	IF68_END
IF68_ELSE:
IF68_END:
	leave	
	ret	
add2:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$16, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9

	movq	-16(%rbp), %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %rdi
	call	push1
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
mul2:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$16, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9

	movq	-16(%rbp), %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %rdi
	call	push1
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
leq2:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$16, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9

	movq	-8(%rbp), %rax
	pushq	%rax


	movq	-16(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovleq	%r12, %rax
	pushq	%rax

	popq	%rax
	movq	%rax, %rdi
	call	push1
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
dup1:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	subq	$8, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	push1
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
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	push1
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
swap2:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$16, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	push1
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
	call	push1
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
rot3:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	%rdx, -24(%rbp)
	subq	$24, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	push1
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
	call	push1
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
	call	push1
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
eval:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$56, %rsp
LOOP149:
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	call	print_stack
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	movq	prgm(%rip), %rax
	pushq	%rax
	movq	pc(%rip), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)

	movq	$1, %rax
	negq	%rax
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

	popq	%rax
	cmpq	$0, %rax
	je	IF158_ELSE

	movq	$3, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, pc(%rip)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	prgm(%rip), %rax
	pushq	%rax

	movq	$1, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	movq	%rax, %rdi
	movq	prgm(%rip), %rax
	pushq	%rax

	movq	$2, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	call	*%rax
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	LOOP149
	jmp	IF158_END
IF158_ELSE:
IF158_END:

	movq	$1, %rax
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

	popq	%rax
	cmpq	$0, %rax
	je	IF179_ELSE

	movq	$1, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	%rax, %r12
	movq	%r12, -16(%rbp)

	movq	$2, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, pc(%rip)

	movq	$1, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, sp(%rip)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-16(%rbp), %rax
	movq	%rax, %rdi
	movq	prgm(%rip), %rax
	pushq	%rax

	movq	$1, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	call	*%rax
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	LOOP149
	jmp	IF179_END
IF179_ELSE:
IF179_END:

	movq	$2, %rax
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

	popq	%rax
	cmpq	$0, %rax
	je	IF206_ELSE

	movq	$1, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)

	movq	$2, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	%rax, %r12
	movq	%r12, -32(%rbp)

	movq	$2, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, pc(%rip)

	movq	$2, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, sp(%rip)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-24(%rbp), %rax
	movq	%rax, %rdi
	movq	-32(%rbp), %rax
	movq	%rax, %rsi
	movq	prgm(%rip), %rax
	pushq	%rax

	movq	$1, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	call	*%rax
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	LOOP149
	jmp	IF206_END
IF206_ELSE:
IF206_END:

	movq	$3, %rax
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

	popq	%rax
	cmpq	$0, %rax
	je	IF242_ELSE

	movq	$1, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	%rax, %r12
	movq	%r12, -40(%rbp)

	movq	$2, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	%rax, %r12
	movq	%r12, -48(%rbp)

	movq	$3, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	leaq	(,%rax,8), %rdx
	leaq	stack(%rip), %rax
	movq	(%rdx,%rax), %rax
	movq	%rax, %r12
	movq	%r12, -56(%rbp)

	movq	$2, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, pc(%rip)

	movq	$3, %rax
	pushq	%rax


	movq	sp(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, sp(%rip)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-40(%rbp), %rax
	movq	%rax, %rdi
	movq	-48(%rbp), %rax
	movq	%rax, %rsi
	movq	-56(%rbp), %rax
	movq	%rax, %rdx
	movq	prgm(%rip), %rax
	pushq	%rax

	movq	$1, %rax
	pushq	%rax


	movq	pc(%rip), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11

	popq	%rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	call	*%rax
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	LOOP149
	jmp	IF242_END
IF242_ELSE:
IF242_END:
	movq	-8(%rbp), %rax
	cmpq	$0, %rax
	je	LOOP149_END
	jmp	LOOP149
LOOP149_END:
	leave	
	ret	
run:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	subq	$8, %rsp
	movq	-8(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, prgm(%rip)
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, sp(%rip)
	movq	%rax, %r12
	movq	%r12, pc(%rip)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	call	eval
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
	subq	$320, %rsp
	movq	$32, %rax
	negq	%rax
	movq	%rax, -16(%rbp)
	leaq	jrz1(%rip), %rax
	movq	%rax, -24(%rbp)
	movq	$1, %rax
	negq	%rax
	movq	%rax, -32(%rbp)
	movq	$0, %rax
	movq	%rax, -40(%rbp)
	leaq	push1(%rip), %rax
	movq	%rax, -48(%rbp)
	movq	$1, %rax
	negq	%rax
	movq	%rax, -56(%rbp)
	leaq	mul2(%rip), %rax
	movq	%rax, -64(%rbp)
	movq	$2, %rax
	movq	%rax, -72(%rbp)
	leaq	rot3(%rip), %rax
	movq	%rax, -80(%rbp)
	movq	$3, %rax
	movq	%rax, -88(%rbp)
	leaq	add2(%rip), %rax
	movq	%rax, -96(%rbp)
	movq	$2, %rax
	movq	%rax, -104(%rbp)
	movq	$1, %rax
	negq	%rax
	movq	%rax, -112(%rbp)
	leaq	push1(%rip), %rax
	movq	%rax, -120(%rbp)
	movq	$1, %rax
	negq	%rax
	movq	%rax, -128(%rbp)
	leaq	dup1(%rip), %rax
	movq	%rax, -136(%rbp)
	movq	$1, %rax
	movq	%rax, -144(%rbp)
	movq	$0, %rax
	movq	%rax, -152(%rbp)
	leaq	pop1(%rip), %rax
	movq	%rax, -160(%rbp)
	movq	$1, %rax
	movq	%rax, -168(%rbp)
	movq	$3, %rax
	movq	%rax, -176(%rbp)
	leaq	jrz1(%rip), %rax
	movq	%rax, -184(%rbp)
	movq	$1, %rax
	negq	%rax
	movq	%rax, -192(%rbp)
	leaq	leq2(%rip), %rax
	movq	%rax, -200(%rbp)
	movq	$2, %rax
	movq	%rax, -208(%rbp)
	movq	$1, %rax
	movq	%rax, -216(%rbp)
	leaq	push1(%rip), %rax
	movq	%rax, -224(%rbp)
	movq	$1, %rax
	negq	%rax
	movq	%rax, -232(%rbp)
	leaq	dup1(%rip), %rax
	movq	%rax, -240(%rbp)
	movq	$1, %rax
	movq	%rax, -248(%rbp)
	leaq	swap2(%rip), %rax
	movq	%rax, -256(%rbp)
	movq	$2, %rax
	movq	%rax, -264(%rbp)
	movq	$1, %rax
	movq	%rax, -272(%rbp)
	leaq	push1(%rip), %rax
	movq	%rax, -280(%rbp)
	movq	$1, %rax
	negq	%rax
	movq	%rax, -288(%rbp)
	movq	$10, %rax
	movq	%rax, -296(%rbp)
	leaq	push1(%rip), %rax
	movq	%rax, -304(%rbp)
	movq	$1, %rax
	negq	%rax
	movq	%rax, -312(%rbp)
	leaq	-312(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	run
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

