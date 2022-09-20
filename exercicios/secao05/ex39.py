"""
39) Uma empresa decide dar um aumento aos seus funcionários de acordo com uma
tabela que considera o salário atual e o tempo de serviço de cada funcionário.
Os funcionários com menor salário terão um aumento proporcionalmente maior do que
os funciopnários com um salário maior, e conforme o tempo de serviço na empresa, cada
funcionário irá receber um bônus adicional de salário. Faça um programa que leia:
    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionário na empresa (número de anos de trabalho na
    empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima
o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha
direito a nenhum aumento.
    |   Salário Atual   |   Reajuste    | Tempo de Serviço |  Bônus     |
    | Até 500,00        |     25%       | Abaixo de 1 ano  | Sem bônus  |
    | Até 1000,00       |     20%       | De 1 a 3 anos    |  100,00    |
    | Até 1500,00       |     15%       | De 4 a 6 anos    |  200,00    |
    | Até 2000,00       |     10%       | De 7 a 10 anos   |  300,00    |
    | Acima de 2000,00  | Sem reajuste  | Mais de 10 anos  |  500,00    |
"""
from ex36_functions import real_br_money_mask

salario_atual: float = 0
tempo_servico: int = 0

print(
    '=' * 31
    + '\n'
    + 'REAJUSTE SALARIAL'.center(31, '-')
    + '\n'
    + '=' * 31
    + '\n'
)
while True:
    try:
        salario_atual = float(
            input('Salário atual: R$').strip().replace(',', '.')
        )
    except ValueError:
        print('Valor inválido! Informe novamente...\n')
        continue
    else:
        if salario_atual <= 0:
            print('Valor inválido! Informe novamente...\n')
            continue
        while True:
            try:
                tempo_servico = int(input('Tempo de serviço: ').strip()[0:2:1])
            except ValueError:
                print('Duração em anos inválida! Informe novamente...\n')
                continue
            else:
                if tempo_servico < 0 or tempo_servico > 80:
                    print('Duração em anos inválida! Informe novamente...\n')
                    continue
                break
        break

if salario_atual <= 500:
    print(
        f'Seu reajuste é de 25% sobre o salário: R${real_br_money_mask(salario_atual)};\n'
        f'Salario com reajuste: R${real_br_money_mask(salario_atual * 1.25)}\n'
        'Com o bônus por tempo de serviço: ',
        end='',
    )
elif 500 < salario_atual <= 1000:
    print(
        f'Seu reajuste é de 20% sobre o salário: R${real_br_money_mask(salario_atual)};\n'
        f'Salario com reajuste: R${real_br_money_mask(salario_atual * 1.2)}\n'
        'Com o bônus por tempo de serviço: ',
        end='',
    )
elif 1000 < salario_atual <= 1500:
    print(
        f'Seu reajuste é de 15% sobre o salário: R${real_br_money_mask(salario_atual)};\n'
        f'Salario com reajuste: R${real_br_money_mask(salario_atual * 1.15)}\n'
        'Com o bônus por tempo de serviço: ',
        end='',
    )
elif 1500 < salario_atual <= 2000:
    print(
        f'Seu reajuste é de 10% sobre o salário: R${real_br_money_mask(salario_atual)};\n'
        f'Salario com reajuste: R${real_br_money_mask(salario_atual * 1.1)}\n'
        'Com o bônus por tempo de serviço: ',
        end='',
    )
else:
    print(
        f'Sem reajuste sobre o salário: R${real_br_money_mask(salario_atual)};\n'
        f'Salario: R${real_br_money_mask(salario_atual)}\n'
        'Com o bônus por tempo de serviço: ',
        end='',
    )

if tempo_servico < 1:
    print('sem bônus...')
elif 1 <= tempo_servico <= 3:
    print('+ R$100,00 adicionados ao seu salário reajustado!')
elif 4 <= tempo_servico <= 6:
    print('+ R$200,00 adicionados ao seu salário reajustado!')
elif 7 <= tempo_servico <= 10:
    print('+ R$300,00 adicionados ao seu salário reajustado!')
else:
    print('+ R$500,00 adicionados ao seu salário reajustado!')
