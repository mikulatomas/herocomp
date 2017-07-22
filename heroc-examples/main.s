	.file	"main.c"
	.global	main
	.text
line_of_stars:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
LOOP16:
	movq	$0, %rax
	pushq	%rax
	movq	%rdi, %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovlq	%r12, %rax
	pushq	%rax
	pop	%rax
	cmpq	$0, %rax
	movq	$0, %rax
	movq	$1, %r12
	cmove	%r12, %rax
	cmpq	$0, %rax
	je	LOOP16_END
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	movq	$42, %rax
	movq	%rax, %rdi
	call	print_char
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
LOOP16_NEXT:
	movq	%rdi, %rax
	pushq	%rax
	decq	%rax
	movq	%rax, %rdi
	popq	%rax
	jmp	LOOP16
LOOP16_END:
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	call	print_nl
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	leave	
	ret	
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	movq	$2, %rax
	movq	%rax, %r15
	movq	%r15, -8(%rbp)
	push	%rdi
	push	%rsi
	push	%rdx
	push	%rcx
	push	%r8
	push	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	call	line_of_stars
	pop	%r9
	pop	%r8
	pop	%rcx
	pop	%rdx
	pop	%rsi
	pop	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

