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