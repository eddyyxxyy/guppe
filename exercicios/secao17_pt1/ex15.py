"""
15) Basenado-se no exercício 14 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do objeto.
"""
from ex14 import Moto4


class Moto5(Moto4):
    def __init__(
        self, marca, modelo, cor, marcha, menor_marcha, maior_marcha, ligada
    ):
        super().__init__(
            marca, modelo, cor, marcha, menor_marcha, maior_marcha, ligada
        )


def main() -> None:
    moto = Moto5('Honda', 'CG', 'Preta', 0, 0, 2, ligada=False)
    print(moto.imprimir)
    print(moto.status)
    moto.liga_desliga()
    print(moto.status)


if __name__ == '__main__':
    main()
