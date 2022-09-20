"""
Conjuntos

Quando falamos de conjuntos estamos fazendo referência a teoria dos conjuntos em matemática.

- Em Python, os conjuntos são chamados de Sets.

- Sets (conjuntos) não possuem valores duplicados.
- Sets (conjuntos) não possuem valores ordenados.
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles,
quando não precisamos nos preocupar com chaves/valores e itens duplicados.

Os conjuntos são referênciados em Python com {}.

Diferença entre conjuntos/sets e mapas/dicionários.
- Um dicionário tem chave: valor
- Um set tem apenas valor

exemplo de declaração:
- s = set({1, 2, 3, 4, 5, 1, 2, 2, 2, 3, 4, 5, 5})

Para remover valores:
- s.discard(valor)  # se não tiver o valor não dará erro nem retornará nada.
- s.remove(valor)  # se não tiver o valor dará KeyError.

Shallow e Deep copy são aplicados...

Usando o clear() podemos limpar tod0 o conjunto...

Utilizando o union geramos um set com valores únicos, sem repetição.
"""
