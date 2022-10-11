"""
23) Basenado-se no exercício 22 adicione os atributos numeroCanais
e, volumeMaximo, onde numeroCanais indica o número máximo de canais
que o televisor pode sintonizar e volumeMaximo indica qual o maior nível
de volume possível. O método imprimir deve ser modificado de forma a mostrar
na tela os valores de todos os atributos.
"""
from ex20 import Televisor


class Televisor1(Televisor):
    def __init__(self, ligada, canal, volume, numero_canais, volume_maximo):
        super().__init__(ligada, canal, volume)
        self.__canal = canal
        self.__volume = volume
        self.__numero_canais = numero_canais
        self.__volume_maximo = volume_maximo

    @property
    def canal(self):
        return self.__canal

    @property
    def volume(self):
        return self.__volume

    @property
    def numero_canais(self):
        return self.__numero_canais

    @property
    def volume_maximo(self):
        return self.__volume_maximo

    @property
    def imprimir(self):
        return (
            self.ligado,
            self.volume,
            self.canal,
            self.volume_maximo,
            self.numero_canais,
        )

    @numero_canais.setter
    def numero_canais(self, canal_maximo):
        self.__numero_canais = canal_maximo

    @volume_maximo.setter
    def volume_maximo(self, volume_maximo):
        self.__volume_maximo = volume_maximo

    @canal.setter
    def canal(self, canal):
        if isinstance(canal, int):
            if canal <= self.__numero_canais:
                self.__canal = canal
            else:
                raise ValueError(f'O canal máximo é {self.numero_canais}')

    @volume.setter
    def volume(self, volume):
        if isinstance(volume, int):
            if volume <= self.__volume_maximo:
                self.__volume = volume
            else:
                raise ValueError(f'O canal máximo é {self.volume_maximo}')


def main() -> None:
    televisao = Televisor1(False, 1, 15, 25, 100)
    info = televisao.imprimir
    print(
        f'Status: {info[0]}'
        f'\nVolume atual: {info[1]}'
        f'\nCanal atual: {info[2]}'
        f'\nVolume máximo: {info[3]}'
        f'\nCanal máximo: {info[4]}\n'
    )
    televisao.canal = 14
    televisao.volume = 50
    info = televisao.imprimir
    print(
        f'Status: {info[0]}'
        f'\nVolume atual: {info[1]}'
        f'\nCanal atual: {info[2]}'
        f'\nVolume máximo: {info[3]}'
        f'\nCanal máximo: {info[4]}'
    )


if __name__ == '__main__':
    main()
