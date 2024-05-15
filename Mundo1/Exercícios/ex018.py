#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo: '))
sen = sin(radians(angulo))
print('O ângulo de {}° tem o SENO de {:.2f}'.format(angulo, sen))
cos = cos(radians(angulo))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(angulo, cos))
tg = tan(radians(angulo))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(angulo, tg))
