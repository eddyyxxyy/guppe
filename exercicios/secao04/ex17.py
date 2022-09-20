"""
17) Leia um valor de comprimento em centímetros e apresente-o convertida
em centímetros. A fórmula de conversão é: P = C/2.54, sendo C o comprimento
em centímetros e P o comprimento em polegadas.
"""
# P = C / 2.54
cm = float(
    input('Informe a medida em centímetros: ').strip().replace(',', '.')
)
print(f'A medida de {cm:.2f}cm corresponde a {round(cm / 2.54)} polegadas.')
