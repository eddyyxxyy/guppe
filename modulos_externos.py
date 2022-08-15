"""
Módulos Externos

Para instalar módulos que não vem integrados com o Python (os built-ins), utilizamos um gerenciador de pacotes chamado
pip (Python Installer Package)

Você pode conhecer todos os pacotes externos oficiais em → https://pypi.org

colorama → É utilizado para permitir a impressão de textos coloridos no terminal

# Instalando um módulo:

pip install nome_do_módulo

# Utilizando o pacote instalado (colorama):

# pip install colorama → instala o pacote

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
"""
