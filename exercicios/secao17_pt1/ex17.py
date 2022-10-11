"""
17) Escreva um código que apresente a classe Eletrdoméstico, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os valores de
todos os atributos. O atributo ligado será booleano e deverá indica o estado
atual do eletrodoméstico, se ligado ou desligado.
"""


class Eletrodomestico:
    def __init__(self, ligada: bool = False):
        self.__ligado = ligada

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, ligado):
        self.__ligado = ligado

    @property
    def imprimir(self):
        return self.ligado


def main() -> None:
    geladeira = Eletrodomestico()
    print(geladeira.imprimir)


if __name__ == '__main__':
    main()
