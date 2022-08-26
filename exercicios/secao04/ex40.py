"""
40) Uma empresa contrata um encanador a R$30,00 por dia.
Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima
a quantida liquida que deverá ser paga. Sabendo-se que são descontandos 8% para imposto de renda.
"""
dt = int(input('Informe o número de dias trabalhados (R$30,00 por dia): '))
print(f'O valor a ser recebido, retirados os 8% de impostos, é: R${(dt * 30) * 0.92:.2f}.'.replace('.', ','))
