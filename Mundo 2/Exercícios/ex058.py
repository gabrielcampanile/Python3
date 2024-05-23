'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''

from time import sleep
from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 1 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi?\n')
sleep(1)

acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
        tentativas += 1

print('\nAcertou com {} tentativas. Parabéns!'.format(tentativas))