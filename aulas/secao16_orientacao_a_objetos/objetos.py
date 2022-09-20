"""
POO - Objetos

Objetos -> São instâncias da Classe, ou seja, após o mapeamento do objeto
do mundo real para sua representação computacional, devemos poder criar
quantos objetos forem necessários. Podemos pensar nos objetos/instâncias
de uma Classe como variáveis do tipo definido na classe.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False

    def checa_lampada(self):
        return self.ligada

    def liga_desliga(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


class ContaCorrente:

    contador = 0

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


lamp1 = Lampada('Branca', 110, 60)  # Instância/Objeto do tipo Lampada
# lamp1.liga_desliga()  # Liga e desliga a lâmpada
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000, 20000)  # Instância do tipo ContaCorrente

user1 = Usuario(
    'Edson', 'Pimenta', 'edson@gmail.com', '123456'
)  # Instância do tipo Usuário
