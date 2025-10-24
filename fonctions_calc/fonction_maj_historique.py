def maj_historique(historique, liste):
    """Met à jour la liste d’historique."""
    liste.delete(0, "end")
    for item in reversed(historique[-6:]):
        liste.insert("end", item)