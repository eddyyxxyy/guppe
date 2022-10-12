from hardware import Hardware
from pc import PC


class TestaEquipamento:
    @staticmethod
    def main():
        hardware = Hardware(status=True, price=1500.00)
        pc = PC(status=True, price=1500.00, cpu='Intel i5', motherboard='Asus')

        print(f'Hardware:\n' f'{hardware}\n\n' f'PC:\n' f'{pc}')


def main() -> None:
    TestaEquipamento.main()


if __name__ == '__main__':
    main()
