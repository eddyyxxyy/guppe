class Robo:
    def __init__(self, nome, bateria=100, habilidades=None):
        if habilidades is None:
            habilidades = []
        self._nome = nome
        self._bateria = bateria
        self._habilidade = habilidades

    @property
    def nome(self):
        return self._nome

    @property
    def bateria(self):
        return self._bateria

    @property
    def habilidades(self):
        return self._habilidade

    def carregar(self):
        self._bateria = 100

    def dizer_nome(self):
        if self._bateria > 0:
            self._bateria -= 1
            return f'Beep Boop, eu sou {self._nome.upper()}'
        return 'Sem bateria! Por favor, recarregue e tente novamente.'

    def aprender_habilidade(self, nova_habilidade: str, custo: int):
        if self._bateria >= custo:
            self._bateria -= custo
            self._habilidade.append(nova_habilidade)
            return f'Uau! Aprendi {nova_habilidade.capitalize}.'
        return 'Bateria insuficiente! Por favor, recarregue e tente novamente.'
