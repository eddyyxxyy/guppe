from datetime import datetime
anonasc = int(input('Informe seu ano de nascimento: '))
print(f'Sua idade é: {datetime.today().year - anonasc} anos!')
