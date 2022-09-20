"""
44) Receba a altura do degrau de uma escada e a altura que o usuário
deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário
deverá subir para atingir seu objetivo.
"""
ae = float(
    input('Informe a altura de cada degrau (em cm): ')
    .strip()
    .replace(',', '.')
)
ad = float(input('Informe a altura que deseja alcançar (em m): '))
qd = int(ad * 100) / ae
print(f'A quantidade de degraus que você deverá subir é {round(qd)} degraus.')
