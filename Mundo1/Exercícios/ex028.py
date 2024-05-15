#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
cores = {'limpa': '\033[m',
         'ciano': '\033[1;36m',
         'vermelho': '\033[31m',
         'cinzaepreto': '\033[7;37m'}
computador = randint(0, 5) # Faz o computador pensar
print('{}-=-'.format(cores['ciano']) * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...'.format(cores['vermelho']))
print('{}-=-{}'.format(cores['ciano'], cores['limpa']) * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('{}PROCESSANDO...{}'.format(cores['cinzaepreto'], cores['limpa']))
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
