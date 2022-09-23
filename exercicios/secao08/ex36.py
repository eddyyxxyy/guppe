"""
36) Faça uma função não-recursiva que receba um número inteiro positivo N
e retorne o superfatorial desse número. O superfatorial de um número N
é deifinida pelo produto dos N primeiros fatoriais de N. Assim, o super
fatorial de 4 é sf(4) = 1! * 2! * 3! * 4! = 288
"""
from math import factorial

from exercicios.secao08.ex26 import get_int


def super_factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result


def main() -> None:
    n = get_int('Enter no. to find his superfactorial: ', positive=True)
    result_n = super_factorial(n)
    print(f'sf({n}):' f'\n-> {result_n}')


if __name__ == '__main__':
    main()
