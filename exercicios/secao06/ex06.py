"""
6) Faça um programa que leia 10 inteiros e imprima sua média.
"""

from collections.abc import Iterator
from locale import LC_ALL, atof, format_string, setlocale


def get_numbers(n: int) -> Iterator[float]:
    for question in range(1, n + 1):
        while True:
            try:
                yield atof(input(f'{question}º número:\n-> '))
                break
            except ValueError:
                print('Entrada inválida! Tente novamente...')


def main() -> None:
    setlocale(LC_ALL, 'pt-BR')
    print(
        '=' * 22
        + '\n'
        + 'MÉDIA DE 10 INTEIROS'.center(22, '-')
        + '\n'
        + '=' * 22
        + '\n'
    )
    numbers = tuple(get_numbers(10))
    formatted_numbers = ', '.join(format_string('%.1f', x) for x in numbers)
    print(
        '\nNúmeros:'
        f'\n{formatted_numbers}'
        f'\nSoma: {format_string("%.1f", sum(numbers) / len(numbers))}'
    )


if __name__ == '__main__':
    main()

"""
print(
    '=' * 22 + '\n' +
    'MÉDIA DE 10 INTEIROS'.center(22, '-') + '\n' +
    '=' * 22 + '\n'
)

average_numbers: list = list()

for i in range(10):
    while True:
        try:
            number = int(input(f'Informe o {i + 1}º número:\n->  ').strip())
        except ValueError:
            print('Valor inválido! Informe somente números inteiros...\n')
            continue
        else:
            average_numbers.append(number)
            break

print(
    f'\nValores: {average_numbers}\n'.replace('[', '').replace(']', '') +
    f'A média dos valores: {sum(average_numbers) / len(average_numbers)}'
)
"""
