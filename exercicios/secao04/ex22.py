"""
22) Leia um valor de comprimeto em jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0.91 * J, sendo J o comprimeto emm jardas
e M o comprimeto em metros.
"""
# M = 0.91 * J
cjd = float(input('Informe o comprimento em jardas: ').strip().replace(',', '.'))
print(f'O comprimento de {cjd:.1f} jardas corresponde a {cjd * 0.91:.1f} metros.')
