"""
5) Escreva um código que apresente a classe Retangulo, com atributos
comprimento, largura, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos area
e perimetro. O método imprimir deve mostrar na tela os valores de todos os
atributos. Salienta-se que a área de retângulo é obtida peça fórmula (comprimento *
largura) e o perímetro por (2 * comprimento) + (2 * largura)
"""


class Retangulo:
    def __init__(self, lado, largura):
        self.__lado = lado
        self.__largura = largura
        self.__perimetro = None
        self.__area = None

    def calcula_area(self):
        self.__area = self.__lado * self.__largura

    def calcula_perimetro(self):
        self.__perimetro = self.__lado * 2 + self.__largura * 2

    @property
    def imprimir(self):
        return self.__lado, self.__largura, self.__perimetro, self.__area


def main() -> None:
    retangulo = Retangulo(2, 4)
    print(retangulo.imprimir)
    retangulo.calcula_area()
    retangulo.calcula_perimetro()
    print(retangulo.imprimir)


if __name__ == '__main__':
    main()
