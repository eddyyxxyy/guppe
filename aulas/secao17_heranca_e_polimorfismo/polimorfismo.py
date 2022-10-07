"""
POO - Polimorfismo

Poli - Muitos
Morfis - Formas

Quando reimplementamos um método presente na Super Classe em Classes
Filhas, estamos realizando uma sobreescrita de método, chamada de
Overriding.

O Overriding é Polimorfismo, que é alterar o comportamento de um
determinado objeto.
"""


class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def falar(self):
        raise NotImplementedError(
            'A Classe Filha precisa implementar este método.'
        )

    def comer(self):
        print(f'{self.nome} está comendo...')


class Cachorro(Animal):
    def __init__(self, nome):
        super(Cachorro, self).__init__(nome)

    def falar(self):
        print(f'{self.nome} fala au au!')


class Gato(Animal):
    def __init__(self, nome):
        super(Gato, self).__init__(nome)

    def falar(self):
        print(f'{self.nome} fala miau!')


class Rato(Animal):
    def __init__(self, nome):
        super(Rato, self).__init__(nome)

    def falar(self):
        print(f'{self.nome} fala Ha Ha!')


# Testes

felix = Gato('Felix')
felix.comer()
felix.falar()
print()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()
print()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()
