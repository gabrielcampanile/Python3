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

print('-=' * 3 + f'  SORTEANDO {n} JOGOS  ' + '-=' * 3)
for c in range(0, n):
    for d in range(0, 6):
        jogo.append(randint(1, 60))
    jogo.sort()
    print(f'Jogo {c+1:2}:', ' '.join(f'{num:2d}' for num in jogo))
    sleep(1)
    jogos.append(jogo[:])
    jogo.clear()
print('-=' * 3 + f'{"< BOA SORTE ! >":^22}' + '-=' * 3)