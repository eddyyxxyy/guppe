"""
17) Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((basemaior + basemenor) * altura) / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""


def trapezio(a: float, b: float, c: float) -> float:
    """
    Function that takes 3 numbers as parameters and returns the area of a trapeze.
    :param a: lenght -> bigger base
    :param b: lenght -> smaller base
    :param c: height -> distance between bases
    :return: trapeze area
    """
    return ((a + b) * c) / 2


area_trapezio = 0
while True:
    try:
        bmaior: float = float(
            input('Informe o comprimento da base maior: ')
            .strip()
            .replace(',', '.')
        )
        if bmaior <= 0:
            print(
                'O comprimento de deve ser maior que 0.\n'
                '\n¡OPERAÇÃO SENDO REINICIADA!\n'
            )
            continue
        bmenor: float = float(
            input('Informe o comprimento da base menor: ')
            .strip()
            .replace(',', '.')
        )
        if bmenor <= 0:
            print(
                'O comprimento de deve ser maior que 0.\n'
                '\n¡OPERAÇÃO SENDO REINICIADA!\n'
            )
            continue
        if bmaior <= bmenor:
            print(
                'O comprimento da base maior DEVE ser maior que a base menor.\n'
                '\n¡OPERAÇÃO SENDO REINICIADA!\n'
            )
            continue
        altura: float = float(
            input('Informe o comprimento da altura: ')
            .strip()
            .replace(',', '.')
        )
        if altura <= 0:
            print(
                'O comprimento de deve ser maior que 0.\n'
                '\n¡OPERAÇÃO SENDO REINICIADA!\n'
            )
    except ValueError:
        print('Valor inválido!\n' '\n¡OPERAÇÃO SENDO REINICIADA!\n')
        continue
    else:
        area_trapezio = trapezio(bmaior, bmenor, altura)
        break
print(f'A área do trapézio corresponde à {area_trapezio}²!')
