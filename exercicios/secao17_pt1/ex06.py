"""
6) Baseando-se no exercício 5 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação
do objeto.
"""


class Retangulo:
    def __init__(self, lado, largura, perimetro, area):
        self.__lado = lado
        self.__largura = largura
        self.__perimetro = perimetro
        self.__area = area

    def calcula_area(self):
        self.__area = self.__lado * self.__largura

    def calcula_perimetro(self):
        self.__perimetro = self.__lado * 2 + self.__largura * 2

    @property
    def imprimir(self):
        return self.__lado, self.__largura, self.__perimetro, self.__area


def main() -> None:
    retangulo = Retangulo(2, 4, 12, 8)
    print(retangulo.imprimir)


if __name__ == '__main__':
    main()
