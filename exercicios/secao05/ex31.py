"""
31) Faça um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela a seguir, verifique e mostre qual a classificação
dessa pessoa.
    |    Altura    |                       Peso                       |
    |              |Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90  |
    |Menor que 1,20|   A   |             D             |      G       |
    |De 1,20 a 1,70|   B   |             E             |      H       |
    |Maior que 1,70|   C   |             F             |      I       |
"""
print('-=' * 15 + '\n' + 'CLASSIFICAÇÃO POR PESO/ALTURA'.center(30, '-') + '\n' + '=-' * 15)
altura: float = 0
peso: float = 0
while True:
    try:
        altura = float(input('Informe sua altura: ').strip().replace(',', '.'))
    except ValueError:
        print('\nAltura inválida! Informe novamente...\n')
        continue
    else:
        if altura < 0.54 or altura > 2.50:
            print('\nAltura inválida! Informe novamente...\n')
            continue
        while True:
            try:
                peso = float(input('Informe seu peso: ').strip().replace(',', '.'))
            except ValueError:
                print('\nPeso inválido! Informe novamente...\n')
                continue
            else:
                if peso < 25 or peso > 600:
                    print('\nPeso inválido! Informe novamente...\n')
                    continue
                break
    break
if altura < 1.20:
    if peso < 60:
        print('Sua classificação: A.')
    elif 60 <= peso <= 90:
        print('Sua classificação: D.')
    else:
        print('Sua classificação: G')
elif 1.20 <= altura <= 1.70:
    if peso < 60:
        print('Sua classificação: B.')
    elif 60 <= peso <= 90:
        print('Sua classificação: E.')
    else:
        print('Sua classificação: H')
else:
    if peso < 60:
        print('Sua classificação: C.')
    elif 60 <= peso <= 90:
        print('Sua classificação: F.')
    else:
        print('Sua classificação: I')
