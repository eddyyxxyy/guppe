"""
27) Leia um  valor de área em hectares e apresente-o convertido em
metros quadrados m². A fórmula de conversão é: M = H * 10000,
sendo M a área em metros quadrados e H a área em hectares.
"""
# m² = H * 10000
ahec = float(input('Informe a área em hectares: ').strip().replace(',', '.'))
print(f'Uma área de {ahec} hectares corresponde à {ahec * 10000:.2f}m².')
