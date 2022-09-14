"""
8) Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que
estão acima da diagonal principal.

if linha < coluna:  # Acima da diagonal principal

elif linha == coluna:  # Diagonal principal

elif linha > coluna:  # Abaixo da diagonal principal
"""
from locale import setlocale, LC_ALL, atoi


def get_int_array(rows: int, columns: int) -> list[list[int]]:
    array = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = atoi(
                        input(f'Enter no. to [{i},{j}]:\n-> ')
                    )
                    break
                except ValueError:
                    print('\033[31mINVALID! Try again...\033[m\n')
            row.append(value)
        array.append(row)
    return array


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = get_int_array(3, 3)
    sum_above_diagonal_array = 0
    print('\nArray:')
    for i in range(3):
        print(array[i])
        for j in range(3):
            if i < j:
                sum_above_diagonal_array += array[i][j]
    print(
        '\nSum of values above main diagonal:'
        f'\n-> {sum_above_diagonal_array}.'
    )



if __name__ == '__main__':
    main()
