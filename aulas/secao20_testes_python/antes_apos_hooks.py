"""
Unittest - Antes e após Hooks

-------------------------------------------------
Hooks -> São os testes em si, ou seja, a execução
dos testes.
-------------------------------------------------

Logo, antes e após os hooks são as etapas que os
testes passam antes e após os testes.

setUp() -> É executado antes de cada método de
testes. É util para criamos instâncias de objetos
e outros dados.

teardown() -> É executado ao final de cada método
de teste, é útil para excluir dados ou fechar
conexões com bancos de dados.
"""
import unittest


class ModuloTest(unittest.TestCase):
    def setUp(self) -> None:
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # o tearDown vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # o tearDown vai rodar após o teste
        pass

    def tearDown(self) -> None:
        # Configurações do tearDown()
        pass
