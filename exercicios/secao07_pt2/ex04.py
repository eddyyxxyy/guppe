"""
4) Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e coluna)
do maior valor.
"""
from collections import deque
from locale import LC_ALL, atof, setlocale


def get_float_array(rows, columns) -> deque[deque]:
    """
    Takes in the number of rows and columns
    to be read and return a deque[deque[float]]

    :param rows: int
    :param columns: int
    :return: deque[deque[float]]
    """
    array = deque()
    for c in range(0, rows):
        row = deque()
        for i in range(0, columns):
            while True:
                try:
                    value = atof(input(f'Enter no. for [{c},{i}]:\n-> '))
                    break
                except ValueError:
                    print('\033[31mINVALID! Try again!\033[m')
            row.append(value)
        array.append(row)
    return array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = get_float_array(4, 4)
    largest_number = deque()
    for index, row in enumerate(array):
        if index == 0:
            largest_number = [index, row.index(max(row)), max(row)]
        if max(row) > largest_number[2]:
            largest_number = [index, row.index(max(row)), max(row)]
    print('\nArray:')
    for row in range(4):
        for column in range(4):
            print(f'{array[row][column]:n}', end='  ')
        print()
    print(
        '\nLargest number in array:'
        f'\n-> {largest_number[2]:n} -> in position [{largest_number[0]},{largest_number[1]}].'
    )


if __name__ == '__main__':
    main()
