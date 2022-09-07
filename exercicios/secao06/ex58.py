"""
58) Faça um programa que some os números primos existem entre a
e b, onde a e b são números informados pelo usuário.
"""
from collections.abc import Iterator
from locale import setlocale, LC_ALL, format_string


def get_pos_int(msg: str) -> int:
    while True:
        try:
            number: int = int(input(msg).strip())
            if number <= 0:
                raise ValueError
            return number
        except ValueError:
            print('Invalid number! Try again...')


def prime_range(lower: int, upper: int) -> Iterator[int]:
    for num in range(lower, upper + 1):
        if num >= 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num


def main() -> None:
    setlocale(LC_ALL, 'pt-BR')
    lower = get_pos_int('Enter an positive integer:\n-> ')
    upper = get_pos_int('Enter an positive integer:\n-> ')
    result = tuple(prime_range(lower, upper))
    formatted_result = ', '.join(
        format_string('%d', x) for x in result
    )
    print(
        '\n' + '-' * 30 + '\n' +
        f'\nBetween {lower} and {upper}:'
        f'\n-> {len(result)} prime numbers;'
        '\n\nThe numbers between:'
        f'\n-> {formatted_result}.'
        '\n\nThe sum of all prime numbers:'
        f'\n-> {sum(result)}'
    )


if __name__ == '__main__':
    main()
