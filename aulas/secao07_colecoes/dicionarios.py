"""
Dicionários

OBS: em alguma linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por {}.

Exemplo de declaração de dicts:
- paises = {'br': 'Brasil', 'eua': 'Estados Unidos", 'pi': 'Paraguai'}
           chave:  valor,  chave:      valor,        chave:  valor
OBS: Tanto a chave como o valor podem ser de qualquer tipo e são sempre separados por 2 pontos ":", podemos misturar
tipos de dados

# DICINÁRIOS NÃO SÃO INDEXADOS, DEVEMOS ACESSAR PELAS CHAVES.
# Imprimimos os valores através das chaves:
- print(paises['br']) → retorna Brasil, caso a chave não exista retornará KeyError

Acessando elementos via get:
- print(paises.get('br')) → caso não exista o elemento, a key, ele retorna None em vez de KeyError
# ↑ É O JEITO RECOMENDADO ↑
# podemos definir um valor padrão de retorno caso o get falhe, é só colocar "," após o elemento procurado e informar
o retorno

Tuplas são bons exemplos para Keys de dicionários, pois são imutáveis, por exemplo podemos utilizar como key coordena-
das de um local e como valor dessa key o nome do local.

Adicionando elementos num dicionário:
- dicionario['key'] = valor
- novo_valor = {'key': valor}
  dicionario.update(novo_valor)
- dicionario.update({'key': valor})

# Para adicionar ou alterar valores em um dicionário a forma é a mesma.
# Não podemos ter chaves repetidas em dicionários, se usarmos uma chave já existente ele só atualiza o valor contido na
chave.

Remover dados de um dicionário:
- dicionario.pop('key')
# Caso não encontre a key, retorna KeyError.
# Esse método remove e retorna o valor apagado
- del dicionario['key']
# Caso não encontre a key, retorna KeyError.
# Esse método remove e não retorna o valor apagado.

Para limpar dicionários, zera-los:
- dicionario.clear()

Shallow copy e Deep copy se aplicam da mesma forma, com copy fazendo o Deep (não gera relação entre os dicionários) e
com atribuição (gerando relação entre os dicionários).
- Deep copy: dicionario2 = dicionario1.copy()
- Shallow copy: dicionario2 = dicionario1
"""
