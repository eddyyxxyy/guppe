"""
25) Leia um valor de área em acres e apresente-o convertido
em metros quadrados m². A fórmula da conversão é: M = A*4048.58,
sendo M a área em metros quadrados e A a área em acres
"""
# M = A * 4048.58
aac = float(input('Informe a área em acres: ').strip().replace(',', '.'))
print(f'Uma área de {aac:.5f} acres corresponde à {aac * 4048.58:.2f}m².')
