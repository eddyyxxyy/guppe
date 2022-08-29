"""
28) Faça um programa que leia três números inteiros positivos e efetue
o cálculo de uma das seguintes médias de acordo com um valor numérico
digitado pelo usuário:
    (a) Geométrica: ³√x * y * z
    (b) Ponderada: (x + 2 * y + 3 * z) / 6
    (c) Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))
    (d) Aritmética: (x + y + z) / 3
"""
x: int
y: int
z: int
option: str
print('-=' * 15 + '\n' + 'CÁLCULO DE MÉDIAS'.center(30, '-') + '\n' + '=-' * 15)
while True:
    try:
        x = int(input('Informe um valor para x: ').strip())
    except ValueError:
        print('\nValor inválido!\n')
        continue
    else:
        while True:
            try:
                y = int(input('Informe um valor para y: ').strip())
            except ValueError:
                print('\nValor inválido!\n')
                continue
            else:
                while True:
                    try:
                        z = int(input('Informe um valor para z: ').strip())
                    except ValueError:
                        print('\nValor inválido!\n')
                        continue
                    else:
                        break
            break
    break
print('-' * 30 + '\n' +
      f'Valores escolhidos: \nx = {x},\ny = {y},\nz = {z}'.ljust(30) + '\n' +
      '-' * 30)
print(
    'Qual média gostaria de calcular?\n'
    '(a) Geométrica: Raiz cúbica de (x * y * z)\n'
    '(b) Ponderada: (x + 2 * y + 3 * z) / 6\n'
    '(c) Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))\n'
    '(d) Aritmética: (x + y + z) / 3\n'
)
while True:
    try:
        option = str(input('->  ').strip().lower())[0]
    except IndexError:
        print('\nOpção inválida! Tente novamente...\n')
        continue
    else:
        if option not in 'abcd':
            print('\nOpção inválida! Tente novamente...\n')
            continue
        print()
        if option == 'a':
            print('A média geométrica é:\n'
                  f'({x} * {y} * {z}) ** (1 / 3) = {(x * y * z) ** (1 / 3)}')
        elif option == 'b':
            print('A média ponderada é:\n'
                  f'({x} + 2 * {y} + 3 * {z}) / 6 = {(x + 2 * y + 3 * z) / 6}')
        elif option == 'c':
            print('A média harmônica é:\n'
                  f'1 / (1 / {x}) + (1 / {y}) + (1 / {z}) = {1 / (1 / x) + (1 / y) + (1 / z)}')
        elif option == 'd':
            print('A média aritmética é:\n'
                  f'({x} + {y} + {z}) / 3 = {(x + y + z) / 3}')
    break
