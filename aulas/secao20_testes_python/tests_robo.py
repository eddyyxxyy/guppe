import unittest

from robo import Robo


class TestRobo(unittest.TestCase):
    def setUp(self) -> None:
        # print('setUp sendo executado')
        self.megaman = Robo('MegaMan', bateria=50)

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(
            self.megaman.dizer_nome(), f'Beep Boop, eu sou MEGAMAN'
        )
        self.assertEqual(
            self.megaman.bateria, 49, 'A bateria deveria estar em 49%'
        )

    def tearDown(self) -> None:
        # print('tearDown sendo executado!')
        pass


if __name__ == '__main__':
    unittest.main()
