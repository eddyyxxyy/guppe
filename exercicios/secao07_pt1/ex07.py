"""
7) Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""
from collections.abc import Iterator
from locale import atoi, setlocale, LC_ALL, format_string


def get_ints(n: int) -> Iterator[int]:
    """
    Input n integers and yields the value n times
    :param n: int
    :return: Iterator[int]
    """
    for i in range(n):
        while True:
            try:
                number = atoi(
                    input(f'Enter the {i + 1}º integer:\n-> ').strip()
                )
                yield number
                break
            except ValueError:
                print('Invalid number! Try again...')


def main():
    setlocale(LC_ALL, 'pt-BR')
    numbers = tuple(get_ints(10))
    formatted_numbers = ', '.join(
        format_string('%d', x) for x in numbers
    )
    print(
        '-' * 30 +
        '\nNumbers:'
        f'\n-> {formatted_numbers}.'
        '\nLargest number:'
        f'\n-> {max(numbers):n}.'
        '\nIndex of largest number:'
        f'\n-> {numbers.index(max(numbers))}'
    )

if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

vetor = []
for i in range(10):
    vetor.append(int(input(f'Informe um valor na posição {i}: ')))
print(f'O vetor é: {vetor}')
print(f'Seu maior número é {max(vetor)} e a posição deste máximo se encontra no índice {vetor.index(max(vetor))}')
"""
