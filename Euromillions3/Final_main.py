#___________________Import des modules______________________
from doctest import debug
from tkinter.messagebox import showinfo

import pyautogui
from tkinter import *
from PIL import ImageTk, Image
import random  # CQFD
import time  # dates et heures
import sys
import time  # dates et heures
import datetime # Formatage dates
import tkinter
from timeit import default_timer
# from tkinter.messagebox import *
from PIL.ImageOps import expand
#_____________________________________Info & Tutos_________________________________________
# Alt 0128 sur le clavier numérique = €
# Infos ALERTES avec "tkinter" tuto là=> https://www.youtube.com/watch?v=CeoSsIYQ2vU


#__________________________________________Funct° Tirage _______________________
def graine(): # mieux que "random.seed ()"
    g = 0
    secondes = []
    secondes = time.localtime()
    secondes = (secondes[5])  # les secondes de maintenant
    g = g + int(secondes)
    g = g + random.randint(100,940)  # nouvelle graine pour chaque appel à f° mélange ; issue du hasard de la f°
                                            # graine + randint entre 101 et 999
    return g

def tirage_gagnant():   # _______Tirage gagnant___________________________
    # global boules_5, etoiles_2, e_boules_5, e_etoile_2
    global boules, etoiles, g, e_boules_5, e_etoile_2
    boules = []  # liste de 50 boules
    etoiles = []
    g = 0  # graine
    # n = []
    secondes = []
    g = graine()
    for i in range(1, 51):  # Liste ordonnée de 1 à l
        boules.append(i)  # Ajout de la valeur de i en position i de la liste
    # 12 étoiles
    # etoiles= [] # liste de 12 étoiles
    for i in range(1, 13):  # Liste ordonnée de 1 à l
        etoiles.append(i)  # Ajout de la valeur de i en position i de la liste
    # ici j'ai les listes boules[1-50] et etoiles [1-12]
    # On passe au calcul du tirage GAGNANT avec la fonction melange

    boules_5 = []  # Dans ces 2 listes nous allons ranger les boules
    etoiles_2 = []  # et les étoiles gagnantes
    # ________________________Tirage de 5 boules plus 2 étoiles suposées être la combinaison gagnante_____________________________
    # appel de la fonction melange
    boules_5: list = melange(boules, 5, g)  # 3 Arguments
    etoiles_2: list = melange(etoiles, 2, g)  # 3 Arguments
    # _______________________________Conversion en e_Ensemble pour le FUTUR ___________________________________
    e_boules_5 = set(boules_5)  # Conversion en e_Ensemble pour les futures comparaisons avec les tirages d'essais
    e_etoile_2 = set(etoiles_2)  # Conversion en e_Ensemble

    # Ici nous avons 2 listes boules_5 composée de 5 boules parmis 50 et etoiles_2 composée de 2 étoiles parmis 12
    # sous forme de str
    # Ce qui nous donne le tirage gagnant de référence

    # ___________________________AFFICHAGE dans fen_______________________________________
    # Affichage du tirage gagnant de référence dans les cercles bleus et dans les étoiles jaunes
    # (x=174, y=88) # centre premier cercle bleu puis "pas" pixels entre chaque cercle    #
    # print(boules_5, etoiles_2) # Test CTRL
    xytuple = ([[174,88],[238,88],[302,88],[368,88],[432,88],[519,95],[591,95]])
    for i in range(0,5):
        x1 = xytuple [i] [0] # On pioche dans la liste a 2D
        y1 = xytuple [i] [1]
        var = boules_5[i]
        var1 = str(var)
        if (len(var1)) == 1:  # si 1 seul caractere
            var1 = " " + var1 + " " # on le centre
        var1 = Label(fen, text=var1, font=("Arial Black", 17), bg="#234187", fg='white')
        var1.place(x = x1, y=y1)

    for i in range(5, 7):
        x1 = xytuple[i][0]
        y1 = xytuple[i][1]
        var = etoiles_2[i-7] # Petite correction pour ne pas faire une autre boucle sur une autre liste de 2 valeurs
        var1 = str(var)
        if (len(var1)) == 1:  # si 1 seul caractere
            var1 = " " + var1 + " " # on le centre
        var1 = Label(fen, text=var1, font=("Arial Black", 13), bg="#FBB941", fg='red')
        var1.place(x=x1, y=y1)
    # ________________________Affichage Info RANDOM___________________________
    info_tirage = Label(fen, text="   TIRAGE obtenu \navec " + str(g) + " random\n        par chiffre           ",
                        font=("arial black", 10), bg='#374C9D', fg='white')
    info_tirage.place(x=640, y=74)  # x=640, y=74
    # ____________________________________________________________________________________________


