'''
Écrivez une fonction qui écrit “Quel est votre message ?” et demande à l’utilisateur de rentrer un message tant que l’utilisateur n’a pas saisi “silence!”. Lorsque l’utilisateur saisit “silence!”, le programme affiche “D’accord.” et s’arrête.
'''
def silence():
    reponse = ""
    while reponse != "silence!":
        reponse = input("Quel est votre message ?")
    print("D'accord")

'''
Écrivez une fonction appelée concat_chaines qui prend deux chaînes en tant que paramètres et renvoie une nouvelle chaîne résultant de leur concaténation.
'''
 
def concat_chaines(chaine1, chaine2):
    return chaine1 + chaine2

'''
Écrivez une fonction appelée compter_voyelles qui prend une chaîne en tant que paramètre et renvoie le nombre de voyelles dans cette chaîne.
'''
def compter_voyelles(chaine):
    voyelles = ['a','e','i','o','u']
    longueur = len(chaine)
    compteur = 0
    for i in range(longueur):
        if chaine[i] in voyelles:
            compteur = compteur + 1
    return(compteur)
         
    
    
'''
Écrivez une fonction appelée compter_voyelles_distinctes qui prend une chaîne en tant que paramètre et renvoie le nombre de voyelles différentes dans cette chaîne.
'''
def compter_voyelles_distinct(chaine):
    voyelles = ['a','e','i','o','u']
    longueur = len(chaine)
    compteur = 0
    for i in range(longueur):
        if chaine[i] in voyelles:
            compteur = compteur + 1
            voyelles.remove(chaine[i])
    return(compteur)

'''
Écrivez une fonction appelée recap_voyelles qui prend une chaîne en tant que paramètre et renvoie le nombre d’occurrence de chacune des voyelles dans la chaîne.
'''
def recap_voyelles(chaine):
    voyelles = ['a','e','i','o','u']
    longueur = len(chaine)
    recap = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in range(longueur):
        if chaine[i] in voyelles:
            recap[chaine[i]] = recap[chaine[i]] + 1
    return(recap)

'''
Écrivez une fonction appelée generer_message qui prend un nom et un âge en tant que paramètres et renvoie un message personnalisé, par exemple, “Bonjour [nom] ! Vous avez [âge] ans.”
'''
def generer_message(nom, age):
    message = "Bonjour " + nom + " ! Vous avez " + age + " ans." 
    return(message)
    
'''
Écrivez une fonction appelée est_majuscule qui prend une lettre en tant que paramètre et renvoie True si la lettre est en majuscule, sinon renvoie False.
'''
def est_majuscule(lettre):
    return(lettre.isupper())


'''
Ecrivez une fonction appelée calcul_moyenne qui prend une liste de nombres comme paramètre et renvoie leur moyenne. La liste peut être de taille variable.
'''
def calcul_moyenne(liste):
    somme = 0
    longueur = len(liste)
    for i in range(longueur):
        somme = somme + liste[i]
    return(somme/longueur)

'''
Écrivez une fonction appelée est_palindrome qui prend une chaîne de caractères comme paramètre et renvoie True si la chaîne est un palindrome (se lit de la même manière de gauche à droite et de droite à gauche, comme “kayak” ou “Hannah”), sinon renvoie False.
'''
def est_palindrome(chaine):
    chaine_list = []
    inverse_list = []
    for i in range(len(chaine)):
        chaine_list.append(chaine[i])
    for i in range(len(chaine)):
        inverse_list.append(chaine[len(chaine) - i - 1])
    print(chaine_list)
    print(inverse_list)
    if inverse_list == chaine_list :
        return True
    else :
        return False
'''
Améliorer l’exercice précédent en écrivant une fonction appelée est_palindrome_ameliore qui ignore les espaces et la casse. Par exemple, “Eva, Can I See Bees In A Cave ?” sera considéré comme un palindrome.
'''
def est_palindrome_ameliore(chaine):
    chaine_list = []
    inverse_list = []
    exclus = [",","?"," "]
    for i in range(len(chaine)):
        if chaine[i] not in exclus :
            chaine_list.append(chaine[i].lower())
    for i in range(len(chaine)):
        if chaine[len(chaine) - i - 1] not in exclus :
            inverse_list.append(chaine[len(chaine) - i - 1].lower())
    print(chaine_list)
    print(inverse_list)
    
    if inverse_list == chaine_list :
        return True
    else :
        return False

    
#################### Programme Principal ############################

if __name__ == '__main__':
    #silence()
    resultat = concat_chaines("Bonjour ", "Alice")   
    print(resultat)
    nb_voyelles = compter_voyelles("Aaaa")
    print(nb_voyelles)
    nb_voyelles_dist = compter_voyelles_distinct("Bonjour")
    print(nb_voyelles_dist)
    recap = recap_voyelles("aeiouuuua")
    print(recap)
    message = generer_message("Alice", "34")
    print(message)
    majuscule = est_majuscule('a')
    print(majuscule)
    majuscule = est_majuscule('A')
    print(majuscule)
    moyenne = calcul_moyenne([1,2,3])
    print(moyenne)
    palindrome = est_palindrome("bonjour")
    print(palindrome)
    palindrome = est_palindrome("hannah")
    print(palindrome)
    palindrome_ameliore = est_palindrome_ameliore("bonjour")
    print(palindrome_ameliore)
    palindrome_ameliore = est_palindrome_ameliore("Eva, Can I See Bees In A Cave ?")
    print(palindrome_ameliore)
