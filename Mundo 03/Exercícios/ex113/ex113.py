'''Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

from Utilidades import leiaInt, leiaFloat

# Programa Principal
n = leiaInt('Digite um número: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')