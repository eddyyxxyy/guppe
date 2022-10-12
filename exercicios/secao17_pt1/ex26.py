"""
26) Escreva um código que apresente a classe Microondas, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os
valores de todos os atributos. O atributo ligado será boleano e verá indicar
o estado atual do microondas, se ligado ou desligado.
"""


class Microwave:
    def __init__(self, status: bool):
        self.__status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, boolean):
        self.__status = boolean

    @property
    def info(self):
        return self.status


def main() -> None:
    microwave = Microwave(True)
    microwave.status = False
    print('Status:', 'On' if microwave.info else 'Off')


if __name__ == '__main__':
    main()
