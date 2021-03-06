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
no *ordena(no *lista, int max);

int main(void)
{
  no *lista = inicializa();

  int max, i, num;

  scanf("%d", &max);

  for (i = 0; i < max; i++)
  {
    scanf("%d", &num);
    lista = insere_inicio(lista, num);
  }

  lista = ordena(lista, max);
  imprimir(lista);

  return 0;
}

no *ordena(no *lista, int max)
{
  int i;
  no *atual = (no *)malloc(sizeof(no));
  no *proximo = (no *)malloc(sizeof(no));

  atual = lista;

  for (i = 0; i < max; i++)
  {
    proximo = atual->prox;
    while (proximo!=NULL)
    {
      int aux = 0;
      if (atual->conteudo > proximo->conteudo)
      {
        aux = atual->conteudo;
        atual->conteudo = proximo->conteudo;
        proximo->conteudo = aux;
      }
      proximo = proximo->prox;
    }
    atual = atual->prox;
  }

  return lista;
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
  while (lista)
  {
    printf("%d ", lista->conteudo);
    lista = lista->prox;
  }
  printf("\n\n");
}