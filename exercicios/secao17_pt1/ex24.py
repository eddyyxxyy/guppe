"""
24) Baseando-se no exercicio 23 adicione os métodos canalAcima e
canalAbaixo, sendo que o método canalAcima deve sintonizar sempre
o próximo canal em relaão ao canal atual, onde ao chegar ao maior
canal possível deverá voltar ao canal 1. O método canalAbaixo deve
sintonizar sempre o canal anterior em relação ao canal atual, onde
ao chegar ao canal 1 deverá voltar ao maior canal possível, simulando
desta forma o funcionamento de um televisor.
"""
from ex23 import Televisor1


class Televisor2(Televisor1):
    def __init__(self, ligada, canal, volume, numero_canais, volume_maximo):
        super().__init__(ligada, canal, volume, numero_canais, volume_maximo)

    def canal_acima(self):
        if self.canal == self.numero_canais:
            self.canal = 1
        else:
            self.canal += 1

    def canal_abaixo(self):
        if self.canal == 1:
            self.canal = self.numero_canais
        else:
            self.canal -= 1


def main() -> None:
    televisao = Televisor2(False, 1, 15, 25, 100)
    print(televisao.imprimir)
    televisao.canal_abaixo()
    print(televisao.imprimir)
    televisao.canal_acima()
    print(televisao.imprimir)
    televisao.canal_acima()
    televisao.canal_acima()
    televisao.canal_acima()
    print(televisao.imprimir)
    televisao.canal_abaixo()
    print(televisao.imprimir)


if __name__ == '__main__':
    main()
