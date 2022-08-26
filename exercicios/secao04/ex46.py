"""
46) Faça um programa que leia um número inteiro positivo de
três digitos (de 100 a 999). Gere outro número formado pelos
dígitos invertidos do número lido. Exemplo:
    NúmeroLido = 123
    NúmeroGerado = 321
"""
tresdigitos = str(input('Informe um número inteiro de 3 digitos: ').strip())
print(f'O mesmo número, mas com os digitos invertidos, corresponde à {tresdigitos[::-1]}')