def melange(nom, nb, g):  # Fonction 3 paramètres nom= de la liste nb= 5 ou 2 étoiles, retourne une liste triée n
    # Cette f° mélange g fois la liste en parametre "nom", puis retourne dans n les nb premieres valeurs, 5 ou 2,
    n = []
    # g = g + graine1
    # print ("Randomisé", (g),"fois pour le tirage",txt)
    for i in range(1, g + 1):
        random.shuffle(nom)  # Mélange de la liste graine fois
        # print (nom) # cf console pour verification
        n = sorted(nom[0:nb])  # retourne la liste n triée
        # print(i)  # c'est le nb de random
        #   print (n) # cf console pour verification
    return n



# __________________________________________Funct° Timer  à supprimer_______________________
def updateTime():
    global str_time
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours,minutes = divmod(minutes,60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    canvas.itemconfigure (text_clock, text = str_time)
    # fen.after(1000, updateTime) # Ici on affiche


# __________________________________________Funct° action _______________________
def action(envent):
    # nb_get = tkinter.IntVar()
    global N
    # N = tkinter.StringVar()
    N = int(nb_get.get())

    # val.config( state="disabled")
    # nb_get.delete(0, END)
    N_str = format_integer(str(N)) # N_str pour affichage et N pour les calculs
    lblNombre = tkinter.Label(fen, text="Vous avez choisi\nde tenter votre chance \navec " + N_str + " tirages ", font=("arial", 13), bg='#374C9D', fg='white')
    lblNombre.place(x=223, y=7)
    # txt_nb_tirages = Label(fen, text="Vous avez choisi\nde tenter votre chance \navec  " + str(N) + " tirages ", font=("arial black", 11), bg='#374C9D', fg='white')
    # txt_nb_tirages.place(x=230, y=1)
    # ____________________________________________________________________

    debut()
def debut():
    # tirage_gagnant()
    # global boules_5, etoiles_2, e_boules_5, e_etoile_2
    global compteur, e_tirages, e_boules_5, e_etoile_2my

    now = default_timer() - start
    myDateTime1 = datetime.datetime.now()  # On sauvegarde now pour calculer tmps_calc
# _________________________________________Ici on vient d'afficher le tirage gagnant CAD
# ______ 2 listes : boules_5 et etoiles_2 copiées dans 2 ensembles e_boules_5 et e_etoiles_2
    # def les_jeux_sont_faits():
    gains_totaux = 0  # init
    compteur = N # N = le Nb de tirages pour tenter de gagner, compteur = les resultats perdants
    for i in range(1, N + 1):  # Construction de N grilles de 5 boules et 2 étoiles d'un hypothétique joueur

        # nb_tirages = tkinter.Label(fen, text=str(i)) #
        # nb_tirages.place(x=10, y=20) # ici
        tirages = melange(boules, 5, g)  # Tirage de 5 boules
        e_tirages = set(tirages)  # Conversion des nb boules en e_Ensemble d'un joueur
        #____Ici on a une tentative de 5 boules
        # print ("tirage:", (i), e_tirages)
        # txt = "des **"
        etoile = melange(etoiles, 2, g)  # Tirage de 2 étoiles
        e_etoile = set(etoile)  # Conversion des nb étoiles en e_Ensemble d'un joueur
        # ____Ici on a une tentative de 2 étoiles

        # print ("tirage:", (i), e_tirages, "étoiles ", e_etoile) # REM les ensembles ne peuvent pas être triés
        # print ("tirage:", (i), tirages, "étoiles ", etoile)
        # __________________________Ici on a 4 listes et 4 ensembles identiques entre eux_________
        # _____________________Je crée une suite de conditions pour vérifier les gagnant que je rangerai dans un tabeau
        # la fonction 'intersection' entre 2 ensembles retoune combien et quels sont les boules et/ou étoiles identiques
        # _______________________________________________________________________________________

        e_boules_gagnantes: set = e_boules_5 & e_tirages  # Intersection = boules en commun entre le N° gagnant et les N° du joueur
        e_etoiles_gagnantes: set = e_etoile_2 & e_etoile
        # nb_boules_gagnantes = len(e_boules_gagnantes) # Utilisé dans les case plus loin
        # nb_etoiles_gagnantes = len(e_etoiles_gagnantes) # Utilisé dans les case plus loin


        match len(e_boules_gagnantes):
            case 0:
                nb_boules_gagnantes = len(e_boules_gagnantes)
                # print(str(nb_boules_gagnantes)+" boules gagnantes ")
                # print(e_boules_gagnantes)
                b_resultat = 0
                # titre_0 = Label(fen, text= e_etoile, font=("Arial Black", 11), bg="white", fg='#374C9D')
                # titre_0.place(x=128, y=655)  # en haut # titre.pack(expand=YES) # texte au millieu de la fenetre

            case 1:
                nb_boules_gagnantes = len(e_boules_gagnantes)
                # print(str(nb_boules_gagnantes)+" boules gagnantes ")
                # print([e_boules_gagnantes])
                b_resultat = 10

            case 2:
                nb_boules_gagnantes = len(e_boules_gagnantes)
                # print(str(nb_boules_gagnantes) + " boules gagnantes ")
                # print([e_boules_gagnantes])
                b_resultat = 20

            case 3:
                nb_boules_gagnantes = len(e_boules_gagnantes)
                # print(str(nb_boules_gagnantes) + " boules gagnantes ")
                # print([e_boules_gagnantes])
                b_resultat = 30
                txt = ""
            case 4:
                nb_boules_gagnantes = len(e_boules_gagnantes)
                # print(str(nb_boules_gagnantes) + " boules gagnantes ")
                # print([e_boules_gagnantes])
                b_resultat = 40
            case 5:
                nb_boules_gagnantes = len(e_boules_gagnantes)
                # print(str(nb_boules_gagnantes) + " boules gagnantes ")
                # print([e_boules_gagnantes])
                b_resultat = 50
        match len(e_etoiles_gagnantes):
            case 0:
                nb_etoiles_gagnantes = len(e_etoiles_gagnantes)
                # print(str(nb_etoiles_gagnantes) + " etoiles gagnantes ")
                # print([e_etoiles_gagnantes])
                e_resultat = 0
            case 1:
                nb_etoiles_gagnantes = len(e_etoiles_gagnantes)
                # print(str(nb_etoiles_gagnantes) + " etoiles gagnantes ")
                # print([e_etoiles_gagnantes])
                e_resultat = 1
            case 2:
                nb_etoiles_gagnantes = len(e_etoiles_gagnantes)
                # print(str(nb_etoiles_gagnantes) + " etoiles gagnantes ")
                # print([e_etoiles_gagnantes])
                e_resultat = 2
        # if resultat >= 21 :
        #     print(boules_5,etoiles_2)
        #     print("resultat : ", resultat)
        #     # time.sleep(5)
        resultat = b_resultat + e_resultat
        # print("resultat :", resultat)
        if resultat < 12 or resultat == 20: # C'est perdu
            compteur -= 1  # On soustrait 1 au Nb de tirages = Nb de tirages gagnants
            # print(boules_5,etoiles_2)
            # print("Perdu < 12 ou ==20 : ", resultat)
        else : # C'est gagné
            # print("resultat : ", resultat)
            # print("C'est gagné le résultat est >11 ", resultat)

            # print(boules_5, etoiles_2)
            # print("resultat :")
            #
    #______________ traitement du resultats dans la double liste result_lst [0] [1]
            a = (result_lst[0].index(resultat)) # On stocke +1 dans la liste des gagnants 3 boules + 2 étoiles resulat = 32
            # print(len(result_lst))
            result_lst[1][a] +=1 # un gagnant de plus

            # print("The index of element " + str(resultat) + " is ", result_lst[0].index(resultat))
            # print("The index of element " + str(resultat) + " is ", result_lst[1].index(resultat))
    # print(result_lst[1])
    for i in range(0,15) : # Nb de lignes pour les résultats
        gagne = format_integer(str(result_lst[1][i]))
        coord_xy = tkinter.Label(fen, text=gagne, font=("arial black", 11), fg="#374C9D")
        coord_xy.place(x= calcule_x(0,gagne,9.5), y=ytuple[i])  # 128 = colonne 0
        # coord_xy.place(x = 128, y = ytuple[i]) # 128 = colonne 0
    # _________________Affichage des gains pour une grille gagnante____________________________
    for i in range(0, 15):  # Nb de lignes pour les grilles
        gain = (gain_par_grille[0][i] * result_lst[1][i]) # Le gain par grille * par le nb de grilles gagnées
        gains_totaux = gains_totaux + gain # tester ce calcul !!!
        gain = ("%.2f" % gain) # "%.2f" % formate un fload à 2 décimales
        # Ici on formate la chaine pour rendre plus lisibles les milliars ha !! ha!!
        gain = format_float(str(gain))
        gain = gain + "€"
        coord_xy = tkinter.Label(fen, text = gain, font=("arial black", 11), fg="#374C9D") # "%.2f" % Formate fload 2 décimales
        coord_xy.place(x=calcule_x(5,gain + "€",9.5), y=ytuple[i])  # 640 = dernière colonne
        # coord_xy.place(x=640, y=ytuple[i])  # 640 = dernière colonne

    mise_initiale = N*2.5 # 2.5 euros par grille
    # test
    # les variables affichées ci-dessous sont formatées par les f° format_float ou format_integer suivant leur type
    # l'intruction ("%.2f" % variable_float) complete les décimales des float qui ne s'affichent qu'avec .0 et non .00 et c'est un grand mystère....
    info_label = tkinter.Label(fen, text= format_integer(str(compteur)) + " Tirages gagnants et " + format_integer(str(N-compteur))
                + " tirages perdants sur : "
                  + format_integer(str(N))+ " tirages au total\n" + "Soit " + format_float(str("%.2f" % gains_totaux)) +" € de gagnés"
                " pour une mise initiale de : " + format_float(str("%.2f" % mise_initiale)) +" €", font=("arial black", 12), fg="#374C9D")
    info_label.place( x= 28, y = 655)

    # date = time.localtime()
    # date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    # print(date)

    tmps_calc = str(datetime.datetime.now() - myDateTime1) # On calcule le temps passé
    # Ici formatage de str(td) = tmps_calc = XX h XX mn XX s
    tmps_calc = tmps_calc[:-6] # supprime les 6 derniers caracteres cad les microsecondes et je garde le point
    tmps_calc = tmps_calc.replace(":", "h ",1) # 1ere occurence de : remplacé par h
    tmps_calc = tmps_calc.replace(":", "min ", 1) # tjs 1ere occurence de : remplacé par min
    tmps_calc = tmps_calc.replace(".", "s", 1) # remplace le point par secondes
    # date = (str(date[2]) + "/" + str(date[1]) + "/" + str(date[0]) + " à " + str(date[3]) + "H " + str(date[4]) + "mn " + str(date[5]) + "sec")
    date = Label(fen, text="Calculs réalisés en : " + tmps_calc, font=("Arial Black", 11), bg="#374C9D", fg='white')  # date heure mn s
    date.place(x=28, y=710)

    # print("Fin de Match/Case ", compteur, "Tirages gagnants sur", N) # Test

    #______________________________Et maintenant on  affiche pour sauvegarder écran_____________________________________
    Valider = tkinter.Button(fen, text="Sauvegarder une\ncopie d'écran", font=("Arial Black", 11), bg="#374C9D", fg="aqua", command=copie_ecran)
    Valider.place_configure(x=xtuple[5], y=710, width=150, height=50)
    # _________________Ici on ouvre un message BOX pour informer de la fin du PRG_________________
    showinfo("                             Fin du PRG", "        Euromillions Release 1.0\nBuild platform: 64-bit x86 Windows\n    Written using PyCham 2024.2.3\n© 2024-C4P Cr0CH37. All rights reserved.")
#_____________________________________Copie d'écran dans le Rep. Screenshots du dossier en cours_______________________________________
# crée un fichier unique du type 10 000_tirages du 2024-10-18_22_44_21.jpg
#____________________________date et heure du jour + Nb de tirages______+extension .jpg_____________

def copie_ecran (): # Eventuellement utiliser option r"/à@ etc...." pour le chemin => "E:\Euromillions\ScreenShoot_Resultats"
    date = []
    date = time.localtime()
    nom_screenshot = ("Screenshots/" +  str(date[0]) + "-" + str(date[1]) + "-" + str(date[2]) + "_" + str(date[3]) +  str(date[4]) + str(date[5]) +format_integer(str(N)) + "_tirages.jpg")
    # print(nom_screenshot) test

    reg_ghlh = ("1010", "100", "794", "900") # reg = region pour la copie ghlh=>pour=>gauche haut largeur hauteur
    screen = pyautogui.screenshot(region=(int(reg_ghlh[0]),int(reg_ghlh[1]),int(reg_ghlh[2]),int(reg_ghlh[3])))
    # Copie la zone d'écran cf. tuple reg_ghlh [0,1,2,3]
    screen.save(nom_screenshot) #

    # print(resultat)
#____ Ici 15 valeurs possibles dans resultat______________
# 52,51,50,42,41,32,40,22,31,30,12,2,21,20,1 # gagnent qq chose mais 1 et 20 sont perdants
# 0,11,10 ne sont pas pris en compte dans la matrice (grille jpg), mais sont comptabilisés comme perdants avec 1 et 20

def coor_aff(): # Ici on stoke dans deux tuples xtuple, ytuple les coordonnées d'affichage pour bgrnd "Res_Euromillions_OK1.jpg"
    global xtuple, ytuple, ztuple,larg_col_tuple, result_lst, gain_par_grille # pour plus tard
    # result_lst double liste avec la variable resultats & nb de tirages gagnants dans le même ordre
    result_lst = [[52,51,50,42,41,32,40,22,31,30,12,2,21,20,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]] # [176,208,240,272,303,335,368,399,430,461,493,525,557,589,620] dans la 2ème liste on incrémente les tirages gagnants
    gain_par_grille = [[230000000.00,4413400.00,30174.50,1402.70,135.60,69.30,41.00,17.00,12.30,9.30,8.00,0.00,5.90,3.90,0.00],[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]]

    # valeur de resultat (ex: 32 =3 boules + 2 étoiles) à placer dans la colonne 0 cad 128
    # en fonction du rang dans result_tuple on trouve la ligne par ex: si result 52=rang 0 alors ligne 176 = rang 0 de ytuple
    ytuple = (176,208,240,272,303,335,368,399,430,461,493,525,557,589,620,655) # coordonnées des 16 lignes de l'axe des Data des Lignes Boules & étoiles
    xtuple = (128,218,322,394,543,640) # idem pour les Colonnes
    #__________________________Valeurs auxilières de correction et de calcul_________________________________
    ztuple = (9,29,49,59,69,79,79,79,79,89,89,89,89,89,89) # Aligne les val ds la colonne 3 => xtuple[405] à D pour les gains par grille
    larg_col_tuple = (80,94,71,135,85,140) # Largeur des col pour placer le txt (80,94,71,139,85,125)

    # for i in range(0, len(ytuple)): # CTRL de remplissage toutes les case pour test de validation des data
    #     for j in range(0, len(xtuple)):
    #         ylab_coord = str(ytuple[i]) #
    #         xlab_coord = str(xtuple[j])
    #         # print("x =", xlab_coord, "y =", ylab_coord) # CTRL
    #         coord_xy = tkinter.Label(fen,text = xlab_coord + "X" + ylab_coord, font=("arial", 10), fg = "black")
    #         coord_xy.place(x = xtuple[j], y = ytuple[i])

    # return
#______________________________________Calcule_x__________________________________________________
# reçoit 3 paramètres : la colonne où on veut afficher, la chaine qu'on veut afficher
# la largeur en pixels d'un caractère en fonction de la police ici 11 qui est 9.5 ou police 9 qui est 7.2
def calcule_x (colonne,chaine,larg_police) :
    w = len(chaine)*larg_police # 9.5 = police 11 ou 7.1 police 9 longeur du chiffre en pixels
    w = xtuple[colonne]+((larg_col_tuple[colonne]) - w)
    return w # retourne la coordonnée x pour aligner à Droite les valeurs dans les cases de la colonne

#__________________________format_float________________________________________________
# Ici on formate la chaine pour rendre plus lisibles les milliars ha !! ha!!
def format_float(chaine): # reçoit la chaine à formater ex : 230000000.00 donnera => 230 000 000.00

        # chaine = "%.2f" % chaine  # formate avec .00 à la fin sino il n'y en a qu'un...484139400.0 ???
        chaine = chaine[::-1]  # on inverse la chaine donc chaine = eniahc
        # chaine = chaine[::-1] trouvé là => https://docs.python.org/3.12/library/stdtypes.html#str.split
        temp = ""
        compteur1 = 0  # Début (en fait, depuis la fin) du comptage des caractères

        for j in chaine:  # On parcourt en ordre inverse
            # fonctionne jusqu'à 1000 000 000 000 000 000.00   =>Mille milliards de millions
            compteur1 += 1
            # temp = temp + j
            if compteur1 == 7:  # Ici on se trouve à 3 char après le point
                temp = temp + " " + j  # placer " " au bon endroit avec un pas de 4
            elif compteur1 == 10:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 13:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 16:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 19:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 22:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 25:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 28:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 31:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            else:
                temp = temp + j  # Ici on a un nombre du type 0.00 jusqu'à 999.00

        chaine = temp[::-1]
        return chaine

#________________________________________________format_integer___________________________________
# Ici on formate la chaine pour rendre plus lisibles les milliars ha !! ha!
def format_integer(chaine):
    for i in range(0, 16): # reçoit la chaine à formater ex : 230000000 donnera => 230 000 000
        temp = ""
        compteur1 = 0 # Début du comptage des caractères
        for j in reversed(chaine) : #:  # en ordre inverse / de la fin de la chaine jusqu'au début avec un pas de 3
            # fonctionne jusqu'à 1000 000 000 000 000 000   =>Mille milliards de millions
            # reversed trouvé là => https://www.docstring.fr/blog/inverser-nimporte-quel-objet-avec-python/
            # fonctionne jusqu'à 1000 000 000 000 000 000   =>Mille milliards de millions
            compteur1 += 1
            # temp = temp + j
            if compteur1 == 4:  # Ici on se trouve à 4 char
                temp = temp + " " + j  # placer " " au bon endroit
            elif compteur1 == 7:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 10:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 13:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 16:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 19:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 22:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 25:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            elif compteur1 == 28:  # Ici on se trouve à 3 char plus loin
                temp = temp + " " + j
            else:
                temp = temp + j  # Ici on a un nombre du type 0.00 jusqu'à 999.00

            chaine = ""
        for j in reversed(temp) :
            chaine = chaine + j
        return chaine

# _____________________Premières INSTRUCTIONS du PRG_______________________
global boules_5, etoiles_2, e_boules_5, e_etoile_2, nb_get, compteur, date

# ______________________Partie principale du PRG _________________________


fen = Tk()
fen.title("EuroMillions")

# fen.iconbitmap("Loto.ico") # Icone coin H/G fenetre Déplacé plus loin car affiche une fenetre indésirable

#__________________Importation de l'image____________________________________
# Ici je crée un tuple "reg_ghlh" gauche haut largeur hauteur
# reg_ghlh = ("1000", "70", "794", "899", "+", "x") pour constuire la str placement
# qui place la fenêtre sur l'écran
# plus tard j'utilise ses coordonnées pour faire une copie d'écran avec
# screen = pyautogui.screenshot()

bgrnd = ImageTk.PhotoImage(Image.open("Res_Euromillions.jpg"))  # 1280x1895
reg_ghlh = ("1000", "70", "794", "899", "+", "x")
placement = reg_ghlh[2] + reg_ghlh[5] + reg_ghlh[3] + reg_ghlh[4] + reg_ghlh[0] + reg_ghlh[4] + reg_ghlh[1]
fen.geometry(placement)
# fen.geometry("794x899+1000+70")  # 720x420 = Dimensions+1000+70 = Placement sur l'écran"
lblbgrnd = Label(fen, image = bgrnd)
lblbgrnd.place(x=0, y=0)  # Affiche le fond d'écran
date = []
date = time.localtime()
#____________________________Appel timer____________________________________________
canvas = Canvas(fen,width=80,height=30,bg="white")  #(#374C9D") # width= largueur,height= hauteur
# tps_passe =   #"en =>" + str_time
# canvas.place(x=405, y=700) #(x=xtuple[3], y=700) # affichage
# canvas.pack(padx=10,pady=400)
start = default_timer()
text_clock = canvas.create_text(40,15, font=("arial black", 12), fill="aqua") # coord du txt dans la boite, font, fill = couleur
updateTime() # Ne s'affiche pas pdt
#_________________________________________________________________________________

# ______________________________________________Habillage de bgrnd___________________________________

date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
date = Label(fen, text="Résultat du tirage du :\n" + date, font=("Arial Black", 17), bg="#374C9D", fg='white')  # date heure mn s
date.place(x=400, y=2) # ANC x=391, y=2

titre = Label(fen, text="Tirage supposé\ngagnant ", font=("Arial Black", 13), bg="white", fg='#374C9D')
titre.place(x=4, y=78)  # en haut # titre.pack(expand=YES) # texte au millieu de la fenetre
# ______________________Habillage de bgrnd____________________________
coor_aff () # TEST = remplit la grille jpg avec les coordonnées respectives
tirage_gagnant() # Tire et affiche le tirage gagnant dans les cercles bleus et étoiles
#___________________________________txt explicatif en bas_________________________________________
txt_explicatif = ("Bienvenu dans ce PRG qui simule des tirages d'Euromillion.\nIl fait un premier tirage de 5 N° compris entre 1 et 50, "
                  "puis 2 N° étoiles compris entre 1 et 12\nCe tirage est considéré comme la grille gagnante.\nLe PRG procède ensuite à un nombre"
                  " de tirages que vous aurez décidé.\n"
                  "Ces tirages à 2.50€ chacun visent à s'approcher du tirage initial, jusqu'au nombre que vous avez choisi.\n"
                  "Pour 10 000 essais la durée des calcules est d'environ 1mn 30s.\nVous avez une chance de gagner sur 139 838 160"
                  "\nsoit une probabilité de 0,00000000715 de ganger le gros lot.")
txt = Label(fen, text = txt_explicatif, font=("Arial Black", 10, "italic"), bg="white", fg='#374C9D' )
txt.place(x = 10, y = 750)
#________________________________________Affichage des gains pour une grille gagnante____________________________
for i in range(0, 15):  # Nb de lignes pour les grilles
    col = 3 # colonne d'affichage
    gain = format_float("%.2f" % gain_par_grille[0][i]) # "%.2f" % formate un fload à 2 décimales
    gain = gain + "€"
    coord_xy = tkinter.Label(fen, text= gain, font=("arial black",10), fg="#374C9D")
    coord_xy.place(x = calcule_x(3,gain,7.8) , y = ytuple[i])  # 405 = début du 1er pixel de la colonne 3
    # coord_xy.place(x = (405+ztuple[i]), y = ytuple[i]) # 405 = début du 1er pixel de la colonne 3

#_________________________________________Widgets Nb Tirages______________________________________
# Ecrire un "Tant que nb_get >0 faire sinon retour et message"
lblNombre = tkinter.Label(fen, text="Entrez le Nb de tirages\nque vous voulez tenter : ", font=("Arial Black", 10), bg="#374C9D", fg='white' )
lblNombre.place(x=220, y=2)
nb_get = Entry(fen, width = 15, font=("Arial Black", 10), bg="white", fg='#374C9D') # minvalue= 1, maxvalue = 50 ne marche pas
nb_get.insert(0,"10_000") # 10000= val par Default txt value 9 999 999 max taille du champs TENTER avec SPINBOX ou un OBSEVER
nb_get.place(x=245, y=48)

fen.bind("<Return>", action)

#______________________________________________________________________________________________

fen.iconbitmap("Loto.ico") # Icone coin H/G fenetre Déplacé ici car affiche une fenetre indésirable
fen.resizable(width=False, height= False) #CQFD On ne touche pas cette fenetre ! Na!
print("PRG en cours d'exécution...")

fen.mainloop()
# _______________________Controles à la SORTIE Fouille au corps !!________________________
# copie_ecran()
# print("Fin de loop", N, compteur, "Tirages gagnants") # test
# print(compteur, "Fin du PRG à :") # test
#_______________________________FIN du PRG___________________________________
# showinfo("Fin du PRG","Coucou "+N)
# print("showInfo Box")
sys.exit(0)  # Sortie propre du PRG

