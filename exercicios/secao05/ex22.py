"""
22) Leia a idade e o tempo de serviço de um trabalhador e escreva
se ele pode ou não se aposentar. As condições para posentadoria são
    - Ter pelo menos 64,
    - Ou ter trabalhado pelo menos 30 anos,
    - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
"""
from datetime import datetime

year_today = datetime.today().year
age = 0
ct = 0
while True:
    try:
        age = int(input('Informe sua idade: ').strip())
        age_gap = year_today + 14 - age
    except ValueError:
        print('Valor inválido!')
        continue
    else:
        while True:
            try:
                ct = int(
                    input('Informe seu tempo de serviço (em anos): ').strip()
                )
            except ValueError:
                print('Valor inválido!')
                continue
            else:
                if ct > year_today - age_gap:
                    print(
                        'Valor inválido! Você não ter mais anos de serviço do que o '
                        'permitido para ter começado a trabalhar (14 anos como aprendiz).'
                    )
                    continue
                else:
                    break
    break
if (age >= 64) or (ct >= 30) or ((age >= 60) and (ct >= 25)):
    print('Pode se aposentar!')
else:
    print('Não pode se aposentar!')
