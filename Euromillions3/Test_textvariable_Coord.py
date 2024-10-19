from tkinter import *
from PIL import ImageTk, Image
import random  # CQFD
import time  # dates et heures
import sys
import time  # dates et heures
import tkinter
from timeit import default_timer
from PIL.ImageOps import expand


def FNC_Axes ( event ) :

    kabscisse = ( SCA_Abscisse.get ( ) , 0 , SCA_Abscisse.get ( ) , 400 )

    kordonnee = ( 0 , SCA_Ordonnee.get ( ) , 400 , SCA_Ordonnee.get ( ) )

    CAN_Toile.coords ( CAN_Abscisse , *kabscisse )

    CAN_Toile.coords ( CAN_Ordonnee , *kordonnee )



def FNC_Inserer ( ) :

    CAN_Toile.create_text ( SCA_Abscisse.get ( ) , SCA_Ordonnee.get ( ) , anchor = SPI_Ancre.get ( ) , text = TKV_Texte.get ( ) )

    TKV_Texte.set ( "" )



TKI_Principal = tkinter.Tk ( )

bgrnd = ImageTk.PhotoImage(Image.open("Res_Euromillions_OK1.jpg"))  # 1280x1895
TKI_Principal.geometry("794x899+1000+70")  # 720x420 = Dimensions+1000+70 = Placement sur l'écran"
lblbgrnd = Label(TKI_Principal, image = bgrnd)
lblbgrnd.place(x=50, y=0)  # Affiche le fond d'écran
TKV_Texte = tkinter.StringVar ( )


BUT_Quitter = tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy )

BUT_Inserer = tkinter.Button ( TKI_Principal , text = "Insérer" , command = FNC_Inserer )

ENT_Texte = tkinter.Entry ( TKI_Principal , textvariable = TKV_Texte ) # textvariable ...

SCA_Abscisse = tkinter.Scale ( TKI_Principal , orient = "horizontal" , to = 399 , command = FNC_Axes ) # Bornes

SCA_Ordonnee = tkinter.Scale ( TKI_Principal , to = 399 , command = FNC_Axes )

SPI_Ancre = tkinter.Spinbox ( TKI_Principal , values = ( "center" , "n" , "ne" , "e" , "se" , "s" , "sw" , "w" , "nw" ) , width = 7 )


CAN_Toile = tkinter.Canvas ( TKI_Principal , bg = "white" , height = 400 , width = 400 )

CAN_Abscisse = CAN_Toile.create_line ( 0 , 0 , 0 , 0 )

CAN_Ordonnee = CAN_Toile.create_line ( 0 , 0 , 0 , 0 )


SCA_Ordonnee.grid ( row = 0 , column = 0 , sticky = "nesw" )

CAN_Toile.grid ( row = 0 , column = 1 , columnspan = 3 , sticky = "nesw" )

SCA_Abscisse.grid ( row = 1 , column = 1 , columnspan = 3 , sticky = "nesw" )

ENT_Texte.grid ( row = 2 , column = 1 , sticky = "nesw" )

BUT_Inserer.grid ( row = 2 , column = 2 , sticky = "nesw" )

SPI_Ancre.grid ( row = 2 , column = 3 , sticky = "nesw" )

BUT_Quitter.grid ( row = 3 , column = 1 , columnspan = 4 , sticky = "nesw" )


SCA_Abscisse.set ( 200 ) # Point de départ trait vertical

SCA_Ordonnee.set ( 200 ) # Point de départ trait horizontal


TKI_Principal.mainloop ( )