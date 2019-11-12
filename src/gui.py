## Paintttext - Convert texte to image and image to text
## Copyright © 2019 anat3000
import webbrowser

from tkinter import *
from tkinter.messagebox import *

class TttGUI(Tk):
    def nondisp(self):
        showerror("En cours de développement...", "Nous y travaillons...")

    def apropos(self):
        showinfo("A propos - Version", "Version : 0.0.1\nCe n'est que le commencement...")

    def askquit(self):
        if askyesno("Do you want to quit ?", "Do you want to quit ?"):
            root.quit()

    def view_changelog(self):
        menu3.add_command(label="A propos", command=apropos)
    def __init__(self):
        #init Tk class
        super().__init__()
        #set properties of the window
        self.iconbitmap("icon.xbm")
        
        ##menu bar
        menubar = Menu(self)
        
        #file menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Créer", command=nondisp)
        file_menu.add_command(label="Editer", command=nondisp)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=askquit)

        menubar.add_cascade(label="Fichier", menu=file_menu)

        #help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Changelog", command=apropos)
        help_menu.add_command(label="À propos", command=changelog)

        menubar.add_cascade(label="Aide", menu=help_menu)

        self.config(menu=menubar)

root = TttGUI()
root.mainloop()
exit(0)
