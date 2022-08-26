"""
38) Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
sabendo que ele recebeu um aumento de 25%.
"""
sf = float(str(input('Informe o valor do seu salário para cálcular um aumento de 25%: \033[37mR$\033[m').strip().replace(',', '.')))
print(f'O novo salário é de R${sf * 1.25:.2f}.')
