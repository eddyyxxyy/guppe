"""
12) Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem decrescente
"""

print(
    '=' * 35 + '\n' +
    'N NÚMEROS NATURAIS (INVERSAMENTE)'.center(35, '-') + '\n' +
    '=' * 35 + '\n'
)

number: int = 0
i: int = 0

while True:
    try:
        number = int(input('Informe um número inteiro positivo: ').strip())
    except ValueError:
        print('Valor inválido! Tente novamente...\n')
    else:
        if number <= 0:
            print('Valor inválido! Tente novamente...\n')
        else:
            print()
            for i in range(number, -1, -1):
                if i == number:
                    lenght = len(str(i))
                    print(f'\033[32;1m{i}')
                    print('\033[32;1m' + '↑'.center(lenght))
                else:
                    print('\033[m' + f'{i}')
                    i += 1
            break
