# -*- coding: utf-8 -*-
import sys
# import rand

denominateur = 0

# Un message d'erreur se lit de bas en haut !

def erreur0():
    """ 
    la fonction erreur0 affiche le message suivant :
    "Bravo ! Vous avez corrigé la première fonction." 
    """
    # print "Bravo ! Vous avez corrigé la première fonction." 

def erreur1():
    """ 
    la fonction erreur1 affiche le message suivant :
    "Le message s'est affiché correctement." 
    """
    # print(message)

def erreur2():
    """ 
    La fonction erreur2 
    """
    while True: 	
    	print("la condition est toujours vraie");
    	
def erreur3(n):
    """ 
    La fonction erreur3 renvoie la division du paramètre n par 10 
    """
    numerateur = n
    return numerateur // denominateur 
    	
def erreur4(n):
    """ 
    la fonction erreur4 affiche le message suivant :
    "J'étudie à l'université Paris {n}"
    """
    print("J'étudie à l'université Paris" + n)
        	
def erreur5():
    """ 
    La fonction erreur5 renvoie un entier aléatoire entre 0 et 20 
    """
    return rand.randint(0,20)
    
            	
def erreur6():
    """ 
    La fonction erreur6 affiche les nombres
    contenus dans la liste L.
    """
    L = [42, 23, 34, 2, 1, 9]
    for element in range(len(L)):
        print(element)

def erreur6():
    """ 
    La fonction erreur6 affiche les nombres
    contenus dans la liste L.
    """
    L = [42, 23, 34, 2, 1, 9]
    for element in range(len(L)):
        print(element)

def erreur7():
    """ 
    La fonction erreur7 affiche le troisième élément
    de la liste languages : "Java".
    """

    languages = ['Python', 'JavaScript', 'Java']
    print(languages[3])
    
if __name__ == "__main__":
    # help(erreurO)
    # erreur0()
    
    help(erreur1)
    # erreur1()
    
    help(erreur2)
    # erreur2()
    
    help(erreur3)
    # erreur3()
    
    help(erreur4)
    # faites afficher "J'étudie à l'université Paris 8" à la fonction erreur4 :
    # erreur4()
    
    help(erreur5)
    # erreur5()
    
    help(erreur6)
    erreur6()
    
    # help(erreur7)
    erreur7()
