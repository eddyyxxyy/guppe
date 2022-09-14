"""
10) Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos
que estão na diagonal principal.

if linha < coluna:  # Acima da diagonal principal

if linha == coluna:  # Diagonal principal

if linha > coluna:  # Abaixo da diagonal principal
"""
from locale import setlocale, LC_ALL

from exercicios.secao07_pt2.ex08 import get_int_array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = get_int_array(3, 3)
    sum_array_diagonal: int = 0
    print('\nArray:')
    for i in range(len(a)):
        print(a[i])
        for j in range(len(a[i])):
            if i == j:
                sum_array_diagonal += a[i][j]
    print(
        '\nSum of main diagonal of array:'
        f'\n-> {sum_array_diagonal}.'
    )


if __name__ == '__main__':
    main()
