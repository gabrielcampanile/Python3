'''Crie uma tupla preenchida com os 20 primeiros colocados da times do Campeonato Brasileiro de Futebol, na ordem de colocação.'''

times = ('Flamengo', 'Bahia', 'Botafogo', 'São Paulo', 'Athletico-PR', 'Red Bull Bragantino', 'Palmeiras', 'Internacional', 'Cruzeiro', 'Atlético-MG', 'Fortaleza', 'Grêmio', 'Vasco da Gama', 'Juventude', 'Fluminense', 'Criciúma', 'Corinthians', 'Atlético-GO', 'Vitória', 'Cuiabá')

print('-'*40)
print('Times do Brasileirão Betano 2024:')
print('-'*40)

for i in range(0, len(times)):
    print(f'{i+1}º {times[i]}')

print('-'*40)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-'*40)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-'*40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-'*40)
print(f'O São Paulo está na {times.index("São Paulo") + 1}ª posição.')