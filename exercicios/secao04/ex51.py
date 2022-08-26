"""
51) Escreva um programa que leia as coordenadas x e y de pontos
no R² e calcule sua distância da origem (0, 0)
"""
x = int(input('Informe x: ').strip())
y = int(input('Informe y: ').strip())
distancia = int((((0 - x) ** 2) + ((0 - y) ** 2)) ** (1 / 2))
print(f'A distância entre a origem (0,0) e o ponto de'
      f' coordenadas ({x},{y}) é: {distancia}')
