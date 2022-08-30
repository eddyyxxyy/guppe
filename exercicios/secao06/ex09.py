"""
9) Faça um programa que leia um número inteiro N e depois imprima
os N primeiros números naturais ímpares
"""

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
