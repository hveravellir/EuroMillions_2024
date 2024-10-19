# ___________________Import des modules______________________
from tkinter import *
from PIL import ImageTk, Image
import random  # CQFD
import time  # dates et heures
import sys
import time  # dates et heures
import tkinter
from timeit import default_timer
from PIL.ImageOps import expand
#

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
def affichage():
    monTexte.set("Bonjour "+champ.get()+", j'espère que vous allez bien")
    champ.delete(0,END)
fen=Tk()
monTexte=StringVar()
monTexte.set("Faisons connaissance")
#mise en place du label 1
texteLabel1=Label(fen, text = "Entrez votre prénom :")
texteLabel1.pack()
#mise en place du widget Entry
champ=Entry(fen)
champ.pack()
#mise en place du label 2 (variable : monTexte)
texteLabel2 = Label(fen, textvariable = monTexte)
texteLabel2.pack()
#mise en place du bouton
btn=Button(fen, text="Valider", command=affichage)
btn.pack()
#mainloop
fen.mainloop()
