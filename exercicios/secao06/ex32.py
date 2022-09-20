"""
32) Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes,
e tem como saída o número de cada dado e a relação entre eles (>, <, =) de
cada lançamento
"""
from collections.abc import Iterator
from locale import atoi
from random import randint


def get_integer(msg: str = 'Enter an integer:\n-> ') -> int:
    while True:
        try:
            number = atoi(input(msg).strip())
            return number
        except ValueError:
            print('Invalid number! Try again...')


def throw_dice() -> Iterator[tuple]:
    times_thrown = get_integer(
        'Enter the number of times you want to throw the dices:\n-> '
    )
    for times in range(times_thrown):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        yield d1, d2


def main():
    throws = tuple(throw_dice())
    for index, throw in enumerate(throws):
        print(f'\n{index + 1}º throw:' f'\n-> {throw}', end='')
        if throw[0] == throw[1]:
            print(' -> Same numbers')
        else:
            if throw[0] > throw[1]:
                print(f' -> First dice > Second dice')
            else:
                print(f' -> Second dice > First dice')


if __name__ == '__main__':
    main()
