"""
56) Faça um programa que calcule a soma de todos os números primos
abaixo de dois milhões.

# Crivo de Eratóstenes aplicado
"""
from collections.abc import Iterator
from locale import setlocale, LC_ALL


def sum_primes(n):
    sum_prime = 0
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum_prime += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum_prime


def main() -> None:
    prime_sum = sum_primes(2000000)
    setlocale(LC_ALL, 'pt-BR')
    print(
        'Sum of all prime numbers below 2 million:'
        f'\n-> {prime_sum:n}'
    )


if __name__ == '__main__':
    main()
