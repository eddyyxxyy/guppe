"""
6) Escreva um programa que, dados dois números inteiros, mostre na tela
o maior deles, assim como a diferença existentes entre ambos.
"""
normal_text = '\033[m'
red_text = '\033[31m'
blue_text = '\033[34m'
n1 = round(
    float(
        input(f'Informe um {red_text}número{normal_text} inteiro: ')
        .strip()
        .replace(',', '.')
    )
)
n2 = round(
    float(
        input(f'Informe outro {blue_text}número{normal_text} inteiro: ')
        .strip()
        .replace(',', '.')
    )
)
if n1 == n2:
    print(
        f'Os números {red_text}{n1}{normal_text} e {blue_text}{n2}{normal_text} são iguais!'
    )
elif n1 > n2:
    print(
        f'O número {red_text}{n1}{normal_text} é maior que {blue_text}{n2}{normal_text}!'
    )
else:
    print(
        f'O número {blue_text}{n2}{normal_text} é maior que {red_text}{n1}{normal_text}!'
    )
