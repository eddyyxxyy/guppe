"""
7) Escreva um código que apresente a classe Circulo,
com atributos raio, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calculaPerimetro
devem efetual seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se que a área de um círculo é obtida pela fórmula
(pi * raio * raio) e o perímetro por (2 * pi * raio), onde pi = 3,141516
"""
from math import pi
from numbers import Number


class FiguraGeometrica:
    def __init__(self):
        pass

    def calcular_perimetro(self):
        """Método Abstrato"""
        raise NotImplementedError

    def calcular_area(self):
        """Método Abstrato"""
        raise NotImplementedError

    def imprimir(self):
        """Método abstrato"""
        raise NotImplementedError


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        super(Circulo, self).__init__()
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, raio):
        if not isinstance(raio, Number):
            raise TypeError('Valor inválido para o raio.')
        self.__raio = raio

    @property
    def calcular_area(self):
        return (self.raio**2) * pi

    @property
    def calcular_perimetro(self):
        return 2 * pi * self.raio

    def imprimir(self):
        return (
            f'Raio: {self.raio}\n'
            f'Área: {self.calcular_area:.2f}\n'
            f'Perímetro: {self.calcular_perimetro:.2f}'
        )


def main() -> None:
    circulo = Circulo(2)
    print(circulo.imprimir())


if __name__ == '__main__':
    main()
