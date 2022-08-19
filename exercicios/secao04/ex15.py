# G = R * 180 / pi
from math import pi
rad = float(str(input('Informe o ângulo em radianos: ')).strip().replace(',', '.'))
print(f'Um ângulo de {rad:.2f} radianos corresponde a {round(rad * 180 / pi)} graus.')
