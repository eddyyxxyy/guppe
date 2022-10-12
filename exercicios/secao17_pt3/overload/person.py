class Person:
    def __init__(self, code: int, name: str, age: int):
        print('Person class initializer')
        self.__code = code
        self.__name = name
        self.__age = age

    def show(self, value: int = 1):
        if value == 1:
            return (
                f'Id: {self.__code}\n'
                f'Name: {self.__name}\n'
                f'Age: {self.__age}'
            )
        else:
            return f'Id: {self.__code}\n' f'Name: {self.__name}'
