"""
27) Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os
elementos que são primos e suas respectivas posições no vetor.
"""
from collections import deque
from collections.abc import Iterable, Iterator
from locale import LC_ALL, format_string, setlocale

from exercicios.secao07_pt1.ex07 import get_ints


def extract_prime_numbers(n: Iterable) -> Iterator:
    for i in n:
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += 1
        if c == 1:
            yield i


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    primes = deque(extract_prime_numbers(get_ints(10)))
    if len(primes):
        formatted_primes = ', '.join(format_string('%d', x) for x in primes)
        print('\nPrime numbers:' f'\n-> {formatted_primes}.')
    else:
        print('\nThere was no prime number entered.')


if __name__ == '__main__':
    main()
