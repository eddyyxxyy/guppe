"""
15) Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/r, sendo G o ângulo
em graus e R em radianos e r = 3.14.
"""
# G = R * 180 / pi
from math import pi

rad = float(
    str(input('Informe o ângulo em radianos: ')).strip().replace(',', '.')
)
print(
    f'Um ângulo de {rad:.2f} radianos corresponde a {round(rad * 180 / pi)} graus.'
)
