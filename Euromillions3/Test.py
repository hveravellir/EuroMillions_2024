import tkinter



def FNC_Modifier ( event ) :

    CAN_Toile.itemconfig ( 1 , start = SCA_Debut.get ( ) , extent = SCA_Ecart.get ( ) , style = SPI_Style.get ( ) )

    kmessage = f"\n start : { CAN_Toile.itemcget ( 1 , 'start' ) }\n"

    kmessage += f" extent : { CAN_Toile.itemcget ( 1 , 'extent' ) }\n"

    kmessage += f" style : { CAN_Toile.itemcget ( 1 , 'style' ) }\n"

    LAB_Etat [ "text" ] = kmessage

    print(kmessage)


TKI_Principal = tkinter.Tk ( )


BUT_Quitter = tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy )

SCA_Debut = tkinter.Scale ( TKI_Principal , orient = "horizontal" , to = 360 , length = 150 , command = FNC_Modifier )

SCA_Ecart = tkinter.Scale ( TKI_Principal , orient = "horizontal" , to = 360 , length = 150 , command = FNC_Modifier )

SPI_Style = tkinter.Spinbox ( TKI_Principal , values = ( "pieslice" , "arc" , "chord" ) , command = lambda : FNC_Modifier ( None ) )

LAB_Etat = tkinter.Label ( TKI_Principal , relief = "solid" , justify = "left" , anchor = "w" )


CAN_Toile = tkinter.Canvas ( TKI_Principal , bg = "white" , width = 250 , height = 250 )

CAN_Toile.create_arc ( 20 , 20 , 230 , 230 , fill = "orange" , width = 5 )


CAN_Toile.grid ( row = 0 , column = 0 , columnspan = 2 , sticky = "nesw" )

LAB_Etat.grid ( row = 1 , column = 0 , columnspan = 2 , sticky = "nesw" )

tkinter.Label ( TKI_Principal , text = "start :" , justify = "right" , anchor = "se" ).grid ( row = 2 , column = 0 , sticky = "e" )

SCA_Debut.grid ( row = 2 , column = 1 , sticky = "w" )

tkinter.Label ( TKI_Principal , text = "extent :" , justify = "right" , anchor = "se" ).grid ( row = 3 , column = 0 , sticky = "e" )

SCA_Ecart.grid ( row = 3 , column = 1 , sticky = "w" )

tkinter.Label ( TKI_Principal , text = "style :" , justify = "right" , anchor = "se" ).grid ( row = 4 , column = 0 , sticky = "e" )

SPI_Style.grid ( row = 4 , column = 1 , sticky = "nesw" )

BUT_Quitter.grid ( row = 5 , column = 0 , columnspan = 2 , sticky = "nesw" )


SCA_Debut.set ( 45 )

SCA_Ecart.set ( 270 )


TKI_Principal.mainloop ( )