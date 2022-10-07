"""
POO - Herança Multipla

Herança Multipla nada mais é do que a possibilidade de uma Classe herdar
de multiplas Classes todos os seus atributos e métodos.

OBS: A herança multipla pode ser feita de duas maneiras:
    - Multiderivação Direta;
    - Multiderivação Indireta.


# Exemplo 1 - Multiderivação Direta:

# class Base1:
#     ...


# class Base2:
#     ...


# class Base3:
#     ...


# class Multiderivada(Base1, Base2, Base3):
#     ...


# Exemplo 2 - Multiderivação Indireta:

class Base1:
    ...


class Base2(Base1):
    ...


class Base3(Base2):
    ...


class Multiderivada(Base3):
    ...


OBS: Não importa se a derivação é de um Direta ou Indireta, a Classe que
receber a herança herderá todos os atributos e métodos das Super Classes.
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimenta(self):
        return f'Eu sou {self.__nome}'

    @property
    def nome(self):
        return self.__nome


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} está nadando!'

    def cumprimenta(self):
        return f'Eu sou o {self.nome} e moro no mar!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} está andando!'

    def cumprimenta(self):
        return f'Eu sou o {self.nome} e sou terrestre'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


def main() -> None:
    # Testando

    baleia = Aquatico('Wally')
    print(baleia.nadar())
    print(baleia.cumprimenta())
    print()

    tatu = Terrestre('Xim')
    print(tatu.andar())
    print(tatu.cumprimenta())
    print()

    pinguim = Pinguim('Tux')
    print(pinguim.andar())
    print(pinguim.nadar())
    print(pinguim.cumprimenta())  # Method Resolution Order - MRO
    print()

    # Objeto é instância de...

    print(f'Tux é instância de Pinguim? {isinstance(pinguim, Pinguim)}')
    print(f'Tux é instância de Aquático? {isinstance(pinguim, Aquatico)}')
    print(f'Tux é instância de Terrestre? {isinstance(pinguim, Terrestre)}')
    print(f'Tux é instância de Animal? {isinstance(pinguim, Animal)}')
    print(f'Tux é instância de object? {isinstance(pinguim, object)}')


if __name__ == '__main__':
    main()
