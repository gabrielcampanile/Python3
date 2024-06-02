'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

wins = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = computador + jogador
    jogada = ''
    while jogada not in 'PpIi':
        jogada = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    result = 'PAR' if total % 2 == 0 else 'IMPAR'
    
    print('-' * 40)
    print(f'Você jogou {jogador} e o computador jogou {computador}, total de {total}. DEU {result}')
    print('-' * 40)

    if jogada == result[0]:
        print('Você VENCEU!\nVamos jogar novamente...')
        print('=-' * 20)
        wins += 1
    else:
        print('Você PERDEU!')
        print('=-' * 20)
        break

print(f'GAME OVER! Você venceu {wins} vezes.')
    