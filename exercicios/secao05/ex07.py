"""
7) Faça um programa que receba dois números e mostre o maior.
Se por acaso, os dois números forem iguais, imprima a mensagem
'Números iguais'.
"""
normal_text = '\033[m'
red_text = '\033[31m'
blue_text = '\033[34m'
n1 = float(input(f'Informe um {red_text}número{normal_text}: ').strip().replace(',', '.'))
n2 = float(input(f'Informe outro {blue_text}número{normal_text}: ').strip().replace(',', '.'))
if n1 == n2:
    print(f'Os números {red_text}{n1}{normal_text} e {blue_text}{n2}{normal_text} são iguais!')
else:
    print(f'O número {red_text}{n1}{normal_text} é diferente de {blue_text}{n2}{normal_text}!')
