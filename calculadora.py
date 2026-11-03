"""Pequena biblioteca de funções matemáticas para o exercício de GitHub Actions."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


def fatorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fatorial definido apenas para inteiros não negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def eh_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == "__main__":
    print("2 + 3 =", somar(2, 3))
    print("5! =", fatorial(5))
    print("17 é primo?", eh_primo(17))
