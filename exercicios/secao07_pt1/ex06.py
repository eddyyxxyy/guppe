"""
6) Faça um programa que receba do usuáro um vetor com 10 posições.
Em sequida deverá ser impresso o maior e o menor elemento do vetor.
"""
from collections.abc import Iterator
from locale import format_string, setlocale, LC_ALL


def float_iterator(n: int, msg: str) -> Iterator[float]:
    for i in range(n):
        while True:
            try:
                number = float(input(msg).strip())
                yield number
                break
            except ValueError:
                print('Invalid number! Try again...\n')


def main():
    setlocale(LC_ALL, 'pt-BR')
    numbers = tuple(float_iterator(10, 'Enter a number:\n-> '))
    formatted_numbers = ', '.join(
        format_string('%.1f', number) for number in numbers
    )
    print(
        '-' * 30 +
        '\nNumbers:'
        f'\n-> {formatted_numbers}.'
        '\nLargest number:'
        f'\n-> {max(numbers):n}'
        '\nSmallest number:'
        f'\n-> {min(numbers):n}'
    )


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:

vetor = []
for i in range(10):
    vetor.append(int(input(f'Informe o {i + 1}º valor: ')))
print(f'Para o vetor {vetor}, temos:')
print(f'Seu valor máximo: {max(vetor)}')
print(f'Seu valor mínimo: {min(vetor)}')
"""
