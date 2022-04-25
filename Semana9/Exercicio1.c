#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char msg[51];
    fgets(msg, 51, stdin);
    len(msg);
    return 0;
}
int len(char *msg)
{
    int tam = strlen(msg) - 1;
    printf("%d", tam);
}