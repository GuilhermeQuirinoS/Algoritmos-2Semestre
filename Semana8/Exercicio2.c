#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int n1, n2;
    int *x1, *x2;

    printf("Digite o tamanho do vetor X1:\n");
    scanf("%i", &n1);
    printf("Digite o tamanho do vetor X2:\n");
    scanf("%d", &n2);

    x1 = malloc(n1 * sizeof(int));
    x2 = malloc(n2 * sizeof(int));

    printf("Insira os valores do vetor X1:\n");
    for (int i = 0; i < n1; i++)
    {
        scanf("%d", x1 + i);
    }
    printf("Insira os valores do vetor X2:\n");
    for (int i = 0; i < n2; i++)
    {
        scanf("%d", x2 + i);
    }

    uniao(x1, n1, x2, n2);
    free(x1);
    free(x2);
    return 0;
}

int uniao(int *x1, int n1, int *x2, int n2)
{
    int n3, n = 0;
    int *x3;
    for (int i = 0; i < n1; i++)
    {
        for (int j = 0; j < n2; j++)
        {
            if (x1[i] == x2[j])
            {
                n += 1;
            }
        }
    }

    x3 = malloc((n) * sizeof(int));
    int i, j = 0;
    printf("Interseccao de X1 e X2:\n");
    for (i = 0; i < n1; i++)
    {
        if (x1[i] == x2[i])
        {
            x3[j] = x1[i];
            j++;
        }
    }
    for (i = 0; i < n2; i++)
    {
        if (x1[i] == x2[i])
        {
            x3[j] = x2[i];
            j++;
        }
    }
    organiza(n, x3);
    n3 = repetidos(n, x3);
    for (i = 0; i < n3; i++)
    {
        printf("%d ", *(x3 + i));
    }

    free(x3);
}

int repetidos(int n3, int *x1)
{
    int i, j, k;
    for (i = 0; i < n3; i++)
    {
        for (j = i + 1; j < n3; j++)
        {
            if (x1[i] == x1[i + 1])
            {
                for (k = j; k < n3; k++)
                {
                    x1[k] = x1[k + 1];
                }
                n3--;
            }
            else
            {
                j++;
            }
        }
    }
    return (n3);
}

void organiza(int n3, int *x1)
{
    int i, j, aux;
    for (i = 0; i < n3; i++)
    {
        for (j = i + 1; j < n3; j++)
        {
            if (x1[i] > x1[j])
            {
                aux = x1[i];
                x1[i] = x1[j];
                x1[j] = aux;
            }
        }
    }
}