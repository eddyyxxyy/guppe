"""
10) Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida
em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade
em km/h e M em m/s.
"""
# M = K / 3.6
vkm = str(input('Informe a velocidade em km/h: ')).strip().replace(',', '.')
print(
    f'A velocidade de {float(vkm):.1f}km/h corresponde a {float(vkm) / 3.6:.1f}m/s'
)
