"""
52) Escreva uma função que recebe uma matriz quadrada de ordem
N e calcule a sua transposta (se B é a matriz transposta de A então aij = bji).
"""


def transpose(array: list) -> list:
    return list(map(list, zip(*array)))


def main():
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    array_transposed = transpose(array)
    # print(tuple(zip(*array)))
    print('Array:')
    for row in array:
        print(row)
    print('\nArray transpose:')
    for row in array_transposed:
        print(row)


if __name__ == '__main__':
    main()
