import time
from multiprocessing import Pool

CONTADOR = 50_000_000


def contagem_regressiva(num: int):
    while num > 0:
        num -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    r2 = pool.apply_async(contagem_regressiva, [CONTADOR // 2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'Tempo em segundos: {fim - inicio}')
