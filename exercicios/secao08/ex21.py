"""
21) Escreva uma função para determinar a quantidade de números
primos abaixo de N.
"""
from collections.abc import Iterator
from locale import LC_ALL, atoi, format_string, setlocale


def get_int_larger_than_one(name: str):
    while True:
        try:
            value = atoi(input(f'Enter {name}:\n-> '))
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print(f'\033[31mINVALID {name.upper()}! Try again...\033[m\n')


def eratosthenes_sieve(limit: int) -> Iterator[int]:
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):
                a[n] = False


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    limit = get_int_larger_than_one('integer')
    prime_numbers = eratosthenes_sieve(limit)
    formatted_primes = ', '.join(
        format_string('%d', num) for num in prime_numbers
    )

    print(
        f'\nPrime numbers smaller than {limit:n}:' f'\n-> {formatted_primes}.'
    )


if __name__ == '__main__':
    main()
