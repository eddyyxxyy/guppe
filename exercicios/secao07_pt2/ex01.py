"""
1) Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""
from locale import setlocale, LC_ALL, atof


def get_array_test(rows, columns):
    array = list()
    for c in range(0, rows):
        row = list()
        for i in range(0, columns):
            while True:
                try:
                    value = atof(
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
    array = get_array(4, 4)
    elements_larger_than_10 = []
    for element in array:
        for value in element:
            if value > 10:
                elements_larger_than_10.append(value)
    print('\nMatriz:')
    for element in array:
        print(f'{element}')
    print(
        '\nAmount of values that are > 10:'
        f'\nNumbers -> {elements_larger_than_10}'
        f'\nAmount -> {len(elements_larger_than_10)}'
    )


if __name__ == '__main__':
    main()
