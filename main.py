import tkinter as tk
from tkinter import messagebox
import os
import sys

# === Import des fonctions depuis le dossier fonctions_calc ===
sys.path.append(os.path.join(os.path.dirname(__file__), "fonctions_calc"))

from fonction_appuyer import appuyer
from fonction_calculer import calculer
from fonction_effacer import effacer
from fonction_cancel import effacer_dernier
from fonction_maj_historique import maj_historique
from fonction_vider_historique import vider_historique

# === Fenêtre principale ===
root = tk.Tk()
root.title("Calculatrice Tkinter Pro")
root.geometry("350x500")
root.resizable(False, False)

# === Variables globales ===
expression = ""
historique = []

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
        action = lambda: calculer(entree, historique, liste)
    elif texte == "C":
        action = lambda: effacer(entree)
    elif texte == "⌫":
        action = lambda: effacer_dernier(entree)
    else:
        action = lambda t=texte: appuyer(t, entree)
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

tk.Button(root, text="Effacer l'historique", command=lambda: vider_historique(historique, liste)).pack(pady=5)

root.mainloop()
