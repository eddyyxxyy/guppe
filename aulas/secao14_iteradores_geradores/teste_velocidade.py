"""
Teste de velocidade com Expressões Geradoras


# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)  # Generator
print(next(ge1))  # 1
print(next(ge1))  # 2
print(next(ge1))  # 3


# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2)  # Generator Expression
print(next(ge2))  # 1
print(next(ge2))  # 2
print(next(ge2))  # 3

"""

# Realizando o teste de velocidade
import time

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # Com 100 milhões: 6.2 segundos
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # Com 100 milhões: 7.5 segundos
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')
