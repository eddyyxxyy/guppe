"""
2) Crie um classe Agenda que pode armazenar 10 pessoas e seja capas de
realizar as seguintes operações:
    . void armazenaPessoa(String nome, int idade, float altura);
    . void removePessoa(String nome);
    . int buscaPessoa(String nome);  // informa em que posição da agenda está a pessoa
    . void imprimeAgenda();  // imprime os dados de todas as pessoas da agenda
    . void imprimePessoa(int index);  // imprime os dados da pessoa que está na posição
                                         "i" da agenda
"""

from ex01 import Person


class Schedule:
    def __init__(self):
        self.__contacts: list[Person] = []
        self.__max_contacts: int = 10

    def reg_person(self, name: str, age: int, height: float):
        if len(self.__contacts) > 9:
            print('The Schedule already on max.\n')
        else:
            self.__contacts.append(Person(name, age, height))
            print(f'Success! {name} was added to contacts list!\n')

    def rem_person(self, name: str):
        for contact in self.__contacts:
            if contact.name == name:
                self.__contacts.remove(contact)
                print(
                    f'Success! {contact.name} was removed from contacts list!\n'
                )

    def find_person(self, name: str):
        for contact in self.__contacts:
            if contact.name == name:
                print(
                    f'{contact.name} is in index {self.__contacts.index(contact)}.\n'
                )

    def print_person(self, index: int):
        print(
            self.__contacts[index].info,
            '\n' if 10 >= index >= 0 else f'There is no id {index}!\n',
        )

    def print_schedule(self):
        for contact in self.__contacts:
            print(
                f'{self.__contacts.index(contact)}: '
                f'\n-> {contact.name}'
                f'\n-> {contact.age}'
                f'\n-> {contact.height}\n'
            )


def main() -> None:
    schedule = Schedule()
    schedule.reg_person('Edson Pimenta', 22, 1.82)
    schedule.reg_person('Genivaldo Pereira', 45, 1.75)
    schedule.reg_person('Francis Bruno', 31, 1.80)
    schedule.reg_person('Silvana Miranda', 51, 1.62)
    schedule.reg_person('Arthur Ablublé', 16, 1.78)
    schedule.reg_person('Gabriel Silveira', 23, 1.30)
    schedule.reg_person('Isabela Gavilan', 19, 2.10)
    schedule.reg_person('Adriana Gavilan', 79, 1.73)
    schedule.reg_person('Aurélio Pimenta', 17, 1.55)
    schedule.print_schedule()
    schedule.reg_person('Jubileu Sucinto', 79, 1.73)
    schedule.reg_person('Ahuja Lalulio', 17, 1.55)
    schedule.print_schedule()
    schedule.find_person('Francis Bruno')
    schedule.print_person(2)
    schedule.rem_person('Jubileu Sucinto')
    schedule.print_schedule()


if __name__ == '__main__':
    main()
