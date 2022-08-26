"""
9) Crie um programa que lê 6 valores inteiros pares e,
em seguida, mostre na tela os valores lidos na ordem inversa.
"""
lista = []

for i in range(6):
    while True:
        lista.append(int(input('Informe um número par: ')))
        if lista[i] % 2 != 0:
            lista.pop()
            print('O número precisa ser par...')
        else:
            print('Número par adicionado com sucesso.')
            break

print(f'A lista de pares invertida: {list(reversed(lista))}')
