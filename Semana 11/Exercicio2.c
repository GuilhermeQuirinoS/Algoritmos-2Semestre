#include <stdlib.h>
#include <stdio.h>
#include <math.h>


void repete (int[],int,int,int);

int main(){
    int n;
    scanf("%d",&n);
    int vetor[n];
    int temp;
    for(int i=0;i<n;i++){
        scanf("%d",vetor+i);
        //printf("%d",vetor[i]);
    }
    
     for (int i = 0; i < n; i++) {     
         for (int j = i+1; j < n; j++) {     
          if(vetor[i] > vetor[j]) {    
              temp = vetor[i];    
              vetor[i] =vetor[j];    
              vetor[j] = temp;    
          }     
  }
     }
//for(int i=0;i<n;i++){
     //   printf("%d",vetor[i]);
    //}
    repete(vetor,0,n,1);
}
/*
void repete (int v[],int pos,int total){
    int auxiliar = v[pos];
    int conta=0;
if (pos>total-1){
        return;}
    
    for(int i=pos;i<total;i++){
        if (v[i]!=auxiliar){
            break;
        }
        conta+=1;
    }
    
    
    printf("%d aparece %d vez(es)\n",v[pos],conta);
   // printf("%d\n",pos);
   return repete(v,pos+conta,total);
    
}*/
void repete (int v[],int pos,int total, int conta){
    
if (pos>total-1){
        return;}
    
    if (v[pos]!=v[pos+1]){
printf("%d aparece %d vez(es)\n",v[pos],conta);
   // printf("%d\n",pos);
        return repete(v,pos+1,total,1);
    }
    
    
    
   return repete(v,pos+1,total,conta + 1);
    
}

//printf("%d aparece %d vez(es)\n", v[j-1], p);