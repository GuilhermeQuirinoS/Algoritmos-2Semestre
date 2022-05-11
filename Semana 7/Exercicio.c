#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
struct pessoa
{
    float altura;
    float peso;
    int idade;
};
Maria;
int Maria;
*/
/*
struct Date
{
    int dia;
    char mes[50];
    int ano;
} object;

int main(){
    struct Date Nasc;
    printf("Digite o dia:\n");
    scanf("%d", &Nasc.dia);
    printf("Escreva o mes:\n");
    scanf("%s", &Nasc.mes);
    printf("Digite o ano:\n");
    scanf("%d", &Nasc.ano);

    printf("Data: %d/%s/%d\n", Nasc.dia, Nasc.mes, Nasc.ano);
}
*/

/* Ordena3 */

struct Ponto
{
    double x;
    double y;
    double z;
};

void leiaPonto(struct Ponto *p)
{
    scanf("%lf", &(p->x));
    scanf("%lf", &(p->y));
    scanf("%lf", &(p->z));
}

void imprimePonto(struct Ponto p)
{
    printf("%.4lf\n", p.x);
    printf("%.4lf\n", p.y);
    printf("%.4lf\n", p.z);
}

struct Ponto ordena(struct Ponto p)
{
    
}

int main(void)
{
    struct Ponto p;

    leiaPonto(&p);

    imprimePonto(ordena(p));

    return 0;
}
/* Exercício 3
Elaborar um programa cuja entrada são 3 números reais e cuja saída apresenta esses
números em ordem crescente.
Utilize estrutura, dupla precisão e 4 casas depois da vírgula.
Exemplo:
Entrada
2.4 0.9 1.8
Saída
0.9000
1.8000
2.4000
For example:
Input	Result
1.2
4.8
2.9
1.2000
2.9000
4.8000
 */

#include <stdio.h>
#include <stdlib.h>


struct{
double p1;
double p2;
double p3;
}p;

int main(void){
  scanf("%lf", &p.p1);
  scanf("%lf", &p.p2);
  scanf("%lf", &p.p3);
  if(p.p1>p.p2&&p.p2>p.p3){
    printf("%.4lf\n%.4lf\n%.4lf", p.p3,p.p2,p.p1);
  }
  if(p.p1>p.p3 && p.p3>p.p2){
    printf("%.4lf\n%.4lf\n%.4lf", p.p2,p.p3,p.p1);
  }
  if(p.p2>p.p1 && p.p1>p.p3){
    printf("%.4lf\n%.4lf\n%.4lf", p.p3,p.p1,p.p2);
  }
  if(p.p2>p.p3 && p.p3>p.p1){
    printf("%.4lf\n%.4lf\n%.4lf", p.p1,p.p3,p.p2);
  }
  if(p.p3>p.p2 && p.p2>p.p1){
    printf("%.4lf\n%.4lf\n%.4lf", p.p1,p.p2,p.p3);
  }
  if(p.p3>p.p1 &&p.p1>p.p2){
    printf("%.4lf\n%.4lf\n%.4lf", p.p2,p.p1,p.p3);
  }
}

/* Exercício 4
Elaborar um programa cuja entrada são n pontos no plano que são os vértices de um
polígono de no máximo 100 lados.
Determine o perímetro desse polígono.
Utilize estrutura, dupla precisão e 4 casas depois da vírgula.
Exemplo:
Entrada                         Saída
4                                    Perimetro: 4.0000
0 0 1 0 1 1 0 1
3                                    Perimetro: 3.4142 
0 0 1 0 0 1
For example:
Input	Result
4
0 0 1 0 1 1 0 1
Perimetro: 4.0000 */

#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

struct pontos
{
  int x;
  int y;
} vetor;

int main(){
  int n, i;
  float soma = 0;
  scanf("%d", &n);
  struct pontos vetor [n];
  for(i=0;i<n;i++){
    scanf("%d", &vetor[i].x);
    scanf("%d", &vetor[i].y);
  }
  for (i=0;i<n;i++){
    if(i != n-1){
      soma+=sqrt((pow((vetor[i+1].x-vetor[i].x), 2)+pow((vetor [i+1].y-vetor[i].y), 2)));
    }
    else{
      soma+=sqrt((pow((vetor[0].x-vetor[n-1].x), 2)+pow((vetor [0].y-vetor[n-1].y),2)));
    }
    
  }

  float dist;
  dist = soma;
 printf("Perimetro: %.4lf\n", dist);
  }

