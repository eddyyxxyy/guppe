# K = 1.61 * M
dm = str(input('Informe a distância em milhas: ')).strip().replace(',', '.')
print(f'A distância {float(dm):.1f}mi corresponde a: {float(dm) * 1.61:.1f}km')
