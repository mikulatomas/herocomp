
line_of_stars (n)
{
    long i;
    for (; ! (n < 0); n --) {
	print_char (42);
    }
    print_nl ();
}

main ()
{
    /* nice triangle, while-style */
    long n = 9;
    while (n >= 0) {
	line_of_stars (n);
	n --;
    }
}
