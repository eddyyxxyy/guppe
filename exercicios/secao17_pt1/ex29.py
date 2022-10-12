"""
29) Baseando-se no exercício 28 adicione o atributo portaFechada que
deverá ser boleano e deverá indicar se a porta do microondas está
ou não fechada. O método imprimir deve ser modificado de forma a mostrar
na tela os valores de todos os métodos.
"""
from ex28 import Microwave1


class Microwave2(Microwave1):
    def __init__(self, status: bool, closed: bool):
        super().__init__(status)
        self.__closed = closed

    @property
    def closed(self):
        return self.__closed

    @closed.setter
    def closed(self, boolean):
        if self.__closed:
            pass
        else:
            self.__closed = boolean

    @Microwave1.info.getter
    def info(self):
        return self.status, self.__closed


def main() -> None:
    microwave = Microwave2(True, True)
    info = microwave.info
    print(f'Status: {info[0]}\n' f'Door is closed? {info[1]}')


if __name__ == '__main__':
    main()
