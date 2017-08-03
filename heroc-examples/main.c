
long pc;
long sp;
long prgm;
long stack [65536];

print_stack ()
{
    long i;

    print_char ('[');
    for (i = 0; i < sp; i ++) {
	if (i > 0) {
	    print_char (',');
	    print_char (' ');
	}
	print_long (stack [i]);
    }
    print_nl ();
}

push1 (x) { stack [sp] = x; sp ++; }
pop1 (x) { }
jrz1 (x) { sp --; if (stack [sp] == 0) { pc += x; } }
add2 (x, y) { push1 (x + y); }
mul2 (x, y) { push1 (x * y); }
leq2 (y, x) { push1 (x <= y); }
dup1 (x) { push1 (x); push1 (x); }
swap2 (x, y) { push1 (x); push1 (y); }
rot3 (x, y, z) { push1 (x); push1 (z); push1 (y); }

eval ()
{
    long last;

    do {
	print_stack ();
	last = prgm [pc];
	if (last == -1) {
	    pc += 3;
	    prgm [pc - 2] (prgm [pc - 1]);
	    continue;
	}
	if (last == 1) {
	    long a1 = stack [sp - 1];
	    pc += 2;
	    sp -= 1;
	    prgm [pc - 1] (a1);
	    continue;
	}
	if (last == 2) {
	    long a1 = stack [sp - 1], a2 = stack [sp - 2];
	    pc += 2;
	    sp -= 2;
	    prgm [pc - 1] (a1, a2);
	    continue;
	}
	if (last == 3) {
	    long a1 = stack [sp - 1], a2 = stack [sp - 2], a3 = stack [sp - 3];
	    pc += 2;
	    sp -= 3;
	    prgm [pc - 1] (a1, a2, a3);
	    continue;
	}
    } while (last);
}

run (p)
{
    prgm = p;
    pc = sp = 0;
    eval ();
}

main ()
{
    /* stack-based evaluation of expressions */
    long p = {-1, &push1, 10,
		 -1, &push1, 1,
		 2, &swap2,
		 1, &dup1,
		 -1, &push1, 1,
		 2, &leq2,
		 -1, &jrz1, 3,
		 1, &pop1,
		 0,
		 1, &dup1,
		 -1, &push1, -1,
		 2, &add2,
		 3, &rot3,
		 2, &mul2,
		 -1, &push1, 0,
		 -1, &jrz1, -32};
    run (p);
}
