"""
7) Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""
vetor = []
for i in range(10):
    vetor.append(int(input(f'Informe um valor na posição {i}: ')))
print(f'O vetor é: {vetor}')
print(f'Seu maior número é {max(vetor)} e a posição deste máximo se encontra no índice {vetor.index(max(vetor))}')
