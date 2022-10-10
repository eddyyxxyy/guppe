"""
1) Escreva um código que apresente a classe Pessoa, com atributos nome,
endereço e telefone e, o método imprimir. O método imprimir deve mostrar todos
os valores de todos os atributos.
"""


class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def imprimir(self):
        return (
            f'Nome: {self.__nome}\n'
            f'Endereço: {self.__endereco}\n'
            f'Telefone: {self.__telefone}'
        )


def main() -> None:
    edson = Pessoa('Edson Pimenta', 'Franca - São Paulo', '16 1234-5678')
    print(edson.imprimir() + '\n')

    edson.nome = 'Edinho Pimenta'
    edson.endereco = 'São Paulo - Franca'
    edson.telefone = '16 8765-4321'
    print(edson.imprimir())


if __name__ == '__main__':
    main()
