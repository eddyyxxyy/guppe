"""
Generators

- Geradores (Generators) são Iterators;
OBS: O contrário não é verdadeiro, pois nem tod0 Iterator é um Generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
    - Funções geradoras usam a palavra reservada yield;
- Generators podem ser criados com expressões geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras):

Funções:
- Utilizam return;
- Retorna somente uma vez;
- Quando executada, pode retorna um valor ou nenhum valor (None);

Geradores:
- Utilizam yield;
- Pode utilizar yield multiplas vezes;
- Quando executada, retorna um generator;


# Exemplo de generator function:


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


# OBS: Uma Generator Function não é um Generator, ela gera o Generator

gen = conta_ate(5)
# print(type(gen))  # imprime <class 'generator'>
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



gen = conta_ate(10)

for n in gen:
    print(n)



gen = conta_ate(10)

print(next(gen), '\n')

# Com o gen ja foi iterado uma vez, ele só está aguardando o restante da operação

for n in gen:
    print(n)

# Com a impressão vemos que foi iniciado do 2 e terminou normalmente no 10


# Para gerar todos os iteráveis do Iterator podemos dar cast nele como lista

gen = list(conta_ate(10))

print(gen)
"""

# Exemplo de generator function:


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


# OBS: Uma Generator Function não é um Generator, ela gera o Generator
