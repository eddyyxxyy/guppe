# H = M * 0.0001
amt = float(input('Informe a área em metros quadrados: ').strip().replace(',', '.'))
print(f'Uma área de {amt:.2f}m² corresponde à {amt * 0.0001:.5f} hectares.')
