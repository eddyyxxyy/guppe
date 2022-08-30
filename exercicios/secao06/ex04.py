"""
4) Escreva um programa que declare um inteiro, incialize-o com 0,
e incremente-o de 1000 em 1000, imprimindo seu valor na tela,
até que seu valor seja 100000(cem mil).
"""

print(
    '=' * 69 + '\n' +
    'DE 0 A 100.000 (MULTIPLOS DE 1.000)'.center(69, '-') + '\n' +
    '=' * 69 + '\n'
)

for i in range(0, 100_001, 1000):
    if i % 10_000 == 0 and i != 0:
        print()
    print(f'{i}'.center(5), end=', ')
print('FIM!')
