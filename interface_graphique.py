from calculs import *
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self["bg"] = "#121213"
        self.geometry("500x550")
        self.configStyles()
        self.initGraphique()

    
    def initGraphique(self):
        #écran
        ecran = tk.Frame(self, bg="#121213")
        ecran.pack(side="top", fill="x", pady=20, padx=20)
        
        self.display_current_formula = tk.Label(ecran, text="0", bg="#5e5e5e", anchor="w", justify="left", font=("Arial", 30), fg="white")
        self.display_current_formula.pack(fill="x")
        
        self.display_result = tk.Label(ecran, text="", bg="#5e5e5e", justify="left", anchor="w", font=("Arial", 20), fg="white")
        self.display_result.pack(fill="x")

        #boutons
        buttons = tk.Frame(self, bg="#121213")
        buttons.pack(fill="both", padx=20, pady=20)

        for n in range(4):
            buttons.rowconfigure(n, weight=1)
        for n in range(4):
            buttons.columnconfigure(n, weight=1)

        button_names = [["1", "2", "3", "+"],
                        ["4", "5", "6", "-"],
                        ["7", "8", "9", "x"],
                        ["0", "exp", "fibo", "/"],
                        ["=", "AC"]]
        
        for i in range(4):
            for j in range(4):
                button = ttk.Button(buttons, text=button_names[i][j],
                                   command = lambda name=button_names[i][j]: self.button_pressed(name))
                button.grid(row=i, column=j, padx=5, pady=5)
        for j in range(0, 4, 2):
            button = ttk.Button(buttons, text=button_names[4][j//2],
                               command = lambda name=button_names[4][j//2]: self.button_pressed(name), 
                               style="GreenButton.TButton")
            button.grid(row=4, column=j, columnspan=2, padx=5, pady=5, sticky="nswe")


        self.current_formula = "0"

    
    def button_pressed(self, name):
        if name == "=":
            self.display_result.configure(text=str(self.calculeResultat(self.current_formula)))
        
        else:           
            if name == "AC":
                self.current_formula = "0"
                self.display_result.configure(text="")
            elif self.current_formula == "0":
                self.current_formula = name
            else:
                self.current_formula += name
            self.display_current_formula.configure(text=self.current_formula)


    def calculeResultat(self, formula):
        return "0"

    
    #configuration du style des boutons
    def configStyles(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("TButton", background="#3a3a3c", relief="flat", foreground="white",
                        padding=[0,10], font=("Courier", 30))
        style.map("TButton", background=[("pressed", "#5f5f63"), 
                                        ("active", "#4a4a4d")],
                                        foreground=[("active", "white")],
                  relief=[("pressed", "sunken")])
        self.option_add('*TButton*takeFocus', 0)
        
        style.configure("GreenButton.TButton", background="#53794e")
        style.map("GreenButton.TButton", background=[("pressed", "#6e9e67"), 
                                                    ("active", "#5f8d59")],
                                                    foreground=[("active", "white")])


app = App()
app.mainloop()