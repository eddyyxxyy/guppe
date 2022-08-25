"""
Entendendo Iterators and Iterables - Iterador e Iterável

Iterator ->
    - Um objeto que pode ser iterádo;
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada;

# A diferença entre ambos é clara, o Iterable é aquele que retorna o Iterator, o Iterator é aquele que é iterado


nome = 'Geek'  # É um iterable, mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable, mas não é um iterator

# print(next(nome))  # Dará TypeError, pois iterable não tem a função next()
# print(next(numeros))  # Dará TypeError, pois iterable não tem a função next()

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))  # G
print(next(it1))  # e
print(next(it1))  # e
print(next(it1))  # k
# print(next(it1))  # Dá o erro StopIteration

print(next(it2))  # 1
print(next(it2))  # 2
print(next(it2))  # 3
print(next(it2))  # 4
print(next(it2))  # 5
print(next(it2))  # 6
# print(next(it2))  # Dá o erro StopIteration
"""
