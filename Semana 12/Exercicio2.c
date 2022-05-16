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

void busca(no *lista, int chave);

int main(void)
{
  int tam, num, chave;
  no *lista = inicializa();
  printf("Digite a quantidade de itens a serem inseridos \n");
  scanf("%d", &tam);

  printf("Digite os valores \n");
  for (int i = 0; i < tam; i++)
  {
    scanf("%d", &num);
    lista = insere_inicio(lista, num);
  }
  printf("Digite a chave de busca \n");
  scanf("%d", &chave);
  busca(lista, chave);
}

void busca(no *lista, int chave)
{
  int count = 0;
  int encontro = 0;

  while (lista)
  {
    if (lista->conteudo == chave)
    {
      printf("Encontrado na posição %d", count);
      encontro++;
    }
    count++;
    lista = lista->prox;
  }
  if (encontro == 0)
  {
    printf("Item não encontrado");
  }
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