"""
67) Faça uma rotina que receba como parâmetro um vetor de caracteres e
seu tamanho. A função deverá de ler uma string do teclado, caractere por caractere
usando a função getchat() até que o usuário digite enter ou o tamanho máximo do
vetor seja alcançado.
"""
import sys


def routine():
    string = ""
    while True:
        c = sys.stdin.read(1)  # reads one byte at a time, similar to getchar()
        if c == ' ':
            break
        string += c
    return string


def main() -> None:
    print(routine())


if __name__ == '__main__':
    main()
