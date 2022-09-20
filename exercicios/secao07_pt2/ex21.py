"""
21) Faça um programa que leia duas matrizes 2 x 2 com valores reais.
Ofereça ao usuário um menu de opções:
(a) somar as duas matrizes
(b) subtrair a primeira matriz da segunda
(c) adicionar uma constante às duas matrizes
(d) imprimir as matrizes
"""
from locale import LC_ALL, atof, setlocale

from exercicios.secao07_pt2.ex17 import get_float_array


def get_option():
    while True:
        try:
            option = (
                input(
                    'a) Sum a1 and a2;'
                    '\nb) Subtract a1 from a2:'
                    '\nc) Sum a constant to arrays:'
                    '\nd) Show a1 and a2.'
                    '\n-> '
                )
                .strip()
                .lower()[0]
            )
            if option not in 'abcd':
                raise ValueError
            break
        except ValueError:
            print('\nINVALID! Try again...')
    return option


def get_value():
    while True:
        try:
            value = atof(input('Enter no. to sum to arrays:\n->'))
            return value
        except ValueError:
            print('\nINVALID! Try again...')


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    a1 = get_float_array(2, 2)
    print()
    a2 = get_float_array(2, 2)
    a3 = []
    a4 = []
    for row in range(2):
        sum_rows = []
        sub_rows = []
        for column in range(2):
            sum_rows.append(a1[row][column] + a2[row][column])
            sub_rows.append(a2[row][column] - a1[row][column])
        a3.append(sum_rows)
        a4.append(sub_rows)
    print('\n')
    print('MENU'.center(20))
    option = get_option()
    if option == 'a':
        for row in a3:
            print(row)
    elif option == 'b':
        for row in a4:
            print(row)
    elif option == 'c':
        value = get_value()
        for row in range(2):
            for column in range(2):
                a1[row][column] += value
                a2[row][column] += value
        for row in a1:
            print(row)
        print()
        for row in a2:
            print(row)
    else:
        for row in a1:
            print(row)
        print()
        for row in a2:
            print(row)


if __name__ == '__main__':
    main()
