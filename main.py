import tkinter as tk
from tkinter import messagebox

# === Fenêtre principale ===
root = tk.Tk()
root.title("Calculatrice Tkinter Pro")
root.geometry("350x500")
root.resizable(False, False)

# === Variables ===
expression = ""
historique = []


# === Fonctions ===
def appuyer(t):
    """Ajoute le caractère cliqué à l’expression."""
    global expression
    expression += str(t)
    entree.delete(0, tk.END)
    entree.insert(tk.END, expression)


def effacer():
    """Efface tout le contenu."""
    global expression
    expression = ""
    entree.delete(0, tk.END)


def effacer_dernier():
    """Efface le dernier caractère."""
    global expression
    expression = expression[:-1]
    entree.delete(0, tk.END)
    entree.insert(tk.END, expression)


def calculer():
    """Évalue l’expression et met à jour l’historique."""
    global expression, historique
    try:
        expr = expression.replace("×", "*").replace("÷", "/").replace("^", "**")
        resultat = eval(expr)
        entree.delete(0, tk.END)
        entree.insert(tk.END, str(resultat))
        historique.append(f"{expression} = {resultat}")
        maj_historique()
        expression = str(resultat)
    except Exception as e:
        messagebox.showerror("Erreur", f"Expression invalide : {e}")
        expression = ""


def maj_historique():
    """Met à jour la liste d’historique."""
    liste.delete(0, tk.END)
    for item in reversed(historique[-6:]):  # on affiche les 6 derniers
        liste.insert(tk.END, item)


def vider_historique():
    """Vide l’historique."""
    global historique
    historique = []
    liste.delete(0, tk.END)


# === Champ d’entrée ===
entree = tk.Entry(root, font=("Arial", 18), justify="right", bd=5, relief="sunken")
entree.pack(pady=10, fill="x", padx=10)

# === Grille de boutons ===
boutons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("÷", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("×", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("^", 4, 2), ("+", 4, 3),
    ("%", 5, 0), ("⌫", 5, 1), ("C", 5, 2), ("=", 5, 3)
]

cadre_boutons = tk.Frame(root)
cadre_boutons.pack(padx=10, pady=10)

for (texte, ligne, col) in boutons:
    if texte == "=":
        action = calculer
    elif texte == "C":
        action = effacer
    elif texte == "⌫":
        action = effacer_dernier
    else:
        action = lambda t=texte: appuyer(t)
    tk.Button(
        cadre_boutons,
        text=texte,
        width=5,
        height=2,
        font=("Arial", 14),
        command=action
    ).grid(row=ligne, column=col, padx=3, pady=3)

# === Historique ===
tk.Label(root, text="Historique :", font=("Arial", 12, "bold")).pack()
liste = tk.Listbox(root, height=6, font=("Arial", 10))
liste.pack(fill="x", padx=10, pady=5)

tk.Button(root, text="Effacer l'historique", command=vider_historique).pack(pady=5)

root.mainloop()
