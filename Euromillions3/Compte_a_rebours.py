# https://www.youtube.com/watch?v=elHeX7TBSoU

import time  # dates et heures
from tkinter import *



# __________________________________________Funct° Timer _______________________
def Timer(duree):
    while duree >= 0:
        time.sleep(1)
        texte_timer["text"] = str(duree), "s"
        app.update()

        if duree == 0 :
            app.destroy()
        duree -= 1


app = Tk()
app.minsize(155, 155)
texte_timer = Label(app, text="",font=("Arial Black", 27), bg="#374C9D", fg='white')
texte_timer.pack(expand=YES)
Timer(5)
app.mainloop()
