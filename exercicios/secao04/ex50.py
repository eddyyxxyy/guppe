"""
50) Implemente um programa que calcule o ano de nascimmento
de uma pessoa a partir de sua idade e do ano atual.
"""
from datetime import datetime
anonasc = int(input('Informe seu ano de nascimento: '))
print(f'Sua idade é: {datetime.today().year - anonasc} anos!')
