def appuyer(touche):
    """Ajoute la touche à l’expression ou remplace le résultat précédent."""
    global expression, resultat_affiche
    if resultat_affiche:
        # si un résultat est affiché et qu’on tape un chiffre ou un point, on remplace
        if touche.isdigit() or touche == '.':
            expression = touche
        else:
            expression += touche
        resultat_affiche = False
    else:
        expression += touche
    entree.delete(0, tk.END)
    entree.insert(tk.END, expression)