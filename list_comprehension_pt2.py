"""
List Comprehension - Parte II

- Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension


# Exemplos:

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando

# OBS: qualquer número par módulo de 2 é 0 e 0 em Python gera False, então:
pares = [numero for numero in numeros if not numero % 2]  # Verifica que o valor não é 1, não é True, e coloca na lista
impares = [numero for numero in numeros if numero % 2]   # Verifica que o valor não é 0, não é False, e coloca na lista

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)

"""
