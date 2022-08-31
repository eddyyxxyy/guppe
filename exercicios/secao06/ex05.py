"""
5) Faça um programa que peça ao usuário para digitar
10 valores e some-os.
"""

from locale import atof, format_string, setlocale, LC_ALL
from collections.abc import Iterator


def get_numbers(n: int) -> Iterator[float]:
    for question in range(1, n + 1):
        while True:
            try:
                yield atof(input(f'{question}º número: '))
                break
            except ValueError:
                print('Entrada inválida! Tente novamente...')


def main() -> None:
    setlocale(LC_ALL, 'pt-BR')
    numbers = tuple(get_numbers(10))
    formatted_numbers = ", ".join(
        format_string('%.1f', x) for x in numbers
    )
    print(
        '\nNúmeros:'
        f'\n{formatted_numbers}'
        f'\nSoma: {format_string("%.1f", sum(numbers))}.'
    )


if __name__ == '__main__':
    main()

"""
print(
    '=' * 20 + '\n' +
    'SOMA DE 10 NÚMEROS'.center(20, '-') + '\n' +
    '=' * 20 + '\n'
)

sum_numbers: list = list()

for question in range(1, 11):
    while True:
        try:
            print(f'Informe o {question}º número: ')
            asnwer = float(input('->  ').strip().replace(',', '.'))
        except ValueError:
            print('Valor inválido! Tente novamente...\n')
            continue
        else:
            sum_numbers.append(asnwer)
            break

print(
    '\nNúmeros informados:\n'
    f'{sum_numbers}\n'.replace('[', '').replace(']', '') +
    f'\nA soma dos números acima equivale à {sum(sum_numbers)}.'
)
"""