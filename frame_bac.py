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

class erreurPopup:
    def __init__(self, parent, message ):
 
        self.top = tk.Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry("250x50")
        self.label = tk.Label(self.top, text=message)
        self.label.pack()

class modal:
    def __init__(self, parent, typebac ):
 
        self.top = tk.Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry("400x600")
        
        self.tblentry = [
            {"Text" : "Moyenne 1er semestre en Première", "Coeficiant" : 2.5},
            {"Text" : "Moyenne 2nd semestre en Première", "Coeficiant" : 2.5},
            {"Text" : "Moyenne 1er semestre en Terminale", "Coeficiant" : 2.5},
            {"Text" : "Moyenne 2nd semestre en Terminale", "Coeficiant" : 2.5},
            {"Text" : "Note Histoire E3C 1ère", "Coeficiant" : 2.5},
            {"Text" : "Note Histoire E3C Terminale", "Coeficiant" : 2.5},
            {"Text" : "Note Enseingement Scientifique E3C 1ère", "Coeficiant" : 2.5},
            {"Text" : "Note Enseingement Scientifique E3C Terminale", "Coeficiant" : 2.5},
            {"Text" : "Note LV1 E3C 1ère", "Coeficiant" : 2.5},
            {"Text" : "Note LV1 E3C Terminale", "Coeficiant" : 2.5},
            {"Text" : "Note LV2 E3C 1ère", "Coeficiant" : 2.5},
            {"Text" : "Note LV2 E3C Terminale", "Coeficiant" : 2.5},
            {"Text" : "Note Spécialité 1ère", "Coeficiant" : 5},
            {"Text" : "Note EPS Terminale", "Coeficiant" : 5},
            {"Text" : "Note Français Oral", "Coeficiant" : 5},
            {"Text" : "Note Français Ecrit", "Coeficiant" : 5},
            {"Text" : "Note Spécialité 1 Terminale", "Coeficiant" : 16},
            {"Text" : "Note Spécialité 2 Terminale", "Coeficiant" : 16},
            {"Text" : "Note Philosophie", "Coeficiant" : 8},
            {"Text" : "Note Grand Oral", "Coeficiant" : 8},
            ]
        
        self.labelentry, self.entry = [0]*len(self.tblentry), [0]*len(self.tblentry)

        for i in range(0, len(self.tblentry)):
            tbl = self.tblentry[i]
            self.labelentry[i] = tk.Label(self.top, text=tbl["Text"])
            self.labelentry[i].grid(column=0, row= i)
            self.entry[i] = numEntry(self.top)
            self.entry[i].coef = tbl["Coeficiant"]
            self.entry[i].grid(column=1, row = i)

        self.ValidButton = tk.Button(self.top, text="Valider",command=self.Valid)
        self.ValidButton.grid(row=20)
            
    def Valid(self):
        tblfinal = []
        for i in range(0, len(self.tblentry)):
            entry = self.entry[i]
            if (entry.get() != ""):
                tblfinal.append({ "Coeficiant": entry.coef, "Note": int(entry.get())})
            else:
                d = erreurPopup(root, "Vous n'avez pas entrer toutes les valeurs")
                self.wait_window(d.top)
                break

        print(tblfinal)
            
    def cancel(self, event=None):
        self.top.destroy()

root = tk.Tk()
a = main(root)
root.mainloop()