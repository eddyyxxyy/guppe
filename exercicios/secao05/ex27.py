"""
27) Excreva um programa que, dada a idade de um nadador, classique-o em
uma das seguintes categorias:
     Categoria   | Idade
     Infantil A  | 5 a 7
     Infantil B  | 8 a 10
     Juvenil A   | 11 a 13
     Juvenil B   | 14 a 17
     Sênior      | maiores de 18 anos
"""
print('=' * 30 + '\n' + 'CATEGORIA DO NADADOR'.center(30, '-') + '\n' + '=' * 30)
age: int = 0
keep: str = ''
while True:
    try:
        age = int(input('Informe a idade do nadador: ').strip())
    except ValueError:
        print('\nIdade inválida! Tente novamente...\n')
        continue
    else:
        if age < 0 or age >= 100:
            print('\nIdade inválida! Tente novamente...\n')
            continue
        elif age < 5:
            print(f'O nadador terá de esperar {5 - age} anos para ingressar no clube de nadadores.')
            break
        else:
            if 5 <= age <= 7:
                print(f'O nadador de {age} anos está na categoria Infantil A.')
            elif 8 <= age <= 10:
                print(f'O nadador de {age} anos está na categoria Infantil B.')
            elif 11 <= age <= 13:
                print(f'O nadador de {age} anos está na categoria Juvenil A.')
            elif 14 <= age <= 17:
                print(f'O nadador de {age} anos está na categoria Juvenil B.')
            else:
                print(f'O nadador de {age} anos está na categoria Sênior.')
        while True:
            try:
                keep = input('\nDeseja ver verificar a classificação de '
                             'outro nadador? \033[37mSim/Não\033[m ').strip().upper()[0]
            except IndexError:
                print('\nResposta inválida! Responda com S ou N...\n')
                continue
            else:
                if keep not in 'SN':
                    print('\nResposta inválida! Responda com S ou N...\n')
                    continue
                else:
                    break
        if keep == 'S':
            continue
        else:
            break
