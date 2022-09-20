"""
11) Leia uma velocidade em m/s (metros por segundo) e apresente-a
convertida em km/h (quilômetros por hora). A fórmula de conversão é: K = M * 3.6,
sendo K a velocidade km/h e M em m/s
"""
# K = M * 3.6
vms = str(input('Informe a velocidade em m/s: ')).strip().replace(',', '.')
print(
    f'A velocidade {float(vms):.1f} corresponde a: {float(vms) * 3.6:.1f}km/h'
)
