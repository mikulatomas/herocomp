
print_string (x, len)
{
    long i;
    for (i = 0; i < len; i ++) {
	print_char (x [i]);
    }
    print_nl ();
}

main ()
{
    /* EXTRAS: string literals = arrays of long integers */
    print_string ("Hello, World!", 13);
    long a;
    print_string ("Muhehe, Fubar", 13);
}
