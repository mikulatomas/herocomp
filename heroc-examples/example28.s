	.file	"example28.heroc"
	.global	main
	.text
print_array:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$24, %rsp
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)
LOOP30:
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
	je	LOOP30_END
	movq	-24(%rbp), %rax
	cmpq	$0, %rax
	je	IF16_ELSE
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
	jmp	IF16_END
IF16_ELSE:
IF16_END:
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
LOOP30_NEXT:
	movq	-24(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -24(%rbp)
	popq	%rax
	jmp	LOOP30
LOOP30_END:
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
swap:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	%rdx, -24(%rbp)
	subq	$32, %rsp
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-16(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	movq	%rax, %r12
	movq	%r12, -32(%rbp)
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-24(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	movq	%rax, %r12
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-16(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	%r10, %rax
	movq	%r12, (%rax)
	movq	-32(%rbp), %rax
	movq	%rax, %r12
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-24(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	%r10, %rax
	movq	%r12, (%rax)
	leave	
	ret	
partition:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	%rdx, -24(%rbp)
	subq	$48, %rsp
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-24(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
	movq	%rax, %r12
	movq	%r12, -40(%rbp)
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
	movq	%r12, -48(%rbp)
	movq	-16(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -32(%rbp)
LOOP102:
	movq	$1, %rax
	pushq	%rax
	movq	-24(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11
	movq	-32(%rbp), %rax
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
	je	LOOP102_END
	movq	-40(%rbp), %rax
	pushq	%rax
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-32(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	(%r10), %rax
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
	je	IF88_ELSE
	movq	-48(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -48(%rbp)
	popq	%rax
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	movq	-48(%rbp), %rax
	movq	%rax, %rsi
	movq	-32(%rbp), %rax
	movq	%rax, %rdx
	call	swap
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	IF88_END
IF88_ELSE:
IF88_END:
LOOP102_NEXT:
	movq	-32(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -32(%rbp)
	popq	%rax
	jmp	LOOP102
LOOP102_END:
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	movq	$1, %rax
	pushq	%rax
	movq	-48(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11
	popq	%rax
	movq	%rax, %rsi
	movq	-24(%rbp), %rax
	movq	%rax, %rdx
	call	swap
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	movq	$1, %rax
	pushq	%rax
	movq	-48(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11
	popq	%rax
	leave	
	ret	
quick_sort_rec:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	%rdx, -24(%rbp)
	subq	$32, %rsp
	movq	-24(%rbp), %rax
	pushq	%rax
	movq	-16(%rbp), %rax
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
	je	IF120_ELSE
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
	movq	-24(%rbp), %rax
	movq	%rax, %rdx
	call	partition
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	movq	%rax, %r12
	movq	%r12, -32(%rbp)
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
	movq	$1, %rax
	pushq	%rax
	movq	-32(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11
	popq	%rax
	movq	%rax, %rdx
	call	quick_sort_rec
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
	movq	$1, %rax
	pushq	%rax
	movq	-32(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11
	popq	%rax
	movq	%rax, %rsi
	movq	-24(%rbp), %rax
	movq	%rax, %rdx
	call	quick_sort_rec
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	IF120_END
IF120_ELSE:
IF120_END:
	leave	
	ret	
quick_sort:
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
	movq	$0, %rax
	movq	%rax, %rsi
	movq	$1, %rax
	pushq	%rax
	movq	-16(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	subq	%r10, %r11
	pushq	%r11
	popq	%rax
	movq	%rax, %rdx
	call	quick_sort_rec
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
	subq	$408, %rsp
	movq	$5, %rax
	movq	%rax, -16(%rbp)
	movq	$3, %rax
	movq	%rax, -24(%rbp)
	movq	$2, %rax
	movq	%rax, -32(%rbp)
	movq	$9, %rax
	movq	%rax, -40(%rbp)
	movq	$8, %rax
	movq	%rax, -48(%rbp)
	movq	$4, %rax
	movq	%rax, -56(%rbp)
	movq	$6, %rax
	movq	%rax, -64(%rbp)
	movq	$3, %rax
	movq	%rax, -72(%rbp)
	movq	$2, %rax
	movq	%rax, -80(%rbp)
	movq	$3, %rax
	movq	%rax, -88(%rbp)
	movq	$4, %rax
	movq	%rax, -96(%rbp)
	movq	$3, %rax
	movq	%rax, -104(%rbp)
	movq	$9, %rax
	movq	%rax, -112(%rbp)
	movq	$8, %rax
	movq	%rax, -120(%rbp)
	movq	$2, %rax
	movq	%rax, -128(%rbp)
	movq	$5, %rax
	movq	%rax, -136(%rbp)
	movq	$1, %rax
	movq	%rax, -144(%rbp)
	movq	$2, %rax
	movq	%rax, -152(%rbp)
	movq	$4, %rax
	movq	%rax, -160(%rbp)
	movq	$8, %rax
	movq	%rax, -168(%rbp)
	leaq	-168(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
	movq	$4, %rax
	movq	%rax, -184(%rbp)
	movq	$2, %rax
	movq	%rax, -192(%rbp)
	movq	$1, %rax
	movq	%rax, -200(%rbp)
	movq	$4, %rax
	movq	%rax, -208(%rbp)
	movq	$3, %rax
	movq	%rax, -216(%rbp)
	movq	$0, %rax
	movq	%rax, -224(%rbp)
	movq	$4, %rax
	movq	%rax, -232(%rbp)
	movq	$2, %rax
	movq	%rax, -240(%rbp)
	movq	$1, %rax
	movq	%rax, -248(%rbp)
	movq	$3, %rax
	movq	%rax, -256(%rbp)
	movq	$3, %rax
	movq	%rax, -264(%rbp)
	movq	$2, %rax
	movq	%rax, -272(%rbp)
	movq	$4, %rax
	movq	%rax, -280(%rbp)
	movq	$3, %rax
	movq	%rax, -288(%rbp)
	movq	$4, %rax
	movq	%rax, -296(%rbp)
	leaq	-296(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -176(%rbp)
	movq	$0, %rax
	movq	%rax, -312(%rbp)
	movq	$1, %rax
	movq	%rax, -320(%rbp)
	movq	$2, %rax
	movq	%rax, -328(%rbp)
	movq	$3, %rax
	movq	%rax, -336(%rbp)
	movq	$4, %rax
	movq	%rax, -344(%rbp)
	movq	$5, %rax
	movq	%rax, -352(%rbp)
	movq	$6, %rax
	movq	%rax, -360(%rbp)
	movq	$7, %rax
	movq	%rax, -368(%rbp)
	movq	$8, %rax
	movq	%rax, -376(%rbp)
	movq	$9, %rax
	movq	%rax, -384(%rbp)
	leaq	-384(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -304(%rbp)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	movq	$20, %rax
	movq	%rax, %rsi
	call	quick_sort
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
	movq	-176(%rbp), %rax
	movq	%rax, %rdi
	movq	$15, %rax
	movq	%rax, %rsi
	call	quick_sort
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
	movq	-176(%rbp), %rax
	movq	%rax, %rdi
	movq	$15, %rax
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
	movq	-304(%rbp), %rax
	movq	%rax, %rdi
	movq	$10, %rax
	movq	%rax, %rsi
	call	quick_sort
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
	movq	-304(%rbp), %rax
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
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

