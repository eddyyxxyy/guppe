"""
1) Escreva um programa que:
    (a) Crie/abra um arquivo texto de nome "arq.txt"
    (b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário
    entre com o caractere '0'
    (c) Feche o arquivo
Agora, abra e leia o arquivo, caarctere por caractere, escreva na tela todos os caracteres
armazenados
"""


def main() -> None:
    with open('arquivos/arq.txt', 'w+', encoding='UTF-8') as arq:
        while True:
            char = str(input('Enter a char (0 to end):\n-> ').strip()[0])
            if char == '0':
                break
            arq.write(char)
        arq.seek(0)
        for char in arq.read():
            print(char)


if __name__ == '__main__':
    main()
