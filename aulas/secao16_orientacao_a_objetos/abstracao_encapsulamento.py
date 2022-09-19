"""
POO - Abstração e Encapsulamento

O grande objetivo da programação orientada a objeto é encapsular nosso código
dentro de um grupo lógico e hierarquico utilizando classes.

Seria encapsular, colocar em uma classe, os dados relevantes do que será instânciado,
do que precisa ser instânciado. A abstração é o ato de expor os dados relevantes de
uma classe escondendo atributos e métodos privados de usuários.


"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo!')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo < valor:
                print(f'Não há saldo suficiente para sacar {valor}')
            self.__saldo -= valor
        else:
            print('O valor deve ser positivo!')


# Testando

conta1 = Conta('Geek', 150.00, 1500)

# print(conta1.numero)
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)
#
# conta1.numero = 42
# conta1.titular = 'Xuxa'
# conta1.saldo = 999999999999999999
# conta1.limite = 99999999999999999999999

print(conta1.__dict__)

conta1.extrato()
conta1.depositar(150)
conta1.sacar(2000)

print(conta1.__dict__)