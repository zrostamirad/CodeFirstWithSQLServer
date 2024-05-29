from connection import *
from cls import *
from tkinter import *
from tkinter import ttk, messagebox
import os

repository = Repository()

class App(Frame):
    def __init__(self, screen=None):
        super().__init__(screen)
        self.master = screen
        self.CreateWidget()

    def CreateWidget(self):
        pass




if __name__ == "__main__":
    screen = Tk()
    screen.geometry("%dx%d+%d+%d" % (800, 500, 350, 30))
    screen.resizable = (False, False)
    screen.title("User Managment")
    pageMe = App(screen)
    screen.mainloop()
    pass