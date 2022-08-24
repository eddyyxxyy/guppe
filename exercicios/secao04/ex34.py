from math import pi
rc = float(str(input('Informe o raio do círculo: ').strip().replace(',', '.')))
print(f'A área de um círculo de raio {rc} corresponde à {rc ** 2 * pi:.2f}².')
