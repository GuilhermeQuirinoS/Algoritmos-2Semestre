#include <string.h>
#include <stdio.h>
#include <stdlib.h>
void inverte(char *orig)
{
    int metade = (strlen(orig) / 2);
    int i,aux = 0;
    for (i = 0; i < metade; i++)
    {
        aux = orig[(strlen(orig) - 2) - i];
        orig[(strlen(orig) - 2) - i] = orig[i];
        orig[i] = aux;
    }
    printf("%s", orig);
}

int main()
{
    char orig[61];
    fgets(orig, 61, stdin);
    inverte(orig);
}