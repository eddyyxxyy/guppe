"""
23) Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto
se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.
Por exemplo: 1988, 1992, 1996.
"""
from datetime import date

a = 0
while a != -1:
    try:
        print(
            '\n\033[37mDigite -1 para sair ou coloque'
            ' 0 para analisar o ano atual...\033[m\n'
        )
        a = int(input('Informe um ano para saber se é bissexto: ').strip())
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        if a == -1:
            break
        if a == 0:
            a = date.today().year
            if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
                print(f'O ano {a} é bissexto!')
            else:
                print(f'O ano {a} não é bissexto!')
        elif a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            print(f'O ano {a} é bissexto!')
        else:
            print(f'O ano {a} não é bissexto!')
