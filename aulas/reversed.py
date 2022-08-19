"""
Reversed

OBS: Não confundir com a função reverse() que estudamos nas listas. A função reverse() só funciona em listas,
já a função reversed() funciona com qualquer interável, sua função é inverter qualquer iterável.


# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(lista)
print(res)  # a função reversed retorna um iterável chamado list_reverseiterator, podemos converter o elemento para
# para mostra-lo
print(list(res))
print(type(res))

# Lembrando que se convertermos para set, conjunto, ele não considera a ordem, então não faz sentido utilizar o
# reversed()

# Podemos iterar sobre o reversed():

for letra in reversed('Geek University'):
    print(letra, end='')
print()
# Podemos fazer o mesmo sem o uso do for:

print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil com o slice de strings:

print('Geek University'[::-1])

# Podemos também utilizar o reversed para fazer um loop for reverso:

for n in reversed(range(0, 11)):
    print(n)

# Apesar de que também já vimos como fazer isso utilizando o próprio range:

for n in range(10, -1, -1):
    print(n)

"""
