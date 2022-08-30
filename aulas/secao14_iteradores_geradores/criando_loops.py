"""
Criando sua própria versão de loop

# Loops convencionais

for numero in [1, 2, 3, 4, 5]:
    print(numero)

for letra in 'Geek University':
    print(letra)

# Mas por debaixo dos panos eles transformam os Iterables em Iterators:

iter([1, 2, 3, 4, 5])
iter('Geek University')



# Codando meu próprio for

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)
"""
