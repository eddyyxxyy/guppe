"""
19) Baseando-se no exercicio 18 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso.
"""
from ex18 import Eletrodomestico1


class Eletrodomestico2(Eletrodomestico1):
    def __init__(self, ligada):
        super().__init__(ligada)

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False


def main() -> None:
    eletrodomestico = Eletrodomestico2(False)
    print(eletrodomestico.ligado, '\n')
    eletrodomestico.ligar()
    print(eletrodomestico.ligado, '\n')
    eletrodomestico.desligar()
    print(eletrodomestico.ligado, '\n')


if __name__ == '__main__':
    main()
