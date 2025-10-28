from calculs import *
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self["bg"] = "#121213"
        self.geometry("400x200")


        left_panel = tk.Frame(self)
        left_panel.pack(side="left")
        right_panel = tk.Frame(self)
        right_panel.pack(side="right")

        self.lbox_options = tk.Listbox(left_panel, height=6)
        for option in ["Addition", "Soustraction", "Multiplication", "Division", "Exponentielle", "Fibonacci"]:
            self.lbox_options.insert("end", option)
        self.lbox_options.pack()
        self.lbox_options.bind("<<ListboxSelect>>", self.switchFrames)

        operations = {"Addition":"+", "Soustraction":"-", "Multiplication":"x", "Division":"/"}
        fonctions = {"Exponentielle":"exp", "Fibonacci":"fibonacci"}

        self.frames_calculs = {}
        for option in ["Addition", "Soustraction", "Multiplication", "Division", "Exponentielle", "Fibonacci"]:
            self.frames_calculs[option] = tk.Frame(right_panel)
            self.frames_calculs[option].grid(column=0, row=0, sticky="nsew")

            subframe_top = tk.Frame(self.frames_calculs[option])
            subframe_top.pack(side="top")
            subframe_bottom = tk.Frame(self.frames_calculs[option])
            subframe_bottom.pack(side="bottom")

            resultat = tk.StringVar()
            tk.Label(subframe_bottom, textvariable=resultat).pack(side="bottom")

            if option in operations:
                first_number = tk.Entry(subframe_top, justify="center")
                first_number.pack(side="left")
                operator = tk.Label(subframe_top, text=operations[option])
                operator.pack(side="left")
                second_number = tk.Entry(subframe_top, justify="center")
                second_number.pack(side="right")
                tk.Button(subframe_bottom, text="Calculer", 
                          command=lambda resultat=resultat, operator=option, first_number=first_number, second_number=second_number: 
                          resultat.set("Résultat : "+str(self.calculeResultat(operator, first_number.get(), second_number.get())))
                          ).pack(side="top")

            else:
                function = tk.Label(subframe_top, text=fonctions[option]+"(")
                function.pack(side="left")
                number = tk.Entry(subframe_top, justify="center")
                number.pack(side="left")
                parenthesis = tk.Label(subframe_top, text=")")
                parenthesis.pack(side="left")
                tk.Button(subframe_bottom, text="Calculer", 
                          command=lambda resultat=resultat, operator=option, number=number: 
                          resultat.set("Résultat : "+str(self.calculeResultat(operator, number.get())))
                          ).pack(side="top")

            resultat = tk.StringVar()
            tk.Label(subframe_bottom, textvariable=resultat).pack(side="bottom")


        self.lbox_options.select_set(0)
        self.frames_calculs["Addition"].tkraise()




    
    def switchFrames(self, event):
        selected_index = self.lbox_options.curselection()
        selected_option = self.lbox_options.get(selected_index)
        self.frames_calculs[selected_option].tkraise()

    
    def calculeResultat(self, operator, first_number, second_number=None):
        #si il n'y a pas de deuxième nombre, c'est qu'on calcule une fonction
        if second_number == None:
            try:
                first_number = int(first_number)
                if operator == "Exponentielle":
                    return exponentielle(first_number)
                else:
                    return fibonacci(first_number)
            except ValueError:
                return "Erreur"

        #sinon c'est une operation    
        else:
            try:
                first_number = int(first_number)
                second_number = int(second_number)
                if operator == "Addition":
                    return addition(first_number, second_number)
                elif operator == "Soustraction":
                    return soustraction(first_number, second_number)
                elif operator == "Multiplication":
                    return multiplication(first_number, second_number)
                else:
                    return division(first_number, second_number)
            except ValueError:
                return "Erreur"
            except ZeroDivisionError:
                return "Erreur"


                
        






app = App()
app.mainloop()
