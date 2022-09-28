"""
57) Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e
uma coluna N e retorne a soma dos elementos dessa coluna.
"""
from random import sample


def sum_column(array: list, column: int) -> int:
    result = 0
    for row in range(len(array)):
        for col in range(len(array)):
            if col == column:
                result += array[row][col]
    return result


def main() -> None:
    array = [
        sample(range(1, 11), 6),
        sample(range(1, 11), 6),
        sample(range(1, 11), 6),
        sample(range(1, 11), 6),
        sample(range(1, 11), 6),
        sample(range(1, 11), 6),
        sample(range(1, 11), 6),
    ]
    print('Array:')
    for row in array:
        print(row)
    print(f'\nSum of elements from column 0: {sum_column(array, 0)}')


if __name__ == '__main__':
    main()
