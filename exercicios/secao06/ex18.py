"""
18) Escreva um algoritmo que leia certa quantidade de números
e imprima o maior deles e quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""
from collections.abc import Iterator
from locale import atoi, format_string


def get_times():
    while True:
        try:
            times: int = atoi(
                input('How many numbers you want to analyse?\n-> ').strip()
            )
            if times < 0:
                print('The amount of numbers must be positive or zero.\n')
                continue
            return times
        except (ValueError, AssertionError):
            print('The amount of numbers must be positive or zero.\n')


def get_numbers(
    times: int, msg: str = 'Enter a number:\n-> '
) -> Iterator[int]:
    counter: int = 0
    while counter < times:
        counter += 1
        try:
            number: int = atoi(input(msg).strip())
            if number <= 0:
                print('Number must be a positive integer...\n')
                continue
            yield number
        except ValueError:
            print('Invalid value!\n')


def main():
    from time import sleep

    times = get_times()
    if times == 0:
        print('Shutting down operation...')
        sleep(2)
        exit()
    numbers = tuple(get_numbers(times, 'Enter a positive integer:\n-> '))
    formatted_numbers = ', '.join(format_string('%d', x) for x in numbers)
    print(
        '\nNumbers:'
        f'\n{formatted_numbers}'
        '\nLargest number:'
        f'\n{max(numbers)}'
        '\nAmount of time largest number appears:'
        f'\n{numbers.count(max(numbers))}'
    )


if __name__ == '__main__':
    main()
