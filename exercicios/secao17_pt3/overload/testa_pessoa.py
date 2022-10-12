from person import Person


class TestPerson(Person):
    def __init__(self, code: int, name: str, age: int):
        print('TestPerson class initializer')
        super().__init__(code, name, age)

    @classmethod
    def instantiate(cls, code: int, name: str, age: int):
        instance = Person(code, name, age)
        return instance


def main() -> None:
    person0 = TestPerson(0, 'Juliano Cabral', 30)
    print(person0.show(), '\n')
    print(person0.show(2), '\n')
    person1 = TestPerson.instantiate(1, 'Gabriela Cintra', 35)
    print(person1.show())


if __name__ == '__main__':
    main()
