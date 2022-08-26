"""
35) Sejam a e b os catetos de um triângulo, onde a hipotenusa
é obtida pela equação: hipotenusa = √a² + b². Faça um
programa que receba os valores de a e b e calcule o valor
da hipotenusa através da equação. Imprima o resultado dessa operação.
"""
from math import sqrt
cats = [float(str(input('Informe o comprimento do cateto "a": ').strip().replace(',', '.'))),
        float(str(input('Informe o comprimento do cateto "b": ').strip().replace(',', '.')))]
print(f'O comprimento da hipotenusa é de: {sqrt(cats[0] ** 2 + cats[1] ** 2)}')