"""
16) Leia um valor de comprimento em polegadas e apresente-o convertido
em centímetros. A fórmula de conversão é: P = C / 2.54, sendo C o comprimento
em centímetros e P o comprimento em polegadas.
"""
# C = P * 2.54
pol = float(input('Informe a medida em polegadas: ').strip().replace(',', '.'))
print(f'A medida de {pol:.1f} polegadas corresponde a {pol * 2.54:.1f} centímetros')
