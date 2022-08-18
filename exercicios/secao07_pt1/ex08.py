lista = []
for i in range(6):
    lista.append(int(input('Informe um valor: ')))
print(f'A lista: {lista}')
print(f'A lista lida inversamente: {list(reversed(lista))}')
# print(f'A lista lida inversamente: ', end='')
# print(*lista[::-1], sep=', ')
