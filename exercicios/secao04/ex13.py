# M = K / 1.61
dkm = float(str(input('Informe a distância em km: ')).strip().replace(',', '.'))
print(f'A distância {dkm:.1f}km corresponde a: {dkm / 1.61:.1f}mi')
