"""
11) Baseando-se no exercício 10 adicione os métodos marchaAcima e
marchaAbaixo que deverão efetuar a troca de marchas, onde o método
marchaAcima deverá subir uma marcha, ou seja, se a moto estiver em
primeira marcha, deverá ser trocada para segunda marcha e assim por diante.
O método marchaAbaixo deverá realiar o oposto, ou seja, descer a marcha.
O método imprimir deve ser modificado de forma a mostrar na tela os valores
de todos os atributos.
"""
from ex09 import Moto


class Moto2(Moto):
    def __init__(self, marca, modelo, cor, marcha):
        super(Moto2, self).__init__(marca, modelo, cor, marcha)

    def marcha_acima(self):
        if int(self.marcha[0]) < 2:
            self.marcha = int(self.marcha[0]) + 1
        else:
            raise ValueError('A moto não possui marchas acima da segunda!')

    def marcha_abaixo(self):
        if int(self.marcha[0]) > 0:
            self.marcha = int(self.marcha[0]) - 1
        else:
            raise ValueError('A moto não possui marchas abaixo da neutra (0).')


def main() -> None:
    moto = Moto2('Honda', 'CG', 'Preta', 0)
    print(moto.imprimir)
    moto.marcha_acima()
    print(moto.imprimir)
    moto.marcha_acima()
    print(moto.imprimir)
    # moto.marcha_acima()
    # print(moto.imprimir)
    moto.marcha_abaixo()
    print(moto.imprimir)
    moto.marcha_abaixo()
    print(moto.imprimir)
    # moto.marcha_abaixo()
    # print(moto.imprimir)


if __name__ == '__main__':
    main()
