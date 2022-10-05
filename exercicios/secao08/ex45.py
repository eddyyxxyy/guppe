"""
45) Faça uma função que calcule o desvio padrão de um vetor contendo n números
Desvio Padrão = raiz quadrada de ((E (v[i] - M)²) / n)
onde m é a media do vetor.
"""
from math import sqrt
from random import sample


def standard_deviation(array: list):
    return sqrt(
        sum(
            ((value - sum(array) / len(array)) ** 2) / len(array)
            for value in array
        )
    )


def main() -> None:
    array = sample(range(0, 100), 5)
    print(
        'Array:'
        f'\n-> {array}'
        '\nStandard deviation:'
        f'\n-> {standard_deviation(array)}'
    )


if __name__ == '__main__':
    main()
