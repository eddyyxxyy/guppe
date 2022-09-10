"""
26) Faça um programa que calcule o desvio padrão de um vetor
v contendo n = 10 números, onde m é a média do vetor.
    Desvio Padrão = raiz quadrada de ((E (v[i] - M)²) / n)
"""
from collections.abc import Iterable
from locale import setlocale, LC_ALL
from math import sqrt

from exercicios.secao07_pt1.ex07 import get_ints


def standard_deviation(iterable: Iterable) -> float:
    mean = sum(iterable) / len(tuple(iterable))
    var = sum((iterab - mean) ** 2 for iterab in iterable) / len(tuple(iterable))
    return sqrt(var)


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    n: tuple[int] = tuple(get_ints(10))
    st_dev: float = standard_deviation(n)
    print(
        '-' * 30,
        '\nStandard deviation:'
        f'\n-> {st_dev:n}.'
    )


if __name__ == '__main__':
    main()
