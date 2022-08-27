"""
21) Escreva o menu de opções abaixo. Leia a opção do usuário e
execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
    Escolha a opção:
    1 - Soma de 2 números.
    2 - Diferença entre 2 números (maior pelo menor).
    3 - Produto entre 2 números.
    4 - Divisão entre 2 números (o denominador não pode ser zero).
    Opção
"""
import ex18_functions

print('=' * 30 + '\n' + 'MENU'.center(30, '-') + '\n' + '=' * 30)
print('Escolha a opção: '.ljust(30))
print(
    '1 - Soma de 2 números;\n'
    '2 - Diferença entre 2 números (maior pelo menor);\n'
    '3 - Produto entre 2 números;\n'
    '4 - Divisão entre 2 números.\n'
)
selected_option = 0
while True:
    try:
        selected_option = round(float(input('Opção escolhida ->  ').strip().replace(',', '.')))
    except ValueError:
        print('Valor inválido!\n')
        continue
    else:
        if not 1 <= selected_option <= 4:
            print('Valor inválido!\n')
            continue
        else:
            break
while selected_option == 1:
    try:
        n1 = float(input('Informe o primeiro número da soma: ').strip().replace(',', '.'))
    except ValueError:
        print('Valor inválido!\n')
        continue
    else:
        while True:
            try:
                n2 = float(input('Informe o segundo número da soma: ').strip().replace(',', '.'))
            except ValueError:
                print('Valor inválido!\n')
                continue
            else:
                print('\nOperação de soma:\n')
                print(f'{n1} + {n2} = {ex18_functions.sumnumbers(n1, n2)}')
                break
    break
while selected_option == 2:
    try:
        n1 = float(input('Informe o primeiro número da diferença do '
                         'maior pelo menor: ').strip().replace(',', '.'))
    except ValueError:
        print('Valor inválido!\n')
        continue
    else:
        while True:
            try:
                n2 = float(input('Informe o segundo número da diferença do '
                                 'maior pelo menor: ').strip().replace(',', '.'))
            except ValueError:
                print('Valor inválido!\n')
                continue
            else:
                print('\nOperação de subtração:\n')
                if n1 > n2:
                    print(f'{n1} - {n2} = {ex18_functions.subtract(n1, n2)}')
                    break
                else:
                    print(f'{n2} - {n1} = {ex18_functions.subtract(n2, n1)}')
                    break
    break
while selected_option == 3:
    try:
        n1 = float(input('Informe o primeiro número da multiplicação: ').strip().replace(',', '.'))
    except ValueError:
        print('Valor inválido!\n')
        continue
    else:
        while True:
            try:
                n2 = float(input('Informe o segundo número da multiplicação: ').strip().replace(',', '.'))
            except ValueError:
                print('Valor inválido!\n')
                continue
            else:
                print('\nOperação de multiplicação:\n')
                print(f'{n1} x {n2} = {ex18_functions.multiply(n1, n2)}')
                break
    break
while selected_option == 4:
    try:
        n1 = float(input('Informe o número à ser dividido: ').strip().replace(',', '.'))
    except ValueError:
        print('Valor inválido!\n')
        continue
    else:
        if n1 == 0:
            print('Valor inválido!\n')
            continue
        while True:
            try:
                n2 = float(input('Informe o divisor: ').strip().replace(',', '.'))
            except ValueError:
                print('Valor inválido!\n')
                continue
            else:
                if n2 == 0:
                    print('Valor inválido!\n')
                    continue
                else:
                    print('\nOperação de divisão:\n')
                    print(f'{n1} / {n2} = {ex18_functions.divide(n1, n2)}')
                    break
    break
