"""
Raise - Levantando os próprios erros

raise → Lança exceções

OBS: raise não é uma função, é uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro,
a forma geral de utilização é:

raise TipoDoErro('Mensagem de Erro')


# Exemplo real de uso:


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 4)  # TypeError: cor precisa ser uma string
# colore(4, 'Azul')  # TypeError: texto precisa ser uma string

# Lembrando, NÃO estamos TRATANDO ERROS, estamos lançando o erro, visualizando a própria exceção/erro

Refatorando o exemplo anterior:

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')

OBS: O raise, assim como o retorn, finaliza a função, ou seja, nada após o raise será executado uma vez que o raise
entrou em ação.

"""
