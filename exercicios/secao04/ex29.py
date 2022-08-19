media = []
for i in range(4):
    media.append(float(input(f'Informe sua {i + 1} nota: ').strip().replace(',', '.')))
print(f'A média do aluno foi de: {sum(media) / len(media):.1f}.')
