"""
16) Basenado-se no exercício 15 adicione os métodos ligar e deligar que
deverão mudar o conteúdo do atibuto ligada conforme o caso.
"""
from ex15 import Moto5


def main() -> None:
    moto = Moto5('Honda', 'CG', 'Preta', 0, 0, 2, ligada=False)
    print(moto.imprimir)
    print(moto.status)
    moto.liga_desliga()
    print(moto.status)


if __name__ == '__main__':
    main()
