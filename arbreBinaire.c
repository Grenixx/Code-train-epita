
#include <stdlib.h>
#include <stdio.h>

struct arbreBinaire
{
    //jveux deux pointeur vers fg et fd et un vers le parent 
    //struct arbreBinaire fg;
    int elem;
    struct arbreBinaire* fg;
    struct arbreBinaire* fd;
    struct arbreBinaire* p;
    
};

void main(){
    struct arbreBinaire a1;
    a1.elem=5;
    a1.fg = NULL;
    a1.fd = NULL;
    a1.p = NULL;

    struct arbreBinaire a2;
    a2.elem=3;
    a2.fg = NULL;
    a2.fd = NULL;
    a2.p = NULL;

    a1.fg = &a2;
    a2.p = &a1;

    printf("%d\n", (*a1.fg).elem);
    //printf("%d\n", a1.fg->elem);
}