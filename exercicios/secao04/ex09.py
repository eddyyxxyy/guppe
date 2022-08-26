"""
9) Leia uma temperatura em graus Celsius e apresente-a convertida em
graus Kelvin. A fórmula de conversão é: K = C + 273.15,
sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""
# K = C + 273.15
tc = str(input('Informe a temperatura em ºC: ')).strip().replace(',', '.')
print(f'A temperatuda {float(tc):.2f}ºC em ºK corresponde a: {float(tc) + 273.15:.2f}')
