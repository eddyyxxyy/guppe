"""
13) Baseando-se no exercício 12 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""
from ex12 import Moto3


def main() -> None:
    moto = Moto3('Honda', 'CG', 'Preta', 0, 0, 2)
    print(moto.imprimir)


if __name__ == '__main__':
    main()
