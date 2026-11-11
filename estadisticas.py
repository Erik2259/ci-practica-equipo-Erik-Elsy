"""Funciones estadísticas básicas sobre listas de números."""


def _validar(valores):
    if not valores:
        raise ValueError("La lista no puede estar vacía")


def promedio(valores):
    """Devuelve la media aritmética de la lista."""
    _validar(valores)
    return sum(valores) / len(valores)


def mediana(valores):
    """Devuelve la mediana de la lista."""
    _validar(valores)
    ordenados = sorted(valores)
    mitad = len(ordenados) // 2
    if len(ordenados) % 2 == 1:
        return ordenados[mitad]
    return (ordenados[mitad - 1] + ordenados[mitad]) / 2


def maximo(valores):
    """Devuelve el valor máximo de la lista."""
    _validar(valores)
    return max(valores)


def minimo(valores):
    """Devuelve el valor mínimo de la lista."""
    _validar(valores)
    return min(valores)


def rango(valores):
    """Devuelve la diferencia entre el máximo y el mínimo."""
    _validar(valores)
    return max(valores) - min(valores)
