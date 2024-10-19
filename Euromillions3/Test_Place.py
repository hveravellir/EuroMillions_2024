import tkinter



def FNC_Afficher ( event ) :

    if BUT_Etat [ "text" ] == "Afficher" : return

    LAB_Test.place_configure ( width = int ( SCA_Largeur.get ( ) ) )

    LAB_Test.place_configure ( height = int ( SCA_Hauteur.get ( ) ) )

    LAB_Test.place  ( x = int ( SCA_Abscisse.get( ) ) )

    LAB_Test.place ( y = int ( SCA_Ordonnee.get ( ) ) )

    LAB_Test.place ( anchor = SPI_Position.get ( ) )

    BOX_Code.delete ( 0 , "end" )

    for kattribut , kvaleur in LAB_Test.place_info ( ).items ( ) : BOX_Code.insert ( 0 , f"{ kattribut } = { kvaleur }" )



def FNC_Effacer ( ) :

    if BUT_Etat [ "text" ] == "Effacer" :

        BUT_Etat [ "text" ] = "Afficher"

        LAB_Test.place_forget ( )

        BOX_Code [ "background" ] = "lavender"

        BOX_Code.delete ( 0 , "end" )

        BOX_Code.insert ( 0 , "LISTE DES CONTROLES." )

        BOX_Code.insert ( "end", "" )

        for kcontrole in TKI_Principal.place_slaves ( ) : BOX_Code.insert ( "end" , kcontrole )

    else :

        BUT_Etat [ "text" ] = "Effacer"

        BOX_Code [ "background" ] = "aqua"

        FNC_Afficher ( None )



TKI_Principal = tkinter.Tk ( )

TKI_Principal.geometry ( "800x300+100+50" )


BUT_Quitter = tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy )

BUT_Etat = tkinter.Button ( TKI_Principal , text = "Afficher" , command = FNC_Effacer )

SCA_Largeur = tkinter.Scale ( TKI_Principal , orient = "horizontal" , from_ = 1 , to = 450 , command = FNC_Afficher )

SCA_Hauteur = tkinter.Scale ( TKI_Principal , orient = "horizontal" , from_ = 1 , to = 350 , command = FNC_Afficher )

SCA_Abscisse = tkinter.Scale ( TKI_Principal , orient = "horizontal" , from_ = -100 , to = 450 , command = FNC_Afficher )

SCA_Ordonnee = tkinter.Scale ( TKI_Principal , orient = "horizontal" , from_ = -100 , to = 350 , command = FNC_Afficher)

SPI_Position = tkinter.Spinbox ( TKI_Principal , wrap = True , command = lambda : FNC_Afficher ( None ) )

BOX_Code = tkinter.Listbox ( TKI_Principal , fg = "blue" , bg = "white" , relief = "groove" )


FRM_Zone = tkinter.LabelFrame ( TKI_Principal , text = " --- ZONE DE TEST --- " )

LAB_Test = tkinter.Label ( FRM_Zone , text = "TEST" , fg = "blue" , bg = "aqua" , relief = "solid" )


BOX_Code.place_configure ( x = 0 , y = 0 , width = 200 , height = 250 )

BUT_Quitter.place_configure ( x = 0 , y = 250 , width = 200 , height = 50 )

FRM_Zone.place_configure ( x = 200 , y = 0 , width = 400 , height = 300 )

tkinter.Label ( TKI_Principal , text = "width" , justify = "right" ).place ( x = 650 , y = 40 , anchor = "se" )

SCA_Largeur.place ( x = 650 , y = 40 , width = 150 , anchor = "sw" )

tkinter.Label ( TKI_Principal , text = "height" , justify = "right" ).place ( x = 650 , y = 90 , anchor = "se" )

SCA_Hauteur.place ( x = 650 , y = 90 , width = 150 , anchor = "sw" )

tkinter.Label ( TKI_Principal , text = "x" , justify = "right" ).place ( x = 650 , y = 140 , anchor = "se" )

SCA_Abscisse.place ( x = 650 , y = 140 , width = 150 , anchor = "sw" )

tkinter.Label ( TKI_Principal , text = "y" , justify = "right" ).place ( x = 650 , y = 190 , anchor = "se" )

SCA_Ordonnee.place ( x = 650 , y = 190 , width = 150 , anchor = "sw" )

tkinter.Label ( TKI_Principal , text = "anchor" , justify = "right" ).place ( x = 650 , y = 240 , anchor = "se" )

SPI_Position.place ( x = 650 , y = 240 , width = 150 , anchor = "sw" )

BUT_Etat.place_configure ( x = 600 , y = 250 , width = 200 , height = 50 )


SCA_Largeur.set ( 120 )

SCA_Hauteur.set ( 50 )

SCA_Abscisse.set ( 0 )

SCA_Ordonnee.set ( 0 )

SPI_Position [ "values" ] = ( "n" , "ne" , "e" , "se" , "s" , "sw" , "w" , "nw" )

SPI_Position.delete ( 0 , "end" )

SPI_Position.insert ( 0 , "nw" )

BOX_Code [ "background" ] = "aqua"


FNC_Effacer ( )


TKI_Principal.mainloop ( )