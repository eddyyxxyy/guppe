"""
33) Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
"""
lq = float(
    str(
        input('Informe o comprimento do lado de um quadrado: ')
        .strip()
        .replace(',', '.')
    )
)
print(f'A área de um quadrado de lado {lq} corresponde à {lq * lq}².')
