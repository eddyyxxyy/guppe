"""
24) Escreva um porgrama que leia um número inteiro e calcule a
soma de todos os divisores desse número, com exceção dele próprio.
Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""
from collections.abc import Iterator
from locale import atoi, format_string


def get_number(msg: str = 'Enter a number:\n-> ') -> int:
    while True:
        try:
            num = atoi(input(msg).strip())
            return num
        except ValueError:
            print('Invalid number! Try again...\n')


def get_divisors() -> Iterator[int]:
    number = get_number()
    if number <= 0:
        yield 0
    for num in range(1, number + 1):
        if number % num == 0:
            yield num


def main():
    divisors = tuple(get_divisors())
    formatted_divisors = ', '.join(
        format_string('%d', x) for x in divisors[:-1]
    )
    print(
        f'\n\033[37mNot including {divisors[-1]}\033[m'
        f'\nDivisors for {divisors[-1]}:'
        f'\n-> {formatted_divisors}'
        f'\nSum of all divisors:'
        f'\n-> {sum(divisors[:-1])}'
    )


if __name__ == '__main__':
    main()
