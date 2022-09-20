"""
6) Leia uma temperatura em gruas Celsius e apresente-a convertida
em graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""
# F = C * (9.0 / 5) + 32.0
tc = float(input('Informe a temperatura em ºC: '))
print(
    f'A temperatura {tc:.1f}ºC em ºF corresponde a: {tc * (9.0 / 5.0) + 32.0:.1f}ºF'
)
