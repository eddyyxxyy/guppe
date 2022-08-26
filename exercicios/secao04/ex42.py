"""
42) Receba o salário-base de um funcionário. Calcule e imprima o salário
a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
"""
sb = float(input('Informe seu salário: \033[1;37mR$\033[m').strip().replace(',', '.'))
print(f'Seu salário após o calculo de impostos e acréssimos é: R${(sb * 1.05) - (sb - sb * 0.93)}')
