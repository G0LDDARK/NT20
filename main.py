# Made by GLDDRK
# Importationd des modules
import os

# Fonction qui initalise le script
def main():
    os.system("clear||cls")
    print("Ce programme a été créer par GLDDRK, version 1.1")
    print("Bienvenue sur les calculateur de note sur 20 et de pourcentage")
    PN = input("Quel fonctionnalité du programme voulez vous utiliser? P pour Poucentage, N pour Note")
    if PN.lower() == str("n"):
        note()
    elif PN.lower() == str("p"):
        pourcentage()
    else:
        print(PN, "n'est pas un choix possible!")
        main()

# Fonction qui calcule la note
def note():
    note = input("Quelle est votre note : "); fnote = float(note)
    sur = input("Sur combien est votre note : "); fsur = float(sur)
    notesur = fnote / fsur * 20; snotesur = str(notesur)
    print("Votre note de", note, "sur", sur, "correspond a", snotesur, "/ 20")
    restart()

# Fonction qui calcule le pourcentage
def pourcentage():
    cb = input("Combien : "); fcb = float(cb)
    sur = input("Sur combien : "); fsur = float(sur)
    pr = fcb / fsur * 100; spr = float(pr)
    print(cb, "sur", sur, "représente", pr, "%")
    restart

# Fonction qui permet de recommencer
def restart():
    r = input("Voulez vous recommencer O : oui / Autre : non ")
    if r.lower == str("o"):
        os.system("clear||cls")
        main()
    else:
        os.system("clear||cls")
        print("Mecri de m'avoir utiliser")
        exit()

main()
#Калашников