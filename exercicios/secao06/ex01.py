"""
1) Faça um programa que determine e mostre os cincos primeiros
múltiplos de 3, considerando números maiores que 0
"""

print(
    '=' * 20 + '\n' +
    '5 MULTIPLOS DE 3'.center(20, '-') + '\n' +
    '=' * 20 + '\n'
)

for i in range(6):
    if i != 0 and i != 5:
        print(i * 3, end=', ')
    elif i != 0 and i == 5:
        print(i * 3)
