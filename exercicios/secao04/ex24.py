# A = M² * 0.000247
amq = float(input('Informe a área em metros quadrados: ').strip().replace(',', '.'))
print(f'Uma área de {amq:.1f}m² corresponde à {amq * 0.000247:.5f} acres.')
