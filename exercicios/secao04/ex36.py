"""
36) Leia a altura e o raio de um cilindro círcular e imprima
o volume do cilindro. O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = r * raio² * altura, onde r = 3.141592
"""
from math import pi
cc = [float(str(input('Informe a altura do cilíndro circular: ').strip().replace(',', '.'))),
      float(str(input('Informe o raio do cilíndro circular: ').strip().replace(',', '.')))]
print(f'O volume do cilíndro corresponde à {pi * cc[1] ** 2 * cc[0]}³')
