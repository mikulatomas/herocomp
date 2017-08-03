	.file	"example29.heroc"
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
	movq	$30, %rax
	pushq	%rax
	movq	$20, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
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
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$30, %rax
	pushq	%rax
	movq	$20, %rax
	pushq	%rax
	movq	$10, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11
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
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$7, %rax
	pushq	%rax
	movq	$6, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11
	movq	$5, %rax
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
	movq	$7, %rax
	pushq	%rax
	movq	$6, %rax
	pushq	%rax
	movq	$5, %rax
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
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$2, %rax
	pushq	%rax
	movq	$6, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11
	movq	$50000, %rax
	pushq	%rax
	popq	%r10
	popq	%r11
	pushq	%rdx
	pushq	%rcx
	movq	%r11, %rcx
	movq	%r10, %rdx
	sarl	%cl, %edx
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
	movq	$2, %rax
	pushq	%rax
	movq	$6, %rax
	pushq	%rax
	movq	$50000, %rax
	pushq	%rax
	popq	%r10
	popq	%r11
	pushq	%rdx
	pushq	%rcx
	movq	%r11, %rcx
	movq	%r10, %rdx
	sarl	%cl, %edx
	movl	%edx, %eax
	cltq	
	popq	%rcx
	popq	%rdx
	pushq	%rax
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
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
	movq	$1, %rax
	pushq	%rax
	movq	$3, %rax
	pushq	%rax
	movq	$10, %rax
	pushq	%rax
	popq	%rax
	popq	%r10
	pushq	%rdx
	cdq	
	idiv	%r10
	popq	%rax
	pushq	%rdx
	movq	%rax, %rdx
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
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	$10, %rax
	pushq	%rax
	movq	$3, %rax
	pushq	%rax
	movq	$10, %rax
	pushq	%rax
	popq	%rax
	popq	%r10
	pushq	%rdx
	cdq	
	idiv	%r10
	popq	%rax
	pushq	%rdx
	movq	%rax, %rdx
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
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
	movq	$3, %rax
	pushq	%rax
	movq	$10, %rax
	pushq	%rax
	movq	$10, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11
	popq	%rax
	popq	%r10
	pushq	%rdx
	cdq	
	idiv	%r10
	popq	%rax
	pushq	%rdx
	movq	%rax, %rdx
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
	movq	$10, %rax
	pushq	%rax
	movq	$10, %rax
	pushq	%rax
	movq	$66, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11
	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmove	%r12, %rax
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
	movq	$10, %rax
	pushq	%rax
	movq	$10, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmove	%r12, %rax
	pushq	%rax
	movq	$66, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	imulq	%r10, %r11
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

