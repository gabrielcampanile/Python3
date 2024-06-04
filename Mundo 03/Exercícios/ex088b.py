'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from time import sleep
from random import randint

print('-' * 30)
print(f'{"JOGUE NA MEGA SENA":^30}')
print('-' * 30)

n = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
jogo = []

tot = 0

while tot < n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    tot += 1

print('-=' * 3 + f'  SORTEANDO {n} JOGOS  ' + '-=' * 3)
for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
print('-=' * 3 + f'{"< BOA SORTE ! >":^22}' + '-=' * 3)