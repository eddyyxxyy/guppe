"""
30)Faça um programa que leia dois vetores de 10 elementos. Crie
um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que
contém apenas os números que estão em ambos os vetores. Não deve
conter números repetidos.
"""
from collections.abc import Iterable, Iterator
from locale import LC_ALL, atoi, format_string, setlocale


def get_ints(n: int) -> Iterator[int]:
    """
    Yields n times an integer value to form an Iterator.
    :param n: int
    :return: Iterator[int]
    """
    for i in range(n):
        while True:
            try:
                integer = atoi(input(f'Enter the {i + 1}º integer:\n-> '))
                yield integer
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def intersection(lst1: Iterable, lst2: Iterable) -> set:
    """
    Takes in 2 iterables to return their intersection
    :param lst1: Iterable
    :param lst2: Iterable
    :return: set
    """
    return set(lst1).intersection(lst2)


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    v1 = tuple(get_ints(10))
    print()
    v2 = tuple(get_ints(10))
    v3 = intersection(v1, v2)
    print(
        '\nV1:' '\n->',
        ', '.join(format_string('%d', x) for x in v1) + '.',
        '\nV2:' '\n->',
        ', '.join(format_string('%d', x) for x in v2) + '.',
        '\nV3 (Intersection of V1 and V2):' '\n->',
        ', '.join(format_string('%d', x) for x in v3) + '.',
    )


if __name__ == '__main__':
    main()
