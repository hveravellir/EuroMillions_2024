import tkinter
from tkinter import *

import time
Fen = Tk()
Fen.geometry("600x600+1000+300") # "600x600 Dimensions+300+200 Placement sur l'écran"
# v = tkinter.StringVar()
v = "Cube1"

def go_go_go():
    # canvas.delete(0,END)
    # canvas.itemconfig(1, texte = "  ") # ? rien
    # time.sleep(3)
    v ="Cube2"
    # texte = v

    v = canvas.create_text("75", "75", text= v, font="arial 18 bold", fill="blue")

    canvas.coords(v,"225","75") # ? rien


    print(v)
# Modifier les coordonnées d'un bouton ou d'un txt après l'affichage il faut donner un nom au txt ou au bouton

canvas = Canvas(Fen, width="300", height="300", background="aqua")
v = canvas.create_text("75","75",text= v, font = "arial 18 bold", fill = "red")
# canvas.create_line("150","0","150","300")
# canvas.create_line("0","150","300","150")
canvas.pack()

bouton = (Button(Fen, text = "Click me", command = go_go_go))
bouton.pack()
# Fen.update() # ? rien
Fen.mainloop()

# si, on peut changer le texte avec: canvas.itemconfig( id_du_lutin, text = "Nouveau texte" )
#
# Sinon , pour changer le texte, il fallait redire que le texte = v après avoir modifié v