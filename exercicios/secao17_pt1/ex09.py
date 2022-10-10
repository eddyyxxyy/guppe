"""
9) Escreva um código que apresente a classe Moto, com
atributos marca, modelo, cor e marcha e, o método imprimir. O método
imprimir deve mostrar na tela os valores de todos os atributos. O
atributos marcha indica em que a marcha a Moto se encontra no momento, sendo
representado de forma inteira, onde 0 - neutro, 1 - primeira, 2 - segunda, etc.
"""
from typing import Literal


class Moto:
    def __init__(self, marca, modelo, cor, marcha: Literal[0, 1, 2]):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__marcha = marcha

    @property
    def imprimir(self):
        return self.marca, self.modelo, self.cor, self.marcha

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @property
    def marcha(self):
        if self.__marcha == 0:
            return '0 - Neutro'
        elif self.__marcha == 1:
            return '1 - Primeira'
        elif self.__marcha == 2:
            return '2 - Segunda'
        else:
            return 'Você terá de redefinir a marcha para visualizar.'

    @marca.setter
    def marca(self, marca):
        if not isinstance(marca, str):
            raise TypeError('Nome de marca inválido!')
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo):
        if not isinstance(modelo, str):
            raise TypeError('Nome de modelo inválido!')
        self.__modelo = modelo

    @cor.setter
    def cor(self, cor):
        if not isinstance(cor, str):
            raise TypeError('Cor inválida!')
        self.__cor = cor

    @marcha.setter
    def marcha(self, marcha):
        if not isinstance(marcha, int):
            raise TypeError('Marcha inválida!')
        if marcha == 0:
            self.__marcha = 0
        elif marcha == 1:
            self.__marcha = 1
        elif marcha == 2:
            self.__marcha = 2
        else:
            self.__marcha = 0


def main() -> None:
    moto = Moto('Honda', 'CG', 'Preta', 0)
    print(moto.imprimir)
    moto.marcha = 1
    print(moto.imprimir)


if __name__ == '__main__':
    main()
