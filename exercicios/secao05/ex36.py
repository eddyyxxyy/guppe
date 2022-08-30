"""
36) Escreva um programa que, dado o valor da venda, imprima a comissão
que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:
    | Venda mensal                                            | Comissão
    | Maior ou igual a R$100.000,00                           | R$700,00 + 16% das vendas
    | Menor que R$100.000,00 e maior ou igual a R$80.000,00   | R$650,00 + 14% das vendas
    | Menor que R$80.000,00 e maior ou igual a R$60.000,00    | R$600,00 + 14% das vendas
    | Menor que R$60.000,00 e maior ou igual a R$40.000,00    | R$550,00 + 14% das vendas
    | Menor que R$40.000,00 e maior ou igual a R&20.000,00    | R$500,00 + 14% das vendas
    | Menor que R$20.000,00                                   | R$400,00 + 14% das vendas
"""
from ex36_functions import real_br_money_mask

value: float = 0
# Títle and comission values
print(
    '=' * 42 + '\n' +
    'TABELA DE COMISSÕES'.center(42, '-') + '\n' +
    '=' * 42 + '\n' +
    '| ' + 'Venda Mensal'.ljust(24, ' ') + '|' + 'Comissão'.center(14, ' ') + '|\n' +
    '=' * 42 + '\n' +
    '| ' + 'Mais ou igual a 100 mil'.ljust(24, ' ') + '| 700,00 + 16% |\n' +
    '| ' + 'Entre 100 mil e 80 mil'.ljust(24, ' ') + '| 650,00 + 14% |\n' +
    '| ' + 'Entre 80 mil e 60 mil'.ljust(24, ' ') + '| 600,00 + 14% |\n' +
    '| ' + 'Entre 60 mil e 40 mil'.ljust(24, ' ') + '| 550,00 + 14% |\n' +
    '| ' + 'Entre 40 mil e 20 mil'.ljust(24, ' ') + '| 500,00 + 14% |\n' +
    '| ' + 'Menos de 20 mil'.ljust(24, ' ') + '| 400,00 + 14% |\n' +
    '=' * 42 + '\n'
)
while True:
    try:
        value = float(input(
            'Informe o valor de sua venda mensal: \033[37mDigite -1 para sair\033[m\n'
            '-> \033[37mR$\033[m').strip().replace(',', '.')
            )
    except ValueError:
        print('\nValor inválido! Tente novamente...\n')
        continue
    else:
        if value == -1:
            break
        else:
            if value < 5000:
                print('\nValor inválido! Tente novamente...\n')
                continue
            elif value >= 100_000:
                print(f'Sua comissão será de R${real_br_money_mask(700 + 0.16 * value)}')
            elif 100_000 > value >= 80_000:
                print(f'Sua comissão será de R${real_br_money_mask(650 + 0.14 * value)}')
            elif 80_000 > value >= 60_000:
                print(f'Sua comissão será de R${real_br_money_mask(600 + 0.14 * value)}')
            elif 60_000 > value >= 40_000:
                print(f'Sua comissão será de R${real_br_money_mask(550 + 0.14 * value)}')
            elif 40_000 > value >= 20_000:
                print(f'Sua comissão será de R${real_br_money_mask(500 + 0.14 * value)}')
            else:
                print(f'Sua comissão será de R${real_br_money_mask(400 + 0.14 * value)}')
