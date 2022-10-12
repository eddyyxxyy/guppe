"""
28) Baseando-se no exercício 27 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso.
"""
from ex26 import Microwave


class Microwave1(Microwave):
    def __init__(self, status: bool):
        super().__init__(status)

    def turn_on(self):
        if self.status:
            pass
        else:
            self.status = True

    def turn_off(self):
        if self.status:
            self.status = False
        else:
            pass


def main() -> None:
    microwave = Microwave1(True)
    print('Status:', 'On' if microwave.info else 'Off')
    microwave.turn_off()
    print('Status:', 'On' if microwave.info else 'Off')
    microwave.turn_on()
    print('Status:', 'On' if microwave.info else 'Off')


if __name__ == '__main__':
    main()
