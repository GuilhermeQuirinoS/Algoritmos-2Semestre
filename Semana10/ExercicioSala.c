#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char ch[100];
    FILE *fp;
    fp = fopen("arq.txt", "w");
    printf("Arquivo criado!Escreva sua mensagem:\n");
    for (int i = 0; i < strlen(ch); i++)
    {
        if (fgets(ch, strlen(ch), stdin))
        {
            fputs(ch, fp);
        }
        if (ch[i] = '0')
        {
            fclose(fp);
        }
    }
    return 0;
}