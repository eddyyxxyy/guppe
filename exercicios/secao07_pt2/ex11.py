"""
11) Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão
na diagonal secundária.

if linha < coluna:  # Acima da diagonal principal

if linha == coluna:  # Diagonal principal

if linha > coluna:  # Abaixo da diagonal principal
"""
from locale import setlocale, LC_ALL

from numpy import asarray, trace, diagonal, fliplr

from exercicios.secao07_pt2.ex08 import get_int_array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = get_int_array(3, 3)
    a1 = asarray(a)
    a1 = fliplr(a1)
    print('\nArray:')
    for row in a:
        print(row)
    print('\nAntidiagonal (sum): ', trace(a1))
    print('Antidiagonal (elements): ', diagonal(a1))


if __name__ == '__main__':
    main()
