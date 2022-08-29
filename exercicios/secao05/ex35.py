"""
35) Leia uma data e determine se ela é válida. Ou seja, verifique se o
mês está entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem
29 dias em anos bissextos, e 28 dias em anos não bissextos.

ATENÇÃO: Já foi feita uma refatoração, fazendo o tratamento de erro e,
assim, permitindo que as entradas de dados sejam já feitas da forma mais
correta possível!
"""
print(
    '=' * 30 + '\n' +
    'VALIDAÇÃO DE DATA'.center(30, '-') + '\n'
    + '=' * 30 + '\n'
)

dia: int = 0
mes: int = 0
ano: int = 0

while True:
    try:
        dia = int(input('Dia: ').strip())
    except ValueError:
        print('\nDia inválido! Insira novamente...\n')
        continue
    else:
        if dia < 1 or dia > 31:
            print('\nDia inválido! Insira novamente...\n')
            continue
        break
while True:
    try:
        mes = int(input('Mês: ').strip())
    except ValueError:
        print('\nMês inválido! Insira novamente...\n')
        continue
    else:
        if mes < 1 or mes > 12:
            print('\nMês inválido! Insira novamente...\n')
            continue
        break
while True:
    try:
        ano = int(input('Ano: ').strip())
    except ValueError:
        print('\nAno inválido! Insira novamente...\n')
        continue
    else:
        if ano < 0:
            print(
                '\nAno inválido! Não são aceitos anos '
                'antes de Cristo. Insira novamente...\n'
            )
            continue
        break

valida = False

# Meses com 31 dias
if mes == 1 or mes == 3 or mes == 5 or \
        mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        valida = True

# Meses com 30 dias
elif mes == 4 or mes == 6 or \
        mes == 9 or mes == 11:
    if dia <= 30:
        valida = True
elif mes == 2:

    # Testa se é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or \
            (ano % 400 == 0):
        if dia <= 29:
            valida = True
    elif dia <= 28:
        valida = True

if valida:
    print(f'A data {dia}/{mes}/{ano} é válida!')
else:
    print(f'A data {dia}/{mes}/{ano} é inválida')
