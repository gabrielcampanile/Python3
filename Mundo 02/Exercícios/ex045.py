'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
cores = {'empatou': '\033[33m',
         'venceu': '\033[32m',
         'perdeu': '\033[31m',
         'limpar': '\033[m'}
computador = randint(0, 2)

print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)

if jogador == computador:
    print('{}EMPATE{}'.format(cores['empatou'], cores['limpar']))
elif (jogador == 0 and computador == 2) or \
     (jogador == 1 and computador == 0) or \
     (jogador == 2 and computador == 1):
    print('{}JOGADOR VENCEU{}'.format(cores['venceu'], cores['limpar']))
else:
    print('{}COMPUTADOR VENCEU{}'.format(cores['perdeu'], cores['limpar']))

# import random

# def jokenpo(player_choice):
#     choices = ['rock', 'paper', 'scissors']
#     computer_choice = random.choice(choices)

#     print(f"Player's choice: {player_choice}")
#     print(f"Computer's choice: {computer_choice}")

#     if player_choice == computer_choice:
#         print("It's a tie!")
#     elif (player_choice == 'rock' and computer_choice == 'scissors') or \
#          (player_choice == 'paper' and computer_choice == 'rock') or \
#          (player_choice == 'scissors' and computer_choice == 'paper'):
#         print("Player wins!")
#     else:
#         print("Computer wins!")

# player_choice = input("Enter your choice (rock, paper, scissors): ")
# jokenpo(player_choice)
