"""
16) Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha
na tela usando vários símbolos de igual (Ex: ========). A função recebe
por parâmetro quantos sinais de igual serão mostrados
"""
from locale import LC_ALL, setlocale


def desenha_linha(times: int) -> str:
    return '=' * times


def main() -> None:
    setlocale(LC_ALL, 'pt_BR.UTF-8')
    print(desenha_linha(15))


if __name__ == '__main__':
    main()
