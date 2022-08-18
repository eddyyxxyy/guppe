lista1 = []
lista2 = []
for i in range(10):
    lista1.append(float(input(f'Informe um valor para a posição {i}: ')))
    lista2.append(lista1[i] * 2)
print(lista1)
print(lista2)
