"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/desserialização

OBS: O módulo Pickle não é seguro contra dados maliciosos,
desta forma não é recomendado trabalhar com arquivos Pickle
vindo de outras pessoas que você não conheça ou de qualquer
fonte desconhecida.


# Fazendo a criação de um arquivo pickle, serializado

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print(f'{self._Animal__nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} está latindo...')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('arquivos/animais.pickle', 'wb') as file:
    pickle.dump((felix, pluto), file)
"""

# Fazendo a leitura de um arquivo pickle

import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} está comendo...')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('arquivos/animais.pickle', 'rb') as file:
    gato, cachorro = pickle.load(file)
    print(f'O gato chamasse {gato.nome}')
    gato.miar()
    print(f'O tipo do gato é {type(gato)}')
    print(f'O cachorro chamasse {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')
