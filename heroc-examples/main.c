main ()
{
    {
        long a = 1;
        {
            long a = 10;
        }
        long d;
        long e;
        long f;
        d = e = f = a;
    }
    return 1;
}
