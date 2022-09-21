#include <stdio.h>

/* déclaration */
void is_mult3_liste(int n);
void is_mult3_reste(int n);

/* implémentation */
void is_mult3_liste(int n){
  int L[33] = {3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99}; 
  int arrLen = sizeof L;
  
  int isElementPresent = 0;
     
  for (int i = 0; i < arrLen; i++) {
    if (L[i] == n) {
      isElementPresent = 1;
      break;
    }
  }
  
  if (isElementPresent == 1){
    printf("%d est un multiple de 3\n", n);
  }
  else{
    printf("%d n'est pas un multiple de 3\n", n);
  }
}

void is_mult3_reste(int n){
  if (n % 3 == 0){
    printf("%d est un multiple de 3\n", n);
  }
  else{
    printf("%d n'est pas un multiple de 3\n", n);
  }
}

/* Programme principal */

int main() {
  int n=100;
  printf("Programme MdP_demo.c");
  printf("calcul du résultat par la première méthode :\n");
  is_mult3_liste(n);
  printf("calcul du résultat par la seconde méthode :\n");
  is_mult3_reste(n);
  return 0;
}
