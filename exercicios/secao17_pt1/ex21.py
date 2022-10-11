"""
21) Basenado-se no exercício 20 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do
objeto.
"""
from ex20 import Televisor


def main() -> None:
    televisao = Televisor(True, 12, 25)
    print(televisao.imprimir)


if __name__ == '__main__':
    main()
