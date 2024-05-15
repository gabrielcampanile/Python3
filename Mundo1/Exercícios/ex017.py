#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
#hi = (pow(co, 2) + pow(ca, 2)) ** (1/2)
hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))
