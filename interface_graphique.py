import calculs
import tkinter as tk

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self["bg"] = "#121213"
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
                button = tk.Button(buttons, text=button_names[i][j], 
                                   command = lambda name=button_names[i][j]: self.button_pressed(name),
                                   bg="#3a3a3c", fg="white", font=("Arial", 30), width=5)
                button.grid(row=i, column=j, padx=5, pady=5)
        for j in range(0, 4, 2):
            button = tk.Button(buttons, text=button_names[4][j//2],
                               command = lambda name=button_names[4][j//2]: self.button_pressed(name),
                               bg="#53794e", fg="white", font=("Arial", 30), width=5)
            button.grid(row=4, column=j, columnspan=2, padx=5, pady=5, sticky="nswe")


        self.current_formula = "0"

    
    def button_pressed(self, name):
        if name == "=":
            self.display_result.configure(text=str(self.calculeResultat(self.current_formula)))
        
        else:           
            if name == "AC":
                self.current_formula = "0"
            elif self.current_formula == "0":
                self.current_formula = name
            else:
                self.current_formula += name
            self.display_current_formula.configure(text=self.current_formula)


    def calculeResultat(self, formula):
        return "0"


app = App()
app.mainloop()