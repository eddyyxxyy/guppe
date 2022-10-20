import random

#  https://www.alt-codes.net/suit-cards.php
NAIPES: list[str] = '♠ ♡ ♢ ♣'.split()
CARTAS: list[str] = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARTA = tuple[str, str]
BARALHO = list[CARTA]


def criar_baralho(aleatorio=False) -> BARALHO:
    """Cria um baralho com 52 cartas"""
    baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(
    baralho: BARALHO,
) -> tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    baralho: BARALHO = criar_baralho(aleatorio=True)
    jogadores: list[str] = 'P1 P2 P3 P4'.split()
    maos: dict[str, BARALHO] = {
        j: m for j, m in zip(jogadores, distribuir_cartas(baralho))
    }

    for jogador, baralho in maos.items():
        carta: str = ' '.join(f'{j}{c}' for (j, c) in baralho)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
