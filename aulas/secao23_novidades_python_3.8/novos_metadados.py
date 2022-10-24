"""
Novos Metadados

from importlib import metadata

print(metadata.version('numpy'))
print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip')
print(list(metadados_pip))
print(metadados_pip['Project-URL'])
print(metadata.requires('numpy'))
"""
