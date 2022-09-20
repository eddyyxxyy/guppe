"""
18) Faça um programa que leia um vetor de 10 números. Leia um
número x. Conte os múltiplos de um número inteiro x num vetor
e mostre-os na tela.
"""
from collections import deque
from collections.abc import Iterator
from locale import LC_ALL, atof, atoi, format_string, setlocale


def get_floats(n: int) -> Iterator[float]:
    for i in range(n):
        while True:
            try:
                number = atof(input(f'Enter {i + 1}º number:\n-> '))
                yield number
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def get_int():
    while True:
        try:
            number = atoi(input('Enter an integer:\n-> '))
            return number
        except ValueError:
            print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = tuple(get_floats(10))
    print()
    x = get_int()
    multiples = deque()
    for number in numbers:
        multiples.append(x * number)
    formatted_multiples = ', '.join(
        format_string('%.1f', x) for x in multiples
    )
    print('\nMultiples:' f'\n-> {formatted_multiples}.')


if __name__ == '__main__':
    main()
