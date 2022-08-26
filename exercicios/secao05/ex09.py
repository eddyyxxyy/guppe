"""
9) Leia o salário de um trabalhador e o valor da prestação
de um empréstimo. Se a prestação for maior que 20% do salário imprima:
'Empréstimo não concedido', caso contrário imprima: 'Empréstimo concedido'
"""
print('-' * 30 + '\n' + 'ANÁLISE DE EMPRÉSTIMO'.center(30, '-') + '\n' + '-' * 30)
st = float(input('Informe o seu salário: R$').strip().replace(',', '.'))
pe = float(input('Informe o valor da prestação do empréstimo: R$').strip().replace(',', '.'))
if pe > st * 0.2:
    print(f'Empréstimo negado, pois a prestação de R${pe:.2f} é maior do que 20% de seu salário (R${st * 0.2:.2f}).')
else:
    print(f'Empréstimo aprovado!')
