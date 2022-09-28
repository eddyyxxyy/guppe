"""
56) Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e uma linha N
e retorne a soma dos elementos dessa linha.
"""
from random import sample


def sum_row(array: list, row: int) -> int:
    return sum(array[row])


def main() -> None:
    array = [
        sample(range(1, 11), 7),
        sample(range(1, 11), 7),
        sample(range(1, 11), 7),
        sample(range(1, 11), 7),
        sample(range(1, 11), 7),
        sample(range(1, 11), 7),
        sample(range(1, 11), 7),
    ]
    print('Array:')
    for row in array:
        print(row)
    print(f'\nSum of elements from row 0: {sum_row(array, 0)}')
    print(f'Sum of elements from row 1: {sum_row(array, 1)}')
    print(f'Sum of elements from row 2: {sum_row(array, 2)}')
    print(f'Sum of elements from row 3: {sum_row(array, 3)}')
    print(f'Sum of elements from row 4: {sum_row(array, 4)}')
    print(f'Sum of elements from row 5: {sum_row(array, 5)}')
    print(f'Sum of elements from row 6: {sum_row(array, 6)}')


if __name__ == '__main__':
    main()
