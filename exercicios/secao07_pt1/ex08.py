"""
8) Crie um programa que lê 6 valores inteiros e, em seguida, mostre
na tela os valores lidos na ordem inversa
"""
from collections import deque
from collections.abc import Iterator
from locale import atoi, setlocale, LC_ALL, format_string


def get_even_ints(n: int) -> Iterator[int]:
    count: int = 1
    for i in range(n):
        while True:
            try:
                number = atoi(
                    input(f'Enter the {count}º integer:\n-> ').strip()
                )
                yield number
                count += 1
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    numbers = deque(get_even_ints(6))
    formatted_numbers = ', '.join(
        format_string('%d', x) for x in numbers
    )
    numbers.reverse()
    formatted_numbers_inverted = ', '.join(
        format_string('%d', x) for x in numbers
    )
    print(
        '-' * 30 +
        '\nNumbers:'
        f'\n-> {formatted_numbers}.'
        '\nInverted numbers:'
        f'\n-> {formatted_numbers_inverted}.'
    )


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

lista = []
for i in range(6):
    lista.append(int(input('Informe um valor: ')))
print(f'A lista: {lista}')
print(f'A lista lida inversamente: {list(reversed(lista))}')
# print(f'A lista lida inversamente: ', end='')
# print(*lista[::-1], sep=', ')
"""
