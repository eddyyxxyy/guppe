"""
9) Crie um programa que lê 6 valores inteiros pares e,
em seguida, mostre na tela os valores lidos na ordem inversa.
"""
from collections import deque
from collections.abc import Iterator
from locale import LC_ALL, atoi, format_string, setlocale


def get_even_ints(n: int) -> Iterator[int]:
    count: int = 1
    for i in range(n):
        while True:
            try:
                number = atoi(
                    input(f'Enter the {count}º even integer:\n-> ').strip()
                )
                if number % 2 != 0:
                    raise ValueError
                yield number
                count += 1
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    even_numbers = deque(get_even_ints(6))
    formatted_numbers = ', '.join(format_string('%d', x) for x in even_numbers)
    even_numbers.reverse()
    formatted_numbers_inverted = ', '.join(
        format_string('%d', x) for x in even_numbers
    )
    print(
        '-' * 30 + '\nNumbers:'
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
    while True:
        lista.append(int(input('Informe um número par: ')))
        if lista[i] % 2 != 0:
            lista.pop()
            print('O número precisa ser par...')
        else:
            print('Número par adicionado com sucesso.')
            break

print(f'A lista de pares invertida: {list(reversed(lista))}')
"""
