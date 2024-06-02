'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
color = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',}
print('{}-='.format(color['azul'], color['limpa']) * 20)
print('{}Analisador de Triângulos{}'.format(color['amarelo'], color['limpa']))
print('{}-={}'.format(color['azul'], color['limpa']) * 20)

r1 = int(input('R1: '))
r2 = int(input('R2: '))
r3 = int(input('R3: '))

if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print('Não formam um triângulo')
else:
    print('Formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓCELES')
    else:
        print('ESCALENO')
