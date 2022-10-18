"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

Mas o que são Testes Unitários?
    - É a forma de se testar unidades individuais
    de código fonte;

Quando falamos de unidades individuais estamos falando de:
    - Funções;
    - Métodos;
    - Classes;
    - Módulos;
    - Etc...

O objetivo destes teste unitários é mostrar que cada unidade
atende especificamente a sua especificação.

# OBS: Teste Unitário não é algo atrelado somente à Python,
é algo ligado diretamente a qualidade do código desenvolvido,
não importando qual linguagem está utilizando sua aplicação.

# OBS: Entretando, o módulo Unittest, é altamente indicado
para a realização dos testes em Python, pois dá o suporte
à sua realização da forma Pythônica.


Para criar nossos testes, criamos Classes que herdam de
unittest.TestCase e a partir de então ganhamos todos os
assertions presentes no módulo.

Para rodar os testes, utilizamos unittest.main().

TestCase -> Casos de teste para sua unidade.

Conhecendo as Assertions:

assertEqual(a, b)          |    a == b
assertNotEqual(a, b)       |    a != b
assertTrue(a)              |    bool(a) is True
assertFalse(a)             |    bool(a) is False
assertIs(a, b)             |    a is b
assertIsNot(a, b)          |    a is not b
assertIsNone(a)            |    a is None
assertIsNotNone(a)         |    a is not None
assertIn(a, b)             |    a in b
assertNotIn(a, b)          |    a not in b
assertIsInstance(a, b)     |    isinstance(a, b)
assertIsNotInstance(a, b)  |    not isinstance(a, b)

Por convenção, todos os testes em um TestCase devem ter
seu nome iniciado com test_


Para executar os testes com unittest:

- python nome-do-módulo-de-teste.py
- python nome-do-módulo-de-teste.py -v


Docstrings nos testes:
    - Podemos acrescentar (e é o recomendado, o certo)
    docstrings nos nossos testes.
"""
