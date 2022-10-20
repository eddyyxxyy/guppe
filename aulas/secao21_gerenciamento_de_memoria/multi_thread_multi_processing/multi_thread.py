import time
from threading import Thread

CONTADOR = 50_000_000


def contagem_regressiva(num: int):
    while num > 0:
        num -= 1


t1 = Thread(target=contagem_regressiva, args=(CONTADOR // 2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR // 2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')  # 2.125131607055664
