def div(*nombres):
    """
    Divise le premier argument par le deuxième.

    :param arg1: Le dividende.
    :param arg2: Le diviseur.
    :return: Le quotient des deux nombres.
    :raises ValueError: Si le diviseur est zéro.
    """
    if len(nombres) != 2:
        raise ValueError("Deux arguments sont requis pour la division.")
    arg1, arg2 = nombres
    if arg2 == 0:
        raise ValueError("Division par zéro n'est pas permise.")
    return arg1 / arg2