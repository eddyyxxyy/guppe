"""
23) Faça um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A²
"""
from locale import LC_ALL, setlocale

from exercicios.secao07_pt2.ex17 import get_float_array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = get_float_array(3, 3)
    b = []
    for row in range(3):
        temp_row = []
        for column in range(3):
            temp_row.append(a[row][column] ** 2)
        b.append(temp_row)
    print('\nArray A:')
    for row in a:
        print(row)
    print('\nArray B:')
    for row in b:
        print(row)


if __name__ == '__main__':
    main()
