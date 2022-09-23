"""
35) Faça uma função não-recursiva que receba um número inteiro positivo n
e retorne o fatorial quádruplo desse número. O fatorial quádruplo de um número n é dado
por: (2 * n)! / n!
"""
from math import factorial

from ex33 import get_positive_int


def quad_factorial(n: int):
    return factorial(2 * n) / factorial(n)


def main() -> None:
    num = get_positive_int('Enter positive integer: ')
    result = quad_factorial(num)
    print(f'{num}!!!! = {result}')


if __name__ == '__main__':
    main()
