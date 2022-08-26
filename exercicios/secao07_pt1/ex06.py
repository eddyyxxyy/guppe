"""
6) Faça um programa que receba do usuáro um vetor com 10 posições.
Em sequida deverá ser impresso o maior e o menor elemento do vetor.
"""
vetor = []
for i in range(10):
    vetor.append(int(input(f'Informe o {i + 1}º valor: ')))
print(f'Para o vetor {vetor}, temos:')
print(f'Seu valor máximo: {max(vetor)}')
print(f'Seu valor mínimo: {min(vetor)}')
