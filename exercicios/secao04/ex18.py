"""
18) Leia um valor de um volume em metros cúbicos m³ e apresente-o
convertido em litros. A fórmula de conversão é: L = 1000 * M,
sendo L o volume em litros e M o volume em metros cúbicos
"""
# L = M * 1000
mcub = float(input('Informe o volume em m³: ').strip().replace(',', '.'))
print(f'O volume de {mcub:.2f}m³ equivale a {mcub * 1000:.2f} litros.')
