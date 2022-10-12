"""
31) Basenado-se no exerício 30 modifique o método ligar para que só ligue
o equipamento quando a porta do mesmo estiver fechada, simulando assim
o funcionamento de um microondas.
"""
from ex30 import Microwave


def main() -> None:
    microwave = Microwave()
    print(microwave.info())
    microwave.open_plate()
    print(microwave.info())
    microwave.turn_on()
    microwave.close_plate()
    print(microwave.info())


if __name__ == '__main__':
    main()
