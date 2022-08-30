"""
40) O custo ao consumidor de um carro novo é a soma do custo de fábrica, da
comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados
sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e
escreva o custo ao consumidor
    |      CUSTO DE FÁBRICA          | % DO DISTRIBUIDOR | % DOS IMPOSTOS |
    | até R$12.000,00                |         5         |    isento      |
    | entre R$12.000,00 e 25.000,00  |        10         |      15        |
    | acima de R$25.000,00           |        15         |      20        |
"""
from ex36_functions import real_br_money_mask

cf: float = 0  # Custo de fábrica

print(
    '=' * 30 + '\n' +
    'PRECIFICADOR DE VEÍCULOS'.center(30, '-') + '\n' +
    '=' * 30 + '\n'
)

while True:
    try:
        cf = float(input(
            'Custo de fábrica: \n'
            '\033[37m-> R$\033[m'
        ).strip().replace(',', '.'))
    except ValueError:
        print('\nCusto de fabricação inválido! Tente novamente...\n')
        continue
    else:
        if cf <= 0:
            print('\nCusto de fabricação inválido! Tente novamente...\n')
            continue
        break

if cf <= 12_000:
    print(
        f'\nO preço final do carro é de: R${real_br_money_mask(cf * 1.05)};\n'
        '\nPelo valor ser abaixo ou igual à R$12.000,00:\n'
        f'Comissão do distribuidor de 5% (R${real_br_money_mask(cf * 1.05 - cf)}) sobre custo de fabricação;\n'
        'Isento de impostos.'
    )
elif 12_000 < cf < 25_000:
    print(
        f'\nO preço final do carro é de: R${real_br_money_mask((cf * 1.1) + (cf * 1.15 - cf))};\n'
        '\nPelo valor ser acima de R$12.000,00 e abaixo R$25.000,00:\n'
        f'Comissão do distribuidor de 10% (R${real_br_money_mask(cf * 1.1 - cf)}) sobre custo de fabricação;\n'
        f'15% de impostos sobre custo de fabricação (R${real_br_money_mask(cf * 1.15 - cf)});\n'
        f'Totalidade das taxas: R${real_br_money_mask((cf * 1.1 - cf) + (cf * 1.15 - cf))}.'
    )
else:
    print(
        f'\nO preço final do carro é de: R${real_br_money_mask((cf * 1.15) + (cf * 1.2 - cf))};\n'
        '\nPelo valor ser acima de R$25.000,00:\n'
        f'Comissão do distribuidor de 10% (R${real_br_money_mask(cf * 1.15 - cf)}) sobre custo de fabricação;\n'
        f'20% de impostos sobre custo de fabricação (R${real_br_money_mask(cf * 1.2 - cf)});\n'
        f'Totalidade das taxas: R${real_br_money_mask((cf * 1.15 - cf) + (cf * 1.2 - cf))}.'
    )
