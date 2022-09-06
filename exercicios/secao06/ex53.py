"""
53) Escreva um programa que leia um número inteiro positivo n e em
seguida imprima n linhas do chamado Triangulo de Floyd. Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 10 21
"""
from locale import atoi


def get_positive_int(msg: str = 'Enter an integer:\n-> ') -> int:
    while True:
        try:
            number: int = atoi(input(msg))
            if number < 1:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def floyd_triangle(rows):
    c = 0
    for i in range(1, rows + 1):
        for j in range(0, i):
            c += 1
            print(c, end=' ')
        print()


def main() -> None:
    rows = get_positive_int()
    floyd_triangle(rows)


if __name__ == '__main__':
    main()
