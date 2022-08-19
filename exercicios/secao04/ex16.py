# C = P * 2.54
pol = float(input('Informe a medida em polegadas: ').strip().replace(',', '.'))
print(f'A medida de {pol:.1f} polegadas corresponde a {pol * 2.54:.1f} centímetros')
