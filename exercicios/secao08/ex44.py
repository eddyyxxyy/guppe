"""
44) Faça uma função que receba como parâmetro um vetor X de
30 elementos inteiros e retorne, também por parâmetro, dois vetores
A e B. O vetor A deve conter os elementos pares de X eo vetor B, os
elementos impares
"""
from random import sample


def even_odd_arrays(x: list, a=None, b=None) -> tuple[list, list]:
    if b is None:
        b = []
    if a is None:
        a = []
    a = [num for num in x if num % 2 == 0]
    b = [num for num in x if num % 2 == 1]
    return a, b


def main() -> None:
    array = sample(range(0, 100), 30)
    arrays_a_b = even_odd_arrays(array)
    print(f'{array}' f'\n{arrays_a_b[0]}' f'\n{arrays_a_b[1]}')


if __name__ == '__main__':
    main()
