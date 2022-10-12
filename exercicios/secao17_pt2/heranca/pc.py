from hardware import Hardware


class PC(Hardware):
    def __init__(self, status, price, cpu: str, motherboard: str):
        super().__init__(status, price)
        self.__cpu = cpu
        self.__motherboard = motherboard

    @property
    def cpu(self):
        return self.__cpu

    @property
    def motherboard(self):
        return self.__motherboard

    @cpu.setter
    def cpu(self, name: str):
        self.__cpu = name

    @motherboard.setter
    def motherboard(self, name: str):
        self.__motherboard = name

    def __repr__(self):
        return f'{self.status}, {self.price}, {self.cpu}, {self.motherboard}'

    def __str__(self):
        return (
            f'Status: {self.status}\n'
            f'Price: {self.price}\n'
            f'CPU: {self.cpu}\n'
            f'Motherboard: {self.motherboard}'
        )
