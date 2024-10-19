import tkinter



def FNC_Enfoncer ( event )  :

    CAN_Toile.scan_mark ( event.x , event.y )


def FNC_Deplacer ( event ) :

    CAN_Toile.scan_dragto ( event.x , event.y , SCA_Vitesse.get ( ) )



TKI_Principal = tkinter.Tk ( )


BUT_Quitter = tkinter.Button ( TKI_Principal , text = "Quitter" , command = TKI_Principal.destroy )

SCA_Vitesse = tkinter.Scale ( TKI_Principal , orient = "horizontal" , from_ = 1 , to = 50 )


CAN_Toile = tkinter.Canvas ( TKI_Principal , bg = "white" , scrollregion = ( -200 , -200 , 1000 , 1000 ) , width = 300 , height = 300 )

for kligne in range ( 9 ) :

    CAN_Toile.create_line ( 0 , ( kligne * 100 ) , 800 , ( kligne * 100 ) , fill = "black" )

    CAN_Toile.create_line ( ( kligne * 100 ) , 0 , ( kligne * 100 ) , 800 , fill = "black" )

CAN_Toile.create_rectangle ( 10 , 10 , 110 , 110 , fill = "pink" )

CAN_Toile.create_rectangle ( 290 , 10 , 390 , 110 , fill = "red" )

CAN_Toile.create_rectangle ( 10 , 290 , 110 , 390 , fill = "green" )

CAN_Toile.create_rectangle ( 290 , 290 , 390 , 390 , fill = "blue" )

CAN_Toile.create_rectangle ( 180 , 130 , 570 , 170 , fill = "yellow" )

CAN_Toile.create_rectangle ( 130 , 180 , 170 , 570 , fill = "orange" )


CAN_Toile.bind ( "<ButtonPress-1>" , FNC_Enfoncer )

CAN_Toile.bind ( "<Button1-Motion>" , FNC_Deplacer )


CAN_Toile.pack ( )

SCA_Vitesse.pack ( )

tkinter.Label ( TKI_Principal , text = "Sélectionnez une vitesse de défilement" ).pack ( )

BUT_Quitter.pack ( )


TKI_Principal.mainloop ( )