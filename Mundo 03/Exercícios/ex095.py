jogadores = [] # lista
jogador = {} # dicionário
gols = [] # lista
total = 0

while True:
    print('-' * 20)
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()

    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for g in range(0, p):
        gols.append(int(input(f'Quantos gols na {g+1}ª partida? ')))
        total += gols[g]

    jogador['gols'] = gols
    jogador['total'] = total

    jogadores.append(jogador.copy())

    gols.clear()
    total = 0

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 30)
print(f'{"cod":>3}{" nome":<15}{"gols":<15}{"total":<5}')
print('-' * 40)
for j in jogadores:
    for v in j.values:
        print(f'{len(jogadores):>3}{ j["nome"]:<15}{ j["gols"]:<15}{j["total"]:<5}')


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