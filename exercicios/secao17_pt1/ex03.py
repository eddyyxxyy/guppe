"""
3) Escreva um código que apresente a classe Quadrado, com atributos
lado, área e perímetro e, os métodos calcularArea, calcularPerimetro
e imprimir. Os métodos calcularArea e calcularPerimetro devem efetuar
seus respectivos cálculos e colocar os valores nos atributos area e
perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se que a área de um quadrado é obtida pela
fórmula (lado * lado) e o perímetro por (4 * lado).
"""


class Quadrado:
    def __init__(self, lado):
        self.__lado = lado
        self.__area = 0
        self.__perimetro = 0

    def calcular_area(self):
        self.__area = self.__lado * self.__lado
        return self.__area

    def calcular_perimetro(self):
        self.__perimetro = self.__lado * 4
        return self.__perimetro

    def imprimir(self):
        return self.__lado, self.__area, self.__perimetro


def main() -> None:
    quadrado0 = Quadrado(4)
    print(quadrado0.imprimir())
    quadrado0.calcular_area()
    quadrado0.calcular_perimetro()
    print(quadrado0.imprimir())


if __name__ == '__main__':
    main()
