def effacer_dernier(entree):
    """Supprime le dernier caractère de la chaîne entrée"""
    if len(entree) > 0:
        return entree[:-1]
    return entree

texte = "5*5"
texte = effacer_dernier(texte)
print(texte)  # ➜ "5*"

texte = effacer_dernier(texte)
print(texte)  # ➜ "5"

texte = effacer_dernier(texte)
print(texte)  # ➜ ""

