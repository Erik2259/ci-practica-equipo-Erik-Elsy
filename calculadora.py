"""Funciones de la calculadora."""
import math


def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def resta(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicacion(a, b):
    """Devuelve el producto de a y b."""
    return a * b


def division(a, b):
    """Devuelve a entre b. Lanza ValueError si b es cero."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def potencia(base, exponente):
    """Devuelve base elevada al exponente."""
    return base ** exponente


def raiz_cuadrada(n):
    """Devuelve la raíz cuadrada de n. Lanza ValueError si n es negativo."""
    if n < 0:
        raise ValueError("No existe raíz cuadrada real de un número negativo")
    return math.sqrt(n)


def porcentaje(parte, total):
    """Devuelve qué porcentaje representa parte respecto de total."""
    if total == 0:
        raise ValueError("El total no puede ser cero")
    return parte * 100 / total
