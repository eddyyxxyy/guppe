"""
58) Faça uma função que receba, por parâmetro, duas matrizes quadradas
de ordem N, A e B, e retorna uma matriz C
"""
from random import sample


def union_array(array_a: list, array_b: list) -> list:
    result = list()
    for row in range(len(array_a)):
        result.append([])
        for column in range(len(array_a)):
            result[row].append(array_a[row][column] + array_b[row][column])
    return result


def main() -> None:
    array_a = [
        sample(range(1, 11), 4),
        sample(range(1, 11), 4),
        sample(range(1, 11), 4),
        sample(range(1, 11), 4),
    ]
    array_b = [
        sample(range(1, 11), 4),
        sample(range(1, 11), 4),
        sample(range(1, 11), 4),
        sample(range(1, 11), 4),
    ]
    print('Array "A":')
    for row in array_a:
        print(row)
    print('\nArray "B":')
    for row in array_b:
        print(row)
    print('\nArray "C":')
    array_c = union_array(array_a, array_b)
    for row in array_c:
        print(row)


if __name__ == '__main__':
    main()
