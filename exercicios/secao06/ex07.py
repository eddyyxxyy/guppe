"""
7) Faça um programa que leia 10 inteiros positivos, ignorando não positivos,
e imprima sua média
"""
from locale import atoi
from collections.abc import Iterator


def get_numbers(n: int) -> Iterator[int]:
    for question in range(1, n + 1):
        while True:
            try:
                yield atoi(input(f'{question}º number: '))
                break
            except ValueError:
                print('Invalid number! Try again...')


def main() -> None:
    while True:
        try:
            times = atoi(input('How many numbers you want to input?\n->  '))
            break
        except ValueError:
            print('Invalid input! Try again...')
    numbers = tuple(get_numbers(times))
    average = sum(numbers) / len(numbers)
    print(
        'Numbers:'
        f'\n{numbers}'
        f'\nAverage of the numbers: {average}'
    )


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:
print(
    '=' * 44 + '\n' +
    'MÉDIA DE 10 NÚMEROS (INTEIROS E POSITIVOS)'.center(44, '-') + '\n' +
    '=' * 44 + '\n'
)

average_numbers: list = list()

for i in range(10):
    while True:
        try:
            number = int(input(f'Informe o {i + 1}º número inteiro positivo:\n'
                               f'->  ').strip())
        except ValueError:
            print('Valor inválido!')
        else:
            if number > 0:
                average_numbers.append(number)
            else:
                pass
            break

print(
    '\nValores:\n'
    f'{average_numbers}\n'.replace('[', '').replace(']', '') +
    f'A média dos valores equivale à {sum(average_numbers) / len(average_numbers):.2f}'
)
"""
