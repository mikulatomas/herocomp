	.file	"if.c"
	.text
	.globl	lol
	.type	lol, @function
lol:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	$101, -8(%rbp)
	cmpq	$5, -8(%rbp)
	jle	.L2
	movq	$2, -16(%rbp)
.L2:
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	lol, .-lol
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movq	$10, -8(%rbp)
	cmpq	$5, -8(%rbp)
	jle	.L4
	movq	$2, -16(%rbp)
	cmpq	$5, -16(%rbp)
	jle	.L4
	movq	$10, -16(%rbp)
	movl	$0, %eax
	call	lol
.L4:
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Debian 6.3.0-18) 6.3.0 20170516"
	.section	.note.GNU-stack,"",@progbits
