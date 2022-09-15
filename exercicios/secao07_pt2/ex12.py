"""
12) Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.
"""
from numpy import asarray, transpose

from exercicios.secao07_pt2.ex08 import get_int_array


def main() -> None:
    a = get_int_array(3, 3)
    array = asarray(a)
    array_transpose = transpose(array)
    print(
        '\nArray:'
        f'\n{array}'
        '\n\nArray transpose:'
        f'\n{array_transpose}'
    )


if __name__ == '__main__':
    main()
