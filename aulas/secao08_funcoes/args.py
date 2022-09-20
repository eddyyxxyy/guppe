"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer (ou seja, parâmetro de entrada de uma função). Isso significa que você
poderá chamar de qualquer coisa desde que comece com "*";

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo;

Mas o que é *args?
- O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então, desde
já, lembre que tuplas são imutáveis.



Exemplo de função ruim:


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))
# print(soma_todos_numeros(4, 6))  # TypeError
# print(soma_todos_numeros(4, 6, 9, 5))  # TypeError


Exemplo de função boa com *args:


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9, 5))


Outro exemplo:


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_todos_numeros(*numeros))  # Desempacotador "*", para desempacotar os items da lista.

# O asterisco serve para informarmos o Python que estamos passando como argumento uma coleção de dados.
"""
