"""
10) Faça um programa que calcule e mostre a soma dos 50
primeiros números pares.
"""
from locale import format_string, atoi
from collections.abc import Iterator


def sum_n_even_numbers(n: int) -> Iterator[int]:
    for number in range(2, (n + 1) * 2, 2):
        yield number


def main():
    while True:
        try:
            times: int = atoi(input('How many even numbers you want to sum?\n-> '))
            break
        except ValueError:
            print('Invalid input! Try again...')
    numbers = tuple(sum_n_even_numbers(times))
    formatted_numbers = ", ".join(
        format_string("%d", x) for x in numbers
    )
    print(
        'Numbers'
        f'\n-> {formatted_numbers}'
        '\nSum of numbers'
        f'\n-> {sum(numbers)}'
    )


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:
print(
    '=' * 34 + '\n' +
    'SOMA DOS 50 PRIMEIROS PARES'.center(34, '-') + '\n' +
    '=' * 34 + '\n'
)

sum_number: int = 0

for number in range(2, 51, 2):
    sum_number += number

print(f'A soma dos valores equivale à: {sum_number}')
"""