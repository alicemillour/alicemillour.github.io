# -*- coding: utf-8 -*-

import sys

def print_info_programme():
    """
    Affiche le nombre et le nom des arguments du programme.
    """
    argc = len(sys.argv)
    print("La ligne de commande contient {} argument(s) :\n".format(argc))

    liste_arguments_str = (argc-1) * "\n\t- {}"
    liste_arguments_val = sys.argv[1:argc]

    liste_arguments = liste_arguments_str.format(*liste_arguments_val)
    print("- Le premier argument (indice 0) est le nom du script : {}".format(sys.argv[0]))
    
    if argc == 1:
        pass
    elif argc == 2:
        print("- L'autre argument est :".format(sys.argv[0]) + liste_arguments)
    else:
        print("- Les autres arguments sont :".format(sys.argv[0]) + liste_arguments)

def infos():
    print("""
            ===============================================
                       Informations du programme
            ===============================================
            """)

if __name__ == "__main__":
    infos()
    print_info_programme()
