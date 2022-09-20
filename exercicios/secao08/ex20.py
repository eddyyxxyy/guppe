"""
20) Faça um algoritmo que receba um número inteiro positivo n
e calcule o seu fatorial, n!
"""
from locale import LC_ALL, setlocale
from math import factorial

from exercicios.secao08.ex17 import get_positive_int


def n_factor2(n: int):
    result = n
    for i in range(n - 1, 0, -1):
        result *= i
    return result


def n_factor(n: int):
    return factorial(n)


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    n = get_positive_int('n')
    n1 = get_positive_int('n1')
    print(f'\n{n:n}!' f'\n-> {n_factor(n):n}')
    print(f'\n{n1:n}!' f'\n-> {n_factor2(n1):n}')


if __name__ == '__main__':
    main()
