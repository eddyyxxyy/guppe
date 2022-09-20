"""
2) Escreva um prorgama que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes.
A primeira vez deve usar a estrutura de repetição for, a segunda while.
"""
from collections.abc import Iterator
from locale import format_string


def one_to_hundred_for() -> Iterator[int]:
    """yield the numbers from 1 to 100 using for loop"""
    for number in range(1, 101):
        yield number


def one_to_hundred_while() -> Iterator[int]:
    """yield the numbers from 1 to 100 using while loop"""
    number = 0
    while number < 100:
        number += 1
        yield number


def main() -> None:
    print(
        '=' * 30
        + '\n'
        + 'FROM 1 TO 100'.center(30, '-')
        + '\n'
        + '=' * 30
        + '\n'
    )
    numbers_a = tuple(one_to_hundred_for())
    formatted_numbers_a = ', '.join(format_string('%d', x) for x in numbers_a)
    numbers_b = tuple(one_to_hundred_while())
    formatted_numbers_b = ', '.join(format_string('%d', x) for x in numbers_b)
    print('Using for:' f'\n{formatted_numbers_a}')
    print('\nUsing while:' f'\n{formatted_numbers_b}')


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:
print(
    '=' * 24 + '\n' +
    'DE 1 A 100, DUAS VEZES'.center(24, '-') + '\n' +
    '=' * 24 + '\n'
)

for i in range(1, 101):
    print(str(f'{i},').ljust(3), end=' ')
    if i % 10 == 0:
        print()

print()

cont: int = 1
while cont <= 100:
    print(str(f'{cont},').center(3), end=' ')
    if cont % 10 == 0:
        print()
    cont += 1"""
