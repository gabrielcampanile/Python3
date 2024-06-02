'''Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

num = int(input('Digite um número para calcular o seu Fatorial: '))
fat = 1
print('Calculando {}! = '.format(num), end='')

for c in range(num, 0, -1):
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1
print('{}'.format(fat))