/* Exercício 5
Elaborar um programa cuja entrada são 2 números complexos:
Utilize estrutura 
struct Ponto
{
	double R;
	double I;
};
Apresente um menu de opções com a saída selecionada.
For example:
Input	Result
1
3
3
4
1
Digite o valor da parte Real:
Digite o valor da parte Imaginaria:
1.0000 + (3.0000)i
Digite o valor da parte Real:
Digite o valor da parte Imaginaria:
3.0000 + (4.0000)i
=============
1 - Adicao
2 - Multiplicacao
3 - Divisao
4 - Modulo  z1
5 - Modulo  z2
6 - Conjugado  z1
7 - Conjugado  z2
0 - Sair
opcao =>
Adicao
Parte Real: 4.0000
Parte Imaginaria: 7.0000
4.0000 + (7.0000)i */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct Ponto
{
	double R;
	double I;
};

void leiaPonto(struct Ponto *p)
{
    printf("Digite o valor da parte Real:\n");
	scanf("%lf", &( (*p).R ) );
    printf("Digite o valor da parte Imaginaria:\n");
	scanf("%lf", &( (*p).I )  );
	printf("%.4lf + (%.4lf)i\n", (*p).R, p->I);
}

	

int menu()
{
    puts("");
    puts("=============");
    puts("1 - Adicao   ");
    puts("2 - Multiplicacao  ");
    puts("3 - Divisao  ");
    puts("4 - Modulo  z1  ");
    puts("5 - Modulo  z2  ");
    puts("6 - Conjugado  z1  ");
    puts("7 - Conjugado  z2  ");
    puts("0 - Sair  ");
    printf("opcao => ");
    int op;
    scanf("%d", &op);

    return op;
}
void produto(struct Ponto a, struct Ponto b){
    printf("\nMultiplicacao\n");
    double partR = ((a.R)*(b.R)-(a.I)*(b.I));
    double partI = ((a.R)*(b.I)+(a.I)*(b.R));
    printf("Parte Real: %.4lf\n",partR);
    printf("Parte Imaginaria: %.4lf\n", partI);
    printf("%.4lf + (%.4lf)i",partR, partI);
}

void soma(struct Ponto a, struct Ponto b){
    printf("\nAdicao\n");
    double partR = ((a.R)+(b.R));
    double partI = ((a.I)+(b.I));
    printf("Parte Real: %.4lf\n", partR);
    printf("Parte Imaginaria: %.4lf\n", partI);
    printf("%.4lf + (%.4lf)i",partR, partI );
}

void quociente(struct Ponto a, struct Ponto b){
    double partR = ((a.R)*(b.R)+(a.I)*(b.I))/(pow((b.I),2)+pow((b.R),2));
    double partI = ((a.I)*(b.R)-(a.R)*(b.I))/(pow((b.I),2)+pow((b.R),2));
    printf("Parte Real: %.4lf\n",partR);
    printf("Parte Imaginaria: %.4lf\n",partI );
    printf("%.4lf + (%.4lf)i", partR, partI );
}
void modulo(struct Ponto p){
    printf("\nModulo \n");
	printf("O modulo de %.4lf + (%.4lf)i eh %.4lf ", p.R, p.I, sqrt(pow(p.R,2)+pow(p.I,2)));
}
void conjugado(struct Ponto p){
    printf("\nConjugado\n");
    printf("Parte Real: %.4lf\n", p.R);
    printf("Parte Imaginaria: %.4lf\n", -1*(p.I));
    printf("%.4lf + (%.4lf)i", p.R, -1*(p.I) );
}
int main(void)
{
	struct Ponto z1;
	struct Ponto z2;

	leiaPonto( &z1 );
	leiaPonto( &z2 );

    int op = menu();
    if(op == 1)
    {
        soma(z1, z2);
    }
    else if(op == 2)
    {
        produto(z1, z2);
    }
    else if(op == 3)
    {
        quociente(z1, z2);
    }
    else if(op == 4)
    {
        modulo(z1);
    }
    else if(op == 5)
    {
        modulo(z2);
    }
    else if(op == 6)
    {
        conjugado(z1);
    }
    else if(op == 7)
    {
        conjugado(z2);
    }

	return 0;
  }