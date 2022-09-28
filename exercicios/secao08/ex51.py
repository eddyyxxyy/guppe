"""
51) Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule
e retorne a soma dos elementos que estão na diagonal secundária.
"""
from random import sample


def sum_secondary_diag(array: list):
    result = 0
    for row in range(len(array)):
        for column in range(len(array)):
            if (row + column) == (len(array) - 1):
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
        f'\n{sum_secondary_diag(array)}'
    )


if __name__ == '__main__':
    main()
