"""
31) Faça um programa que leia dois vetores de 10 elementos. Crie
um vetor que seja a união entre os 2 vetores anteriores, ou seja,
que contém os números dos dois vetores. Não deve conter números
repetidos.
"""
from collections.abc import Iterator
from locale import setlocale, LC_ALL, atof, format_string


def get_floats(n: int) -> Iterator[float]:
    """
    Yields n floats to an Iterator
    :param n: int
    :return: Iterator[float]
    """
    for i in range(n):
        while True:
            try:
                number = atof(
                    input(f'Enter the {i + 1}º number:\n-> ')
                )
                yield number
                break
            except ValueError:
                print('Invalid grade value! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    v1 = tuple(get_floats(10))
    print()
    v2 = tuple(get_floats(10))
    v3: set = set(v1).union(v2)
    print(
        '\nV1:'
        f'\n->', ', '.join(
            format_string('%.1f', x) for x in v1
        ) +
        '\nV2:'
        f'\n->', ', '.join(
            format_string('%.1f', x) for x in v2
        ) +
        '\nV3 (Union V1-V2):'
        f'\n->', ', '.join(
            format_string('%.1f', x) for x in v3
        )
    )


if __name__ == '__main__':
    main()
