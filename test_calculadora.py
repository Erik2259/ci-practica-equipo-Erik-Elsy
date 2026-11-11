import pytest

from calculadora import (
    division,
    multiplicacion,
    porcentaje,
    potencia,
    raiz_cuadrada,
    resta,
    suma,
)


def test_suma():
    assert suma(2, 3) == 5


def test_resta():
    assert resta(5, 2) == 3


def test_multiplicacion():
    assert multiplicacion(3, 3) == 9


@pytest.mark.parametrize(
    "a, b, esperado",
    [(-2, 3, 1), (0, 0, 0), (1.5, 2.5, 4.0), (-4, -6, -10)],
)
def test_suma_casos_limite(a, b, esperado):
    assert suma(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [(0, 5, -5), (-3, -3, 0), (2.5, 0.5, 2.0)],
)
def test_resta_casos_limite(a, b, esperado):
    assert resta(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [(0, 99, 0), (-2, 4, -8), (-3, -3, 9), (0.5, 4, 2.0)],
)
def test_multiplicacion_casos_limite(a, b, esperado):
    assert multiplicacion(a, b) == esperado


def test_division():
    assert division(10, 2) == 5


def test_division_decimal():
    assert division(1, 4) == 0.25


def test_division_entre_cero():
    with pytest.raises(ValueError):
        division(5, 0)


def test_potencia():
    assert potencia(2, 10) == 1024


def test_potencia_exponente_cero():
    assert potencia(7, 0) == 1


def test_raiz_cuadrada():
    assert raiz_cuadrada(81) == 9


def test_raiz_cuadrada_negativa():
    with pytest.raises(ValueError):
        raiz_cuadrada(-1)


def test_porcentaje():
    assert porcentaje(25, 200) == 12.5


def test_porcentaje_total_cero():
    with pytest.raises(ValueError):
        porcentaje(5, 0)
