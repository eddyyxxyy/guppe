"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder.
Já conhecemos o __init__, que é nosso inicializador, que
junto do __new__ foram nosso construtor, pois o __new__ é
nosso alocador de memória.

Dunder -> Double Underscore

Dunder init -> __init__

Dunder repr -> __repr__ -> Representação do objeto
    - Geralmente é o desenvolvedor que sobescreve o repr
    para visualizar uma representação pretendida do objeto.
    - O seu objetivo, diferente do __str__ é ser NÃO ambíguo,
    ou seja, ele é a representação que ajuda o desenvolvedor
    a entender melhor a classe.

Dunder str -> __str__ -> Representão em string do objeto
    - Uma vez que o repr foi declarado e sobescrito e o __str__
    não, a linguagem assume que __str__ é igual a __repr__.
    - Porém, a pretenção de uso do __str__ se extende à ser
    legível e NÃO ser algo que não é ambíguo, ele somente
    corresponde (por essência) à ser mais bonito e apresentável
    que o __repr__.
    - A função print() e str() chamam o __str__.

Dunder len -> __len__ -> Retorna o tamanho em int do objeto
    - Definimos que o tipo Livro agora retorna com len
    a quantiade de páginas.

Dunder del -> __del__ -> É um finalizador do objeto
    - Aqui não alteramos seu comportamento base, só
    adicionamos a funcionalidade de informar ao usuário
    que foi deletado o objeto instânciado

E temos muitos exemplos mais, com isso podemos entender que os métodos
mágicos nada mais são do que polimorfismos da Classe Pai object.
"""


class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'Título: {self.__titulo}'

    # def __str__(self):
    #     ...
    # return f'Título: {self.__titulo} ' \
    #        f'\nEscrito por: {self.__autor}'

    def __len__(self):
        return self.__paginas

    def __del__(self):
        ...
        # print(f'{self.__titulo} foi deletado da memória.')

    def __add__(self, other):
        return f'{self} - {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar por um valor não inteiro.'


def main() -> None:
    livro = Livro('A Guerra dos Tronos', 'George R. R. Martin', 592)
    livro0 = Livro('A Fúria dos Reis', 'George R. R. Martin', 656)

    print(livro, '\n')
    print(repr(livro), '\n')
    print(livro0, '\n')
    print(repr(livro0), '\n')

    print()
    print(len(livro))
    print(len(livro0))
    print()

    print(livro + livro0)
    print(livro * 3)


if __name__ == '__main__':
    main()
