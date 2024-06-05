'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint  # Importa a função randint do módulo random
from time import sleep  # Importa a função sleep do módulo time
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}  # Cria um dicionário vazio

ranking = dict()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('Valores sorteados:')
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v}')

print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')