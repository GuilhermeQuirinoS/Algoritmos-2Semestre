#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void recebe(int *v, int n)
{
    int i;
    printf("Digite os elementos do vetor:\n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", v + i);
    }
}

int main()
{
    int n, *v;

    printf("Digite o numero de elementos:\n");
    scanf("%d", &n);

    v = malloc(n * (sizeof(int)));
    recebe(v, n);
    printf("Seu vetor:\n");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", *(v + i));
    }
    free(v);
    return 0;
}
