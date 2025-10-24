def appuyer(t):
    """Ajoute le caractère cliqué à l’expression."""
    global expression
    expression += str(t)
    entree.delete(0, tk.END)
    entree.insert(tk.END, expression)