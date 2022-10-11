"""
25) Baseando-se no exercício 24 adicione os métodos volumeAcima
e volumeAbaixo, sendo que o método volumeAcima deve modificar
o volume para o próximo nível de volume possível, onde ao chegar
ao volumeMaximo não poderá possibilitar que o volume seja alterado.
O método volumeAbaixo deve modificar o volume para o nível imediatamente
inferior de volume me relação ao volume atual, não podendo ser menor do
que 0, simulando desta forma o funcionamento de um televisor.
"""
from ex24 import Televisor2


class Televisor3(Televisor2):
    def __init__(self, ligada, canal, volume, numero_canais, volume_maximo):
        super().__init__(ligada, canal, volume, numero_canais, volume_maximo)

    def volume_acima(self):
        if self.volume == self.volume_maximo:
            pass
        else:
            self.volume += 1

    def volume_abaixo(self):
        if self.volume == 0:
            pass
        else:
            self.volume -= 1


def main() -> None:
    televisao = Televisor3(False, 1, 1, 25, 100)
    print(televisao.imprimir)
    televisao.volume_abaixo()
    print(televisao.imprimir)
    televisao.volume_abaixo()
    print(televisao.imprimir)
    televisao.volume = 99
    print(televisao.imprimir)
    televisao.volume_acima()
    print(televisao.imprimir)
    televisao.volume_acima()
    televisao.volume_acima()
    print(televisao.imprimir)


if __name__ == '__main__':
    main()
