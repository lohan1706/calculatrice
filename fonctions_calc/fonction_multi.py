def multi(*args):
    """Retourne le produit de tous les arguments fournis.

    Args:
        args: Nombres à multiplier.

    Returns:
        Le produit des nombres.
    """
    produit = 1
    for nombre in args:
        produit *= nombre
    return produit