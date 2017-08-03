	.file	"example21.heroc"
	.global	main
	.text
fill_array:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	%rdx, -24(%rbp)
	subq	$32, %rsp
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, -32(%rbp)
LOOP24:
	movq	-24(%rbp), %rax
	pushq	%rax
	movq	-32(%rbp), %rax
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
	je	LOOP24_END
	movq	-32(%rbp), %rax
	pushq	%rax
	movq	-16(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11
	popq	%rax
	movq	%rax, %r12
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-32(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	%r10, %rax
	movq	%r12, (%rax)
LOOP24_NEXT:
	movq	-32(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -32(%rbp)
	popq	%rax
	jmp	LOOP24
LOOP24_END:
	leave	
	ret	
print_comma:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$0, %rsp
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
	leave	
	ret	
print_array:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$24, %rsp
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)
LOOP60:
	movq	-16(%rbp), %rax
	pushq	%rax
	movq	-24(%rbp), %rax
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
	je	LOOP60_END
	movq	-24(%rbp), %rax
	cmpq	$0, %rax
	je	IF50_ELSE
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	call	print_comma
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	IF50_END
IF50_ELSE:
IF50_END:
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-24(%rbp), %rax
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
LOOP60_NEXT:
	movq	-24(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -24(%rbp)
	popq	%rax
	jmp	LOOP60
LOOP60_END:
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
	subq	$360, %rsp
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
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
	movq	$0, -104(%rbp)
	movq	$0, -112(%rbp)
	movq	$0, -120(%rbp)
	movq	$0, -128(%rbp)
	movq	$0, -136(%rbp)
	movq	$0, -144(%rbp)
	movq	$0, -152(%rbp)
	movq	$0, -160(%rbp)
	movq	$0, -168(%rbp)
	movq	$0, -176(%rbp)
	movq	$0, -184(%rbp)
	movq	$0, -192(%rbp)
	movq	$0, -200(%rbp)
	movq	$0, -208(%rbp)
	movq	$0, -216(%rbp)
	movq	$0, -224(%rbp)
	movq	$0, -232(%rbp)
	movq	$0, -240(%rbp)
	movq	$0, -248(%rbp)
	movq	$0, -256(%rbp)
	leaq	-256(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -96(%rbp)
	movq	$2, %rax
	movq	%rax, -272(%rbp)
	movq	$4, %rax
	movq	%rax, -280(%rbp)
	movq	$6, %rax
	movq	%rax, -288(%rbp)
	movq	$8, %rax
	movq	%rax, -296(%rbp)
	movq	$9, %rax
	movq	%rax, -304(%rbp)
	movq	$7, %rax
	movq	%rax, -312(%rbp)
	movq	$5, %rax
	movq	%rax, -320(%rbp)
	movq	$3, %rax
	movq	%rax, -328(%rbp)
	movq	$1, %rax
	movq	%rax, -336(%rbp)
	leaq	-336(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -264(%rbp)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	movq	$666, %rax
	movq	%rax, %rsi
	movq	$10, %rax
	movq	%rax, %rdx
	call	fill_array
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
	movq	-96(%rbp), %rax
	movq	%rax, %rdi
	movq	$10, %rax
	movq	%rax, %rsi
	movq	$10, %rax
	movq	%rax, %rdx
	call	fill_array
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
	movq	$10, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11
	movq	-96(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11
	popq	%rax
	movq	%rax, %rdi
	movq	$90, %rax
	movq	%rax, %rsi
	movq	$10, %rax
	movq	%rax, %rdx
	call	fill_array
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
	movq	$10, %rax
	movq	%rax, %rsi
	call	print_array
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
	movq	-96(%rbp), %rax
	movq	%rax, %rdi
	movq	$20, %rax
	movq	%rax, %rsi
	call	print_array
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
	movq	-264(%rbp), %rax
	movq	%rax, %rdi
	movq	$9, %rax
	movq	%rax, %rsi
	call	print_array
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

