"""
Generators Expression

Em aulas anteriores, nós estudamos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension

Mas não vimos:
- Tuple Comprehension

Não as vimos, pois se chamam (Tuple) Generators.

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# Poderiamos ter feito o que está sendo visto acima usando Generators:

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))  # Não é List Comprehension, não temos os colchetes.

# List Comprehension:

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)  # Gera a lista em memória

# Generator:

res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)  # Não gera nada além do generator object, usaremos o list comprehension se formos a lista gerada para algo

# Em questão de performance, o generator ocupa menos espaço em memória e exige menos processamento

# Qual é a utilidade de getsizeof() → Retorna a quantidade de bytes em memória do elemento passado como parâmetro.

from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando na memória. Quanto maior a string, mais espaço ocupa.

print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))



# Memória:

from sys import getsizeof

# Gerando uma lista de números, com List Comprehension:

list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números, com Set Comprehension:

set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números, com Dictionary Comprehension:

dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números, com Generator:

gen = getsizeof(x * 10 for x in range(1000))

# Mostrando quanto em memória está sendo usado:

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')  # 8856
print(f'Set Comprehension: {set_comp} bytes')  # 32984
print(f'Dict Comprehension: {dic_comp} bytes')  # 36960
print(f'Generator Expression: {gen} bytes')  # 104

# O generator gera um processamento muito mais performatico pois ele deixa tudo pronto para usarmos, porém não tem os
# rigidos controles que as outras classes tem, como por exemplo o set, que não aceita valores repetidos e o dict, que
# não aceita chaves repetidas, esses controles internos geram mais espaços de memória sendo ocupados. Eles ocupam memó-
# ria até o fim do programa.



# Posso iterar sobre o Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

"""
