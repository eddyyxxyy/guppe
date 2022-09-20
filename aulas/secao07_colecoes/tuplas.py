"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: isso significa que ao se criar uma tupla ela não muda posteriormente. Toda operação em
uma tupla gera uma nova tupla

OBS: Se declaramos uma variável com virgulas, sem informar o () ou {} ou [], geramos uma tupla:
- tupla = 1, 2, 3, 4, 5 → gera uma tupla
OBS: Cuidados ao declarar uma tupla e tuplas de 1 único elemento:
- tupla = (1) → não é tupla
- tupla = (1,) → é uma tupla
- tupla = 1, → é uma tupla
# Fazendo com que o que defina a tupla seja muito mais a vírgula do que o parenteses em si,

OBS: Podemos gerar uma tupla dinamicamente com o range:
- tupla = tuple(range(10)) → gera uma tupla do 0 ao 9

OBS: Se todos os valores forem inteiros ou reais, podemos pegar o Valor Máximo, Valor Mínimo e Soma:
- print(sum(tupla))
- print(max(tupla))
- print(min(tupla))
# O tamanho não depende dos valores serem inteiros/reais ou não, só conta o número de índices e informa o tamanho da
tupla.

Para verificar se algo está na lista:
tupla = (1, 2, 3)
print(3 in lista)
→ retorna True

Dicas para utilização de tuplas:
- Sempre as utilizamos quando sabemos que não precisaremos modificar os dados contidos na coleção, por exemplo em meses.
OBS: Ainda mais que as tuplas são mais rápidas, com menos utilização de recursos computacionais e deixam seus códigos
mais seguros.
"""
