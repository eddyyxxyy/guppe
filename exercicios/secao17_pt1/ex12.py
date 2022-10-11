"""
12) Basenado-se no exercicio 11 adicione os atributos menorMarcha
e maiorMarcha, onde o atributo menorMarcha indica qual será a menor
marcha possível para a moto e o atributo maiorMarcha indica qual será
a maior marcha possível. Desta forma os métodos marchaAcima e marchaAbaixo
deve ser reescritos de forma a não permitirem a troca de marchar para valores
abaixo da menorMarcha e acima da maiorMarcha. O método imprimir deve ser
modificado de forma a mostrar na tela os valores de todos os atributos.
"""
from ex11 import Moto2


class Moto3(Moto2):
    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha):
        super().__init__(marca, modelo, cor, marcha)
        self.__menor_marcha = menor_marcha
        self.__maior_marcha = maior_marcha

    @property
    def menor_marcha(self):
        return self.__menor_marcha

    @property
    def maior_marcha(self):
        return self.__maior_marcha

    @property
    def imprimir(self):
        return (
            f'Marca: {self.marca}\n'
            f'Modelo: {self.modelo}\n'
            f'Cor: {self.cor}\n'
            f'Marcha Atual: {self.marcha}\n'
            f'Menor marcha possível: {self.menor_marcha}\n'
            f'Maior marcha possível: {self.maior_marcha}'
        )


def main() -> None:
    moto = Moto3('Honda', 'CG', 'Preta', 0, 0, 2)
    print(moto.imprimir)


if __name__ == '__main__':
    main()
