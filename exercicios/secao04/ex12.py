"""
12) Leia uma distância em milhas e apresente-a convertida em quilômetros.
A fórmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetros
e M em milhas.
"""
# K = 1.61 * M
dm = str(input('Informe a distância em milhas: ')).strip().replace(',', '.')
print(f'A distância {float(dm):.1f}mi corresponde a: {float(dm) * 1.61:.1f}km')
