import tkinter as tk

class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self.geometry("400x400")
        self.config(bg="#1e1e1e")
        self.create_widgets()

    def create_widgets(self):
        self.resultat = tk.StringVar()
        self.resultat.set("0")

        ecran = tk.Entry(self, textvariable=self.resultat, font=("Arial", 24), bg="#1e1e1e", fg="#ffffff", bd=0, justify=tk.RIGHT)
        ecran.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8, sticky="nsew")

        boutons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
        ]

        for (text, row, col) in boutons:
            b = tk.Button(self, text=text, font=("Arial", 18), bg="#4e4e4e", fg="#ffffff", command=lambda t=text: self.on_click(t))
            b.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_click(self, text):
        if text == "=":
            try:
                expression = self.resultat.get()
                resultat = eval(expression)
                self.resultat.set(resultat)
            except Exception as e:
                self.resultat.set("Erreur")
        else:
            if self.resultat.get() == "0" or self.resultat.get() == "Erreur":
                self.resultat.set("")
            self.resultat.set(self.resultat.get() + text)

if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
