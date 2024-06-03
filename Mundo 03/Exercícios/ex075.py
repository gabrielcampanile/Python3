'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end=' ')
for par in tupla:
    if par % 2 == 0:
        print(par, end=' ')

# a = int(input('Digite um número: '))
# b = int(input('Digite outro número: '))
# c = int(input('Digite mais um número: '))
# d = int(input('Digite o último número: '))
# tupla = (a, b, c, d)

# nove = 0
# tres = -1
# for num in tupla:
#     if num == 9:
#         nove += 1
#     elif num == 3:
#         tres = tupla.index(num) + 1

# print(f'O valor 9 apareceu {nove} vezes')
# if tres == -1:
#     print(f'O valor 3 não foi digitado em nenhuma posição')
# else:
#     print(f'O valor 3 foi digitado na {tres}ª posição')

# print('Os valores pares digitados foram', end=' ')
# for par in tupla:
#     if par % 2 == 0:
#         print(par, end=' ')
    