
line_of_stars (n)
{
    long i;
    for (; ! (n < 0); n --) {
	print_char (42);
    }
    print_nl ();
    return;
}

main ()
{
    /* nice triangle, for-style */
    long n;
    for (n = 1; n <= 10; n ++) {
	line_of_stars (10 - n);
    }
    return;
}
