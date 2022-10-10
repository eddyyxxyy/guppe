"""
10) Baseando-se no exercício 9 adicione um método construtor que permita
a definição de todos os atributos no momento da instânciação do objeto
"""
from ex09 import Moto


class Moto2(Moto):
    def __init__(self):
        """Construtor Padrão que chama a Classe Pai"""
        super(Moto2, self).__init__('', '', '', 0)


def main() -> None:
    moto1 = Moto2()
    moto1.marca = 'Yamaha'
    print(moto1.imprimir)
    moto1.modelo = 'XJ6'
    print(moto1.imprimir)
    moto1.cor = 'Branca'
    print(moto1.imprimir)
    moto1.marcha = 1
    print(moto1.imprimir)


if __name__ == '__main__':
    main()
