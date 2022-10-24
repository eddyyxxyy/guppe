"""
Novos recursos para Matemática e Estatística


import math

# math.prod -> retorna o produto de um container numérico.
nums_v1 = [2, 3, 6, 8]
nums_v2 = 2, 3, 6, 8
nums_v3 = {2, 3, 6, 8}

# 2 * 3 * 6 * 8
print(math.prod(nums_v1))  # Return: 288
print(math.prod(nums_v2))  # Return: 288
print(math.prod(nums_v3))  # Return: 288


# math.isqrt -> retorna a parte inteira da raiz quadrada de um número.
print(math.isqrt(9))  # 3 -> Raiz inteira
print(math.sqrt(9))  # 3.0 -> Raiz com número real
print(math.isqrt(17))  # 4 -> Raiz inteira
print(math.sqrt(17))  # 4.123105625617661 -> Raiz com número real


# math.dist -> retorna a distancia Euclidiana entre dois pontos.

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))  # 51.12729212465687
print(math.dist(p2d1, p2d2))  # 43.41658669218482


# math.hypot -> retorna a hipotenusa, ou norma Euclidiana

print(math.hypot(*p3d1))  # 65.14598989960932
print(math.hypot(*p2d1))  # 51.419840528729765


# Estatistica
import statistics

# statistic.fmean -> calcula a média de números reais

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(statistics.fmean(valores_reais))  # 25.4191625
print(statistics.fmean(valores_inteiros))  # 24.75


# statistics.geometric_mean -> calcula a média geométrica de números reais

print(statistics.geometric_mean(valores_reais))  # 7.435222238889638
print(statistics.geometric_mean(valores_inteiros))  # 6.326530818100785


# statistics.multimode -> retorna o valor mais frequente em uma sequência

seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))  # ['e']
print(statistics.multimode(seq2))  # [3]
print(statistics.multimode(seq3))  # [1, 2, 3]
"""
