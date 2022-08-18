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
