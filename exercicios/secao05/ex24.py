"""
24) Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%;
SP 12%; RJ %15; MS 8%). Faça um programa qem que o usuário entre com o valor
e o estado destino do produto e o programa retorne o preço final do produto
acrescido do imposto do estado em que ele será vendido. Se o estado digitado
não for válido, mostrar uma mensagem de erro.
"""
from collections import OrderedDict

estados = OrderedDict({'mg': 1.07, 'ms': 1.08, 'rj': 1.15, 'sp': 1.12})
while True:
    try:
        v = float(input('Infor o valor do produto: \033[37mR$\033[m').strip().replace(',', '.'))
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        while True:
            try:
                e = str(input(
                    '\nInforme a sigla do estado destino:\n'
                    'MG - Minas Gerais (7% de impostos);\n'
                    'MS - Mato Grosso do Sul (8% de impostos);\n'
                    'RJ - Rio de Janeiro (15% de impostos);\n'
                    'SP - São Paulo (12% impostos);\n'
                    'Estado escolhido ->  ').strip().lower()
                    )
            except ValueError:
                print('Sigla inválida!')
                continue
            else:
                try:
                    if estados[e]:
                        print(f'O valor do produto será de R${v * estados[e]:.2f}')
                        break
                except KeyError:
                    print('Sigla inválida!')
                    continue
    break
