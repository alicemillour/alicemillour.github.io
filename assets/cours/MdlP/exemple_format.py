# -*- coding: utf-8 -*-

import sys

def message_cours():
    print("""
            ===============================================
                       Fonction message_cours
            ===============================================
            """)

    name = input("nom : ")
    date = input("aujourd'hui, nous sommes le : ")
    duree_du_cours = input("la durée du cours est de (en heures) : ")

    print('Le {} octobre, {} aura passé {}h dans la salle J001.'.format(date,name,duree_du_cours))
    
def affiche_jours():
    print("""
            ===============================================
                        Fonction affiche_jours
            ===============================================
            """)
    lundi = "lundi"
    mardi = "mardi"
    mercredi = "mercredi"
    jeudi = "jeudi"
    vendredi = "vendredi"
    samedi = "samedi"
    dimanche = "dimanche"
    print('{} précède {}, {}, {}, {}, {} et {}.'.format(lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche))
    
    
def affiche_jours_compact():
    print("""
            ===============================================
                    Fonction affiche_jours_compact
            ===============================================
            """)

    jours = "Lundi mardi mercredi jeudi vendredi samedi dimanche"
    liste_jours = jours.split()
    print(liste_jours)
    print('{} précède {}, {}, {}, {}, {} et {}.'.format(*liste_jours))
    
if __name__ == "__main__":
    #message_cours()
    #affiche_jours()
    affiche_jours_compact()
