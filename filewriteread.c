#include <stdio.h>

void main(){
    FILE *file = fopen("count.txt", "w");
    fprintf(file, "heiiiinnnn");
    printf("%c", fgetc(file)+ '0');
    fclose(file);
}
