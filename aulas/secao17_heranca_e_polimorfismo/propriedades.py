"""
POO - Propriedades (Properties)

Em linguagens de programação como o Java, ao declararmos atributos privados
nas classes, costumamos a criar métodos públicos para manipulação desses
atributos. Esses métodos são conhecidos por getters e setters, onde os
getters retornam o valor do atributo e os setters alteram o valor do mesmo.


from locale import setlocale, LC_MONETARY, currency


class Conta:

    contador = 0

    def __init__(self, titular: str, saldo: float, limite: float):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self) -> str:
        return f'Saldo do titular {self.__titular}: ' \
               f'{currency(self.__saldo, grouping=True)}'

    def depositar(self, valor: float) -> None:
        if isinstance(valor, float) and valor > 0:
            self.__saldo += valor

    def sacar(self, valor: float) -> None:
        if isinstance(valor, float) and valor < self.__saldo:
            self.__saldo -= valor

    def transferir(self, valor: float, destino) -> None:
        if isinstance(valor, float) and valor < self.__saldo:
            self.__saldo -= valor
            destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


setlocale(LC_MONETARY, 'pt_BR.UTF-8')

conta0 = Conta('Edson Pimenta', 1200, 5000)
conta1 = Conta('Isabela Gavilan', 10000, 50000)

# print(conta0.extrato())

# conta0.depositar(2000.00)
# print(conta0.extrato())

# print(conta1.extrato())

# conta1.transferir(5000.00, conta0)
# print(conta1.extrato())
# print(conta0.extrato())

# soma = conta0.get_saldo() + conta1.get_saldo()
# print(currency(soma, grouping=True))

print(conta1.__dict__)
conta1.set_limite(99999)
print(conta1.__dict__)

"""
from locale import LC_MONETARY, currency, setlocale


class Conta:

    contador = 0

    def __init__(self, titular: str, saldo: float, limite: float):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self) -> str:
        return (
            f'Saldo do titular {self.__titular}: '
            f'{currency(self.__saldo, grouping=True)}'
        )

    def depositar(self, valor: float) -> None:
        if isinstance(valor, float) and valor > 0:
            self.__saldo += valor

    def sacar(self, valor: float) -> None:
        if isinstance(valor, float) and valor < self.__saldo:
            self.__saldo -= valor

    def transferir(self, valor: float, destino) -> None:
        if isinstance(valor, float) and valor < self.__saldo:
            self.__saldo -= valor
            destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


setlocale(LC_MONETARY, 'pt_BR.UTF-8')

conta0 = Conta('Edson Pimenta', 1200, 5000)
conta1 = Conta('Isabela Gavilan', 10000, 50000)

print(conta0.extrato())
print(conta1.extrato())

soma = conta0.saldo + conta1.saldo
print(
    f'A soma dos saldos de {conta0.titular} e {conta1.titular} é: '
    f'{currency(soma, grouping=True)}'
)

print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)

print(conta0.valor_total)
print(conta1.valor_total)
