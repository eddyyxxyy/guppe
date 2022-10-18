import unittest

from atividades import comer, dormir


class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('Quiabo', True),
            'Estou comendo Quiabo por que quero manter a forma.',
        )

    def test_comer_notsaudavel(self):
        """Testando o retorno com comida não saudável"""
        self.assertEqual(
            comer('Pizza', eh_saudavel=False),
            'Estou comendo Pizza por que a gente só vive uma vez.',
        )

    def test_dormir_pouco(self):
        """Testando o retorno quando se dorme pouco"""
        self.assertEqual(
            dormir(4), 'Continuo cansado após dormir por 4 horas... :('
        )

    def test_dormir_muito(self):
        """Testando o retorno quando se dorme muito"""
        self.assertEqual(
            dormir(10), 'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )


if __name__ == '__main__':
    unittest.main()
