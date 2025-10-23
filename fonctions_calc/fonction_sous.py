def sous(*nombres):
    """
    Soustrait deux nombres.

    :param arg1: Le premier nombre.
    :param arg2: Le deuxième nombre.
    :return: La différence des deux nombres.
    """
    if len(nombres) < 2:
        raise ValueError("Deux arguments sont requis pour la soustraction.")
    result = nombres[0]
    for nombre in nombres[1:]:
        result -= nombre
    return print(result)