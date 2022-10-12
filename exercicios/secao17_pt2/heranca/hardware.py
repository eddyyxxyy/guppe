class Hardware:
    def __init__(self, status: bool, price: float):
        self.__status = status
        self.__price = price

    @property
    def status(self):
        return self.__status

    @property
    def price(self):
        return self.__price

    @status.setter
    def status(self, boolean: bool):
        self.__status = boolean

    @price.setter
    def price(self, value: float):
        self.__price = value

    def __repr__(self):
        return f'{self.__status}, {self.__price}'

    def __str__(self):
        return f'Status: {self.__status}\n' f'Price: {self.__price}'
