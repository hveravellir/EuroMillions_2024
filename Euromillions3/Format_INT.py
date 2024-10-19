

prix = [999999999999999999,23080009000,484139400,30174,1402,135,69,41,17,12,9,8,0,5,3,0]
#
for i in range(0, 16):
    chaine = str(prix[i]) # 2
    # print("La chaine à formater", chaine,) # OK
    z = chaine # Test
    # w = len(chaine)
    temp = ""
    compteur = 0 # Début du comptage des caractères
    for j in reversed(chaine) : #(3, w + 1, 4):  # en ordre inverse / de la fin de la chaine jusqu'au début avec un pas de 3
        # fonctionne jusqu'à 1000 000 000 000 000 000.00   =>Mille milliards de millions
        # reversed trouvé là => https://www.docstring.fr/blog/inverser-nimporte-quel-objet-avec-python/
        # fonctionne jusqu'à 1000 000 000 000 000 000.00   =>Mille milliards de millions
        compteur += 1
        # temp = temp + j
        if compteur == 4:  # Ici on se trouve à 3 char après le point
            temp = temp + " " + j  # placer " " au bon endroit avec un pas de 4
        elif compteur == 7:  # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        elif compteur == 10:  # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        elif compteur == 13:  # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        elif compteur == 16:  # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        elif compteur == 19:  # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        else:
            temp = temp + j  # Ici on a un nombre du type 0.00 jusqu'à 999.00

        # print("compteur =",compteur,"j= ",j, "temp= ", temp)#, "chaine j", temp, "j=", j)
        # print()
        chaine = ""
    for j in reversed(temp) :
        chaine = chaine + j

    print("La chaine à formater", z, "a été transformée en :", chaine) # Test

