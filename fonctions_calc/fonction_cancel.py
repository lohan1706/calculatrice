def effacer_dernier():
    """Efface le dernier caractère."""
    global expression
    expression = expression[:-1]
    entree.delete(0, tk.END)
    entree.insert(tk.END, expression)