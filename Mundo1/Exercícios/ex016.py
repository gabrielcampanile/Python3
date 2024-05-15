#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''from math import trunc
n = float(input('Digite um valor real: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, trunc(n)))'''

n = float(input('Digite um valor real: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))