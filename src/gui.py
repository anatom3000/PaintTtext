## Paintttext - Convert texte to image and image to text
## Copyright © 2019 anat3000
import webbrowser

from tkinter import *
from tkinter.messagebox import *

class TtttGUI(Tk):
    def nondisp(self):
        showerror("En cours de développement...", "Nous y travaillons...")

    def apropos(self):
        showinfo("A propos - Version", "Version : 0.0.1\nCe n'est que le commencement...")

    def askquit(self):
        if askyesno("Do you want to quit ?", "Do you want to quit ?"):
            root.quit()

    def view_changelog(self):
        webbrowser.open_new("https://github.com/anat3000/PaintTtext/blob/master/CHANGELOG")
        
    def open_image(self):
        file = ledialog.askopenfilename()
        # TODO : complete this

    def init_menu(self):
        #menu bar
        menubar = Menu(self)

        #encode menu
        encode_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Delete text", command=self.nondisp)
        file_menu.add_command(label="Load text", command=self.nondisp)
        file_menu.add_separator()
        file_menu.add_command(label="Encode text", command=self.askquit)

        menubar.add_cascade(label="Encode", menu=file_menu)
        
        #encode menu
        encode_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Delete image", command=self.nondisp)
        file_menu.add_command(label="Load image", command=self.nondisp)
        file_menu.add_separator()
        file_menu.add_command(label="Decode text", command=self.askquit)

        menubar.add_cascade(label="Encode", menu=file_menu)

        #help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Changelog", command=self.view_changelog)
        help_menu.add_command(label="À propos", command=self.apropos)

        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)


    def __init__(self):
        #init Tk class
        super().__init__()
        #set properties of the window
        self.iconbitmap("../assets/paintttext.ico")


root = TtttGUI()
root.mainloop()
exit(0)
