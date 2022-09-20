"""
20) Faça um programa que leia uma matriz 3 x 6 com valores reais.
(a) Imprima a soma de todos os elementos das colunas ímpares.
(b) Imprima a média aritmética dos elementos da segunda e quarta colunas.
(c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
(d) Imprima a matriz modificada.
"""
from locale import LC_ALL, setlocale

from exercicios.secao07_pt2.ex13 import get_float_array


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    array = get_float_array(3, 6)
    print('\n\nArray:')
    for row in array:
        print(row)
    odd_sum: float = 0
    arithmetic_average: float = 0
    for row in range(3):
        for column in range(6):
            if (column + 1) % 2 == 1:
                odd_sum += array[row][column]
            if (column + 1) % 2 == 0 and column != 5:
                arithmetic_average += array[row][column]
            if column == 5:
                array[row][column] = array[row][1] + array[row][3]
    arithmetic_average = arithmetic_average / 6
    print(
        f'\n\nSum of all odd columns:\n-> {odd_sum:n}'
        f'\n\nSum of all arithmetic average:\n-> {arithmetic_average:n}'
    )
    print('\n\nModified array:')
    for row in array:
        print(row)


if __name__ == '__main__':
    main()
