# -*- coding: utf-8 -*-

MOT_LISTE = ['foo', 'bar', 'loo']
# https://www.freelang.com/dictionnaire/dic-francais.php
FILE_NAME= 'liste_francais.txt' 

import random
import os

def infos():
    print("""
            ===============================================
                            Jeu du pendu
            ===============================================
            """)


def get_mot():
    mot = input("Entrez un mot à faire deviner: \n")
    return str(mot)

def get_victoire(mot, lettres_devinees):
    check_liste = [lettres in lettres_devinees for lettres in mot]
    return all(check_liste)


def print_mot(mot, lettres_devinees):
    mot_etat = ''

    for lettre in mot:
        if lettre in lettres_devinees:
            mot_etat += lettre
        else:
            mot_etat += '_'
    
    print(mot_etat, '\n')
    print(mot)


def pendu_run(mot):
    nombre_essais = 10
    lettres_essayees = []
    lettres_devinees = []
    victoire = False

    print("Le mot contient {} lettres.".format(len(mot)))

    while (not victoire) and (nombre_essais > 0):
        print("\nIl vous reste", nombre_essais, "essais.")
        print_mot(mot, lettres_devinees)

        lettre = input("Entrez une lettre, ou le mot complet: ").lower()

        if not lettre.isalpha():
            print("""
            ===============================================
             Ceci n'est pas une lettre ou un mot valide...
            ===============================================
            """)
        elif lettre in lettres_essayees:
            print("""
            ===============================================
                 Vous avez déjà essayé cette lettre...
            ===============================================
            """)
        elif (lettre not in mot) and (len(lettre) == 1):
            lettres_essayees.append(lettre)
            nombre_essais -= 1 
            print("""
            ===============================================
                   Cette lettre n'est pas dans le mot.
            ===============================================
            """)
        elif (lettre in mot) and (len(lettre) == 1):
            lettres_essayees.append(lettre)
            lettres_devinees.append(lettre)
            print("""
            ===============================================
                              Bien joué !
            ===============================================
            """)
        elif lettre == mot:
            victoire = True
            print("""
            ===============================================
                              Bien joué !
            ===============================================
            """)
            break
        elif (len(lettre) == len(mot)) and (mot != lettre):
            print("""
            ===============================================
                     Ce n'est pas le bon mot...
            ===============================================
            """)
            nombre_essais -= 1 
        elif len(lettre) > len(mot):
            print("""
            ===============================================
                Il y a trop de lettres dans votre mot...
            ===============================================
            """)
            nombre_essais -= 1 
        elif len(lettre) < len(mot):
            print("""
            ===============================================
                Il y a pas assez de lettres dans votre mot...
            ===============================================
            """)
            nombre_essais -= 1 

        victoire = get_victoire(mot, lettres_devinees)

    if victoire:
        print("""
            ===============================================
                           Vous avez gagné !
            ===============================================
            """)
    elif nombre_essais == 0:
        print("""
            ===============================================
                           Vous avez perdu !
            ===============================================
            """)
        print("Le mot à deviner était :", mot)
    
    rejouer()



if __name__ == "__main__":
    infos()
    mot = get_mot()
    pendu_run(mot)
