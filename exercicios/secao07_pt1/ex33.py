"""
33) Faça um programa que leia um vetor de 15 posições e o compacte, ou
seja, elimine as posições com valor zero. Para isso, todos os elementos
à frente do valor zero, devem ser movidos uma posição para trás no vetor.
"""
from locale import LC_ALL, format_string, setlocale

from exercicios.secao07_pt1.ex31 import get_floats


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    v = tuple(i for i in get_floats(15) if i != 0)
    print('\nV:' '\n->', ', '.join(format_string('%.1f', x) for x in v) + '.')


if __name__ == '__main__':
    main()
