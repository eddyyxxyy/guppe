"""
48) Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule a soma
dos elementos que estão acima da diagonal principal.
"""
from random import sample


def sum_upper_diag(array: list):
    result = 0
    for row in range(len(array)):
        for column in range(len(array)):
            if column > row:
                result += array[row][column]
    return result


def main() -> None:
    array = [
        sample(range(1, 11), 3),
        sample(range(1, 11), 3),
        sample(range(1, 11), 3),
    ]
    print(
        f'{array[0]}'
        f'\n{array[1]}'
        f'\n{array[2]}'
        f'\n{sum_upper_diag(array)}'
    )


if __name__ == '__main__':
    main()
