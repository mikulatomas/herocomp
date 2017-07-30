	.file	"main.c"
	.global	main
	.text
print_string:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$24, %rsp
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)
LOOP21:
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
	je	LOOP21_END
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
	call	print_char
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
LOOP21_NEXT:
	movq	-24(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -24(%rbp)
	popq	%rax
	jmp	LOOP21
LOOP21_END:
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
	subq	$0, %rsp
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	subq	$416, %rsp
	movq	$114, %rax
	movq	%rax, -8(%rbp)
	movq	$97, %rax
	movq	%rax, -16(%rbp)
	movq	$98, %rax
	movq	%rax, -24(%rbp)
	movq	$117, %rax
	movq	%rax, -32(%rbp)
	movq	$70, %rax
	movq	%rax, -40(%rbp)
	movq	$32, %rax
	movq	%rax, -48(%rbp)
	movq	$44, %rax
	movq	%rax, -56(%rbp)
	movq	$101, %rax
	movq	%rax, -64(%rbp)
	movq	$104, %rax
	movq	%rax, -72(%rbp)
	movq	$101, %rax
	movq	%rax, -80(%rbp)
	movq	$104, %rax
	movq	%rax, -88(%rbp)
	movq	$117, %rax
	movq	%rax, -96(%rbp)
	movq	$77, %rax
	movq	%rax, -104(%rbp)
	movq	$40, %rax
	movq	%rax, -112(%rbp)
	movq	$32, %rax
	movq	%rax, -120(%rbp)
	movq	$103, %rax
	movq	%rax, -128(%rbp)
	movq	$110, %rax
	movq	%rax, -136(%rbp)
	movq	$105, %rax
	movq	%rax, -144(%rbp)
	movq	$114, %rax
	movq	%rax, -152(%rbp)
	movq	$116, %rax
	movq	%rax, -160(%rbp)
	movq	$115, %rax
	movq	%rax, -168(%rbp)
	movq	$95, %rax
	movq	%rax, -176(%rbp)
	movq	$116, %rax
	movq	%rax, -184(%rbp)
	movq	$110, %rax
	movq	%rax, -192(%rbp)
	movq	$105, %rax
	movq	%rax, -200(%rbp)
	movq	$114, %rax
	movq	%rax, -208(%rbp)
	movq	$112, %rax
	movq	%rax, -216(%rbp)
	movq	$32, %rax
	movq	%rax, -224(%rbp)
	movq	$32, %rax
	movq	%rax, -232(%rbp)
	movq	$32, %rax
	movq	%rax, -240(%rbp)
	movq	$32, %rax
	movq	%rax, -248(%rbp)
	movq	$10, %rax
	movq	%rax, -256(%rbp)
	movq	$59, %rax
	movq	%rax, -264(%rbp)
	movq	$41, %rax
	movq	%rax, -272(%rbp)
	movq	$51, %rax
	movq	%rax, -280(%rbp)
	movq	$49, %rax
	movq	%rax, -288(%rbp)
	movq	$32, %rax
	movq	%rax, -296(%rbp)
	movq	$44, %rax
	movq	%rax, -304(%rbp)
	movq	$33, %rax
	movq	%rax, -312(%rbp)
	movq	$100, %rax
	movq	%rax, -320(%rbp)
	movq	$108, %rax
	movq	%rax, -328(%rbp)
	movq	$114, %rax
	movq	%rax, -336(%rbp)
	movq	$111, %rax
	movq	%rax, -344(%rbp)
	movq	$87, %rax
	movq	%rax, -352(%rbp)
	movq	$32, %rax
	movq	%rax, -360(%rbp)
	movq	$44, %rax
	movq	%rax, -368(%rbp)
	movq	$111, %rax
	movq	%rax, -376(%rbp)
	movq	$108, %rax
	movq	%rax, -384(%rbp)
	movq	$108, %rax
	movq	%rax, -392(%rbp)
	movq	$101, %rax
	movq	%rax, -400(%rbp)
	movq	$72, %rax
	movq	%rax, -408(%rbp)
	leaq	-408(%rbp), %rax
	movq	%rax, %rdi
	movq	$13, %rax
	movq	%rax, %rsi
	call	print_string
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

