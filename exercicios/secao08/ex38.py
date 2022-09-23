"""
38) Faça uma função não-recursiva que receba um número inteiro
positivo n e retorne o fatorial exponencial desse número. Um
fatorial exponencial é um inteiro positivo n elevado à potência
de n - 1, que por sua vez é elevado à potência de n - 2 e assim
em diante. Ou seja:
n ** (n-1) ** (n-2) ...
"""
from exercicios.secao08.ex26 import get_int


def exponential_factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= pow(n, -i)

    return result


def main() -> None:
    n = get_int('Enter no. to find his exponential factorial: ', positive=True)
    result = exponential_factorial(n)
    print(f'\nef({n}):' f'\n-> {result}')


if __name__ == '__main__':
    main()
