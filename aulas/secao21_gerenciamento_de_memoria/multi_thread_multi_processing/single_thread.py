import time

CONTADOR = 50_000_000


def contagem_regressiva(num: int):
    while num > 0:
        num -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')  # 2.2310030460357666
