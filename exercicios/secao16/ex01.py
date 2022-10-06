"""
1) Crie uma classe para representar uma pessoa, como os atributos privados de
nome, idade e altura. Crie os métodos públicos necessários para sets e gets e
também um método para imprimir os dados de uma pessoa.
"""


class Person:
    def __init__(self, name: str, age: int, height: float):
        self._name = name
        self._age = age
        self._height = height

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def height(self):
        return self._height

    @property
    def info(self):
        return self._name, self._age, self._height

    @name.setter
    def name(self, name: str):
        if name.isalpha():
            self._name = name

    @age.setter
    def age(self, age: int):
        if age >= 0:
            self._age = age

    @height.setter
    def height(self, height: float):
        self._height = height


def main() -> None:
    person_test = Person('Edson Pimenta', 22, 1.82)
    print(person_test.info)


if __name__ == '__main__':
    main()
