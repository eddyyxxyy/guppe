from math import pi
cc = [float(str(input('Informe a altura do cilíndro circular: ').strip().replace(',', '.'))),
      float(str(input('Informe o raio do cilíndro circular: ').strip().replace(',', '.')))]
print(f'O volume do cilíndro corresponde à {pi * cc[1] ** 2 * cc[0]}³')
