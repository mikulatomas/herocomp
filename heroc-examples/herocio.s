	.file	"herocio.c"
	.section	.rodata
.LC0:
	.string	"%li"
	.text
	.globl	print_long
	.type	print_long, @function
print_long:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	print_long, .-print_long
	.section	.rodata
.LC1:
	.string	"Unknown character code: %li"
	.text
	.globl	print_char
	.type	print_char, @function
print_char:
.LFB1:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	%rdi, -8(%rbp)
	cmpq	$0, -8(%rbp)
	js	.L3
	cmpq	$127, -8(%rbp)
	jg	.L3
	movq	-8(%rbp), %rax
	movsbl	%al, %eax
	movl	%eax, %edi
	call	putchar@PLT
	jmp	.L4
.L3:
	movq	stderr(%rip), %rax
	movq	-8(%rbp), %rdx
	leaq	.LC1(%rip), %rsi
	movq	%rax, %rdi
	movl	$0, %eax
	call	fprintf@PLT
.L4:
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	print_char, .-print_char
	.globl	print_nl
	.type	print_nl, @function
print_nl:
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$10, %edi
	call	putchar@PLT
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	print_nl, .-print_nl
	.ident	"GCC: (Debian 6.3.0-18) 6.3.0 20170516"
	.section	.note.GNU-stack,"",@progbits
