def effacer_dernier(entree):
    """Supprime le dernier caractère."""
    contenu = entree.get()
    entree.delete(0, "end")
    entree.insert("end", contenu[:-1])