
main ()
{
    /* iteratve Fibonacci numbers */
    long a = 0, b = 1, i;
    for (i = 0; i < 20; i ++) {
    	long c = b;
    	b = a + b;
    	a = c;
    }
}
