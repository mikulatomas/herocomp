lol(){
    long a = 101;
    if (a>5){
        long a = 2;
    }
}
main ()
{
    /* iteratve Fibonacci numbers */
    long a = 10;
    if (a>5){
        long a = 2;
        if (a > 5) {
            a = 10;
            lol();
        }
    }
}
