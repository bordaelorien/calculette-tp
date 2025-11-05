from Calculatrice import Calculatrice
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self["bg"] = "#18222D"
        self.configStyles()

        self.calculatrice = Calculatrice()

        #la fenêtre est divisée en deux frames
        left_panel = tk.Frame(self, bg="#1E2A37")
        left_panel.pack(side="left", padx=10, pady=10, fill="both")
        right_panel = tk.Frame(self, highlightcolor="#475363", highlightbackground="#475363", highlightthickness=1, 
                               bg="#1E2A37")
        right_panel.pack(side="right", padx=10, pady=10, fill="both")

        #left panel
        self.lbox_options = tk.Listbox(left_panel, height=7, bg="#1E2A37", fg="white", font=("Arial", 15),
                                        relief="flat", selectbackground="#5D6B7E", highlightcolor="#475363",
                                        highlightbackground="#475363", activestyle ="none",
                                        selectmode="single", exportselection=0)
        #création de la listbox avec les options de calculs
        for option in ["Addition", "Soustraction", "Multiplication", "Division", "Exponentielle", "Fibonacci", "EstPremier"]:
            self.lbox_options.insert("end", option)
        self.lbox_options.pack()
        self.lbox_options.bind("<<ListboxSelect>>", self.switchFrames)

        #right panel
        operations = {"Addition":"+", "Soustraction":"-", "Multiplication":"x", "Division":"/"}
        fonctions = {"Exponentielle":"exp", "Fibonacci":"fibonacci", "EstPremier":"estPremier"}

        #création de frames superposées, une pour chaque mode de calcul
        self.frames_calculs = {}
        for option in ["Addition", "Soustraction", "Multiplication", "Division", "Exponentielle", "Fibonacci", "EstPremier"]:
            self.frames_calculs[option] = tk.Frame(right_panel, bg="#1E2A37")
            self.frames_calculs[option].grid(column=0, row=0, sticky="nsew")

            subframe_top = tk.Frame(self.frames_calculs[option], bg="#1E2A37")
            subframe_top.pack(side="top", pady=[10,5])
            subframe_bottom = tk.Frame(self.frames_calculs[option], bg="#1E2A37")
            subframe_bottom.pack(side="bottom")

            resultat = tk.StringVar()
            #label en bas qui affiche le résultat
            ttk.Label(subframe_bottom, textvariable=resultat).pack(side="bottom")

            if option in operations:
                #entry à gauche
                first_number = tk.Entry(subframe_top, bg="#5D6B7E", fg="white", font=("Arial", 15),
                                        justify="center", relief="flat", width=12)
                first_number.pack(side="left", padx=[10,0])
                #symbole de l'opération au milieu
                ttk.Label(subframe_top, text=operations[option]).pack(side="left")
                #entry à droite
                second_number = tk.Entry(subframe_top, bg="#5D6B7E", fg="white", font=("Arial", 15),
                                         justify="center", relief="flat", width=12)
                second_number.pack(side="right", padx=[0,10])
                #bouton qui déclenche le calcul du résultat quand on le clique
                ttk.Button(subframe_bottom, text="Calculer", takefocus=False,
                          command=lambda resultat=resultat, operator=option, first_number=first_number, second_number=second_number: 
                          resultat.set("Résultat : "+str(self.calculeResultat(operator, first_number.get(), second_number.get())))
                          ).pack(side="top")

            else:
                #nom de la fonction à gauche
                ttk.Label(subframe_top, text=fonctions[option]+"(").pack(side="left")
                #entry au milieu
                number = tk.Entry(subframe_top, bg="#5D6B7E", fg="white", font=("Arial", 15),
                                  justify="center", relief="flat", width=12)
                number.pack(side="left")
                #parenthèse à droite
                ttk.Label(subframe_top, text=")").pack(side="left")
                #bouton qui déclenche le calcul du résultat quand on le clique
                ttk.Button(subframe_bottom, text="Calculer", takefocus=False,
                          command=lambda resultat=resultat, operator=option, number=number: 
                          resultat.set("Résultat : "+str(self.calculeResultat(operator, number.get())))
                          ).pack(side="top")


        #on sélectionne l'option "addition" par défaut
        self.lbox_options.select_set(0)
        self.frames_calculs["Addition"].tkraise()




    #met au premier plan l'onglet correspondant au mode sélectionné par l'utilisateur
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
                    return round(self.calculatrice.exponentielle(first_number), 5)
                elif operator == "Fibonacci":
                    return self.calculatrice.fibonacci(first_number)
                else:
                    return self.calculatrice.estPremier(first_number)
            except ValueError:
                return "Erreur"

        #sinon c'est une operation    
        else:
            try:
                first_number = int(first_number)
                second_number = int(second_number)
                if operator == "Addition":
                    return self.calculatrice.addition(first_number, second_number)
                elif operator == "Soustraction":
                    return self.calculatrice.soustraction(first_number, second_number)
                elif operator == "Multiplication":
                    return self.calculatrice.multiplication(first_number, second_number)
                else:
                    return self.calculatrice.division(first_number, second_number)
            except ValueError:
                return "Erreur"
            except ZeroDivisionError:
                return "Erreur"

    
    #configuration du style des widgets avec ttk.Style()      
    def configStyles(self):
        style = ttk.Style()
        
        style.theme_use("default")

        #boutons
        style.configure("TButton", background="#348A31", relief="flat", foreground="white",
                        padding=[0,8], font=("Arial", 15))
        style.map("TButton", background=[("pressed", "#46A543"), 
                                         ("active", "#3B9738")],
                        relief=[("pressed", "sunken")])
        
        #labels
        style.configure("TLabel", background="#1E2A37", foreground="white", padding=[10,12] , font=("Arial", 15))

        


                
        






app = App()
app.mainloop()
