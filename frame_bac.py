# -*- coding: utf-8 -*-
import tkinter as tk
from functools import partial

class numEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit() or self.get() == "": 
            # the current value is only digits; allow this
            if self.get() != "":
                if (int(self.get()) > 20 ):
                    self.set(self.old_value)
                else:
                    self.old_value = self.get()
            else:
                self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)

class main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=None)
        self.master.title("Bac")
        self.master.geometry("700x300")
        
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
    
        self.boutongeneral = tk.Button(self.master, height=100, width=100, image = self.pixelVirtual, text="Main Menu", command=self.dialog)
        self.boutongeneral.grid(row=2, column=1)
        
    def dialog(self):
        d = modal(root, "general")
        root.wait_window(d.top)

class modal:
    def __init__(self, parent, typebac ):
 
        self.top = tk.Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry("400x600")
        
        self.tblmoyennecc = ["Moyenne 1er semestre en Première", "Moyenne 2nd semestre en Première","Moyenne 1er semestre en Terminale", "Moyenne 2nd semestre en Terminale"]
        
        self.labelmoyennecc, self.entrymoyennecc = [0]*len(self.tblmoyennecc), [0]*len(self.tblmoyennecc)
        
        for i in range(0, len(self.tblmoyennecc)):
            self.labelmoyennecc[i] = tk.Label(self.top, text=self.tblmoyennecc[i])
            self.labelmoyennecc[i].grid(column=0, row= i)
            self.entrymoyennecc[i] = numEntry(self.top)
            self.entrymoyennecc[i].grid(column=1, row = i)
            
        self.ValidButton = tk.Button(self.top, text="Valider",command=self.Valid)
        self.ValidButton.grid(row= 5)
            
    def Valid(self):
        notescc = 0
        for i in range(0, len(self.tblmoyennecc)):       
            notescc += int(self.entrymoyennecc[i].get())
        notescc /= len(self.tblmoyennecc)

        print(notescc)
            
    def cancel(self, event=None):
        self.top.destroy()

root = tk.Tk()
a = main(root)
root.mainloop()