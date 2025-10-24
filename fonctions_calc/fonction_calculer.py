def calculer():
    """Évalue l’expression complète."""
    global expression, resultat_affiche, historique

    try:
        # Séparer les nombres et opérateurs
        # Remplace les opérateurs par des séparateurs compatibles Python
        expr = expression.replace('×', '*').replace('÷', '/').replace('^', '**').replace('%', '%')
        # Évalue avec précaution
        res = eval(expr)
        entree.delete(0, tk.END)
        entree.insert(tk.END, str(res))
        resultat_affiche = True

        # Enregistrer dans l’historique
        historique.append(f"{expression} = {res}")
        maj_historique()

        expression = str(res)

    except Exception as e:
        messagebox.showerror("Erreur", f"Expression invalide : {e}")
        expression = ""