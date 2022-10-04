# -*- coding: utf-8 -*-

import sys

def print_info_programme():
    """
    Affiche le nombre et le nom des arguments du programme.
    """
    print(sys.argv)
    print("à compléter")
    return

def infos():
    # Il est d'usage d’écrire une fonction
    # qui affiche que l’on est bien dans le programme et/ou donne
    # des informations sur celui-ci à l’exécution du programme.
    print("""
            ===============================================
                       Informations du programme
            ===============================================
            """)

if __name__ == "__main__":
    infos()
    print_info_programme()
