"""
14) Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * r / 180, sendo G o ângulo em graus
e R em radianos e r = 3.14.
"""
# R = G * pi / 180
from math import pi
graus = float(str(input('Informe o ângulo em graus: ')).strip().replace(',', '.'))
print(f'Um ângulo de {graus:.2f} corresponde a {graus * pi / 180:.2f} radianos.')
