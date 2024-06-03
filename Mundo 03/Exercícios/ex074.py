'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram:', end=' ')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

# print(f'Os valores sorteados foram:', end=' ')
# for c in range(0, len(num)):
#     print(f'{num[c]}', end=' ')
#     if c == 0:
#         maior = menor = num[c]
#     else:
#         if num[c] > maior:
#             maior = num[c]
#         elif num[c] < menor:
#             menor = num[c]

# print(f'\nO maior valor sorteado foi {maior}')
# print(f'O menor valor sorteadi foi {menor}')