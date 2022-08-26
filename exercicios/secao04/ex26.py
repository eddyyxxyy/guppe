"""
26) Leia um valor de área em metros quadrados m² e apresente-o convertido
em hectares. A fórmula de conversão é: H = M * 0.0001, sendo M a área em
metros quadrados e H a área em hectares
"""
# H = M * 0.0001
amt = float(input('Informe a área em metros quadrados: ').strip().replace(',', '.'))
print(f'Uma área de {amt:.2f}m² corresponde à {amt * 0.0001:.5f} hectares.')
