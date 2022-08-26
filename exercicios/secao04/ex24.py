"""
24) Leia um valor de área em metros quadrados e m² e apresente-o
convertido em acres. A fórmula de conversão é: A = M * 0,000247, sendo M
a área em metros quadrados e A área em acres.
"""
# A = M² * 0.000247
amq = float(input('Informe a área em metros quadrados: ').strip().replace(',', '.'))
print(f'Uma área de {amq:.1f}m² corresponde à {amq * 0.000247:.5f} acres.')
