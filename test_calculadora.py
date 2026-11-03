import pytest

from calculadora import somar, subtrair, multiplicar, dividir, fatorial, eh_primo


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_subtrair():
    assert subtrair(10, 4) == 6
    assert subtrair(0, 5) == -5


def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(1, 0)


def test_fatorial():
    assert fatorial(0) == 1
    assert fatorial(5) == 120


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-3)


def test_eh_primo():
    assert eh_primo(2)
    assert eh_primo(17)
    assert not eh_primo(1)
    assert not eh_primo(15)
