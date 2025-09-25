import random

'''
Exécutez ce fichier. Que fait-il ? Modifiez-le pour rajouter l'option de réviser la division.
'''


def revision(nb):
    print("\n---------------\nDébut de la révision :\n---------------\n")

    L_rep = []
    L_quest = []
    L_attendu = []
    score = 0
    for i in range(int(nb)):
        number1 = random.randrange(10)
        number2 = random.randrange(10)
        L_quest.append((number1, number2))
        val = input("Quel est le résultat de {} x {} ? ".format(number1, number2))
        L_rep.append(val)
        attendu = number1 * number2
        L_attendu.append(attendu)
        if int(val) == attendu:
            score += 1
            print("Bravo !")
        else:
            print("Raté !")
    print("\n---------------\nBilan :\n---------------\n")
    
    for i in range(int(nb)):
        print("{} : {} x {}, réponse donnée : {}, réponse attendue : {} \n".format(i, L_quest[i][0], L_quest[i][1], L_rep[i], L_attendu[i]))
    print("score : {}".format(score))
        
if __name__ == "__main__":
    nb_mult = input("Combien de multiplication(s) voulez-vous faire ? ")
    revision(nb_mult)
