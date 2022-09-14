"""
9) Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos
que estão abaixo da diagonal principal

if linha < coluna:  # Acima da diagonal principal

if linha == coluna:  # Diagonal principal

if linha > coluna:  # Abaixo da diagonal principal
"""
from locale import setlocale, LC_ALL

from exercicios.secao07_pt2.ex08 import get_int_array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = get_int_array(3, 3)
    sum_below_diagonal = 0
    print('\nArray:')
    for i in range(3):
        print(array[i])
        for j in range(3):
            if i > j:
                sum_below_diagonal += array[i][j]
    print(
        '\nSum of below above main diagonal:'
        f'\n-> {sum_below_diagonal}.'
    )


if __name__ == '__main__':
    main()
