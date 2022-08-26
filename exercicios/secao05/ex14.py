"""
14) A nota final de um estudante é calculada a partir de três notas atribuídas entre
o intervalo de 0 até 10, respectivamente, a trabalho do laboratório, a uma avaliação
semestral e a um exame final. A média das três notas mencionadaa anteriormente obdece aos
pesos: Trabalho de Laboratório: 2; Avaliaçõ Semestral: 3; Exame final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9),
de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""
from collections import OrderedDict

print('-' * 30 + '\n' + 'Cálculo de Aprovação'.center(30, '-') + '\n' + '-' * 30)
notas = OrderedDict({'lab': 0, 'semestral': 0, 'final': 0})
for prova in notas.keys():
    while True:
        try:
            notas[prova] = (float(input(f'Informe a nota da prova {prova} '
                                        f'(0 a 10): ').strip().replace(',', '.')))
        except ValueError:
            print('Nota inválida!')
        else:
            if notas[prova] > 10 or notas[prova] < 0:
                print('Nota inválida!')
                notas[prova] = 0
            else:
                print(f'Nota adicionada com sucesso.')
                break
media = (2 * notas['lab'] + 3 * notas['semestral'] + 5 * notas['final']) / (2 + 3 + 5)
print(f'\nA média ponderada corresponde à: {media:.1f} (', end='')
if 0 < media < 3:
    print('REPROVADO)')
elif 3 < media < 5:
    print('RECUPERAÇÃO)')
else:
    print('APROVADO)')
