"""
37) Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 >
A7 > A8 > ... > A11, ou seja, está ordenando em ordem crescente até
o sexto elemento, e a partir desse elemento está ordenado em ordem decrescente.
Dado o vetor da questão anterior, proponha um algoritmo para ordenar os
elementos.
"""
from collections.abc import Iterator
from locale import LC_ALL, atof, setlocale


def get_floats(n: int) -> Iterator[float]:
    """
    Yields n floats to an Iterator
    :param n: int
    :return: Iterator[float]
    """
    for i in range(n):
        while True:
            try:
                number = atof(input(f'Enter the {i + 1}º number:\n-> '))
                yield number
                break
            except ValueError:
                print('Invalid grade value! Try again...\n')


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = list(get_floats(11))
    a = sorted(a[:6]) + sorted(a[-1:-6:-1], reverse=True)
    print('\nArray "A":' f'\n-> {a}.')


if __name__ == '__main__':
    main()
