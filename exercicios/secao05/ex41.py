"""
41) Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua
classificação de acordo com a tabela abaixo:
    |     IMC      | Classificação
    | < 18,5       | Abaixo do Peso
    | 18,6 - 24,9  | Saudável
    | 25,0 - 29,9  | Peso em excesso
    | 30,0 - 34,9  | Obesidade Grau I
    | 35,0 - 39,9  | Obesidade Grau II(severa)
    | >= 40        | Obesidade Grau III(mórbida)
"""

altura: float = 0
quilos: float = 0
imc: float = 0

while True:
    try:
        altura = float(input(
            'Sua altura: \033[37mEx: 1.82\033[m\n'
            '->  '
        ).strip().replace(',', '.'))
    except ValueError:
        print('Altura inválida! Informe novamente...\n')
        continue
    else:
        if altura < 0.5:
            print('Altura inválida! Informe novamente...\n')
            continue
        while True:
            try:
                quilos = float(input(
                    'Seu peso: \033[37mEx: 64.5\033[m\n'
                    '->  '
                ).strip().replace(',', '.'))
            except ValueError:
                print('Peso inválido! Informe novamente...\n')
                continue
            else:
                if quilos <= 0:
                    print('Peso inválido! Informe novamente...\n')
                    continue
                break
        break

imc = quilos / (altura * altura)

if imc < 18.5:
    print(
        f'Seu IMC: {imc:.2f}\n'
        f'Classificação: Abaixo do peso'
    )
elif 18.6 <= imc <= 24.9:
    print(
        f'Seu IMC: {imc:.2f}\n'
        f'Classificação: Saudável'
    )
elif 25.0 <= imc <= 29.9:
    print(
        f'Seu IMC: {imc:.2f}\n'
        f'Classificação: Peso em excesso'
    )
elif 30.0 <= imc <= 34.9:
    print(
        f'Seu IMC: {imc:.2f}\n'
        f'Classificação: Obesidade de Grau I'
    )
elif 35.0 <= imc <= 39.9:
    print(
        f'Seu IMC: {imc:.2f}\n'
        f'Classificação: Obesidade de Grau II (Severa)'
    )
else:
    print(
        f'Seu IMC: {imc:.2f}\n'
        f'Classificação: Obesidade de Grau III (Mórbida)'
    )
