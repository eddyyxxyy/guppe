"""
22) Baseando-se no exercicio 21 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso
"""
from ex21 import Televisor


def main() -> None:
    televisao = Televisor(True, 1, 15)
    televisao.desligar()
    print(televisao.imprimir)
    print(televisao.ligado)
    televisao.ligar()
    print(televisao.imprimir)
    print(televisao.ligado)


if __name__ == '__main__':
    main()
