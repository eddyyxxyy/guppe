"""
19) Leia um valor de um volume em litros e apresente-o
convertido em metros cúbicos m³. A fórmula de conversão é: M = L/1000,
sendo o L o volume em litros e M o volume em metros cúbicos.
"""
# M = L / 1000
vl = float(input('Informe o volume em litros: ').strip().replace(',', '.'))
print(f'O valome de {vl:.1f}L corresponde a {vl / 1000}m³.')
