	.file	"main.c"
	.comm	heap,24,16
	.globl	front
	.section	.data.rel.local,"aw",@progbits
	.align 8
	.type	front, @object
	.size	front, 8
front:
	.quad	heap
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
	movq	$10, heap(%rip)
	movq	$10, 8+heap(%rip)
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 6.3.0-18) 6.3.0 20170516"
	.section	.note.GNU-stack,"",@progbits
