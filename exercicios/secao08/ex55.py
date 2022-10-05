"""
55) Faça uma função que recebe, por parâmetro, uma matriz A[3][3] e
retorna a soma dos elementos da sua diagonal principal e da sua diagonal secundária
"""
from random import sample


def sum_diags(array: list):
    result = 0
    for row in range(len(array)):
        for column in range(len(array)):
            if column == row:
                result += array[row][column]
            if (row + column) == (len(array) - 1):
                result += array[row][column]

    return result - array[len(array) // 2][len(array) // 2]


def main() -> None:
    array = [
        sample(range(1, 11), 3),
        sample(range(1, 11), 3),
        sample(range(1, 11), 3),
    ]
    print(
        f'{array[0]}' f'\n{array[1]}' f'\n{array[2]}' f'\n{sum_diags(array)}'
    )


if __name__ == '__main__':
    main()
