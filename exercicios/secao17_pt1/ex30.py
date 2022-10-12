"""
30) Baseando-se no exercício 29 qadicione os métodos fecharPorta e abrirPorta que
deverá mudar o contéudo do atributo portaFechada conforme o caso.
"""


class Microwave:
    def __init__(self, on=False, plate=False):
        self.__on = on
        self.__plate = plate

    def turn_on(self):
        if self.__plate is True:
            self.__on = True
            return 'The microwave already on'
        else:
            self.__on = False
            return 'The plate is open, close it to be able to turn on'

    def open_plate(self):
        self.__plate = False
        return "Microwave's plate is open"

    def close_plate(self):
        self.__plate = True
        return "Microwave's plate is closed"

    def info(self):
        if self.__on is False and self.__plate is False:
            return "Microwave is off and the plate is open, can't turn on"
        elif self.__on:
            return 'Microwave already on'
        elif self.__on is False and self.__plate is True:
            return 'Microwave is off and ready to be turned on'


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
