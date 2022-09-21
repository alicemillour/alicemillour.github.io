# -*- coding: utf-8 -*-

# liste des multiples de 3
L_mult3=[3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93]

def is_mult3_liste(n):
    # implémentation premier algorithme
    if n in L_mult3:
        print("%d est un multiple de 3"%n)
    else:
        print("%d n'est pas un multiple de 3"%n)


def is_mult3_reste(n):
    # implémentation deuxième algorithme
    if n%3==0:
        print("%d est un multiple de 3"%n)
    else:
        print("%d n'est pas un multiple de 3"%n)


### Programme principal

if __name__ == "__main__":
    print("Programme MdP_demo.py")
    n=7
    print("calcul du résultat par la première méthode :")
    is_mult3_liste(n)
    print("calcul du résultat par la seconde méthode :")
    is_mult3_reste(n)
