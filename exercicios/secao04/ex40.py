dt = int(input('Informe o número de dias trabalhados (R$30,00 por dia): '))
print(f'O valor a ser recebido, retirados os 8% de impostos, é: R${(dt * 30) * 0.92:.2f}.'.replace('.', ','))
