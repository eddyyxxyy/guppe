"""
13) Leia uma distância em quilômetros e apresente-a
convertida em milhas. A fórmula de conversão é: M = K / 1.61,
sendo K a distância em quilômetros e M em milhas.
"""
# M = K / 1.61
dkm = float(str(input('Informe a distância em km: ')).strip().replace(',', '.'))
print(f'A distância {dkm:.1f}km corresponde a: {dkm / 1.61:.1f}mi')
