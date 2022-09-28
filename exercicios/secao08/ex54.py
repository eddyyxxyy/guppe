"""
54) Faça uma função que recebe, por parâmetro, uma matriz A[4][4] e retorna
a soma dos seus elementos
"""


def sum_elements(array: list) -> int:
    result = 0
    for row in array:
        result += sum(row)
    return result


def main() -> None:
    array0 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    print('Array:')
    for row in array0:
        print(row)
    print(f'\nSum of all elements: {sum_elements(array0)}')


if __name__ == '__main__':
    main()
