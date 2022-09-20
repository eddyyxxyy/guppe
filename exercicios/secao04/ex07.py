"""
7) Leia uma temperatura em graus Fahrenheit e apresente-a convertida
em graus Celsius. A fórmula de conversão é: C = (F-32.0)*5.0/9.0,
sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""
# C = 5.0 * (F - 32.0) / 9.0
tf = float(input('Informe a temperatura em ºF: '))
print(
    f'A temperatura {tf:.1f}ºF em ºC corresponde a: {5.0 * (tf - 32.0) / 9.0}ºC'
)
