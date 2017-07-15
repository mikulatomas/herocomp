
/*****************************************************************************
 * herocio.c
 * compile with: gcc -m64 -c herocio.c
 *****************************************************************************/

#include <stdio.h>

void print_long (long x)
{
    printf ("%li", x);
}

void print_char (long x)
{
    if ((0 <= x) && (x <= 127)) {
        printf ("%c", (char) x);
    }
    else {
        fprintf (stderr, "Unknown character code: %li", x);
    }
}

void print_nl ()
{
    printf ("\n");
}
