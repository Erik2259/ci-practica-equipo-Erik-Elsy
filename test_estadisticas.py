import pytest

from estadisticas import maximo, mediana, minimo, promedio, rango


def test_promedio():
    assert promedio([2, 4, 6]) == 4


def test_mediana_impar():
    assert mediana([9, 1, 5]) == 5


def test_mediana_par():
    assert mediana([4, 1, 3, 2]) == 2.5


def test_maximo_y_minimo():
    datos = [3, -1, 8, 0]
    assert maximo(datos) == 8
    assert minimo(datos) == -1


def test_rango():
    assert rango([10, 2, 7]) == 8


@pytest.mark.parametrize("funcion", [promedio, mediana, maximo, minimo, rango])
def test_lista_vacia(funcion):
    with pytest.raises(ValueError):
        funcion([])
