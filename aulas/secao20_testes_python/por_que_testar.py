"""
Por que testar nosso código?

- ATENÇÃO -> Testes automatizados!

- Testes reduzem bugs no código existente;

- Testes garantem que novos recursos da sua
  aplicação não quebrem/alterem recursos antigos;

- Testes garantem que problemas resolvidos ante-
  riormente continuem corrigidos;

- Testes garantem que a refatoração que costuma-
  mos a fazer, não tragam novos bugs;

Então chegamos ao TDD (Test Driven Development),
com o TDD primeiro escrevemos nosso teste, como
por exemplo:

felix = Gato('Felix')
felix.miar()
print(felix.nome)

Assim descobrimos que estamos instânciando um
objeto, ou seja, precisamos de uma classe, e
nosso código de teste pede pelo método miar()
e pela propriedade nome.


class Gato:
   '''lasse com características de um gato.'''

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def miar(self):
        print(f'{self._nome} está miando...')


Esses testes, para os adeptos do TDD, são quase
um mantra em seu desenvolvimento. São conhecidos:
  - Red (o vermelho no terminal, quando falha o teste);
  - Green (o verde no terminal, quando é bem sucedido o teste);
  - Refactor (a refatoração do código testado).
"""
