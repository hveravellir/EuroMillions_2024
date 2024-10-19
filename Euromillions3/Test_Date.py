#___________________Import des modules______________________
from tkinter import *
from PIL import ImageTk, Image
import random  # CQFD
import time  # dates et heures
import sys
import time  # dates et heures
import tkinter
from timeit import default_timer
from PIL.ImageOps import expand
import datetime


date = datetime.date.today()
print("print(date) = ",date)
date = datetime.datetime.today()
print("datetime.datetime.today() = ", date)
date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print("date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S') = ", date)
print(date + " date = ", "%d-%m-%Y %H:%M:%S" )
myDateTime1 = datetime.datetime.now() # On sauvegarde now
print("myDateTime1 = datetime.datetime.now() = ", myDateTime1)
a=input("Attendez un peu puis, appuyez sur Enter")

td = datetime.datetime.now() - myDateTime1 # On calcule le temps passé
print("td : ", td) # Temps passé avec les microsecondes !!
# td.strftime('%H:%M:%S')
date = td #.strftime('%d-%m-%Y %H:%M:%S')
print(str(myDateTime1) + " =>myDateTime1")
print(str(td) + " => td")
print( "Temps écoulé : ", (date)) # Format incorrect utliser strftime('%d-%m-%Y %H:%M:%S') Mais comment ??
print (date) # = "%d:%02d:%02d" % (hours, minutes, seconds)