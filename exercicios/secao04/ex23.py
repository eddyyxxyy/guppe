"""
23) Leia um valro de comprimento em metros e apresente-o convertido em jardas.
a fórmula de conversão é: J = M/0.91, snedo J o comprimento em jardas e
M o comprimento em metros.
"""
# J = M / 0.91
cmt = float(
    input('Informe o comprimento em metros: ').strip().replace(',', '.')
)
print(f'O comprimento de {cmt:.1f}m corresponde a {cmt / 0.91:.1f} jardas.')
