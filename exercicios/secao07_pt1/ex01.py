a = [1, 0, 5, -2, -5, 7]
soma = a[0] + a[1] + a[5]
print(f'O valor da soma dos valores na posição 0, 1 e 5 é: {soma}')
a[4] = 100
for indice, numero in enumerate(a):
    print(f'O valor na posição {indice}: {numero}')
