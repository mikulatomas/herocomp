	.file	"example02.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	$0, -8(%rbp)
	movq	$1, -16(%rbp)
	movq	$0, -24(%rbp)
	jmp	.L2
.L3:
	movq	-16(%rbp), %rax
	movq	%rax, -32(%rbp)
	movq	-8(%rbp), %rax
	addq	%rax, -16(%rbp)
	movq	-32(%rbp), %rax
	movq	%rax, -8(%rbp)
	addq	$1, -24(%rbp)
.L2:
	cmpq	$19, -24(%rbp)
	jle	.L3
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 6.3.0-18) 6.3.0 20170516"
	.section	.note.GNU-stack,"",@progbits
