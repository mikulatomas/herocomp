
fac_iter (n, accum)
{
    if (n <= 0) {
	return accum;
    }
    return fac_iter (n - 1, accum * n);
}

fac (n)
{
    return fac_iter (n, 1);
}

main ()
{
    /* factorial: tail recursion */
    long n;
    for (n = 0; n < 10; n ++) {
	print_long (fac (n));
	print_nl ();
    }
}
