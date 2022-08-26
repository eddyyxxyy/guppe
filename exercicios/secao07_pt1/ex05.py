"""
5) Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""
pares = []
n = []
for i in range(10):
    n.append(int(input('Informe um número: ')))
    if n[i] % 2 == 0:
        pares.append(n[i])
print(f'O vetor {n} tem {len(pares)} números pares, a lista de pares é {pares}.')
