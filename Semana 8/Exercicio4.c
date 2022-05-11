#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void recebe(int *m1, int lin1, int col1, int *m2, int lin2, int col2)
{
    int i, j = 0;

    printf("Digite os valores da Matriz 1:\n");
    for (i = 0; i < lin1; i++)
    {
        for (j = 0; j < col1; j++)
        {
            scanf("%d", (m1 + ((i + col1) + j)));
        }
    }
    printf("Digite os valores da Matriz 2:\n");
    for (i = 0; i < lin2; i++)
    {
        for (j = 0; j < col2; j++)
        {
            scanf("%d", (m2 + ((i + col2) + j)));
        }
    }
}

int main()
{
    int *m1, *m2;
    int lin1, col1, lin2, col2;

    printf("Digite a dimensao da Matriz 1:\n");
    scanf("%d %d", &lin1, &col1);
    printf("Digite a dimensao da Matriz 2:\n");
    scanf("%d %d", &lin2, &col2);

    m1 = malloc(lin1 * col1 * sizeof(int));
    m2 = malloc(lin2 * col2 * sizeof(int));

    recebe(m1, lin1, col1, m2, lin2, col2);

    printf("Matriz 1:");
    for (int i = 0; i < lin1; i++)
    {
        printf("\n");
        for (int j = 0; j < col1; j++)
        {
            printf("%d", *(m1 + ((i + col1) + j)));
        }
    }
    printf("\n");
    printf("Matriz 2:");
    for (int i = 0; i < lin2; i++)
    {
        printf("\n");
        for (int j = 0; j < col2; j++)
        {
            printf("%d", *(m2 + ((i + col2) + j)));
        }
    }
    free(m1);
    free(m2);
    return 0;
}
