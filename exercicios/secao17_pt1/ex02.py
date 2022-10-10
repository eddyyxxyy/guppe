"""
2) Baseando-se no exercício 1 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""
from ex01 import Pessoa


def main() -> None:
    edson = Pessoa('Edson Pimenta', 'Franca - São Paulo', '16 1234-5678')
    print(edson.imprimir())


if __name__ == '__main__':
    main()
