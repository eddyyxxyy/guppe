"""
39) Escreva um programa que leia um número inteiro positivo n em seguida
imprima n linhas do chamado Triangulo de Pascal:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
"""
from locale import setlocale, LC_ALL

from exercicios.secao07_pt1.ex35 import get_int


def pascals_triangle(n):
    if n == 1:
        return [[1]]
    new_row = [1]
    result = pascals_triangle(n - 1)
    last_row = result[-1]
    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])
    new_row.append(1)
    result.append(new_row)
    return result


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    for row in pascals_triangle(get_int("Pascal's Triangle")):
        print(*row)


if __name__ == '__main__':
    main()
