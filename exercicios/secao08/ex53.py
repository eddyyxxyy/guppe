"""
53) Faça uma função que verifica se uma matriz quadrada de ordem
N é a matriz identidade.
"""


def is_identity_array(array: list) -> bool:
    result = True
    for row in range(len(array)):
        for column in range(len(array)):
            if row == column:
                if array[row][column] != 1:
                    result = False
            else:
                if array[row][column] != 0:
                    result = False
    return result


def main() -> None:
    array0 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f'Array 0: ({is_identity_array(array0)})')
    for row in array0:
        print(row)
    print(f'\nArray 1: ({is_identity_array(array1)})')
    for row in array1:
        print(row)


if __name__ == '__main__':
    main()
