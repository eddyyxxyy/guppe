"""
22) Faça um programa que leia duas matrizes A e B
de tamanho 3 x 3 e calcule C = A * B.
"""
from locale import LC_ALL, setlocale

from exercicios.secao07_pt2.ex17 import get_float_array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = get_float_array(3, 3)
    print()
    b = get_float_array(3, 3)
    c = []
    for row in range(3):
        temp_row = []
        for column in range(3):
            temp_row.append(a[row][column] * b[row][column])
        c.append(temp_row)
    for row in range(3):
        print(a[row])
    print()
    for row in range(3):
        print(b[row])
    print()
    for row in range(3):
        print(c[row])


if __name__ == '__main__':
    main()
