"""
15) Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima
o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2,
e assim por diante.
"""
print('-' * 30 + '\n' + 'Dias da Semana'.center(30, '-') + '\n' + '-' * 30)
dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')
while True:
    try:
        ds = round(
            float(
                input('Informe um número entre 1 e 7: ')
                .strip()
                .replace(',', '.')
            )
        )
    except ValueError:
        print(f'Valor inválido!')
    else:
        if not 1 <= ds <= 7:
            print(f'Valor inválido!')
        else:
            print(f'O dia da semana que representa {ds} é {dias[ds - 1]}')
            break
