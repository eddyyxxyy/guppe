"""
29) Faça uma função que receba como parâmetro o valor de um ângulo em graus e
calcule o valor do seno hiperbólico desse ângulo usando sua respectiva série de Taylor:
sinh x = E (n=0) = (x ** (2 * n + 1)) / (2 * n + 1)! = x + x**3 / 3! + x**5 / 5! ...
para tod0 x, onde x é o valor do ângulo em radianos. Considerar pi = 3.141593
e n variando de 0 até 5.
"""
from math import factorial, pi


def hyperbolic_sine(angle):
    if angle > 0:
        x = angle * pi / 180
        senh = 0
        for n in range(6):
            numerator = x ** (2 * n + 1)
            denominator = factorial(2 * n + 1)
            senh += numerator / denominator
        return f'{angle}° in radians: {x}' f'\nHyperbolic sine of {x}: {senh}'
    return '\033[31INVALID!\033[m'


def main() -> None:
    print(hyperbolic_sine(30))


if __name__ == '__main__':
    main()
