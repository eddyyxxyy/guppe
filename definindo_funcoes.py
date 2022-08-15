"""
# DRY: Dont Repeat Yourself → Não repita o seu código

Definindo funções

- Funções são um dos pilares de qualquer linguagem de programção, seja no Java, C, PHP, etc;
- Funções existem para criar pequenas partes de código que executam uma tarefa específica, são pequenos trechos
de código que server a um propósito;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas várias vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a
função seja simplificada. PROCURE ESCREVER FUNÇÕES SIMPLES!!!

# Já utilizamos várias funções desde que iniciamos o curso como:
- len()
- max()
- min()
- print()
- count()

Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print():

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('roxo')

print(cores)

# curso.append('Mais dados...')  # AttributeError
#
# print(curso)

Em Python, a forma geral de definir uma função é:

def nome_da_função(parâmetros_de_entrada):
    bloco_da_função


Onde:

nome_da_função → SEMPRE, com letras minúsculas, se for composto, separado por underline (Snake Case);
parâmetros_de_entrada → OPCIONAIS, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_função → Também chamado de Corpo da Função ou Implementação, é onde o processamento da função acontece,
neste bloco pode ter ou não retorno da função.

OBS: Veja que para definir uma função utilizamos uma palavra reservada do Python: def. Informando ao Python que estamos
definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos, que é utilizado em Python para
definir os blocos (identação).

# Definindo a primeira função:


def diz_oi():
    print('Oi!')


# Chamada de execução
diz_oi()

OBS: Veja que, dentro das nossas funções, podemos utilizar outras funções. E veja que, nossa função só executa
UMA TAREFA, ou seja, a única coisa que ela faz é imprimir "Oi!". Esta função não recebe nenhum parâmetro de entrada.
É NECESSÁRIO ter os parênteses ao executar uma função.

Em Python podemos criar uma variável do tipo de uma função e executar essa função através da variável:

canta = funcao_cantar

canta()
"""
