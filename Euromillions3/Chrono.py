
# https://www.youtube.com/watch?v=kHEtn069Bk4

from tkinter import *
from PIL import ImageTk, Image
import random  # CQFD
import time  # dates et heures
import sys
import time  # dates et heures
import tkinter
from timeit import default_timer
from PIL.ImageOps import expand

Fenetre = Tk()
str_time = ""
def updateTime():
    global r, str_time
    r +=1
    print(r)
    now = default_timer() - start # Initialise le chrono à zéro
    minutes, seconds = divmod(now, 60)
    hours,minutes = divmod(minutes,60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    canvas.itemconfigure (text_clock, text = str_time)
    Fenetre.after(1000, updateTime)
# global r
canvas = Canvas(Fenetre,width=200,height=200,bg="red")
canvas.pack(padx=10,pady=10)
start = default_timer()
# text_clock = canvas.create_text(40,20)
text_clock = canvas.create_text(100,100, font=("arial black", 22), fill="white") # coord du txt dans la boite, font, fill = couleur
r = 5

updateTime()
Fenetre.mainloop()
print(("str_time = "), str_time)