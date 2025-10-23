def effacer():
    """Efface tout le champ d’entrée."""
    global expression
    expression = ""
    entree.delete(0, tk.END)