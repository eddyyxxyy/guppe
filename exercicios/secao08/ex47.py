"""
47) Faça uma função que receba ua matriz de 4 x 4 e retorne quantos valores
maiores do que 10 ela possui
"""
from collections.abc import Iterator
from random import sample


def array_values_larger_10(array: list) -> Iterator:
    counter = 0
    for row in array:
        counter += sum(value > 10 for value in row)
    return counter


def main() -> None:
    array = [
        sample(range(1, 21), 4),
        sample(range(1, 21), 4),
        sample(range(1, 21), 4),
        sample(range(1, 21), 4),
    ]
    print(
        f'{array}'
        f'\n{array_values_larger_10(array)}'
    )


if __name__ == '__main__':
    main()
