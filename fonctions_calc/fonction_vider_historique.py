def vider_historique():
    """Vide l’historique."""
    global historique
    historique = []
    liste.delete(0, tk.END)