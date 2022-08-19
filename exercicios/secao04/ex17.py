# P = C / 2.54
cm = float(input('Informe a medida em centímetros: ').strip().replace(',', '.'))
print(f'A medida de {cm:.2f}cm corresponde a {round(cm / 2.54)} polegadas.')
