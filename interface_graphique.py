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
        
        display_current_number = tk.Label(ecran, text="0", bg="#3a3a3c", anchor="w", justify="left", font=("Arial", 30), fg="white")
        display_current_number.pack(fill="x")
        
        display_result = tk.Label(ecran, text="", bg="#3a3a3c", justify="left", anchor="w", font=("Arial", 15), fg="white")
        display_result.pack(fill="x")

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
                button = tk.Button(buttons, bg="#3a3a3c", fg="white", text=button_names[i][j], font=("Arial", 30), width=5)
                button.grid(row=i, column=j, padx=5, pady=5)
        for j in range(0, 4, 2):
            button = tk.Button(buttons, bg="#53794e", fg="white", text=button_names[4][j//2], font=("Arial", 30), width=5)
            button.grid(row=4, column=j, columnspan=2, padx=5, pady=5, sticky="nswe")

app = App()
app.mainloop()