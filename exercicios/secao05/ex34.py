"""
34) Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo
com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma reduçãoo
de conceito.
    |    NOTA       |  CONCEITO (ATÉ 20 FALTAS) | CONCEITO (MAIS DE 20 FALTAS) |
    | 9.0 até 10.0  |             A             |              B               |
    | 7.5 até 8.9   |             B             |              C               |
    | 5.0 até 7.4   |             C             |              D               |
    | 4.0 até 4.9   |             D             |              E               |
    | 0.0 até 3.9   |             E             |              E               |
"""
nota: float = 0
faltas: int = 0
print(
    '=' * 30 + '\n' +
    'CONCEITO CURRiCULAR'.center(30, '-') + '\n'
    + '=' * 30 + '\n'
)
while True:
    try:
        nota = float(input(
            'Qual foi sua nota nesse semestre? \033[37m'
            'Entre 0.0 e 10.0\033[m\n'
            '->  ').strip().replace(',', '.')
            )
    except ValueError:
        print('\nNota inválida! Tente novamente...\n')
        continue
    else:
        if nota < 0.0 or nota > 10.0:
            print('\nNota inválida! Tente novamente...\n')
            continue
        while True:
            try:
                faltas = int(input(
                    'Quantas faltas nesse semestre?\n'
                    '->  ')
                             .strip().replace(',', '.')
                )
            except ValueError:
                print('\nNúmero de faltas inválido!'
                      ' Tente novamente...\n')
                continue
            else:
                if faltas < 0:
                    print('\nNota inválida!'
                          ' Tente novamente...\n')
                    continue
                break
    break
if faltas < 20:
    if 9.0 <= nota <= 10:
        print('Sua nota conceito é A!')
    elif 7.5 <= nota <= 8.9:
        print('Sua nota conceito é B!')
    elif 5 <= nota <= 7.4:
        print('Sua nota conceito é C!')
    elif 4 <= nota <= 4.9:
        print('Sua nota conceito é D!')
    else:
        print('Sua nota conceito é E!')
else:
    if 9.0 <= nota <= 10:
        print('Sua nota conceito é B!')
    elif 7.5 <= nota <= 8.9:
        print('Sua nota conceito é C!')
    elif 5 <= nota <= 7.4:
        print('Sua nota conceito é D!')
    elif 4 <= nota <= 4.9:
        print('Sua nota conceito é E!')
    else:
        print('Sua nota conceito é E!')
