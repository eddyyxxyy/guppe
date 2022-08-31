"""
14) Faça um programa que leia um número inteiro positivo par N e imprima
todos os números pares de 0 até N em ordem decrescente.
"""

from collections.abc import Iterator
from locale import atoi


def get_num(prompt: str = "Enter a number: ") -> int:
    while True:
        try:
            number = atoi(input(prompt + '\n-> ').strip())
            if number <= 0:
                continue
            return number
        except ValueError:
            print("Must enter a positive integer!\n")


def even_numbers_till_n(invert: bool = False) -> Iterator[int]:
    number: int = get_num()
    if invert:
        for num in range(0, number + 1):
            if num % 2 == 0:
                yield num
    else:
        for num in range(number, -1, -1):
            if num % 2 == 0:
                yield num


def main():
    print('All the even numbers till "n"')
    while True:
        try:
            invert = atoi(input('\n(0)Descending or (1)Ascending order?\n-> ').strip())
            if invert != 1 and invert != 0:
                print('Only type 0 or 1...\n')
                continue
            break
        except ValueError:
            print('Must be an integer...\n')
    even_numbers = tuple(even_numbers_till_n(bool(invert)))
    print('Even numbers ', end='')
    if invert == 0:
        print('in descending order (0 included):')
    else:
        print('in ascending order (0 included):')
    for index, value in enumerate(even_numbers):
        if index == len(even_numbers) - 1:
            print(f'{value}.')
        else:
            print(f'{value}, ', end='')


if __name__ == '__main__':
    main()
