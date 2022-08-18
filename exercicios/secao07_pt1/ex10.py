nota_alunos = []
for i in range(15):
    nota_alunos.append(float(input(f'Informe a nota do {i + 1}º aluno: ')))
print(f'A média geral da sala foi de {sum(nota_alunos) / len(nota_alunos):.1f}')
