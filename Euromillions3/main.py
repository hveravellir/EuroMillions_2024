#___________________Import des modules______________________
from tkinter import *
from PIL import ImageTk, Image
import random  # CQFD
import time  # dates et heures
import sys
import time  # dates et heures
import tkinter
#_______________________________________Variables Globales__________________________________


#____________________________________________________________________________________________
def coucou(N):
    print(N)
    # pass

def action():
    # global N
    N = entryNombre.get()
    valider = tkinter.Button(fen, text="Validez votvccv", state="disabled", command = coucou(N)) # command=fen.destroy())
    Valider.place(x=200, y=90)
    entryNombre.delete(0, END)
    entryNombre.insert(0, "Merci vous pouvez fermer la fenêtre")
    valider.config( state="disabled")
    valider.destroy

    # lblDiviseurs['text'] = "Les diviseurs sont :"
    # for i in range(1, N + 1):
    #     if (N % i == 0):
    #         lblDiviseurs['text'] = lblDiviseurs['text'] + " " + str(i) + " "
    # print(N)


fen = tkinter.Tk()
fen.geometry("420x220")  # 1280x920

lblNombre = tkinter.Label(fen, text="Entrez le Nb : ")
lblNombre.place(x=10, y=20)
entryNombre = Entry(fen)
entryNombre.place(x=200, y=20)
lblNombre.place(x=20, y=20)
# lblDiviseurs = Label(fen, text="Les diviseurs sont :")
# lblDiviseurs.place(x=20, y=50)

# Valider = tkinter.Button(fen, text="Validez votre choix", command=action)
# Valider.place(x=200, y=90)
valider = tkinter.Button(fen, text="Validez votvccv", state="disabled")
Valider.place(x=200, y=90)
# print(N)
fen.mainloop()