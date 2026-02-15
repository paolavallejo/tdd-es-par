def es_par(n: int) -> bool:
    """
    Devuelve True si 'n' es un número par; en caso contrario, False.
    Un entero es par cuando el residuo de dividirlo entre 2 es 0.
    """
    return (n % 2) == 0