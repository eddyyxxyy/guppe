"""
32) Escrever um programa que leia o código do produto escolhido do cardápio
de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago
por aquele lanche. Considere que a cada execução somente será calculado um
pedido. O cardápio da lanchonete segue o padrão abaixo:
    | Especificação    | Código | Preço |
    | Cachorro Quente  |  100   | 1.20  |
    | Bauru Simples    |  101   | 1.30  |
    | Bauru com Ovo    |  102   | 1.50  |
    | Hamburguer       |  103   | 1.20  |
    | Cheeseburguer    |  104   | 1.70  |
    | Suco             |  105   | 2.20  |
    | Refrigerante     |  106   | 1.00  |
"""
choice: int = 0
quantity: int = 0
products = dict(
    {
        '100': 1.20,
        '101': 1.30,
        '102': 1.50,
        '103': 1.20,
        '104': 1.70,
        '105': 2.20,
        '106': 1.00,
    }
)
print(
    '-=' * 18 + '\n' + 'LANCHONETE'.center(36, '-') + '\n' + '=-' * 18 + '\n'
)
print(
    'CARDÁPIO'.center(36, '-')
    + '\n'
    + '| '
    + 'Cachorro Quente '.center(18)
    + '| 100 '
    + '| R$1.20 |\n'
    + '| '
    + 'Bauru Simples '.center(18)
    + '| 101 '
    + '| R$1.30 |\n'
    + '| '
    + 'Bauru com ovo '.center(18)
    + '| 102 '
    + '| R$1.50 |\n'
    + '| '
    + 'Hamburguer '.center(18)
    + '| 103 '
    + '| R$1.20 |\n'
    + '| '
    + 'Cheeseburguer '.center(18)
    + '| 104 '
    + '| R$1.70 |\n'
    + '| '
    + 'Suco '.center(18)
    + '| 105 '
    + '| R$2.20 |\n'
    + '| '
    + 'Refrigerante '.center(18)
    + '| 106 '
    + '| R$1.00 |\n'
    + '-' * 36
)
while True:
    try:
        choice = int(input('Informe o código do produto que deseja\n-> '))
    except ValueError:
        print('\nCódigo inválido!\n')
    else:
        if choice < 100 or choice > 106:
            print('\nCódigo inválido!\n')
            continue
        while True:
            try:
                quantity = int(input(f'Informe a quantidade que deseja\n-> '))
            except ValueError:
                print('\nQuantidade inválida!\n')
            else:
                if choice < 100 or choice > 106:
                    print('\nQuantidade inválida!\n')
                    continue
                break
        break
print(f'\nValor a ser pago: R${products[str(choice)] * quantity:.2f}')
