"""
22) Faça um programa que leia dois vetores de 10 posições e calcule
outro vetor contendo, nas posições pares os valores do primeiro
e nas posições impares os valores do segundo.
"""
from collections import deque
from locale import setlocale, LC_ALL, format_string

from exercicios.secao07_pt1.ex21 import get_array


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a = tuple(get_array(10, 'A'))
    print()
    b = tuple(get_array(10, 'B'))
    c = deque()
    for i in range(10):
        c.append(a[i])
        c.append(b[i])
    formatted_a = ', '.join(
        format_string('%d', x) for x in a
    )
    formatted_b = ', '.join(
        format_string('%d', x) for x in b
    )
    formatted_c = ', '.join(
        format_string('%d', x) for x in c
    )
    print(
        '\nArrays:'
        f'\nA -> {formatted_a}.'
        f'\nB -> {formatted_b}.'
        f'\nC -> {formatted_c}.'
    )


if __name__ == '__main__':
    main()
