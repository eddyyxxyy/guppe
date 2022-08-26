"""
20) Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K/0.45, snedo K a massa em quilogramas
e L a massa em libras.
"""
# L = K / 0.45
mq = float(str(input('Informe a massa em quilogramas: ')).strip().replace(',', '.'))
print(f'A massa de {mq:.2f}kg equivale a {mq / 0.45:.2f}li.')
