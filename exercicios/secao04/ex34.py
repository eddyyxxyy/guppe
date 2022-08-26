"""
34) Leia o valor do raio de um círculo e calcule e imprima área do círculo
correspondente. A área do círculo é r * raio², conside r = 3.141592
"""
from math import pi
rc = float(str(input('Informe o raio do círculo: ').strip().replace(',', '.')))
print(f'A área de um círculo de raio {rc} corresponde à {rc ** 2 * pi:.2f}².')
