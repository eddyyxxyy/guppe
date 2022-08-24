from math import sqrt
cats = [float(str(input('Informe o comprimento do cateto "a": ').strip().replace(',', '.'))),
        float(str(input('Informe o comprimento do cateto "b": ').strip().replace(',', '.')))]
print(f'O comprimento da hipotenusa é de: {sqrt(cats[0] ** 2 + cats[1] ** 2)}')