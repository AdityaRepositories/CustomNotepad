
from notepad import *


if __name__=='__main__':

    root = notepad()
    menu = root.menubar()

    root.filemenu(menu)
    root.editmenu(menu)
    root.helpmenu(menu)

    root.config(menu=menu)
    root.mainloop()
    

