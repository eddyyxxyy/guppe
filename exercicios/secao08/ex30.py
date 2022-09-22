"""
30) Faça uma função que receba como parâmetor o valor de um ângulo em graus e calcule
o valor do cosseno hiperbólico desse ângulo usando sua respectiva série de Taylor:
cosh x = E (n=0) = (x**(2*n)) / (2n)! = 1 + (x**2) / 2! + (x*4) / (4)! + ...
para tod0 x, onde x é o valor do ângulo em radianos. Considerar pi = 3.141593 e
n variando de 0 até 5.
"""

from math import factorial, pi


def hyperbolic_cos(angle):
    if angle > 0:
        x = angle * pi / 180
        cosh = 0
        for n in range(6):
            numerator = x ** (2 * n)
            denominator = factorial(2 * n)
            cosh += numerator / denominator
        return (
            f'{angle}° in radians: {x}' f'\nHyperbolic cossine of {x}: {cosh}'
        )
    return '\033[31mINVALID!\033[m'


def main() -> None:
    angle = int(input('Enter value in degrees:\n-> '))
    print(f'\n{hyperbolic_cos(angle)}')


if __name__ == '__main__':
    main()
