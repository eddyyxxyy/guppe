"""
27) Basenado-se no exercício 26 adicione um método construtor
que permita o definição de todos os atributos no momento da
instanciação do objeto.
"""
from ex26 import Microwave


def main() -> None:
    microwave = Microwave(status=True)
    print('Status:', 'On' if microwave.info else 'Off')


if __name__ == '__main__':
    main()
