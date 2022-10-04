# -*- coding: utf-8 -*-

import random

resume = []

def guess_the_number(b):
    a = 0
    nb_try = 0
    unkown_number = random.randint(a,b)
    value = -1
    while value != unkown_number:
        value = int(input("Proposez un nombre entre " + str(a) + " et "+ str(b) + " : "))
        if value < unkown_number:
	        print("Essayez encore ! Le nombre choisi est trop petit")
        elif value > unkown_number:
            print("Essayez encore ! Le nombre choisi est trop grand")
        else:
            print("C'est gagné, " + str(unkown_number) + " était le nombre à deviner.")
        nb_try = nb_try + 1
    return nb_try
            
if __name__ == "__main__":

    nb_games = int(input("Combien de parties voulez-vous jouer ? \n"))
    for i in range(nb_games):
        b = int(input("Saisissez un entier positif : "))
        nb_try = guess_the_number(b)
        print("Vous avez deviné en " + str(nb_try) + " coup(s).")
        resume.append({b : nb_try})
    for i in range(nb_games) :
        for k,v in resume[i].items() :
            print("Partie " + str(i) + " : nombre maximal à deviner = " + str(k) + " / nombre d'essais = " + str(v))
