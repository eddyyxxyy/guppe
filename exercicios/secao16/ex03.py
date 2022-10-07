"""
3) Crie uma classe denominada Elevador para armazenar as informações de um
elevador dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0),
total de andares no prédio, excluindo o térreo, capacidade do elevador, e
quantas pessoas estão presentes nele.
A classe deve também disponibilizar os seguintes métodos:
    . Inicializa: que deve receber como parâmetros a capacidade do elevador e
    o total de andares no prédio (os elevadores sempre começam no térreo vazio);
    . Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda
    houver espaço);
    . Sai: para remover uma pessoa do elevador (só deve remover se houver alguém
    dentro dele);
    . Sobe: para subir um andar (não deve subir se já estiver no último andar);
    . Desce: para descer um andar (não deve descer se já estiver no térreo);
    . Encapsular métodos os atributs da classe (criar métodos set e get).
"""


class Elevator:
    def __init__(self, total_andares, capacidade_pessoas):
        self.__total_andares = total_andares
        self.__capacidade_pessoas = capacidade_pessoas
        self.__andar_atual = 0
        self.__presentes = 0

    def entra(self):
        if self.__presentes < self.__capacidade_pessoas:
            self.__presentes += 1
        else:
            print('O elevador está cheio.')

    def sai(self):
        if self.__presentes > 0:
            self.__presentes -= 1
        else:
            print('Não há ninguém no elevador, ninguém pode sair.')

    def sobe(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
        else:
            print('O elevator está no ultimo andar.')

    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
        else:
            print('O elevator está no térro, não é possível descer.')

    @property
    def total_andares(self):
        return self.__total_andares

    @total_andares.setter
    def total_andares(self, valor):
        if isinstance(valor, int):
            self.__total_andares = valor
        else:
            print('O número total de andares precisa ser inteiro.')

    @property
    def capacidade_pessoas(self):
        return self.__capacidade_pessoas

    @capacidade_pessoas.setter
    def capacidade_pessoas(self, valor):
        if isinstance(valor, int):
            self.__capacidade_pessoas = valor
        else:
            print('O número máximo de pessoas precisa ser inteiro.')

    @property
    def andar_atual(self):
        return self.__andar_atual

    @andar_atual.setter
    def andar_atual(self, valor):
        if isinstance(valor, int) and 0 < valor <= self.__total_andares:
            self.__andar_atual = valor
        else:
            print('Andar inválido!')

    @property
    def presentes(self):
        return self.__presentes

    @presentes.setter
    def presentes(self, valor):
        if isinstance(valor, int) and 0 <= valor <= self.__capacidade_pessoas:
            self.__presentes = valor
        else:
            print('A quantidade de pessoas presentes informada é inválida')


def main():
    elevador0 = Elevator(10, 6)
    print(elevador0.total_andares)
    print(elevador0.capacidade_pessoas)
    elevador0.desce()
    elevador0.sobe()
    print(elevador0.andar_atual)
    elevador0.total_andares = 12
    elevador0.capacidade_pessoas = 8
    print(elevador0.total_andares)
    print(elevador0.capacidade_pessoas)


if __name__ == '__main__':
    main()
