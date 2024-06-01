from connection import *
from cls import *
from customtkinter import *
from tkinter import ttk, messagebox
import os

repository = Repository()


class App(CTkFrame):

    def __init__(self, screen=None):
        super().__init__(screen)
        self.master = screen
        self.CreateWidget()

    def CreateWidget(self):
        self.varName = StringVar()
        self.varLastName = StringVar()
        self.varAge = StringVar()
        persian_font = CTkFont(family="Tahoma", size=12)

        CTkLabel(self.master, text="Name:").pack()
        self.txtname = CTkEntry(self.master, textvariable=self.varName, font=persian_font)
        self.txtname.pack()

        CTkLabel(self.master, text="Last Name:").pack()
        self.txtlastname = CTkEntry(self.master, textvariable=self.varLastName, font=persian_font)
        self.txtlastname.pack()

        CTkLabel(self.master, text="Age:").pack()
        self.txtage = CTkEntry(self.master, textvariable=self.varAge)
        self.txtage.pack()

        self.btn = CTkButton(self.master, text="Register", command=self.Register)
        self.btn.pack()

    #Event
    def Register(self):
        print(self.varAge.get())
        print(self.varName.get())
        obj = personnel(self.varName.get(), self.varLastName.get(), int(self.varAge.get()))
        r = Repository()
        result = r.Add(obj)
        if result:
            messagebox.showinfo("", "ثبتنام شما انجام شد")
            self.varName.set("")
            self.varLastName.set("")
            self.varAge.set("")
            self.txtname.focus_set()
        else:
            messagebox.showerror("", "ثبتنام شما انجام نشد")

        # اجرای پنجره اصلی

if __name__ == "__main__":
    screen = CTk()
    screen.geometry("400x500+650+0")
    set_appearance_mode("dark")
    screen.resizable = (False, False)
    screen.title("User Managment")
    pageMe = App(screen)
    screen.mainloop()
    pass
