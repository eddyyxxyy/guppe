lista = []
for i in range(8):
    lista.append(int(input(f'Informe um valor para a posição {i} do vetor: ')))
x = int(input('Informe a posição no vetor que deseja: '))
y = int(input('Informe outra posição no vetor que deseja: '))
print(f'A soma dos valores na posição {x} e {y} são: {lista[x] + lista[y]}')
