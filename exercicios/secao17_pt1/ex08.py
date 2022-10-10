"""
8) Baseando-se no exercício 7 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""
from numbers import Number

from ex07 import FiguraGeometrica


class Circulo(FiguraGeometrica):
    def __init__(self, raio, area, perimetro):
        super(Circulo, self).__init__()
        self.__raio = raio
        self.__area = area
        self.__perimetro = perimetro

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, value):
        if not isinstance(value, Number):
            raise TypeError('Valor inválido para raio.')
        self.__raio = value

    @property
    def calcular_area(self):
        return self.__area

    @calcular_area.setter
    def calcular_area(self, value):
        if not isinstance(value, Number):
            raise TypeError('Valor inválido para área.')
        self.__area = value

    @property
    def calcular_perimetro(self):
        return self.__perimetro

    @calcular_perimetro.setter
    def calcular_perimetro(self, value):
        if not isinstance(value, Number):
            raise TypeError('Valor inválido para perímetro.')
        self.__perimetro = value

    @property
    def imprimir(self):
        return (
            f'Raio: {self.raio}\n'
            f'Área: {self.calcular_area:.2f}\n'
            f'Perímetro: {self.calcular_perimetro:.2f}'
        )


def main() -> None:
    circulo = Circulo(2, 12.57, 12.57)
    print(circulo.imprimir)


if __name__ == '__main__':
    main()
