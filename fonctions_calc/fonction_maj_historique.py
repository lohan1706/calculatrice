def maj_historique():
    """Met à jour la zone d’historique."""
    liste.delete(0, tk.END)
    for item in historique[-10:][::-1]:  # affiche les 10 derniers
        liste.insert(tk.END, item)