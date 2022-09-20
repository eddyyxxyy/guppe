"""
33) Um produto vai sofrer aumento de acordo com a tabela abaixo.
Leia o preço antigo e calcule e escreva o preço novo, e escreva uma mensagem
em função do preço novo (de acordo com a segunda tabela).
    |     PREÇO ANTIGO     |   PERCENTUAL DE AUMENTO  |
    | até R$50             |            5%            |
    | entre R$50 e R$ 100  |           10%            |
    | acima de R$100       |           15%            |
    |          PREÇO NOVO              |   MENSAGEM   |
    | até R$80                         | Barato       |
    | entre R%80 e R$120 (inclusive)   | Normal       |
    | entre R$ 120 e R$200 (inclusive) | Caro         |
    | acima de R$200                   | Muito caro   |
"""
valor: float = 0
novo_valor: float = 0
print(
    '=' * 48
    + '\n'
    + 'CÁLCULO DE NOVOS PREÇO'.center(48, '-')
    + '\n'
    + '=' * 48
    + '\n'
)
print(
    '=' * 48
    + '\n'
    + '|'
    + 'TABELA DE TAXAS SOBRE PRODUTO'.center(46)
    + '|'
    + '\n'
    + '=' * 48
    + '\n'
    + '| '
    + 'Preço Antigo '.center(21)
    + '| PERCENTUAL DE AUMENTO |\n'
    + '-' * 48
    + '\n'
    + '| '
    + 'Até R$50 '.center(21)
    + '|'
    + '5%'.center(23)
    + '|\n'
    + '| '
    + 'Entre R$50 e R$100 '.center(21)
    + '|'
    + '10%'.center(23)
    + '|\n'
    + '| '
    + 'Acima de R$100 '.center(21)
    + '|'
    + '15%'.center(23)
    + '|\n'
    + '-' * 48
    + '\n'
)
while True:
    try:
        valor = float(
            input('Informe o valor do produto para conversão:\n->  ')
            .strip()
            .replace(',', '.')
        )
    except ValueError:
        print('\nValor inválido! Informe novamente...\n')
        continue
    else:
        if valor <= 0:
            print('\nValor inválido! Informe novamente...\n')
            continue
        print(
            f'\nO valor de R${valor:.2f}, após aplicação de taxas, é de R$',
            end='',
        )
        break
if valor <= 50.00:
    novo_valor = valor * 1.05
    print(f'{novo_valor:.2f} - ', end='')
elif 50.00 < valor <= 100:
    novo_valor = valor * 1.1
    print(f'{novo_valor:.2f} - ', end='')
else:
    novo_valor = valor * 1.15
    print(f'{novo_valor:.2f} - ', end='')
if novo_valor < 80.00:
    print('BARATO!')
elif 80 <= novo_valor <= 120:
    print('NORMAL!')
elif 120 < novo_valor <= 200:
    print('CARO!')
else:
    print('MUITO CARO!')
