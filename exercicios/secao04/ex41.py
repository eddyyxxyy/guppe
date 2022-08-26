"""
41) Faça um programa que leia o valor da hora de trabalho (em reais)
e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário.
Adicionando 10% sobre o valor calculado.
"""
vh = float(input('Informe o valor ganho por hora: \033[1;37mR$\033[m').strip().replace(',', '.'))
ht = int(input('Informe o número de horas trabalhadas: ').strip())
print(f'O valor à ser recebido com o acréssimo de 10% é de: R${vh * ht * 1.1:.2f}')
