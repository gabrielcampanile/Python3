#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))
#Verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando quem é maior
maior = n1
if n2>n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
