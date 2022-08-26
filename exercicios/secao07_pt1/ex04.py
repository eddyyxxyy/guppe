"""
4) Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições
no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.
"""
lista = []
for i in range(8):
    lista.append(int(input(f'Informe um valor para a posição {i} do vetor: ')))
x = int(input('Informe a posição no vetor que deseja: '))
y = int(input('Informe outra posição no vetor que deseja: '))
print(f'A soma dos valores na posição {x} e {y} são: {lista[x] + lista[y]}')
