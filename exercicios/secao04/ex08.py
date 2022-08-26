"""
8) Leia uma temperatura em graus Kelvin e apresente-a convertida em
graus Celsius. A fórmula de conversão é: C = K - 273,15,
sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""
# C = K - 273.15
tk = float(input('Informe a temperatura em ºK: '))
print(f'A temperatura {tk:.2f}ºK em ºC corresponde a: {tk - 273.15:.2f}ºC')
