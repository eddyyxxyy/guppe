lmaiu = str(input('Informe uma letra maiúscula: ').upper()[0])
lminu = ord(lmaiu)
print(f'A letra informada foi "{lmaiu}" e seu código ASCII é {lminu};\n'
      f'Sua letra minúscula seria "{lmaiu.lower()}" e seu código ASCII corresponde à {ord(lmaiu.lower())}.')
