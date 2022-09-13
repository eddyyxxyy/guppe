"""
5) Leia uma matriz 5 x 5. Leia também um valor X. O programa
deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização
(linha e coluna) ou mensagem de "não encontrado".
"""
from collections import deque
from locale import setlocale, LC_ALL, atoi

from exercicios.secao07_pt1.ex35 import get_int


def get_int_array(rows: int, columns: int) -> deque[deque]:
    """
    Takes in the number of rows and columns
    to be read and return a deque[deque[int]]

    :param rows: int
    :param columns: int
    :return: deque[deque[int]]
    """
    array = deque()
    for c in range(0, rows):
        row = deque()
        for i in range(0, columns):
            while True:
                try:
                    value = atoi(
                        input(f'Enter no. for [{c},{i}]:\n-> ')
                    )
                    break
                except ValueError:
                    print('\033[31mINVALID! Try again!\033[m')
            row.append(value)
        array.append(row)
    return array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = get_int_array(5, 5)
    print()
    x = get_int(name='x')
    print()
    for index, row in enumerate(array):
        try:
            row.index(x)
        except ValueError:
            pass
        finally:
            if x in row:
                print(f'First {x} FOUND in [{index},{row.index(x)}].')
            else:
                print(f'{x} not found in row {index}.')


if __name__ == '__main__':
    main()
