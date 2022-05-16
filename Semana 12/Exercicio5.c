#include <stdio.h>
#include <stdlib.h>

typedef struct reg no;

no *inicializa(void);
no *insere_inicio(no *lista, int num);
void imprimir(no *lista);

struct reg
{
  int conteudo;
  struct reg *prox;
};

void particiona(no *lista, int tam);

int main(void)
{
  int tam, num;
  no *lista = inicializa();
  printf("Digite a quantidade de itens a serem inseridos \n");
  scanf("%d", &tam);

  printf("Digite os valores \n");
  for (int i = 0; i < tam; i++)
  {
    scanf("%d", &num);
    lista = insere_inicio(lista, num);
  }
  particiona(lista, tam);
}

void particiona(no *lista, int tam)
{
  int par[tam];
  int impar[tam];

  int i = 0, j = 0, k;

  while (lista)
  {
    if (lista->conteudo % 2 == 0)
    {
      par[i] = lista->conteudo;
      i++;
    }
    else
    {
      impar[j] = lista->conteudo;
      j++;
    }
    lista = lista->prox;
  }

  printf("\nLista par:");
  for (k = i - 1; k >= 0; k--)
  {
    printf("%d ", par[k]);
  }

  printf("\nLista impar:");
  for (k = j - 1; k >= 0; k--)
  {
    printf("%d ", impar[k]);
  }
  printf("\n\n");
}

no *inicializa(void)
{
  return NULL;
}

no *insere_inicio(no *l, int i)
{
  no *novo = (no *)malloc(sizeof(no));
  novo->conteudo = i;
  novo->prox = l;
  return novo;
}

void imprimir(no *lista)
{
  printf("\n Lista: ");
  while (lista)
  {
    printf("%d ", lista->conteudo);
    lista = lista->prox;
  }
  printf("\n\n");
}