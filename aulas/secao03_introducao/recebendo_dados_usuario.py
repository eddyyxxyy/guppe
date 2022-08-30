"""
Recebendo dados do usuário:

input() → Todos os dados recebidos via input() são do tipo String por padrão

Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas.

Exemplos:
- Aspas simples → 'Edson'
- Aspas duplas → "Edson"
- Aspas simples triplas → '''Edson'''
"""
# - Aspas duplas triplas → """Edson"""

# Entrada de dados
print("Qual seu nome? ")
nome = input()  # Input → Entrada

print(f'Seja bem vindo(a), {nome}!')

print("Qual sua idade? ")
idade = input()

# Processamento

# Saída de dados
print(f'O(A) {nome} tem {idade} anos.')
print(f'O(A) {nome} nasceu em {2022 - int(idade)} anos.')
