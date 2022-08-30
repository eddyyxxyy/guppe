"""
11) faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem crescente.
"""

print(
    '=' * 20 + '\n' +
    'N NÚMEROS NATURAIS'.center(20, '-') + '\n' +
    '=' * 20 + '\n'
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
            while i < number + 1:
                if i == number:
                    print('\033[32;1m↓')
                print(i)
                i += 1
            print('\033[m')
            break
