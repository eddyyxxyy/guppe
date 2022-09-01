"""
16) Faça um programa que leia um número inteiro positivo impar N
imprima todos os núemros impares de 1 até N em ordem decrescente.
"""
from collections.abc import Iterator
from locale import atoi, format_string


def get_bool(msg: str) -> bool:
    while True:
        try:
            return {"d": True, "a": False}[input(msg).strip().lower()[0]]
        except KeyError:
            print("Invalid input! Please enter Descending or Ascending!")


def get_posit_odd_integer() -> int:
    while True:
        try:
            posit_odd_integer: int = atoi(input('Enter a positive odd number:\n-> ').strip())
            if posit_odd_integer % 2 == 0:
                print('Number must be odd! Try again...')
                continue
            return posit_odd_integer
        except ValueError:
            print('ERROR! Try again...\n')


def odd_till_n(invert: bool = False) -> Iterator[int]:
    n: int = get_posit_odd_integer()
    if not invert:
        for number in range(1, n + 1, 2):
            yield number
    else:
        for number in range(n, 0, -2):
            yield number


def main():
    invert = get_bool('Ascending or Descending order? \033[37mA or D\033[m\n-> ')
    numbers = tuple(odd_till_n(invert))
    formatted_numbers = ', '.join(
        format_string("%d", x) for x in numbers
    )
    print('Numbers in ', end='')
    if invert:
        print(
            'ascending order:'
            f'\n-> {formatted_numbers}'
        )
    else:
        print(
            'descending order:'
            f'\n-> {formatted_numbers}'
        )


if __name__ == '__main__':
    main()
