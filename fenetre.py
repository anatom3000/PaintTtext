import webbrowser

from tkinter import *
from tkinter.messagebox import *

def nondisp():
    showerror("En cours de développement...", "Nous y travaillons...")

def apropos():
    showinfo("A propos - Version", "Version : 0.0.1\nCe n'est que le commencement...")

def askquit():
    if askyesno("Do you want to quit ?", "Do you want to quit ?"):
        root.quit()

def ch():
    menu3.add_command(label="A propos", command=apropos)

root = Tk()
root.iconbitmap("xlogo64.xbm")

#barre de menu

menubar = Menu(root)

#fichier
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=nondisp)
menu1.add_command(label="Editer", command=nondisp)
menu1.add_separator()
menu1.add_command(label="Quitter", command=askquit)

menubar.add_cascade(label="Fichier", menu=menu1)

#aide
menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Changelog", command=apropos)
menu3.add_command(label="A propos", command=ch)

menubar.add_cascade(label="Aide", menu=menu3)

root.config(menu=menubar)

root.mainloop()
exit(0)
