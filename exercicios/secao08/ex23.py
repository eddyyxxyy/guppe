"""
23) Escreva uma função que gere um triângulo lateral de altura 2*n-1 e n largura.
Por exemplo, a saída para n = 4 seria:
    *
    **
    ***
    ****
    ***
    **
    *
"""
from locale import LC_ALL, setlocale

from exercicios.secao08.ex22 import get_int


def side_triangle(width: int):
    upper_part = []
    result_string = ''
    for i in range(1, width + 1):
        upper_part.append('*' * i)
    complete_triangle = upper_part + upper_part[-2::-1]
    for piece in complete_triangle:
        result_string += piece + '\n'
    return result_string


def main() -> None:
    setlocale(LC_ALL, '')
    number = get_int("Enter no. for side triangle's width:\n-> ")
    a = side_triangle(number)
    print(f'\n{a}')


if __name__ == '__main__':
    main()
