'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {} # dicionário

jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()

p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

gols = [] # lista

for g in range(0, p):
    gols.append(int(input(f'    Quantos gols na {g+1}ª partida? ')))

jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)

print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
    
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {p} partidas.')

# for g in range(0, p):
#     print(f'    => Na partida {g+1}, fez {jogador["gols"][g]}.')
# print(f'Foi um total de {sum(jogador["gols"])} gols!')

for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {v}.')
print(f'Foi um total de {jogador["total"]} gols!')