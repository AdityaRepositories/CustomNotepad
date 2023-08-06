from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os



class notepad(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x600')
        self.title('Untitled - Notepad')
        self.wm_iconbitmap('NotePad icon.ico')
        self.file = None
        self.write = self.textarea()
        self.sc_bar(self.write)


    def textarea(self):
        textArea = Text(self, font='lucida 13')
        textArea.pack(expand=True, fill=BOTH)
        return textArea

    def sc_bar(self, widget):
        scroll = Scrollbar(widget, cursor="arrow")
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=widget.yview)
        widget.config(yscrollcommand=scroll.set)
        return scroll


    # Actions for menu options-
    def message(self):
        showinfo("Notepad", "This is a notepad created by Aditya!")


    def newFile(self):
        self.title('Untitled - Notepad')
        self.file = None
        self.write.delete(1.0, END)

    def save(self):
        if self.file == None:
            self.saveas()

        else:
            with open(self.file, 'w') as f:
                f.write(self.write.get(1.0, END))

            showinfo("Notepad", "File saved successfully!")


    def saveas(self):
        self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.file == "":
            self.file = None

        else:
            with open(self.file, "w") as f:
                f.write(self.write.get(1.0, END))
            
            self.title(os.path.basename(self.file) + ' - Notepad')
            showinfo("Notepad", f"File saved successfully at - {self.file}")


    def done(self):
        self.destroy()

    def open_file(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.file == "":
            self.file = None
        else:
            self.title(os.path.basename(self.file) + ' - Notepad')
            self.write.delete(1.0, END)
            with open(self.file, 'r') as f:
                self.write.insert(1.0, f.read())


    def cut(self):
        self.write.event_generate(("<<Cut>>"))

    def copy(self):
        self.write.event_generate(("<<Copy>>"))

    def paste(self):
        self.write.event_generate(("<<Paste>>"))



    # Menus of NotePad:-
    def menubar(self):
        return Menu(self, bg='gray')

    def filemenu(self, menu_name):
        menu = menu_name

        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label='New', command=self.newFile)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save)
        file_menu.add_command(label='Save as', command=self.saveas)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.done)

        menu.add_cascade(label='File', menu=file_menu)
        return menu


    def helpmenu(self, menu_name):
        menu = menu_name

        help_menu = Menu(menu, tearoff=0)
        help_menu.add_command(label='About us ?', command=self.message)

        menu.add_cascade(label='Help', menu=help_menu)
        return menu


    def editmenu(self, menu_name):
        menu = menu_name

        edit_menu = Menu(menu, tearoff=0)
        edit_menu.add_command(label='Cut', command=self.cut)
        edit_menu.add_command(label='Copy', command=self.copy)
        edit_menu.add_command(label='Paste', command=self.paste)
        menu.add_cascade(label='Edit', menu=edit_menu)
        return menu

