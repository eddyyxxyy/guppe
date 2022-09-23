"""
37) Faça uma função não-recursiva que receba um número inteiro positivo n
e retorne o hiperfatorial desse número. O hiperfatorial de um número n,
escrito H(n), é definido por:
H(n) = | | n / k=1  k**k = 1**1 . 2**2 . 3**3 ... (n - 1) ** n-1 . n**n
"""
from exercicios.secao08.ex26 import get_int


def hyper_factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= pow(i, i)

    return result


def main() -> None:
    n = get_int('Enter no. to find his hyperfactorial: ', positive=True)
    result = hyper_factorial(n)
    print(f'hf({n}):' f'\n-> {result}')


if __name__ == '__main__':
    main()
