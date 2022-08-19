# R = G * pi / 180
from math import pi
graus = float(str(input('Informe o ângulo em graus: ')).strip().replace(',', '.'))
print(f'Um ângulo de {graus:.2f} corresponde a {graus * pi / 180:.2f} radianos.')
