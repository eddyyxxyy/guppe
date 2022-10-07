"""
POO - O método super()

O método super() se refere à Super Classe/Classe Mãe/Classe Pai/Classe Genérica

Na Classe Filha temos herdados todos os métodos e atributos da Classe Pai.
"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'{self.__nome} fala {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('miau')
