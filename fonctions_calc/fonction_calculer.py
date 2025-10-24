from tkinter import messagebox
from fonction_maj_historique import maj_historique

def calculer(entree, historique, liste):
    """Calcule le résultat et met à jour l’historique."""
    expression = entree.get()
    try:
        expr = expression.replace("×", "*").replace("÷", "/").replace("^", "**")
        resultat = eval(expr)
        entree.delete(0, "end")
        entree.insert("end", str(resultat))
        historique.append(f"{expression} = {resultat}")
        maj_historique(historique, liste)
    except Exception as e:
        messagebox.showerror("Erreur", f"Expression invalide : {e}")
        entree.delete(0, "end")