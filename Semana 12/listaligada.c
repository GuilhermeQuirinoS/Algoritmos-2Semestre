#include <stdio.h>

typedef struct reg no;

/*struct reg{
    int conteudo;
    struct reg *prox;
};

int main(void){
   no* primeiro = (no*) malloc(sizeof(no));;
   no* segundo = (no*) malloc(sizeof(no));;

   primeiro->conteudo = 1;
   segundo->conteudo = 2;
   primeiro->prox = segundo;
  
    printf("%d\n", &primeiro);
   printf("%d\n", &segundo);
   printf("%d\n", primeiro->conteudo);
   printf("%d\n", primeiro->prox->conteudo);
  printf("%d\n", segundo->conteudo);

}*/

#include <stdio.h>
#include <stdlib.h>

typedef struct reg no;

no* inicializa (void);
no* insere_inicio(no *lista, int num);
no* remove_inicio(no *lista);
void imprimir (no *lista);

struct reg{
    int conteudo;
    struct reg *prox;
};

int main(void){
  no* lista = inicializa();
  lista=insere_inicio(lista, 2);
  lista=insere_inicio(lista, 1);
  lista= insere_inicio(lista, 3);
  lista =remove_inicio(lista);
  imprimir(lista);

}

/* função de inicialização: retorna uma lista vazia */
no* inicializa (void)
{
 return NULL;
}

/* inserção no início: retorna a lista atualizada */
no* insere_inicio (no* l, int i)
{
 no* novo = (no*) malloc(sizeof(no));
 novo->conteudo = i;
 novo->prox = l;
 return novo;
}

no* remove_inicio (no* l)
{
  if(l == NULL) {
    printf("\nA lista ja esta vazia\n");
    }else{
        no * atual = (no*) malloc(sizeof(no));
        atual = l->prox;
        free(l);
        return atual;
    }
 
}

/*
     Procedimento para imprimir uma lista simplesmente encadeada
*/
void imprimir(no *lista){
    printf("\n Lista: ");
    while(lista){
        printf("%d ", lista->conteudo);
        lista = lista->prox;
    }
    printf("\n\n");
}