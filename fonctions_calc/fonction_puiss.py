def puissance(*nombres):
    """
    Élève le premier argument à la puissance du deuxième.

    :param arg1: La base.
    :param arg2: L'exposant.
    :return: Le résultat de la puissance.
    """
    if len(nombres) != 2:
        raise ValueError("Deux arguments sont requis pour la puissance.")
    arg1, arg2 = nombres
    return print(arg1 ** arg2)
