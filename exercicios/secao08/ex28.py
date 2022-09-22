"""
28) Faça uma função que receba como parâmetro o valor de um ângulo em grau
e calcule o valor do cosseno desse ângulo usando sua respectiva série de Taylor:
cos x = E(n=0) = (-1) ^ n / (2 * n)! * (x ^ 2 * n) = 1 - (x^2 / 2!) + (x^4 / 4!) - ...
para tod0 x, onde x é o valor do ângulo em radianos. Considerar pi = 3.141593 e n variando
de 0 até 5.
"""
from math import factorial, radians

from exercicios.secao08.ex27 import get_degrees


def cos(x, n):
    x = radians(x)
    return sum(
        (-1) ** k * x ** (2 * k) / factorial(2 * k) for k in range(n + 1)
    )


def main() -> None:
    result = cos(
        x=get_degrees('Enter size in degrees for the angle:\n-> '), n=5
    )
    print(result)


if __name__ == '__main__':
    main()
