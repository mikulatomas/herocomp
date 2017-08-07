	.file	"example40.heroc"
	.global	main
	.text
print_string:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$16, %rsp
LOOP5:
	movq	-16(%rbp), %rax
	cmpq	$0, %rax
	je	LOOP5_END
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, %rdi
	call	print_char
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi

	movq	$8, %rax
	pushq	%rax


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
	movq	-16(%rbp), %rax
	pushq	%rax
	decq	%rax
	movq	%rax, -16(%rbp)
	popq	%rax
	jmp	LOOP5
LOOP5_END:
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
copy:
	pushq	%rbp
	movq	%rsp, %rbp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	subq	$24, %rsp
	movq	-16(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -24(%rbp)
LOOP68:

	movq	$0, %rax
	pushq	%rax


	movq	-24(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	cmpq	%r10, %r11
	movq	$0, %rax
	movq	$1, %r12
	cmovge	%r12, %rax
	pushq	%rax

	popq	%rax
	cmpq	$0, %rax
	je	LOOP68_END
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
	pushq	%rax


	movq	-24(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	%r10, %rax
	movq	%r12, (%rax)
LOOP68_NEXT:
	movq	-24(%rbp), %rax
	pushq	%rax
	decq	%rax
	movq	%rax, -24(%rbp)
	popq	%rax
	jmp	LOOP68
LOOP68_END:
	leave	
	ret	
permute:
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
	cmovge	%r12, %rax
	pushq	%rax

	popq	%rax
	cmpq	$0, %rax
	je	IF75_ELSE
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	movq	-24(%rbp), %rax
	movq	%rax, %rsi
	call	print_string
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	jmp	IF75_END
IF75_ELSE:
	movq	-16(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -32(%rbp)
LOOP116:

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
	je	LOOP116_END
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
	movq	-32(%rbp), %rax
	movq	%rax, %rdx
	call	swap
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
	movq	-24(%rbp), %rax
	movq	%rax, %rsi
	call	copy
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


	movq	-24(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	imulq	%r10, %r11
	pushq	%r11


	movq	-8(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %rdi

	movq	$1, %rax
	pushq	%rax


	movq	-16(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %rsi
	movq	-24(%rbp), %rax
	movq	%rax, %rdx
	call	permute
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
LOOP116_NEXT:
	movq	-32(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -32(%rbp)
	popq	%rax
	jmp	LOOP116
LOOP116_END:
IF75_END:
	leave	
	ret	
permutations:
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
	movq	-16(%rbp), %rax
	movq	%rax, %rdx
	call	permute
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
	subq	$8216, %rsp
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
	movq	$0, -96(%rbp)
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
	movq	$0, -264(%rbp)
	movq	$0, -272(%rbp)
	movq	$0, -280(%rbp)
	movq	$0, -288(%rbp)
	movq	$0, -296(%rbp)
	movq	$0, -304(%rbp)
	movq	$0, -312(%rbp)
	movq	$0, -320(%rbp)
	movq	$0, -328(%rbp)
	movq	$0, -336(%rbp)
	movq	$0, -344(%rbp)
	movq	$0, -352(%rbp)
	movq	$0, -360(%rbp)
	movq	$0, -368(%rbp)
	movq	$0, -376(%rbp)
	movq	$0, -384(%rbp)
	movq	$0, -392(%rbp)
	movq	$0, -400(%rbp)
	movq	$0, -408(%rbp)
	movq	$0, -416(%rbp)
	movq	$0, -424(%rbp)
	movq	$0, -432(%rbp)
	movq	$0, -440(%rbp)
	movq	$0, -448(%rbp)
	movq	$0, -456(%rbp)
	movq	$0, -464(%rbp)
	movq	$0, -472(%rbp)
	movq	$0, -480(%rbp)
	movq	$0, -488(%rbp)
	movq	$0, -496(%rbp)
	movq	$0, -504(%rbp)
	movq	$0, -512(%rbp)
	movq	$0, -520(%rbp)
	movq	$0, -528(%rbp)
	movq	$0, -536(%rbp)
	movq	$0, -544(%rbp)
	movq	$0, -552(%rbp)
	movq	$0, -560(%rbp)
	movq	$0, -568(%rbp)
	movq	$0, -576(%rbp)
	movq	$0, -584(%rbp)
	movq	$0, -592(%rbp)
	movq	$0, -600(%rbp)
	movq	$0, -608(%rbp)
	movq	$0, -616(%rbp)
	movq	$0, -624(%rbp)
	movq	$0, -632(%rbp)
	movq	$0, -640(%rbp)
	movq	$0, -648(%rbp)
	movq	$0, -656(%rbp)
	movq	$0, -664(%rbp)
	movq	$0, -672(%rbp)
	movq	$0, -680(%rbp)
	movq	$0, -688(%rbp)
	movq	$0, -696(%rbp)
	movq	$0, -704(%rbp)
	movq	$0, -712(%rbp)
	movq	$0, -720(%rbp)
	movq	$0, -728(%rbp)
	movq	$0, -736(%rbp)
	movq	$0, -744(%rbp)
	movq	$0, -752(%rbp)
	movq	$0, -760(%rbp)
	movq	$0, -768(%rbp)
	movq	$0, -776(%rbp)
	movq	$0, -784(%rbp)
	movq	$0, -792(%rbp)
	movq	$0, -800(%rbp)
	movq	$0, -808(%rbp)
	movq	$0, -816(%rbp)
	movq	$0, -824(%rbp)
	movq	$0, -832(%rbp)
	movq	$0, -840(%rbp)
	movq	$0, -848(%rbp)
	movq	$0, -856(%rbp)
	movq	$0, -864(%rbp)
	movq	$0, -872(%rbp)
	movq	$0, -880(%rbp)
	movq	$0, -888(%rbp)
	movq	$0, -896(%rbp)
	movq	$0, -904(%rbp)
	movq	$0, -912(%rbp)
	movq	$0, -920(%rbp)
	movq	$0, -928(%rbp)
	movq	$0, -936(%rbp)
	movq	$0, -944(%rbp)
	movq	$0, -952(%rbp)
	movq	$0, -960(%rbp)
	movq	$0, -968(%rbp)
	movq	$0, -976(%rbp)
	movq	$0, -984(%rbp)
	movq	$0, -992(%rbp)
	movq	$0, -1000(%rbp)
	movq	$0, -1008(%rbp)
	movq	$0, -1016(%rbp)
	movq	$0, -1024(%rbp)
	movq	$0, -1032(%rbp)
	movq	$0, -1040(%rbp)
	movq	$0, -1048(%rbp)
	movq	$0, -1056(%rbp)
	movq	$0, -1064(%rbp)
	movq	$0, -1072(%rbp)
	movq	$0, -1080(%rbp)
	movq	$0, -1088(%rbp)
	movq	$0, -1096(%rbp)
	movq	$0, -1104(%rbp)
	movq	$0, -1112(%rbp)
	movq	$0, -1120(%rbp)
	movq	$0, -1128(%rbp)
	movq	$0, -1136(%rbp)
	movq	$0, -1144(%rbp)
	movq	$0, -1152(%rbp)
	movq	$0, -1160(%rbp)
	movq	$0, -1168(%rbp)
	movq	$0, -1176(%rbp)
	movq	$0, -1184(%rbp)
	movq	$0, -1192(%rbp)
	movq	$0, -1200(%rbp)
	movq	$0, -1208(%rbp)
	movq	$0, -1216(%rbp)
	movq	$0, -1224(%rbp)
	movq	$0, -1232(%rbp)
	movq	$0, -1240(%rbp)
	movq	$0, -1248(%rbp)
	movq	$0, -1256(%rbp)
	movq	$0, -1264(%rbp)
	movq	$0, -1272(%rbp)
	movq	$0, -1280(%rbp)
	movq	$0, -1288(%rbp)
	movq	$0, -1296(%rbp)
	movq	$0, -1304(%rbp)
	movq	$0, -1312(%rbp)
	movq	$0, -1320(%rbp)
	movq	$0, -1328(%rbp)
	movq	$0, -1336(%rbp)
	movq	$0, -1344(%rbp)
	movq	$0, -1352(%rbp)
	movq	$0, -1360(%rbp)
	movq	$0, -1368(%rbp)
	movq	$0, -1376(%rbp)
	movq	$0, -1384(%rbp)
	movq	$0, -1392(%rbp)
	movq	$0, -1400(%rbp)
	movq	$0, -1408(%rbp)
	movq	$0, -1416(%rbp)
	movq	$0, -1424(%rbp)
	movq	$0, -1432(%rbp)
	movq	$0, -1440(%rbp)
	movq	$0, -1448(%rbp)
	movq	$0, -1456(%rbp)
	movq	$0, -1464(%rbp)
	movq	$0, -1472(%rbp)
	movq	$0, -1480(%rbp)
	movq	$0, -1488(%rbp)
	movq	$0, -1496(%rbp)
	movq	$0, -1504(%rbp)
	movq	$0, -1512(%rbp)
	movq	$0, -1520(%rbp)
	movq	$0, -1528(%rbp)
	movq	$0, -1536(%rbp)
	movq	$0, -1544(%rbp)
	movq	$0, -1552(%rbp)
	movq	$0, -1560(%rbp)
	movq	$0, -1568(%rbp)
	movq	$0, -1576(%rbp)
	movq	$0, -1584(%rbp)
	movq	$0, -1592(%rbp)
	movq	$0, -1600(%rbp)
	movq	$0, -1608(%rbp)
	movq	$0, -1616(%rbp)
	movq	$0, -1624(%rbp)
	movq	$0, -1632(%rbp)
	movq	$0, -1640(%rbp)
	movq	$0, -1648(%rbp)
	movq	$0, -1656(%rbp)
	movq	$0, -1664(%rbp)
	movq	$0, -1672(%rbp)
	movq	$0, -1680(%rbp)
	movq	$0, -1688(%rbp)
	movq	$0, -1696(%rbp)
	movq	$0, -1704(%rbp)
	movq	$0, -1712(%rbp)
	movq	$0, -1720(%rbp)
	movq	$0, -1728(%rbp)
	movq	$0, -1736(%rbp)
	movq	$0, -1744(%rbp)
	movq	$0, -1752(%rbp)
	movq	$0, -1760(%rbp)
	movq	$0, -1768(%rbp)
	movq	$0, -1776(%rbp)
	movq	$0, -1784(%rbp)
	movq	$0, -1792(%rbp)
	movq	$0, -1800(%rbp)
	movq	$0, -1808(%rbp)
	movq	$0, -1816(%rbp)
	movq	$0, -1824(%rbp)
	movq	$0, -1832(%rbp)
	movq	$0, -1840(%rbp)
	movq	$0, -1848(%rbp)
	movq	$0, -1856(%rbp)
	movq	$0, -1864(%rbp)
	movq	$0, -1872(%rbp)
	movq	$0, -1880(%rbp)
	movq	$0, -1888(%rbp)
	movq	$0, -1896(%rbp)
	movq	$0, -1904(%rbp)
	movq	$0, -1912(%rbp)
	movq	$0, -1920(%rbp)
	movq	$0, -1928(%rbp)
	movq	$0, -1936(%rbp)
	movq	$0, -1944(%rbp)
	movq	$0, -1952(%rbp)
	movq	$0, -1960(%rbp)
	movq	$0, -1968(%rbp)
	movq	$0, -1976(%rbp)
	movq	$0, -1984(%rbp)
	movq	$0, -1992(%rbp)
	movq	$0, -2000(%rbp)
	movq	$0, -2008(%rbp)
	movq	$0, -2016(%rbp)
	movq	$0, -2024(%rbp)
	movq	$0, -2032(%rbp)
	movq	$0, -2040(%rbp)
	movq	$0, -2048(%rbp)
	movq	$0, -2056(%rbp)
	movq	$0, -2064(%rbp)
	movq	$0, -2072(%rbp)
	movq	$0, -2080(%rbp)
	movq	$0, -2088(%rbp)
	movq	$0, -2096(%rbp)
	movq	$0, -2104(%rbp)
	movq	$0, -2112(%rbp)
	movq	$0, -2120(%rbp)
	movq	$0, -2128(%rbp)
	movq	$0, -2136(%rbp)
	movq	$0, -2144(%rbp)
	movq	$0, -2152(%rbp)
	movq	$0, -2160(%rbp)
	movq	$0, -2168(%rbp)
	movq	$0, -2176(%rbp)
	movq	$0, -2184(%rbp)
	movq	$0, -2192(%rbp)
	movq	$0, -2200(%rbp)
	movq	$0, -2208(%rbp)
	movq	$0, -2216(%rbp)
	movq	$0, -2224(%rbp)
	movq	$0, -2232(%rbp)
	movq	$0, -2240(%rbp)
	movq	$0, -2248(%rbp)
	movq	$0, -2256(%rbp)
	movq	$0, -2264(%rbp)
	movq	$0, -2272(%rbp)
	movq	$0, -2280(%rbp)
	movq	$0, -2288(%rbp)
	movq	$0, -2296(%rbp)
	movq	$0, -2304(%rbp)
	movq	$0, -2312(%rbp)
	movq	$0, -2320(%rbp)
	movq	$0, -2328(%rbp)
	movq	$0, -2336(%rbp)
	movq	$0, -2344(%rbp)
	movq	$0, -2352(%rbp)
	movq	$0, -2360(%rbp)
	movq	$0, -2368(%rbp)
	movq	$0, -2376(%rbp)
	movq	$0, -2384(%rbp)
	movq	$0, -2392(%rbp)
	movq	$0, -2400(%rbp)
	movq	$0, -2408(%rbp)
	movq	$0, -2416(%rbp)
	movq	$0, -2424(%rbp)
	movq	$0, -2432(%rbp)
	movq	$0, -2440(%rbp)
	movq	$0, -2448(%rbp)
	movq	$0, -2456(%rbp)
	movq	$0, -2464(%rbp)
	movq	$0, -2472(%rbp)
	movq	$0, -2480(%rbp)
	movq	$0, -2488(%rbp)
	movq	$0, -2496(%rbp)
	movq	$0, -2504(%rbp)
	movq	$0, -2512(%rbp)
	movq	$0, -2520(%rbp)
	movq	$0, -2528(%rbp)
	movq	$0, -2536(%rbp)
	movq	$0, -2544(%rbp)
	movq	$0, -2552(%rbp)
	movq	$0, -2560(%rbp)
	movq	$0, -2568(%rbp)
	movq	$0, -2576(%rbp)
	movq	$0, -2584(%rbp)
	movq	$0, -2592(%rbp)
	movq	$0, -2600(%rbp)
	movq	$0, -2608(%rbp)
	movq	$0, -2616(%rbp)
	movq	$0, -2624(%rbp)
	movq	$0, -2632(%rbp)
	movq	$0, -2640(%rbp)
	movq	$0, -2648(%rbp)
	movq	$0, -2656(%rbp)
	movq	$0, -2664(%rbp)
	movq	$0, -2672(%rbp)
	movq	$0, -2680(%rbp)
	movq	$0, -2688(%rbp)
	movq	$0, -2696(%rbp)
	movq	$0, -2704(%rbp)
	movq	$0, -2712(%rbp)
	movq	$0, -2720(%rbp)
	movq	$0, -2728(%rbp)
	movq	$0, -2736(%rbp)
	movq	$0, -2744(%rbp)
	movq	$0, -2752(%rbp)
	movq	$0, -2760(%rbp)
	movq	$0, -2768(%rbp)
	movq	$0, -2776(%rbp)
	movq	$0, -2784(%rbp)
	movq	$0, -2792(%rbp)
	movq	$0, -2800(%rbp)
	movq	$0, -2808(%rbp)
	movq	$0, -2816(%rbp)
	movq	$0, -2824(%rbp)
	movq	$0, -2832(%rbp)
	movq	$0, -2840(%rbp)
	movq	$0, -2848(%rbp)
	movq	$0, -2856(%rbp)
	movq	$0, -2864(%rbp)
	movq	$0, -2872(%rbp)
	movq	$0, -2880(%rbp)
	movq	$0, -2888(%rbp)
	movq	$0, -2896(%rbp)
	movq	$0, -2904(%rbp)
	movq	$0, -2912(%rbp)
	movq	$0, -2920(%rbp)
	movq	$0, -2928(%rbp)
	movq	$0, -2936(%rbp)
	movq	$0, -2944(%rbp)
	movq	$0, -2952(%rbp)
	movq	$0, -2960(%rbp)
	movq	$0, -2968(%rbp)
	movq	$0, -2976(%rbp)
	movq	$0, -2984(%rbp)
	movq	$0, -2992(%rbp)
	movq	$0, -3000(%rbp)
	movq	$0, -3008(%rbp)
	movq	$0, -3016(%rbp)
	movq	$0, -3024(%rbp)
	movq	$0, -3032(%rbp)
	movq	$0, -3040(%rbp)
	movq	$0, -3048(%rbp)
	movq	$0, -3056(%rbp)
	movq	$0, -3064(%rbp)
	movq	$0, -3072(%rbp)
	movq	$0, -3080(%rbp)
	movq	$0, -3088(%rbp)
	movq	$0, -3096(%rbp)
	movq	$0, -3104(%rbp)
	movq	$0, -3112(%rbp)
	movq	$0, -3120(%rbp)
	movq	$0, -3128(%rbp)
	movq	$0, -3136(%rbp)
	movq	$0, -3144(%rbp)
	movq	$0, -3152(%rbp)
	movq	$0, -3160(%rbp)
	movq	$0, -3168(%rbp)
	movq	$0, -3176(%rbp)
	movq	$0, -3184(%rbp)
	movq	$0, -3192(%rbp)
	movq	$0, -3200(%rbp)
	movq	$0, -3208(%rbp)
	movq	$0, -3216(%rbp)
	movq	$0, -3224(%rbp)
	movq	$0, -3232(%rbp)
	movq	$0, -3240(%rbp)
	movq	$0, -3248(%rbp)
	movq	$0, -3256(%rbp)
	movq	$0, -3264(%rbp)
	movq	$0, -3272(%rbp)
	movq	$0, -3280(%rbp)
	movq	$0, -3288(%rbp)
	movq	$0, -3296(%rbp)
	movq	$0, -3304(%rbp)
	movq	$0, -3312(%rbp)
	movq	$0, -3320(%rbp)
	movq	$0, -3328(%rbp)
	movq	$0, -3336(%rbp)
	movq	$0, -3344(%rbp)
	movq	$0, -3352(%rbp)
	movq	$0, -3360(%rbp)
	movq	$0, -3368(%rbp)
	movq	$0, -3376(%rbp)
	movq	$0, -3384(%rbp)
	movq	$0, -3392(%rbp)
	movq	$0, -3400(%rbp)
	movq	$0, -3408(%rbp)
	movq	$0, -3416(%rbp)
	movq	$0, -3424(%rbp)
	movq	$0, -3432(%rbp)
	movq	$0, -3440(%rbp)
	movq	$0, -3448(%rbp)
	movq	$0, -3456(%rbp)
	movq	$0, -3464(%rbp)
	movq	$0, -3472(%rbp)
	movq	$0, -3480(%rbp)
	movq	$0, -3488(%rbp)
	movq	$0, -3496(%rbp)
	movq	$0, -3504(%rbp)
	movq	$0, -3512(%rbp)
	movq	$0, -3520(%rbp)
	movq	$0, -3528(%rbp)
	movq	$0, -3536(%rbp)
	movq	$0, -3544(%rbp)
	movq	$0, -3552(%rbp)
	movq	$0, -3560(%rbp)
	movq	$0, -3568(%rbp)
	movq	$0, -3576(%rbp)
	movq	$0, -3584(%rbp)
	movq	$0, -3592(%rbp)
	movq	$0, -3600(%rbp)
	movq	$0, -3608(%rbp)
	movq	$0, -3616(%rbp)
	movq	$0, -3624(%rbp)
	movq	$0, -3632(%rbp)
	movq	$0, -3640(%rbp)
	movq	$0, -3648(%rbp)
	movq	$0, -3656(%rbp)
	movq	$0, -3664(%rbp)
	movq	$0, -3672(%rbp)
	movq	$0, -3680(%rbp)
	movq	$0, -3688(%rbp)
	movq	$0, -3696(%rbp)
	movq	$0, -3704(%rbp)
	movq	$0, -3712(%rbp)
	movq	$0, -3720(%rbp)
	movq	$0, -3728(%rbp)
	movq	$0, -3736(%rbp)
	movq	$0, -3744(%rbp)
	movq	$0, -3752(%rbp)
	movq	$0, -3760(%rbp)
	movq	$0, -3768(%rbp)
	movq	$0, -3776(%rbp)
	movq	$0, -3784(%rbp)
	movq	$0, -3792(%rbp)
	movq	$0, -3800(%rbp)
	movq	$0, -3808(%rbp)
	movq	$0, -3816(%rbp)
	movq	$0, -3824(%rbp)
	movq	$0, -3832(%rbp)
	movq	$0, -3840(%rbp)
	movq	$0, -3848(%rbp)
	movq	$0, -3856(%rbp)
	movq	$0, -3864(%rbp)
	movq	$0, -3872(%rbp)
	movq	$0, -3880(%rbp)
	movq	$0, -3888(%rbp)
	movq	$0, -3896(%rbp)
	movq	$0, -3904(%rbp)
	movq	$0, -3912(%rbp)
	movq	$0, -3920(%rbp)
	movq	$0, -3928(%rbp)
	movq	$0, -3936(%rbp)
	movq	$0, -3944(%rbp)
	movq	$0, -3952(%rbp)
	movq	$0, -3960(%rbp)
	movq	$0, -3968(%rbp)
	movq	$0, -3976(%rbp)
	movq	$0, -3984(%rbp)
	movq	$0, -3992(%rbp)
	movq	$0, -4000(%rbp)
	movq	$0, -4008(%rbp)
	movq	$0, -4016(%rbp)
	movq	$0, -4024(%rbp)
	movq	$0, -4032(%rbp)
	movq	$0, -4040(%rbp)
	movq	$0, -4048(%rbp)
	movq	$0, -4056(%rbp)
	movq	$0, -4064(%rbp)
	movq	$0, -4072(%rbp)
	movq	$0, -4080(%rbp)
	movq	$0, -4088(%rbp)
	movq	$0, -4096(%rbp)
	movq	$0, -4104(%rbp)
	movq	$0, -4112(%rbp)
	movq	$0, -4120(%rbp)
	movq	$0, -4128(%rbp)
	movq	$0, -4136(%rbp)
	movq	$0, -4144(%rbp)
	movq	$0, -4152(%rbp)
	movq	$0, -4160(%rbp)
	movq	$0, -4168(%rbp)
	movq	$0, -4176(%rbp)
	movq	$0, -4184(%rbp)
	movq	$0, -4192(%rbp)
	movq	$0, -4200(%rbp)
	movq	$0, -4208(%rbp)
	movq	$0, -4216(%rbp)
	movq	$0, -4224(%rbp)
	movq	$0, -4232(%rbp)
	movq	$0, -4240(%rbp)
	movq	$0, -4248(%rbp)
	movq	$0, -4256(%rbp)
	movq	$0, -4264(%rbp)
	movq	$0, -4272(%rbp)
	movq	$0, -4280(%rbp)
	movq	$0, -4288(%rbp)
	movq	$0, -4296(%rbp)
	movq	$0, -4304(%rbp)
	movq	$0, -4312(%rbp)
	movq	$0, -4320(%rbp)
	movq	$0, -4328(%rbp)
	movq	$0, -4336(%rbp)
	movq	$0, -4344(%rbp)
	movq	$0, -4352(%rbp)
	movq	$0, -4360(%rbp)
	movq	$0, -4368(%rbp)
	movq	$0, -4376(%rbp)
	movq	$0, -4384(%rbp)
	movq	$0, -4392(%rbp)
	movq	$0, -4400(%rbp)
	movq	$0, -4408(%rbp)
	movq	$0, -4416(%rbp)
	movq	$0, -4424(%rbp)
	movq	$0, -4432(%rbp)
	movq	$0, -4440(%rbp)
	movq	$0, -4448(%rbp)
	movq	$0, -4456(%rbp)
	movq	$0, -4464(%rbp)
	movq	$0, -4472(%rbp)
	movq	$0, -4480(%rbp)
	movq	$0, -4488(%rbp)
	movq	$0, -4496(%rbp)
	movq	$0, -4504(%rbp)
	movq	$0, -4512(%rbp)
	movq	$0, -4520(%rbp)
	movq	$0, -4528(%rbp)
	movq	$0, -4536(%rbp)
	movq	$0, -4544(%rbp)
	movq	$0, -4552(%rbp)
	movq	$0, -4560(%rbp)
	movq	$0, -4568(%rbp)
	movq	$0, -4576(%rbp)
	movq	$0, -4584(%rbp)
	movq	$0, -4592(%rbp)
	movq	$0, -4600(%rbp)
	movq	$0, -4608(%rbp)
	movq	$0, -4616(%rbp)
	movq	$0, -4624(%rbp)
	movq	$0, -4632(%rbp)
	movq	$0, -4640(%rbp)
	movq	$0, -4648(%rbp)
	movq	$0, -4656(%rbp)
	movq	$0, -4664(%rbp)
	movq	$0, -4672(%rbp)
	movq	$0, -4680(%rbp)
	movq	$0, -4688(%rbp)
	movq	$0, -4696(%rbp)
	movq	$0, -4704(%rbp)
	movq	$0, -4712(%rbp)
	movq	$0, -4720(%rbp)
	movq	$0, -4728(%rbp)
	movq	$0, -4736(%rbp)
	movq	$0, -4744(%rbp)
	movq	$0, -4752(%rbp)
	movq	$0, -4760(%rbp)
	movq	$0, -4768(%rbp)
	movq	$0, -4776(%rbp)
	movq	$0, -4784(%rbp)
	movq	$0, -4792(%rbp)
	movq	$0, -4800(%rbp)
	movq	$0, -4808(%rbp)
	movq	$0, -4816(%rbp)
	movq	$0, -4824(%rbp)
	movq	$0, -4832(%rbp)
	movq	$0, -4840(%rbp)
	movq	$0, -4848(%rbp)
	movq	$0, -4856(%rbp)
	movq	$0, -4864(%rbp)
	movq	$0, -4872(%rbp)
	movq	$0, -4880(%rbp)
	movq	$0, -4888(%rbp)
	movq	$0, -4896(%rbp)
	movq	$0, -4904(%rbp)
	movq	$0, -4912(%rbp)
	movq	$0, -4920(%rbp)
	movq	$0, -4928(%rbp)
	movq	$0, -4936(%rbp)
	movq	$0, -4944(%rbp)
	movq	$0, -4952(%rbp)
	movq	$0, -4960(%rbp)
	movq	$0, -4968(%rbp)
	movq	$0, -4976(%rbp)
	movq	$0, -4984(%rbp)
	movq	$0, -4992(%rbp)
	movq	$0, -5000(%rbp)
	movq	$0, -5008(%rbp)
	movq	$0, -5016(%rbp)
	movq	$0, -5024(%rbp)
	movq	$0, -5032(%rbp)
	movq	$0, -5040(%rbp)
	movq	$0, -5048(%rbp)
	movq	$0, -5056(%rbp)
	movq	$0, -5064(%rbp)
	movq	$0, -5072(%rbp)
	movq	$0, -5080(%rbp)
	movq	$0, -5088(%rbp)
	movq	$0, -5096(%rbp)
	movq	$0, -5104(%rbp)
	movq	$0, -5112(%rbp)
	movq	$0, -5120(%rbp)
	movq	$0, -5128(%rbp)
	movq	$0, -5136(%rbp)
	movq	$0, -5144(%rbp)
	movq	$0, -5152(%rbp)
	movq	$0, -5160(%rbp)
	movq	$0, -5168(%rbp)
	movq	$0, -5176(%rbp)
	movq	$0, -5184(%rbp)
	movq	$0, -5192(%rbp)
	movq	$0, -5200(%rbp)
	movq	$0, -5208(%rbp)
	movq	$0, -5216(%rbp)
	movq	$0, -5224(%rbp)
	movq	$0, -5232(%rbp)
	movq	$0, -5240(%rbp)
	movq	$0, -5248(%rbp)
	movq	$0, -5256(%rbp)
	movq	$0, -5264(%rbp)
	movq	$0, -5272(%rbp)
	movq	$0, -5280(%rbp)
	movq	$0, -5288(%rbp)
	movq	$0, -5296(%rbp)
	movq	$0, -5304(%rbp)
	movq	$0, -5312(%rbp)
	movq	$0, -5320(%rbp)
	movq	$0, -5328(%rbp)
	movq	$0, -5336(%rbp)
	movq	$0, -5344(%rbp)
	movq	$0, -5352(%rbp)
	movq	$0, -5360(%rbp)
	movq	$0, -5368(%rbp)
	movq	$0, -5376(%rbp)
	movq	$0, -5384(%rbp)
	movq	$0, -5392(%rbp)
	movq	$0, -5400(%rbp)
	movq	$0, -5408(%rbp)
	movq	$0, -5416(%rbp)
	movq	$0, -5424(%rbp)
	movq	$0, -5432(%rbp)
	movq	$0, -5440(%rbp)
	movq	$0, -5448(%rbp)
	movq	$0, -5456(%rbp)
	movq	$0, -5464(%rbp)
	movq	$0, -5472(%rbp)
	movq	$0, -5480(%rbp)
	movq	$0, -5488(%rbp)
	movq	$0, -5496(%rbp)
	movq	$0, -5504(%rbp)
	movq	$0, -5512(%rbp)
	movq	$0, -5520(%rbp)
	movq	$0, -5528(%rbp)
	movq	$0, -5536(%rbp)
	movq	$0, -5544(%rbp)
	movq	$0, -5552(%rbp)
	movq	$0, -5560(%rbp)
	movq	$0, -5568(%rbp)
	movq	$0, -5576(%rbp)
	movq	$0, -5584(%rbp)
	movq	$0, -5592(%rbp)
	movq	$0, -5600(%rbp)
	movq	$0, -5608(%rbp)
	movq	$0, -5616(%rbp)
	movq	$0, -5624(%rbp)
	movq	$0, -5632(%rbp)
	movq	$0, -5640(%rbp)
	movq	$0, -5648(%rbp)
	movq	$0, -5656(%rbp)
	movq	$0, -5664(%rbp)
	movq	$0, -5672(%rbp)
	movq	$0, -5680(%rbp)
	movq	$0, -5688(%rbp)
	movq	$0, -5696(%rbp)
	movq	$0, -5704(%rbp)
	movq	$0, -5712(%rbp)
	movq	$0, -5720(%rbp)
	movq	$0, -5728(%rbp)
	movq	$0, -5736(%rbp)
	movq	$0, -5744(%rbp)
	movq	$0, -5752(%rbp)
	movq	$0, -5760(%rbp)
	movq	$0, -5768(%rbp)
	movq	$0, -5776(%rbp)
	movq	$0, -5784(%rbp)
	movq	$0, -5792(%rbp)
	movq	$0, -5800(%rbp)
	movq	$0, -5808(%rbp)
	movq	$0, -5816(%rbp)
	movq	$0, -5824(%rbp)
	movq	$0, -5832(%rbp)
	movq	$0, -5840(%rbp)
	movq	$0, -5848(%rbp)
	movq	$0, -5856(%rbp)
	movq	$0, -5864(%rbp)
	movq	$0, -5872(%rbp)
	movq	$0, -5880(%rbp)
	movq	$0, -5888(%rbp)
	movq	$0, -5896(%rbp)
	movq	$0, -5904(%rbp)
	movq	$0, -5912(%rbp)
	movq	$0, -5920(%rbp)
	movq	$0, -5928(%rbp)
	movq	$0, -5936(%rbp)
	movq	$0, -5944(%rbp)
	movq	$0, -5952(%rbp)
	movq	$0, -5960(%rbp)
	movq	$0, -5968(%rbp)
	movq	$0, -5976(%rbp)
	movq	$0, -5984(%rbp)
	movq	$0, -5992(%rbp)
	movq	$0, -6000(%rbp)
	movq	$0, -6008(%rbp)
	movq	$0, -6016(%rbp)
	movq	$0, -6024(%rbp)
	movq	$0, -6032(%rbp)
	movq	$0, -6040(%rbp)
	movq	$0, -6048(%rbp)
	movq	$0, -6056(%rbp)
	movq	$0, -6064(%rbp)
	movq	$0, -6072(%rbp)
	movq	$0, -6080(%rbp)
	movq	$0, -6088(%rbp)
	movq	$0, -6096(%rbp)
	movq	$0, -6104(%rbp)
	movq	$0, -6112(%rbp)
	movq	$0, -6120(%rbp)
	movq	$0, -6128(%rbp)
	movq	$0, -6136(%rbp)
	movq	$0, -6144(%rbp)
	movq	$0, -6152(%rbp)
	movq	$0, -6160(%rbp)
	movq	$0, -6168(%rbp)
	movq	$0, -6176(%rbp)
	movq	$0, -6184(%rbp)
	movq	$0, -6192(%rbp)
	movq	$0, -6200(%rbp)
	movq	$0, -6208(%rbp)
	movq	$0, -6216(%rbp)
	movq	$0, -6224(%rbp)
	movq	$0, -6232(%rbp)
	movq	$0, -6240(%rbp)
	movq	$0, -6248(%rbp)
	movq	$0, -6256(%rbp)
	movq	$0, -6264(%rbp)
	movq	$0, -6272(%rbp)
	movq	$0, -6280(%rbp)
	movq	$0, -6288(%rbp)
	movq	$0, -6296(%rbp)
	movq	$0, -6304(%rbp)
	movq	$0, -6312(%rbp)
	movq	$0, -6320(%rbp)
	movq	$0, -6328(%rbp)
	movq	$0, -6336(%rbp)
	movq	$0, -6344(%rbp)
	movq	$0, -6352(%rbp)
	movq	$0, -6360(%rbp)
	movq	$0, -6368(%rbp)
	movq	$0, -6376(%rbp)
	movq	$0, -6384(%rbp)
	movq	$0, -6392(%rbp)
	movq	$0, -6400(%rbp)
	movq	$0, -6408(%rbp)
	movq	$0, -6416(%rbp)
	movq	$0, -6424(%rbp)
	movq	$0, -6432(%rbp)
	movq	$0, -6440(%rbp)
	movq	$0, -6448(%rbp)
	movq	$0, -6456(%rbp)
	movq	$0, -6464(%rbp)
	movq	$0, -6472(%rbp)
	movq	$0, -6480(%rbp)
	movq	$0, -6488(%rbp)
	movq	$0, -6496(%rbp)
	movq	$0, -6504(%rbp)
	movq	$0, -6512(%rbp)
	movq	$0, -6520(%rbp)
	movq	$0, -6528(%rbp)
	movq	$0, -6536(%rbp)
	movq	$0, -6544(%rbp)
	movq	$0, -6552(%rbp)
	movq	$0, -6560(%rbp)
	movq	$0, -6568(%rbp)
	movq	$0, -6576(%rbp)
	movq	$0, -6584(%rbp)
	movq	$0, -6592(%rbp)
	movq	$0, -6600(%rbp)
	movq	$0, -6608(%rbp)
	movq	$0, -6616(%rbp)
	movq	$0, -6624(%rbp)
	movq	$0, -6632(%rbp)
	movq	$0, -6640(%rbp)
	movq	$0, -6648(%rbp)
	movq	$0, -6656(%rbp)
	movq	$0, -6664(%rbp)
	movq	$0, -6672(%rbp)
	movq	$0, -6680(%rbp)
	movq	$0, -6688(%rbp)
	movq	$0, -6696(%rbp)
	movq	$0, -6704(%rbp)
	movq	$0, -6712(%rbp)
	movq	$0, -6720(%rbp)
	movq	$0, -6728(%rbp)
	movq	$0, -6736(%rbp)
	movq	$0, -6744(%rbp)
	movq	$0, -6752(%rbp)
	movq	$0, -6760(%rbp)
	movq	$0, -6768(%rbp)
	movq	$0, -6776(%rbp)
	movq	$0, -6784(%rbp)
	movq	$0, -6792(%rbp)
	movq	$0, -6800(%rbp)
	movq	$0, -6808(%rbp)
	movq	$0, -6816(%rbp)
	movq	$0, -6824(%rbp)
	movq	$0, -6832(%rbp)
	movq	$0, -6840(%rbp)
	movq	$0, -6848(%rbp)
	movq	$0, -6856(%rbp)
	movq	$0, -6864(%rbp)
	movq	$0, -6872(%rbp)
	movq	$0, -6880(%rbp)
	movq	$0, -6888(%rbp)
	movq	$0, -6896(%rbp)
	movq	$0, -6904(%rbp)
	movq	$0, -6912(%rbp)
	movq	$0, -6920(%rbp)
	movq	$0, -6928(%rbp)
	movq	$0, -6936(%rbp)
	movq	$0, -6944(%rbp)
	movq	$0, -6952(%rbp)
	movq	$0, -6960(%rbp)
	movq	$0, -6968(%rbp)
	movq	$0, -6976(%rbp)
	movq	$0, -6984(%rbp)
	movq	$0, -6992(%rbp)
	movq	$0, -7000(%rbp)
	movq	$0, -7008(%rbp)
	movq	$0, -7016(%rbp)
	movq	$0, -7024(%rbp)
	movq	$0, -7032(%rbp)
	movq	$0, -7040(%rbp)
	movq	$0, -7048(%rbp)
	movq	$0, -7056(%rbp)
	movq	$0, -7064(%rbp)
	movq	$0, -7072(%rbp)
	movq	$0, -7080(%rbp)
	movq	$0, -7088(%rbp)
	movq	$0, -7096(%rbp)
	movq	$0, -7104(%rbp)
	movq	$0, -7112(%rbp)
	movq	$0, -7120(%rbp)
	movq	$0, -7128(%rbp)
	movq	$0, -7136(%rbp)
	movq	$0, -7144(%rbp)
	movq	$0, -7152(%rbp)
	movq	$0, -7160(%rbp)
	movq	$0, -7168(%rbp)
	movq	$0, -7176(%rbp)
	movq	$0, -7184(%rbp)
	movq	$0, -7192(%rbp)
	movq	$0, -7200(%rbp)
	movq	$0, -7208(%rbp)
	movq	$0, -7216(%rbp)
	movq	$0, -7224(%rbp)
	movq	$0, -7232(%rbp)
	movq	$0, -7240(%rbp)
	movq	$0, -7248(%rbp)
	movq	$0, -7256(%rbp)
	movq	$0, -7264(%rbp)
	movq	$0, -7272(%rbp)
	movq	$0, -7280(%rbp)
	movq	$0, -7288(%rbp)
	movq	$0, -7296(%rbp)
	movq	$0, -7304(%rbp)
	movq	$0, -7312(%rbp)
	movq	$0, -7320(%rbp)
	movq	$0, -7328(%rbp)
	movq	$0, -7336(%rbp)
	movq	$0, -7344(%rbp)
	movq	$0, -7352(%rbp)
	movq	$0, -7360(%rbp)
	movq	$0, -7368(%rbp)
	movq	$0, -7376(%rbp)
	movq	$0, -7384(%rbp)
	movq	$0, -7392(%rbp)
	movq	$0, -7400(%rbp)
	movq	$0, -7408(%rbp)
	movq	$0, -7416(%rbp)
	movq	$0, -7424(%rbp)
	movq	$0, -7432(%rbp)
	movq	$0, -7440(%rbp)
	movq	$0, -7448(%rbp)
	movq	$0, -7456(%rbp)
	movq	$0, -7464(%rbp)
	movq	$0, -7472(%rbp)
	movq	$0, -7480(%rbp)
	movq	$0, -7488(%rbp)
	movq	$0, -7496(%rbp)
	movq	$0, -7504(%rbp)
	movq	$0, -7512(%rbp)
	movq	$0, -7520(%rbp)
	movq	$0, -7528(%rbp)
	movq	$0, -7536(%rbp)
	movq	$0, -7544(%rbp)
	movq	$0, -7552(%rbp)
	movq	$0, -7560(%rbp)
	movq	$0, -7568(%rbp)
	movq	$0, -7576(%rbp)
	movq	$0, -7584(%rbp)
	movq	$0, -7592(%rbp)
	movq	$0, -7600(%rbp)
	movq	$0, -7608(%rbp)
	movq	$0, -7616(%rbp)
	movq	$0, -7624(%rbp)
	movq	$0, -7632(%rbp)
	movq	$0, -7640(%rbp)
	movq	$0, -7648(%rbp)
	movq	$0, -7656(%rbp)
	movq	$0, -7664(%rbp)
	movq	$0, -7672(%rbp)
	movq	$0, -7680(%rbp)
	movq	$0, -7688(%rbp)
	movq	$0, -7696(%rbp)
	movq	$0, -7704(%rbp)
	movq	$0, -7712(%rbp)
	movq	$0, -7720(%rbp)
	movq	$0, -7728(%rbp)
	movq	$0, -7736(%rbp)
	movq	$0, -7744(%rbp)
	movq	$0, -7752(%rbp)
	movq	$0, -7760(%rbp)
	movq	$0, -7768(%rbp)
	movq	$0, -7776(%rbp)
	movq	$0, -7784(%rbp)
	movq	$0, -7792(%rbp)
	movq	$0, -7800(%rbp)
	movq	$0, -7808(%rbp)
	movq	$0, -7816(%rbp)
	movq	$0, -7824(%rbp)
	movq	$0, -7832(%rbp)
	movq	$0, -7840(%rbp)
	movq	$0, -7848(%rbp)
	movq	$0, -7856(%rbp)
	movq	$0, -7864(%rbp)
	movq	$0, -7872(%rbp)
	movq	$0, -7880(%rbp)
	movq	$0, -7888(%rbp)
	movq	$0, -7896(%rbp)
	movq	$0, -7904(%rbp)
	movq	$0, -7912(%rbp)
	movq	$0, -7920(%rbp)
	movq	$0, -7928(%rbp)
	movq	$0, -7936(%rbp)
	movq	$0, -7944(%rbp)
	movq	$0, -7952(%rbp)
	movq	$0, -7960(%rbp)
	movq	$0, -7968(%rbp)
	movq	$0, -7976(%rbp)
	movq	$0, -7984(%rbp)
	movq	$0, -7992(%rbp)
	movq	$0, -8000(%rbp)
	movq	$0, -8008(%rbp)
	movq	$0, -8016(%rbp)
	movq	$0, -8024(%rbp)
	movq	$0, -8032(%rbp)
	movq	$0, -8040(%rbp)
	movq	$0, -8048(%rbp)
	movq	$0, -8056(%rbp)
	movq	$0, -8064(%rbp)
	movq	$0, -8072(%rbp)
	movq	$0, -8080(%rbp)
	movq	$0, -8088(%rbp)
	movq	$0, -8096(%rbp)
	movq	$0, -8104(%rbp)
	movq	$0, -8112(%rbp)
	movq	$0, -8120(%rbp)
	movq	$0, -8128(%rbp)
	movq	$0, -8136(%rbp)
	movq	$0, -8144(%rbp)
	movq	$0, -8152(%rbp)
	movq	$0, -8160(%rbp)
	movq	$0, -8168(%rbp)
	movq	$0, -8176(%rbp)
	movq	$0, -8184(%rbp)
	movq	$0, -8192(%rbp)
	movq	$0, -8200(%rbp)
	leaq	-8200(%rbp), %rax
	movq	%rax, %r12
	movq	%r12, -8(%rbp)
	movq	$0, %rax
	movq	%rax, %r12
	movq	%r12, -8208(%rbp)
LOOP153:

	movq	$3, %rax
	pushq	%rax


	movq	-8208(%rbp), %rax
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
	je	LOOP153_END

	movq	$65, %rax
	pushq	%rax


	movq	-8208(%rbp), %rax
	pushq	%rax


	popq	%r11
	popq	%r10
	addq	%r10, %r11
	pushq	%r11

	popq	%rax
	movq	%rax, %r12
	movq	-8(%rbp), %rax
	pushq	%rax
	movq	-8208(%rbp), %rax
	popq	%r10
	imulq	$8, %rax
	addq	%rax, %r10
	movq	%r10, %rax
	movq	%r12, (%rax)
LOOP153_NEXT:
	movq	-8208(%rbp), %rax
	pushq	%rax
	incq	%rax
	movq	%rax, -8208(%rbp)
	popq	%rax
	jmp	LOOP153
LOOP153_END:
	pushq	%rdi
	pushq	%rsi
	pushq	%rdx
	pushq	%rcx
	pushq	%r8
	pushq	%r9
	movq	-8(%rbp), %rax
	movq	%rax, %rdi
	movq	$4, %rax
	movq	%rax, %rsi
	call	permutations
	popq	%r9
	popq	%r8
	popq	%rcx
	popq	%rdx
	popq	%rsi
	popq	%rdi
	leave	
	ret	
	.ident	"HEROCOMP - Tomas Mikula 2017"

