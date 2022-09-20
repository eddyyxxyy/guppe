"""
10) Faça um porgrama que receba a altura e o sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as sequintes fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 58
"""
alt = float(
    input('Informe sua altura (por exemplo, 1,80): ').strip().replace(',', '.')
)
sexo = str(input('Informe seu sexo (H ou M): ').strip().upper()[0])
if sexo == 'H':
    print(f'Seu peso ideal seria: {72.7 * alt - 58:.1f}kg.')
elif sexo == 'M':
    print(f'Seu peso ideal seria: {62.1 * alt - 58:.1f}kg.')
else:
    print(f'Sexo {sexo} inválido.')
