"""
9) Faça um programa que leia um número inteiro N e depois imprima
os N primeiros números naturais ímpares
"""
from locale import atoi, format_string
from collections.abc import Iterator


def first_n_oddnumbers(n: int) -> Iterator[int]:
    i: int = 0
    odd: int = 1
    while i < n:
        yield odd
        i += 1
        odd += 2


def main():
    while True:
        try:
            n = atoi(input('Number of odd numbers to be shown: '))
            break
        except ValueError:
            print('Invalid number! Try again...')
    numbers = tuple(first_n_oddnumbers(n))
    formatted_numbers = ", ".join(
        format_string("%d", x) for x in numbers
    )
    print(
        f'\nFirst {n} natural odd numbers:'
        f'\n→ {formatted_numbers}'
    )


if __name__ == '__main__':
    main()

"""
# Minha antiga solução:
print(
    '=' * 19 + '\n' +
    'N NÚMEROS IMPARES'.center(19, '-') + '\n' +
    '=' * 19 + '\n'
)

number: int = 0
continuar: str = ''

while True:
    try:
        number = int(input('Informe um número diferentes de 0:\n->  ').strip())
    except ValueError:
        print('Valor inválido! Informe somente números inteiros...\n')
    else:
        if number == 0:
            print('-' * 34)
        i: int = 0
        impar: int = 1
        while i < number:
            print(impar)
            i += 1
            impar += 2
    while True:
        try:
            continuar = str(
                input('Quer verificar outro número? \033[37mSim ou Não\033[m\n->  ').strip().lower()[0]
            )
        except IndexError:
            print('Resposta inválida! Informe somente Sim ou Não...\n')
        else:
            if continuar not in 'sn':
                print('Resposta inválida! Informe somente Sim ou Não...\n')
                continue
            break
    if continuar == 'n':
        break
"""