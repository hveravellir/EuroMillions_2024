

prix = [999999999999999999.99,23080009000.00,484139400.00,30174.50,1402.70,135.60,69.30,41.00,17.00,12.30,9.30,8.00,0.00,5.90,3.90,0.00]
#
for i in range(0, 16):
    chaine = prix[i] # 230000000.0 avec ("%.2f" % w) => 230000000.00
    # z = chaine # test
    chaine = "%.2f" % chaine # formate avec .00 à la fin sino il n'y en a qu'un...484139400.0 ???
    chaine = chaine[::-1] # on inverse la chaine donc chaine =eniahc
    # chaine = chaine[::-1] trouvé là => https://docs.python.org/3.12/library/stdtypes.html#str.split
    temp = ""
    compteur = 0 # Début (en fait, depuis la fin) du comptage des caractères

    for j in chaine : # On parcourt en ordre inverse
        # fonctionne jusqu'à 1000 000 000 000 000 000.00   =>Mille milliards de millions
        compteur +=1
        # temp = temp + j
        if compteur == 7 : # Ici on se trouve à 3 char après le point
            temp = temp + " " + j # placer " " au bon endroit avec un pas de 4
        elif compteur == 10 : # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        elif compteur == 13: # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        elif compteur == 16: # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        elif compteur == 19: # Ici on se trouve à 3 char plus loin
            temp = temp + " " + j
        else :
            temp = temp + j # Ici on a un nombre du type 0.00 jusqu'à 999.00

    temp = temp[::-1]

    print(temp)
    # print("La chaine à formater", z, "a été transformée en :", temp) #test


