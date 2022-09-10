"""
29) Faça um programa que receba 6 números inteiros e mostre:
    . Os números pares digitados;
    . A soma dos números pares digitados;
    . Os números ímpares digitados;
    . A quantidade de número ímpares digitados;
"""
from locale import setlocale, LC_ALL

from exercicios.secao07_pt1.ex07 import get_ints


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_ints(6))
    even_n = tuple(x for x in numbers if x % 2 == 0)
    odd_n = tuple(filter(lambda x: (x % 2 != 0), numbers))
    print(
        '\nEven numbers:'
        f'\n-> {even_n}'
        '\nSum of even numbers:'
        f'\n-> {sum(even_n)}'
        '\nOdd numbers:'
        f'\n-> {odd_n}'
        '\nHow many odd numbers were entered:'
        f'\n-> {len(odd_n)}'
    )


if __name__ == '__main__':
    main()
