#Made by GLDDRK: glddrk.fr
#Importation des modules
import os
#Fonction principale et de calcul
def main():
    os.system("cls||clear")
    print("Ce programme a été créer par GLDDRK, version 1.2")
    print("Programme de calcul de note en note sur 20")
    nt = input("Quelle est votre note : "); fnt = float(nt)
    sr = input("Sur combien est votre note : "); fsr = float(sr)
    ntsr = fnt / fsr * 20; sntsr = str(ntsr)
    print("Votre note de", note, "sur", sur, "correspond à", snotesur, "/ 20")
    restart()

#Fonction qui permet de recommencer
def restart():
    a = input("Voulez vous recommencer O : oui / Autre : non ")
    if a.lower == str("o"):
        os.system("clear||cls")
        main()
    else:
        os.system("clear||cls")
        print("Mecri de m'avoir utiliser")
        exit()
main()
