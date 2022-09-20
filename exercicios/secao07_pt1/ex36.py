"""
36) Leia um vetor com 10 números reais, ordene os elementos deste vetor,
e no final escreva os elementos do vetor ordenado.
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


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    v = sorted(get_floats(10))
    print('\nArray "V":' f'\n-> {v}')


if __name__ == '__main__':
    main()
