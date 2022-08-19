# M = K / 3.6
vkm = str(input('Informe a velocidade em km/h: ')).strip().replace(',', '.')
print(f'A velocidade de {float(vkm):.1f}km/h corresponde a {float(vkm) / 3.6:.1f}m/s')
