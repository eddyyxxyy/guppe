"""
Teste de memória com generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Função usando Listas - 469MB de uso de memória


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste 1
for n in fib_lista(100000):
    print(n)



# Função usando Geradores - 4,5MB de uso de memória


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += contador


# Teste 2
for n in fib_gen(100000):
    print(n)

"""
