"""
8) Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = ((a ** 2) + (b ** 2)) ** 0.5. Faça uma função
que receba os valores de a e b e calcule o valor da hipotenusa através da equação
"""
from locale import LC_ALL, setlocale

from exercicios.secao08.ex07 import get_float


def hypotenuse(a, b):
    return ((a**2) + (b**2)) ** 0.5


def main() -> None:
    setlocale(LC_ALL, '')
    a = get_float('lenght of a')
    b = get_float('lenght of b')
    h = hypotenuse(a, b)
    print(
        '\nA:' f'\n-> {a:n}' '\nB:' f'\n-> {b:n}' '\nHypotenuse:' f'\n-> {h}'
    )


if __name__ == '__main__':
    main()
