vetor = []
for i in range(10):
    vetor.append(int(input(f'Informe o {i + 1}º valor: ')))
print(f'Para o vetor {vetor}, temos:')
print(f'Seu valor máximo: {max(vetor)}')
print(f'Seu valor mínimo: {min(vetor)}')
