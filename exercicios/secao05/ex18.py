"""
18) Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas(as básicas, por exemplo). O usuário escolhe uma das opções e o seu
programa então pede dois valores numéricos e realiza a operação, mostrando o
resultado e saindo.
"""
import ex18_functions

num1 = 0
num2 = 0
selected_option = 0
print('-=' * 15 + '\n' + 'MENU'.center(30, '-') + '\n' + '=-' * 15)
print('Informe a função desejada:'.center(30))
print('1 - Soma;\n' '2 - Subtração;\n' '3 - Multiplicação;\n' '4 - Divisão.')
while True:
    try:
        selected_option = round(float(input('-> ').strip().replace(',', '.')))
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        print(f'Opção selecionada {selected_option}')
        if not 1 <= selected_option <= 4:
            print('Valor inválido!')
            continue
        else:
            while True:
                try:
                    num1 = float(
                        input('Informe o primeiro número: ')
                        .strip()
                        .replace(',', '.')
                    )
                except ValueError:
                    print('Valor inválido!')
                    continue
                else:
                    while True:
                        try:
                            num2 = float(
                                input('Informe o segundo número: ')
                                .strip()
                                .replace(',', '.')
                            )
                        except ValueError:
                            print('Valor inválido!')
                            continue
                        else:
                            break
                    break
            break
"""
Não consegui utilizar HOF nesse exercício
"""
print(f'\nO resultado da operação é: ', end='')
if selected_option == 1:
    print(ex18_functions.sumnumbers(num1, num2))
elif selected_option == 2:
    print(ex18_functions.subtract(num1, num2))
elif selected_option == 3:
    print(ex18_functions.multiply(num1, num2))
elif selected_option == 4:
    print(ex18_functions.divide(num1, num2))
