"""
16) Usando switch, escreva um programa que leia um inteiro entre 1 e 12
e imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2,
e assim por diante.
"""
print('-' * 30 + '\n' + 'Meses do Ano'.center(30, '-') + '\n' + '-' * 30)
meses = (
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
)
while True:
    try:
        ma = round(float(input('Informe um número entre 1 e 12: ').strip().replace(',', '.')))
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        if not 1 <= ma <= 12:
            print('Valor inválido!')
            continue
        else:
            print(f'O mês do ano que corresponde à {ma} é {meses[ma - 1]}!')
            break
