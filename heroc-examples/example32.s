	.file	"example32.heroc"
	.global	main
	.text
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$8, %rsp
	movq	$10, %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	cmpq	$0, %rax
	je	TERNARY8_ELSE
	movq	$20, %rax
	jmp	TERNARY8_END
TERNARY8_ELSE:
	movq	$30, %rax
TERNARY8_END:
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
	je	TERNARY16_ELSE
	movq	$20, %rax
	jmp	TERNARY16_END
TERNARY16_ELSE:
	movq	$30, %rax
TERNARY16_END:
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
	cmpq	$0, %rax
	je	TERNARY28_ELSE
	movq	$20, %rax
	jmp	TERNARY28_END
TERNARY28_ELSE:
	movq	$30, %rax
TERNARY28_END:
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
	cmpq	$0, %rax
	je	TERNARY39_ELSE
	movq	$20, %rax
	jmp	TERNARY39_END
TERNARY39_ELSE:
	movq	$30, %rax
TERNARY39_END:
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
	je	TERNARY36_ELSE
	movq	$40, %rax
	jmp	TERNARY36_END
TERNARY36_ELSE:
	movq	$50, %rax
TERNARY36_END:
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
	je	TERNARY49_ELSE
	movq	$20, %rax
	jmp	TERNARY49_END
TERNARY49_ELSE:
	movq	$30, %rax
	cmpq	$0, %rax
	je	TERNARY54_ELSE
	movq	$40, %rax
	jmp	TERNARY54_END
TERNARY54_ELSE:
	movq	$50, %rax
TERNARY54_END:
TERNARY49_END:
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
	movq	-8(%rbp), %rax
	pushq	%rax
	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovne	%r12, %rax
	pushq	%rax
	popq	%rax
	cmpq	$0, %rax
	je	TERNARY62_ELSE
	movq	$20, %rax
	jmp	TERNARY62_END
TERNARY62_ELSE:
	movq	$30, %rax
	cmpq	$0, %rax
	je	TERNARY67_ELSE
	movq	$40, %rax
	jmp	TERNARY67_END
TERNARY67_ELSE:
	movq	$50, %rax
TERNARY67_END:
TERNARY62_END:
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

