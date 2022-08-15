"""
Listas Python

Listas em Python funcionam como vetores ou matrizes, ou seja, arrays em outras linguagens, com a diferença de serem
DINÂMICO e também podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo, ou seja, nestas linguagens se você criar um Array do tipo Int e com
    tamanho 5 (ou seja, para guardar até 5 valores do tipo Int), este Array será SEMPRE do tipo Int e poderá
    ter SEMPRE no máximo 5 valores.

Já em Python
    - O Array/Lista é dinâmico: não possui tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adi-
    cionando elementos (enquanto houver memória disponível);
    - Qualquer tipo de dado: não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes:
    - []

Para detectar se um valor específico está na lista:
    - if num in lista:

Para ordenar uma lista:
    - lista.sort()

Para contar o número de ocorrências de um valor na lista:
    - lista.count(*valor)

Para adicionar elementos ao final da lista, usamos o append (só podemos adicionar um objeto por vez com esse método):
    - lista.append(42)

Para adicionar elementos também no final da lista, mas usando um iterável como argumento e adicionando eles separada-
mente como objetos únicos:
    - lista.extend([8, 21, 5])

Para inserir um novo item na lista informando a posição do índice, ele não substitui o valor que estava naquele índice,
o insert "empura" o valor que estava no índice informado para a direita da lista:
    - lista.insert(posição, valor)

Para juntar duas listas, ele coloca em uma única lista TODOS os dados da lista1 e lista2 por exemplo (no exemplo abaixo
estamos criando uma nova lista), podemos usar o extend para fazer isso, mas ele não cria uma lista nova, ele somente
adiciona os elemento a lista que está sendo aplicada o método:
    - lista = lista1 + lista2

Para imprimir a lista reversa:
    - print(lista[::-1]
    - lista.reverse()

Para copiar uma lista:
    - lista = lista1.copy()

Para contar quantos elementos existem dentro da lista:
    - len(lista)

Para remover o ultimo elemento de uma lista:
    - lista.pop()  # O pop() não somente remove o ultimo elemento, mas também o retorna e podemos remover um elemento
    pelo índice o passando no argumento, fazendo os elemento que estão a direita do valor retirado são deslocados para
    esquerda (se não houver elemento no índice informado, teremos um IndexError)

Para zerar a lista/remover todos os elementos, deixando ela vazia:
    - lista.clear()

Para repetir elementos em uma lista:
    - lista = lista * 3

Para converter uma string em uma lista, por padrão o split() separa os elementos da lista pelo "espaço" entre eles,
dessa forma separando os elementos por palavras:
    - curso = 'Curso de Python'
      curso = curso.split()

Para converter uma lista em string:
    - lista = ['Programação', 'Python:', 'Essencial']
      curso = ' '.join(lista)  # Estamo fazendo o join pegar cada elemento e os juntar com um espaço entre eles,
                               formando uma string

Para iterar sobre listas:
    - for elemento em lista:
          print(elemento)
    - carrinho = []
      produto = ''
      while produto != 'sair':
          print('Adicione um produto na lista ou digite "sair" para sair: ')
          produto = input()
          if produto != 'sair':
              carrinho.append(produto)
      for produto in carrinho:
          print(produto)

Utilizando variáveis em listas:
    - numeros = [1, 2, 3]
    - n1 = 1
      n2 = 2
      n3 = 3
      numeros = [n1, n2, n3]

Para entender melhor o índice reverso, pense na lista como um círculo, onde o ultimo elemento será o -1 e assim por
diante...

Para gerar índice em um for:
    - for indice, elemento in enumerate(lista):
          print(indice, elemento)

Para encontrar em qual índice da lista está o elemento x (sempre do primeiro elemento encontrado, se houver mais de
um elemento com o mesmo valor, ele sempre trará o primeiro) (caso o elemento não exista, gera ValueError). O "y" será
o índice que ele partirá para a busca, ou seja, será a partir dele que será feita a checagem e o "z" será o ponto de
parada, ou seja, irá buscar o index de x entre y e z:
    - print(lista.index(x, y, z))

Para trabalhar slice de listas:
    - Pegando todos os elementos: lista[::]
    - Pegando todos os restantes a partir de um elemento (excluindo o primeiro): lista[1:]
    - Pegando todos até o informado (excluindo o índice informado, pegaria todos antes do 3 e não o 3): lista[:3]
    - Pegando todos entre os valores informados (excluindo o ultimo): lista[1:3]
    - Pegando todos em ordem inversa: lista[::-1]

Invertendo valores da lista:
    - lista.reverse()
    - lista[x], lista[y] = lista[y], lista[x]

Copiando uma lista para outra (Shallow Copy e Deep Copy):
    - nova_lista = lista.copy()  # Faz uma cópia sem associação da lista "lista" em "nova_lista", Deep Copy.
    - nova_lista = lista  # Faz uma associação entre as duas listas, o que for feito em uma afetará a outra,
    pois foi feita uma cópia por atribuição, isso se chama Shallow Copy.
"""
