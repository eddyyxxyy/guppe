"""
20) Escreva um código que apresente a classe Televisor, com atributos
ligado, canal e volume e, o método imprimir. O método imprimir deve
mostrar na tela os valores de todos os atributos. O atributo ligado
será boleano e deverá indicar o estado atual do televisor, se ligado
ou desligado. O atributo canal deverá indicar o canal atual em que
o televisor está sintonizado. O atributo volume deverá indicar o volume
atual do televisor.
"""
from ex19 import Eletrodomestico2


class Televisor(Eletrodomestico2):
    def __init__(self, ligada, canal=1, volume=15):
        super().__init__(ligada)
        self.__canal = canal
        self.__volume = volume

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, canal):
        self.__canal = canal

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def imprimir(self):
        return self.ligado, self.volume, self.canal


def main() -> None:
    televisao = Televisor(False)
    print(televisao.imprimir, '\n')
    televisao.ligar()
    print(televisao.imprimir, '\n')
    televisao.desligar()
    print(televisao.imprimir, '\n')
    televisao.volume = 20
    televisao.canal = 5
    televisao.ligar()
    print(televisao.imprimir)


if __name__ == '__main__':
    main()
