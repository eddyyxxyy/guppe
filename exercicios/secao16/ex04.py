"""
4) Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o
volume e trocar os canais da televisão.
    . O controle de volume permite aumentar ou diminuir a potência do volume
    de som em uma unidade de cada vez;
    . O controle de canal também permite aumentar e diminuir o número do canal em
    uma unidade, porém, também possibilita trocar para um canal indicado;
    . Também devem existir métodos para consultar o valor do volume de som e o
    canal selecionado.
"""


class Televisao:
    def __init__(self, canal: int = 0, volume: int = 10):
        self.__canal = canal
        self.__volume = volume

    @property
    def controle_volume(self):
        return self.__volume

    @controle_volume.setter
    def controle_volume(self, valor: int):
        self.__volume += valor

    @property
    def controle_canal(self):
        return self.__canal

    @controle_canal.setter
    def controle_canal(self, valor: int):
        if valor > 1:
            self.__canal = valor
        else:
            self.__canal += valor


class ControleRemoto:
    def __init__(self, televisao: Televisao):
        self.__televisao = televisao

    def alterar_volume(self, valor):
        self.__televisao.controle_volume = valor
        print(f'O volume da TV agora é {self.__televisao.controle_volume}')

    def alterar_canal(self, valor):
        self.__televisao.controle_canal = valor
        print(f'O canal da TV agora é {self.__televisao.controle_canal}')


def main() -> None:
    tv = Televisao()

    cr = ControleRemoto(tv)

    cr.alterar_volume(5)
    cr.alterar_volume(-12)
    cr.alterar_volume(-1)

    cr.alterar_canal(16)
    cr.alterar_canal(1)
    cr.alterar_canal(-7)
    cr.alterar_canal(5)


if __name__ == '__main__':
    main()
