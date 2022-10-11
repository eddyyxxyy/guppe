"""
18) Baseando-se no exercício 17 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""
from ex17 import Eletrodomestico


class Eletrodomestico1(Eletrodomestico):
    def __init__(self, ligada):
        super().__init__(ligada)


def main() -> None:
    geladeira = Eletrodomestico1(False)
    print(geladeira.imprimir)


if __name__ == '__main__':
    main()
