"""
13) Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final,
mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
"""
print(
    '-' * 30 + '\n' + 'Cálculo de Aprovação'.center(30, '-') + '\n' + '-' * 30
)
notas = []
for prova in range(3):
    while True:
        try:
            notas.append(
                float(
                    input(f'Informe a nota da {prova + 1}º prova (0 a 100): ')
                    .strip()
                    .replace(',', '.')
                )
            )
        except ValueError:
            print('Nota inválida!')
        else:
            if notas[prova] > 100 or notas[prova] < 0:
                print('Nota inválida!')
                notas.pop()
            else:
                print(f'Nota adicionada com sucesso.')
                break
# media_final = (notas[0] + notas[1] + notas[2]) / 3
media_ponderada = (notas[0] + notas[1] + 2 * notas[2]) / (1 + 1 + 2)
# print(f'A média final corresponde à: {media_final:.1f}')
print(f'A média ponderada corresponde à: {media_ponderada:.1f} (', end='')
if media_ponderada > 60:
    print('APROVADO)')
else:
    print('REPROVADO)')
