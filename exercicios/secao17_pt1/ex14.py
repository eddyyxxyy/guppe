"""
14)Baseando-se no exercício 13 adicione o atributo ligada que terá a função
de indicar se a moto está ligada ou não. Este atributo deverá ser do tipo
boleano. O método imprimir deve ser modificado de forma a mostrar na tela
os vaores de todos os atributos.
"""
from ex13 import Moto3


class Moto4(Moto3):
    def __init__(
        self, marca, modelo, cor, marcha, menor_marcha, maior_marcha, ligada
    ):
        super().__init__(
            marca, modelo, cor, marcha, menor_marcha, maior_marcha
        )
        self.__ligada = ligada

    @property
    def status(self):
        if self.__ligada:
            return 'A moto está ligada'
        else:
            return 'A moto está desligada'

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


def main() -> None:
    moto = Moto4('Honda', 'CG', 'Preta', 0, 0, 2)
    print(moto.imprimir)
    print(moto.status)
    moto.liga_desliga()
    print(moto.status)


if __name__ == '__main__':
    main()
