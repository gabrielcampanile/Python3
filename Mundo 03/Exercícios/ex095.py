'''Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

times = [] # lista
jogador = {} # dicionário
gols = [] # lista

while True:
    print('-' * 30)
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()

    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for g in range(0, p):
        gols.append(int(input(f'Quantos gols na {g+1}ª partida? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)

    times.append(jogador.copy())

    gols.clear()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' * 40)
for key, j in enumerate(times):
    print(f'{key:>3} ', end=' ')
    for dados in j.values():
        print(f'{str(dados):<15}', end=' ')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(times):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {times[busca]["nome"]}:')
        for i, g in enumerate(times[busca]['gols']):
            print(f'    => Na partida {i+1}, fez {g} gols.')

# print('-=' * 30)
# print(jogador)

# print('-=' * 30)
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}.')
    
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]} jogou {p} partidas.')

# for g in range(0, p):
#     print(f'    => Na partida {g+1}, fez {jogador["gols"][g]}.')

# print(f'Foi um total de {total} gols!')