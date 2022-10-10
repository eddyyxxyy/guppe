"""
4) Baseando-se no exercício 3 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""
from ex03 import Quadrado


class Quadrado:
    def __init__(self, lado, area, perimetro):
        self.__lado = lado
        self.__area = area
        self.__perimetro = perimetro

    def calcular_area(self):
        self.__area = self.__lado * self.__lado
        return self.__area

    def calcular_perimetro(self):
        self.__perimetro = self.__lado * 4
        return self.__perimetro

    def imprimir(self):
        return self.__lado, self.__area, self.__perimetro


def main() -> None:
    quadrado0 = Quadrado(4, 16, 16)
    print(quadrado0.imprimir())


if __name__ == '__main__':
    main()
